import curses
import RPi.GPIO as GPIO
import time
from modules.ir_module import run_ir_module
from modules.nfc_module import run_nfc_module
from modules.rf_module import run_rf_module

# Button GPIO pins for the display HAT
button_left = 5      # Left button
button_center = 6    # Center button
button_right = 13    # Right button

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_center, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_right, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Module options
options = ["IR Module", "NFC Module", "RF Module"]
current_selection = 0

# Placeholder functions for each module
def run_ir_module():
    print("Running IR Module...")
    time.sleep(1)  # Replace with actual IR code

def run_nfc_module():
    print("Running NFC Module...")
    time.sleep(1)  # Replace with actual NFC code

def run_rf_module():
    print("Running RF Module...")
    time.sleep(1)  # Replace with actual RF code

# Display CLI Menu
def display_menu(stdscr):
    global current_selection
    stdscr.clear()
    stdscr.addstr(0, 0, "Select Module (Use Left/Right to navigate, Center to select):")

    for idx, option in enumerate(options):
        if idx == current_selection:
            stdscr.addstr(2 + idx, 0, f"> {option}", curses.A_REVERSE)
        else:
            stdscr.addstr(2 + idx, 0, f"  {option}")
    stdscr.refresh()

def button_callback(channel):
    global current_selection
    if channel == button_left:
        current_selection = (current_selection - 1) % len(options)
    elif channel == button_right:
        current_selection = (current_selection + 1) % len(options)

# Main function with curses for CLI
def main(stdscr):
    # Configure button callbacks
    GPIO.add_event_detect(button_left, GPIO.FALLING, callback=button_callback, bouncetime=200)
    GPIO.add_event_detect(button_right, GPIO.FALLING, callback=button_callback, bouncetime=200)

    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(True)

    while True:
        display_menu(stdscr)
        
        # Check if center button is pressed
        if GPIO.input(button_center) == 0:
            # Run the selected module
            stdscr.addstr(6, 0, f"Running {options[current_selection]}...")
            stdscr.refresh()
            time.sleep(0.5)
            if current_selection == 0:
                run_ir_module()
            elif current_selection == 1:
                run_nfc_module()
            elif current_selection == 2:
                run_rf_module()
            stdscr.clear()

        time.sleep(0.1)

# Run the CLI with curses
try:
    curses.wrapper(main)
except KeyboardInterrupt:
    GPIO.cleanup()