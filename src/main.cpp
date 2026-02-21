#include "config.h"
#include "display_module.h"
#include "scheduler.h"
#include "servo_control.h"
#include "ui_manager.h"
#include "wifi_manager.h"
#include <Arduino.h>
#include <Network.h>
#include <SPI.h>
#include <WiFi.h>
#include <Wire.h>


// ============================================================
// ============================================================
// Called when user clicks "PRESS TO DISPENSE" on the confirmation screen
// ============================================================
void onConfirmedDispense(int timeSlotIndex) {
  Serial.printf("[Main] User confirmed dispense for slot %d\n", timeSlotIndex);

  int dispensed = 0;
  for (int m = 0; m < NUM_MODULES; m++) {
    MedModule &mod = moduleGet(m);
    if (mod.slotMask & (1 << timeSlotIndex)) {
      Serial.printf("[Main] Dispensing module %d (%s)\n", m, mod.name);

      // Show dispensing animation
      uiShowDispensing(m);

      // Activate servo
      servoDispense(m);

      // Decrement qty
      if (mod.qty > 0) {
        mod.qty--;
      }

      dispensed++;
    }
  }

  // Save updated quantities
  if (dispensed > 0) {
    schedulerSave();
    uiShowResult(timeSlotIndex, true);
  } else {
    Serial.println("[Main] No modules assigned to this slot");
  }
}

// ============================================================
// Dispense callback — triggered by scheduler when a time slot fires
// ============================================================
void onDispenseTrigger(int timeSlotIndex) {
  Serial.printf("[Main] Time slot %d triggered\n", timeSlotIndex);

  // Check if any modules are actually assigned to this slot
  int assignedCount = 0;
  for (int m = 0; m < NUM_MODULES; m++) {
    MedModule &mod = moduleGet(m);
    if (mod.slotMask & (1 << timeSlotIndex)) {
      assignedCount++;
    }
  }

  if (assignedCount > 0) {
    // Wait for user confirmation instead of dispensing immediately
    uiShowConfirmDispense(timeSlotIndex);
  } else {
    Serial.println("[Main] No modules assigned to this slot (ignored)");
  }
}

// ============================================================
// Manual dispense — toggles ONE specific module servo to hold position
// ============================================================
void onManualDispense(int moduleIndex) {
  if (moduleIndex < 0 || moduleIndex >= NUM_MODULES)
    return;

  MedModule &mod = moduleGet(moduleIndex);
  Serial.printf("[Main] Manual servo toggle for module %d (%s)\n", moduleIndex,
                mod.name);

  servoToggleManual(moduleIndex);
}

// ============================================================
void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("\n=== Medicine Dispenser Starting ===");

  // I2C Bus
  Wire.begin(I2C_SDA_PIN, I2C_SCL_PIN);
  Wire.setClock(400000);
  Serial.printf("[I2C] Bus OK — SDA=%d, SCL=%d\n", I2C_SDA_PIN, I2C_SCL_PIN);

  // GPIO
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  // Display
  displaySetup();

  // Servo
  servoSetup();

  // WiFi
  wifiSetup();

  // Scheduler (RTC + NVS)
  schedulerSetup();
  schedulerSetCallback(onDispenseTrigger);

  // UI
  uiSetup();
  uiSetManualDispenseCallback(onManualDispense);
  uiSetConfirmDispenseCallback(onConfirmedDispense);

  Serial.println("=== Setup Complete ===");
}

// ============================================================
void loop() {
  uiLoop();
  schedulerLoop();
  wifiLoop();
  delay(10);
}
