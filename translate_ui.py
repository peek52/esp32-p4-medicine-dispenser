import re

file_path = "d:\\project\\xx\\src\\ui_manager.cpp"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    # Fonts
    'canvas.setFont(&fonts::FreeSans9pt7b);': 'canvas.setFont(&thaiFont16);',
    'lcd.setFont(&fonts::FreeSans9pt7b);': 'lcd.setFont(&thaiFont16);',
    'canvas.setFont(&fonts::FreeSansBold9pt7b);': 'canvas.setFont(&thaiFont16);',
    'lcd.setFont(&fonts::FreeSansBold9pt7b);': 'lcd.setFont(&thaiFont16);',
    'canvas.setFont(&fonts::FreeSansBold12pt7b);': 'canvas.setFont(&thaiFont24);',
    'lcd.setFont(&fonts::FreeSansBold12pt7b);': 'lcd.setFont(&thaiFont24);',
    'canvas.setFont(&fonts::FreeSans12pt7b);': 'canvas.setFont(&thaiFont24);',
    'lcd.setFont(&fonts::FreeSans12pt7b);': 'lcd.setFont(&thaiFont24);',
    'canvas.setFont(&fonts::FreeSansBold18pt7b);': 'canvas.setFont(&thaiFont24);',
    'lcd.setFont(&fonts::FreeSansBold18pt7b);': 'lcd.setFont(&thaiFont24);',
    'canvas.setFont(&fonts::FreeSansBold24pt7b);': 'canvas.setFont(&thaiFont24);',
    'lcd.setFont(&fonts::FreeSansBold24pt7b);': 'lcd.setFont(&thaiFont24);',
    'canvas.setFont(&fonts::Font2);': 'canvas.setFont(&thaiFont14);',
    'lcd.setFont(&fonts::Font2);': 'lcd.setFont(&thaiFont14);',

    # Slot labels
    '{"M.Bf", "M.Af", "N.Bf", "N.Af",\n                                                "E.Bf", "E.Af", "Bed"}': '{"เช้า.ก", "เช้า.ห", "เที่ยง.ก", "เที่ยง.ห",\n                                                "เย็น.ก", "เย็น.ห", "ก่อนนอน"}',
    '{"Morning", "Noon", "Evening", "Bedtime"}': '{"เช้า", "กลางวัน", "เย็น", "ก่อนนอน"}',

    # Mod names
    '"Slot 1",  "Slot 2",      "Slot 3",    "Slot 4",    "Slot 5",\n    "Slot 6"': '"ช่อง 1",  "ช่อง 2",      "ช่อง 3",    "ช่อง 4",    "ช่อง 5",\n    "ช่อง 6"',
    '"Paracetamol", "Vitamin C", "Antacid",   "Cough Med",\n    "Allergy", "Antibiotic",  "Ibuprofen", "Omeprazole"': '"พาราฯ", "วิตามินซี", "ยาแก้ปวดท้อง",   "ยาแก้ไอ",\n    "ยาแก้แพ้", "ยาฆ่าเชื้อ",  "ไอบูโพรเฟน", "ยาลดกรด"',

    # Home Screen
    '"Medicine Dispenser"': '"ระบบจ่ายยาอัตโนมัติ"',
    '"Next: %s  %02d:%02d"': '"คิวถัดไป: %s  %02d:%02d"',
    '"No upcoming schedule"': '"ไม่มีตารางจ่ายยา"',
    'on ? "Schedule: ON" : "Schedule: OFF"': 'on ? "ตั้งเวลา: เปิด" : "ตั้งเวลา: ปิด"',
    '"Schedule", COL_PRIMARY': '"ตารางเวลา", COL_PRIMARY',
    '"Modules", COL_ACCENT': '"โมดูลยา", COL_ACCENT',
    '"Dispense", COL_DANGER': '"จ่ายยา", COL_DANGER',
    '"Auto Schedule:"': '"จ่ายอัตโนมัติ:"',
    'on ? "ON" : "OFF"': 'on ? "เปิด" : "ปิด"',

    # Schedule Screen
    '"Schedule", 240': '"ตารางเวลา", 240',
    '"Back"': '"กลับ"',
    '"Before"': '"ก่อนอาหาร"',
    '"After"': '"หลังอาหาร"',
    '"Time"': '"เวลา"',
    't1.enabled ? "ON" : "--"': 't1.enabled ? "เปิด" : "--"',
    't2.enabled ? "ON" : "--"': 't2.enabled ? "เปิด" : "--"',
    't6.enabled ? "ON" : "--"': 't6.enabled ? "เปิด" : "--"',

    # Time Picker
    '"Set Time - %s"': '"ตั้งเวลา - %s"',
    '"Hour"': '"ชั่วโมง"',
    '"Min"': '"นาที"',
    '"Save"': '"บันทึก"',
    '"Cancel"': '"ยกเลิก"',

    # Modules Screen
    '"Medicine Modules"': '"จัดการโมดูลยา"',
    '"< Prev"': '"< ก่อนหน้า"',
    '"Next >"': '"ถัดไป >"',

    # Module Detail
    '"Module %d"': '"ตลับยาที่ %d"',
    '"Name:"': '"ชื่อยา:"',
    '"Change"': '"เปลี่ยน"',
    '"Qty:"': '"จำนวน:"',
    '"Dispense at:"': '"จ่ายเวลา:"',

    # Dispensing / Result
    '"Dispensing..."': '"กำลังทำงาน..."',
    '"Module %d: %s"': '"ตลับที่ %d: %s"',
    '"OK"': '"OK"',
    '"X"': '"X"',
    'success ? "Dispensed!" : "Error!"': 'success ? "จ่ายยาสำเร็จ!" : "เกิดข้อผิดพลาด!"',
    '"Returning home..."': '"กำลังกลับหน้าหลัก..."',

    # Manual Dispense Screen
    '"Manual Dispense"': '"สั่งจ่ายยาแมนนวล"',
    '"Qty: %d"': '"คงเหลือ: %d"',
    '"Home"': '"กลับตำแหน่ง"',
    '"Empty"': '"ยาหมด"'
}

for k, v in replacements.items():
    text = text.replace(k, v)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Replacement complete.")
