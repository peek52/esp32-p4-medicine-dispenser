# 💊 ESP32-P4 Medicine Dispenser

A smart, 6-module medicine dispenser system built for the ESP32-P4-Nano board. It features a touch-screen interface, a real-time scheduler, a 6-channel servo control system, and a robust WiFi connection manager.

## 🌟 Features
* **6 Medicine Modules:** Manage up to 6 different medicines, each with independent quantities and schedules.
* **7 Time Slots:** Flexible scheduling system with up to 7 distinct time slots per day (e.g., Morning Before Meal, Bedtime).
* **Modern Touch UI:** A production-ready "Light Mint" UI built with LovyanGFX for a 480x320 display.
  - Interactive modules grid
  - Easy-to-use time picker
  - Real-time digital clock and next-schedule indicator 
* **Dual WiFi Setup:** Connect to the internet via an On-Screen Keyboard (OSK) or via a mobile Captive Portal.
* **Non-Volatile Storage (NVS):** Schedules, quantities, and settings are saved permanently across reboots.

## 🔌 Hardware Setup
1. **Board:** Waveshare ESP32-P4-Nano
2. **Display:** 480x320 LCD with FT6236 Touch Controller (SPI + I2C)
3. **Servo Controller:** PCA9685 (I2C) driving 6 micro-servos
4. **RTC:** DS3231 (I2C) for accurate time-keeping

*Note: The Display Touch, PCA9685, and DS3231 share the same I2C bus (`Wire`).*

## 🛠️ Software Architecture
The codebase is heavily modularized to ensure non-blocking performance:
* `main.cpp`: System initialization, I2C bus sharing logic, and the main event loop.
* `ui_manager.cpp`: LovyanGFX-based state machine handling all UI drawing and touch events.
* `scheduler.cpp`: Manages the TimeSlots, MedModules, and NVS persistence.
* `servo_control.cpp`: Interfaces with the PCA9685 to dispense medicine.
* `wifi_manager.cpp`: Handles WiFi connections, scanning, and the Captive Portal.

## 🚀 How to Build & Flash
This project is built using PlatformIO.

1. Install [PlatformIO](https://platformio.org/) in VS Code.
2. Clone this repository.
3. Open the project folder in VS Code.
4. Run the upload command in the terminal:
   ```bash
   pio run -e esp32-p4-nano -t upload
   ```

## 📝 License
This project is open-source. Feel free to use and modify it for your own dispensing systems!
