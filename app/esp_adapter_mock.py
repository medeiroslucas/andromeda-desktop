from setting import BLUETOOTH_NAME, SEND_COORD_MOCK_FILE


class EspAdapterMock:

    def __init__(self, bluetooth_name=BLUETOOTH_NAME):
        self.bluetooth_name = bluetooth_name
        self.req = None
        self.lat = -16.6653
        self.long = -46.2702

        fil = open(SEND_COORD_MOCK_FILE, "wb")
        fil.close()

    def get_location(self):
        return self.lat, self.long

    @staticmethod
    def send_coord(az, alt):
        coord_str = f"Az: {az}, Alt: {alt}\n"
        mock_coords_file = open(SEND_COORD_MOCK_FILE, "ab")
        mock_coords_file.write(coord_str.encode())
        mock_coords_file.close()
