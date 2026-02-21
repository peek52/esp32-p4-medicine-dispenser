#pragma once

// ============================================================
// ESP32-P4-Nano Medicine Dispenser — Pin Configuration
// Board: Waveshare ESP32-P4-Nano
// ============================================================

// --- I2C Bus (shared: PCA9685, PCF8574, DS3231, FT6236 Touch) ---
#define I2C_SDA_PIN 7
#define I2C_SCL_PIN 8

// --- I2C Device Addresses ---
#define PCA9685_ADDR 0x40 // Servo driver
#define PCF8574_ADDR 0x20 // IR sensor expander
#define FT6236_ADDR 0x38  // Capacitive touch controller
// DS3231 RTC uses default 0x68 (handled by RTClib)

// --- SPI LCD (ST7796S 4.0" 480x320) ---
#define LCD_MOSI_PIN 32
#define LCD_MISO_PIN -1 // Not connected
#define LCD_SCK_PIN 36
#define LCD_CS_PIN 26
#define LCD_DC_PIN 24
#define LCD_RST_PIN 25
// LCD LED/Backlight: hardwired to 3.3V

// --- Touch Panel (FT6236 — I2C, shares bus with above) ---
// CTP_SDA = I2C_SDA_PIN (7)
// CTP_SCL = I2C_SCL_PIN (8)
#define CTP_INT_PIN 21
// CTP_RST: hardwired to 3.3V

// --- Button & LED ---
#define BUTTON_PIN 0 // BOOT button on P4-Nano
#define LED_PIN 6

// --- Display (Landscape Mode) ---
#define LCD_WIDTH 480
#define LCD_HEIGHT 320

// --- Time Slots (7 slots) ---
#define NUM_TIME_SLOTS 7
// Slot IDs:
// 0 = เช้า ก่อนอาหาร
// 1 = เช้า หลังอาหาร
// 2 = เที่ยง ก่อนอาหาร
// 3 = เที่ยง หลังอาหาร
// 4 = เย็น ก่อนอาหาร
// 5 = เย็น หลังอาหาร
// 6 = ก่อนนอน

// --- Medicine Modules (6 slots on PCA9685 ch0-5) ---
#define NUM_MODULES 6
#define MAX_MED_NAME 16

// --- Servo ---
#define SERVO_ANGLE_HOME 27
#define SERVO_ANGLE_DISP 0
#define SERVO_FREQ 50
