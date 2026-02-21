import re

file_path = "d:\\project\\xx\\src\\ui_manager.cpp"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    # Fonts
    'canvas.setFont(&thaiFont16);': 'canvas.setFont(&fonts::FreeSans9pt7b);',
    'lcd.setFont(&thaiFont16);': 'lcd.setFont(&fonts::FreeSans9pt7b);',
    'canvas.setFont(&thaiFont24);': 'canvas.setFont(&fonts::FreeSansBold12pt7b);',
    'lcd.setFont(&thaiFont24);': 'lcd.setFont(&fonts::FreeSansBold12pt7b);',
    'canvas.setFont(&thaiFont14);': 'canvas.setFont(&fonts::Font2);',
    'lcd.setFont(&thaiFont14);': 'lcd.setFont(&fonts::Font2);',

    # Slot labels
    '{"เช้า.ก", "เช้า.ห", "เที่ยง.ก", "เที่ยง.ห",\n                                                "เย็น.ก", "เย็น.ห", "ก่อนนอน"}': '{"M.Bf", "M.Af", "N.Bf", "N.Af",\n                                                "E.Bf", "E.Af", "Bed"}',
    '{"เช้า", "กลางวัน", "เย็น", "ก่อนนอน"}': '{"Morning", "Noon", "Evening", "Bedtime"}',

    # Mod names
    '"ช่อง 1",  "ช่อง 2",      "ช่อง 3",    "ช่อง 4",    "ช่อง 5",\n    "ช่อง 6"': '"Slot 1",  "Slot 2",      "Slot 3",    "Slot 4",    "Slot 5",\n    "Slot 6"',
    '"พาราฯ", "วิตามินซี", "ยาแก้ปวดท้อง",   "ยาแก้ไอ",\n    "ยาแก้แพ้", "ยาฆ่าเชื้อ",  "ไอบูโพรเฟน", "ยาลดกรด"': '"Paracetamol", "Vitamin C", "Antacid",   "Cough Med",\n    "Allergy", "Antibiotic",  "Ibuprofen", "Omeprazole"',

    # Home Screen
    '"ระบบจ่ายยาอัตโนมัติ"': '"Medicine Dispenser"',
    '"คิวถัดไป: %s  %02d:%02d"': '"Next: %s  %02d:%02d"',
    '"ไม่มีตารางจ่ายยา"': '"No upcoming schedule"',
    'on ? "ตั้งเวลา: เปิด" : "ตั้งเวลา: ปิด"': 'on ? "Schedule: ON" : "Schedule: OFF"',
    '"ตารางเวลา", COL_PRIMARY': '"Schedule", COL_PRIMARY',
    '"โมดูลยา", COL_ACCENT': '"Modules", COL_ACCENT',
    '"จ่ายยา", COL_DANGER': '"Dispense", COL_DANGER',
    '"จ่ายอัตโนมัติ:"': '"Auto Schedule:"',
    'on ? "เปิด" : "ปิด"': 'on ? "ON" : "OFF"',

    # Schedule Screen
    '"ตารางเวลา", 240': '"Schedule", 240',
    '"กลับ"': '"Back"',
    '"ก่อนอาหาร"': '"Before"',
    '"หลังอาหาร"': '"After"',
    '"เวลา"': '"Time"',
    't1.enabled ? "เปิด" : "--"': 't1.enabled ? "ON" : "--"',
    't2.enabled ? "เปิด" : "--"': 't2.enabled ? "ON" : "--"',
    't6.enabled ? "เปิด" : "--"': 't6.enabled ? "ON" : "--"',

    # Time Picker
    '"ตั้งเวลา - %s"': '"Set Time - %s"',
    '"ชั่วโมง"': '"Hour"',
    '"นาที"': '"Min"',
    '"บันทึก"': '"Save"',
    '"ยกเลิก"': '"Cancel"',

    # Modules Screen
    '"จัดการโมดูลยา"': '"Medicine Modules"',
    '"< ก่อนหน้า"': '"< Prev"',
    '"ถัดไป >"': '"Next >"',

    # Module Detail
    '"ตลับยาที่ %d"': '"Module %d"',
    '"ชื่อยา:"': '"Name:"',
    '"เปลี่ยน"': '"Change"',
    '"จำนวน:"': '"Qty:"',
    '"จ่ายเวลา:"': '"Dispense at:"',

    # Dispensing / Result
    '"กำลังทำงาน..."': '"Dispensing..."',
    '"ตลับที่ %d: %s"': '"Module %d: %s"',
    '"OK"': '"OK"',
    '"X"': '"X"',
    'success ? "จ่ายยาสำเร็จ!" : "เกิดข้อผิดพลาด!"': 'success ? "Dispensed!" : "Error!"',
    '"กำลังกลับหน้าหลัก..."': '"Returning home..."',

    # Manual Dispense Screen
    '"สั่งจ่ายยาแมนนวล"': '"Manual Dispense"',
    '"คงเหลือ: %d"': '"Qty: %d"',
    '"กลับตำแหน่ง"': '"Home"',
    '"ยาหมด"': '"Empty"'
}

for k, v in replacements.items():
    text = text.replace(k, v)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Replacement complete.")
