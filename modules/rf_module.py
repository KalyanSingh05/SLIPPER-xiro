import spidev
import time

class CC1101:
    def _init_(self, spi_bus=0, spi_device=0):
        # Initialize SPI
        self.spi = spidev.SpiDev()
        self.spi.open(spi_bus, spi_device)
        self.spi.max_speed_hz = 500000
        self.initialize_cc1101()

    def initialize_cc1101(self):
        # Initialize CC1101 with default settings
        # Placeholder for CC1101 initialization commands
        print("Initializing CC1101...")

    def send_data(self, data):
        """Transmit data via RF"""
        print("Sending data:", data)
        self.spi.xfer2([0x7F] + data)  # Sending data with burst write command
        time.sleep(0.1)

    def receive_data(self):
        """Receive data from RF module"""
        print("Listening for RF data...")
        received = self.spi.xfer2([0xFF])  # Dummy read to receive
        print("Data received:", received)
        return received

    def close(self):
        """Close the SPI connection"""
        self.spi.close()

# Example usage
def run_rf_module():
    rf = CC1101()
    try:
        mode = input("Press 's' to send or 'r' to receive: ").lower()
        if mode == 's':
            data = [0x01, 0x02, 0x03]  # Example payload; modify as needed
            rf.send_data(data)
        elif mode == 'r':
            rf.receive_data()
        else:
            print("Invalid mode.")
    finally:
        rf.close()