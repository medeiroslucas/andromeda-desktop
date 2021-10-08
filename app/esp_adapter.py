from setting import BLUETOOTH_NAME
from gattlib import DiscoveryService, GATTRequester


class EspAdapter:

    def __init__(self, bluetooth_name=BLUETOOTH_NAME):
        self.bluetooth_name = bluetooth_name
        self.req = None

        service = DiscoveryService("hci0")
        devices = service.discover(2)

        for address, name in devices.items():
            if name == self.bluetooth_name:
                self.req = GATTRequester(address)
                self.req.connect(True)

    def get_location(self):
        data = self.req.read_by_handle(0x1)[0]

        lat = hex(ord(data[0]))
        long = hex(ord(data[1]))

        return lat, long

    def send_coord(self, az, alt):
        self.req.write_by_handle(0x20, str(bytearray([az, alt])))
