---
name: ESP32-P4-Nano Development
description: Specialized knowledge for developing on the Waveshare ESP32-P4-Nano board, covering Audio (ES8311), WiFi, and PlatformIO configuration.
---

# ESP32-P4-Nano Development Guide

 This skill provides essential information for working with the **Waveshare ESP32-P4-Nano** board.

## 1. PlatformIO Configuration (`platformio.ini`)

Always use the development branch of the platform and include the specific build flag for WiFi.

```ini
[env:esp32-p4-nano]
platform = https://github.com/pioarduino/platform-espressif32/archive/refs/heads/develop.zip
board = esp32-p4-nano
framework = arduino
monitor_speed = 115200

build_flags = 
    -DCORE_DEBUG_LEVEL=0
    -DAUDIO_NO_SD_FS
    -DCONFIG_IDF_TARGET_ESP32P4
    ; CRITICAL: Required for WiFi compilation on P4
    -DCONFIG_ESP32_PHY_MAX_WIFI_TX_POWER=20 
```

## 2. Pin Definitions

### Audio (ES8311 Codec & NS4150B PA)
*   **I2C Control**:
    *   SDA: `7`
    *   SCL: `8`
    *   Address: `0x18`
*   **I2S Audio**:
    *   MCLK: `13` (Must be enabled and active)
    *   BCLK: `12`
    *   LRC / WS: `10`
    *   **DOUT**: `9` (Note: Documentation sometimes conflicts, but 9 is tested working for Output)
    *   DIN: `11` (Input/Mic - verify if needed)
*   **Power Amplifier (PA)**:
    *   PA_ENABLE: `53` (Active HIGH)

### Other Peripherals
*   **USB Type-C**: Programs/UART & Power
*   **USB Type-A**: USB 2.0 OTG (Camera, Device mode)
*   **BOOT Button**: `0` (Useful for factory reset logic)

## 3. Audio Implementation Tips (ES8311)

When initializing the ES8311 driver, ensure:
1.  **MCLK is Enalbed**: You MUST configure the I2S driver to output MCLK on GPIO 13.
2.  **Clock Source**: Configure ES8311 Register `0x01` to `0x3F` to use MCLK pin as the source.
    ```cpp
    // Example ES8311 Reg Config
    es8311_write_reg(0x01, 0x3F); // Use MCLK Pin
    es8311_write_reg(0x32, 0xFF); // Max Volume
    ```
3.  **PA Enable**: Always set GPIO 53 HIGH.

## 4. WiFiManager Integration

*   Library: `tzapu/WiFiManager`
*   **Constraint**: Requires the `CONFIG_ESP32_PHY_MAX_WIFI_TX_POWER` build flag mentioned above, otherwise it fails to compile on ESP32-P4.

## 5. Troubleshooting
*   **No Sound**: Check if MCLK (GPIO 13) is actually outputting a clock signal. Try switching ES8311 to use BCLK (Reg `0x01` = `0x7F`) if MCLK is unstable, but MCLK is preferred.
*   **Upload Failed**: Ensure `fix_encoding.py` is used if on Windows to handle UTF-8 issues in PlatformIO's Python environment.
