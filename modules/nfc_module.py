import time
import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.spi import PN532_SPI

# Define pins and SPI connection
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs_pin = DigitalInOut(board.D5)  # Adjust CS pin according to your wiring
pn532 = PN532_SPI(spi, cs_pin, debug=False)

# Configure PN532 module to read MiFare cards
pn532.SAM_configuration()

def read_nfc():
    """Reads NFC data from a card and stores it."""
    print("Waiting for NFC card...")
    
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is None:
        print("No card detected.")
        return None

    print("Card detected!")
    print("UID:", [hex(i) for i in uid])
    
    # Store UID in a file for later use
    with open("stored_nfc_data.txt", "w") as f:
        f.write(f"UID: {[hex(i) for i in uid]}")
    print("NFC data stored.")

def write_nfc(data):
    """Writes stored NFC data to a detected card (if writable)."""
    print("Looking for a writable NFC card...")

    uid = pn532.read_passive_target(timeout=0.5)
    if uid is None:
        print("No card detected.")
        return
    
    print("Attempting to write to the card...")
    # Write functionality depends on the type of NFC card and may require authentication
    # Below is a placeholder example
    try:
        pn532.ntag2xx_write_block(4, data[:4])  # Adjust for actual data handling
        print("Data written to NFC card.")
    except Exception as e:
        print(f"Error writing to NFC: {e}")

def run_nfc_module():
    """Main function to interact with NFC module."""
    choice = input("Press 'r' to read, 'w' to write: ").lower()
    if choice == 'r':
        read_nfc()
    elif choice == 'w':
        data = input("Enter data to write: ")
        write_nfc(data.encode())
    else:
        print("Invalid choice. Use 'r' to read or 'w' to write.")