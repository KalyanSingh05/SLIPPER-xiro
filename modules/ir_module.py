import pigpio
import time
import json

# Pin configuration
IR_RECEIVE_PIN = 18  # Adjust based on your wiring
IR_SEND_PIN = 17     # Adjust based on your wiring

# Initialize pigpio
pi = pigpio.pi()
if not pi.connected:
    exit()

def record_ir_signal():
    """Records an IR signal and stores it."""
    print("Recording IR signal...")
    pi.set_mode(IR_RECEIVE_PIN, pigpio.INPUT)
    
    wave = []
    start = time.time()

    while True:
        if pi.read(IR_RECEIVE_PIN):
            wave.append(time.time() - start)
            start = time.time()
        
        # Stop recording after 5 seconds or based on your requirement
        if time.time() - start > 5:
            break
    
    # Store the recorded signal in JSON format
    with open("recorded_ir_signal.json", "w") as f:
        json.dump(wave, f)
    print("Signal recorded and saved.")

def play_ir_signal():
    """Plays back a stored IR signal."""
    try:
        with open("recorded_ir_signal.json", "r") as f:
            wave = json.load(f)
        
        pi.set_mode(IR_SEND_PIN, pigpio.OUTPUT)
        print("Replaying IR signal...")
        
        for duration in wave:
            pi.write(IR_SEND_PIN, 1)
            time.sleep(duration)
            pi.write(IR_SEND_PIN, 0)
        
        print("Signal replay complete.")
    except FileNotFoundError:
        print("No recorded signal found.")

def run_ir_module():
    """Main function to handle IR recording and playback."""
    choice = input("Press 'r' to record, 'p' to playback the stored signal: ").lower()
    if choice == 'r':
        record_ir_signal()
    elif choice == 'p':
        play_ir_signal()
    else:
        print("Invalid choice. Please enter 'r' to record or 'p' to play.")