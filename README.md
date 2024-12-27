# SLIPPER-xiro
# Raspberry Pi Zero 2 W Multi-Function Project

This repository contains all the files, configurations, and instructions for building a multi-functional project using a Raspberry Pi Zero 2 W. The project integrates multiple modules, such as the CC1101, PN532 NFC, and IR transmitter/receiver, along with a Waveshare 1.44-inch LCD HAT to create a versatile and interactive device.

---

## Table of Contents

- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Wiring Diagram](#wiring-diagram)
- [Software Requirements](#software-requirements)
- [Setup Instructions](#setup-instructions)
  - [Hardware Setup](#hardware-setup)
  - [Software Installation](#software-installation)
- [Usage](#usage)
- [Known Issues](#known-issues)
- [License](#license)

---

## Features

- **CC1101 Module**: For RF signal transmission and reception.
- **PN532 NFC Module**: For NFC communication (reading and writing).
- **IR Transmitter and Receiver**: For sending and receiving IR signals.
- **Waveshare 1.44-inch LCD HAT**: For displaying information and UI.
- **Python-based Network and Log Monitoring**: Tracks and logs network activity.

---

## Hardware Requirements

- Raspberry Pi Zero 2 W
- CC1101 RF Module
- PN532 NFC Module
- KY-005 IR Transmitter
- KY-022 IR Receiver
- Waveshare 1.44-inch LCD HAT (ST7735S controller)
- 3x7 cm universal prototype board (double sided)
- Power supply and SD card for the Raspberry Pi

---

## Wiring Diagram

### CC1101 Module
- **VCC**: Pin 17 (3.3V)
- **GND**: Pin 25 (GND)
- **MOSI**: Pin 19 (GPIO 10, SPI MOSI)
- **MISO/GDO0**: Pin 21 (GPIO 9, SPI MISO)
- **SCK**: Pin 23 (GPIO 11, SPI SCK)
- **CSN**: Pin 24 (GPIO 8, SPI CE0)
- **GDO1**: Pin 29 (GPIO 5)
- **GDO2**: Pin 31 (GPIO 6)

### PN532 NFC Module
- **VCC**: Pin 1 (3.3V)
- **GND**: Pin 9 (GND)
- **SDA**: Pin 3 (GPIO 2, I2C SDA)
- **SCL**: Pin 5 (GPIO 3, I2C SCL)

### IR Module
#### KY-005 IR Transmitter
- **VCC**: Pin 2 (5V)
- **GND**: Pin 6 (GND)
- **SIG**: Pin 12 (GPIO 18)

#### KY-022 IR Receiver
- **VCC**: Pin 4 (5V)
- **GND**: Pin 20 (GND)
- **SIG**: Pin 11 (GPIO 17)

---

## Software Requirements

- Raspberry Pi OS (Bookworm)
- Python 3.x
- Required Python libraries:
  - `spidev`
  - `RPi.GPIO`
  - `pynput`
  - `pynfc`
  - `PyMouse`
- `fbcp-ili9341` for LCD driver

---

## Setup Instructions

### Hardware Setup

1. Solder all the modules onto the 3x7 cm prototype board using female connectors for easy replacements or upgrades.
2. Ensure all connections match the pin configuration provided in the Wiring Diagram section.
3. Attach the Waveshare 1.44-inch LCD HAT to the GPIO header.

### Software Installation

`For the Installation purpose` [Click here](https://www.waveshare.com/wiki/1.44inch_LCD_HAT#Support)

---

## Usage

1. Power on the Raspberry Pi.
2. The LCD will display the UI, and the Python scripts for mouse control, NFC, and IR functionalities will run automatically.
3. Use the device for RF, NFC, and IR operations as required.

---

## Known Issues

- LCD initialization issues: Verify `fbcp-ili9341` installation and configuration.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.v
