import re
import os

filepath = 'src/ui_manager.cpp'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the color palette
old_palette = re.compile(r'// Color Palette — Dark Theme.*?#define COL_DIVIDER 0x31A6  // Subtle divider', re.DOTALL)
new_palette = """// Color Palette — Light Mint "Production" Theme
// ============================================================
#define COL_BG       0xF7DE // Very light mint background
#define COL_CARD     0xFFFF // Clean white for cards
#define COL_PRIMARY  0x2652 // Teal/Mint (#20C997)
#define COL_ACCENT   0x15D0 // Darker teal (#12B886)
#define COL_SUCCESS  0x460A // Green (#40C057)
#define COL_DANGER   0xFA8A // Red (#FA5252)
#define COL_WARN     0xFC62 // Orange
#define COL_TEXT     0x31C8 // Main texts (#343A40)
#define COL_TEXT_INV 0xFFFF // White text (for buttons/headers)
#define COL_TEXT_DIM 0x8472 // Light gray for secondary text (#868E96)
#define COL_BTN      0xEF7D // Default button bg (#E9ECEF)
#define COL_BTN_ON   0x2652 // Active toggle
#define COL_DIVIDER  0xDF1C // Subtle divider lines (#DEE2E6)
#define COL_SHADOW   0xCE59 // Button shadow (#CED4DA)"""

content = old_palette.sub(new_palette, content)

# Instead of using COL_BG as white text, use COL_TEXT_INV where appropriate
content = re.sub(r'btn\(([^;]*?), COL_(PRIMARY|ACCENT|SUCCESS|DANGER), COL_BG\);', r'btn(\1, COL_\2, COL_TEXT_INV);', content)
content = re.sub(r'setTextColor\(COL_BG,\s*COL_(PRIMARY|ACCENT|SUCCESS|DANGER)\);', r'setTextColor(COL_TEXT_INV, COL_\1);', content)
content = re.sub(r'setTextColor\(COL_BG,\s*col\);', r'setTextColor(COL_TEXT_INV, col);', content)

# Redefine the btn function to add drop shadows 
old_btn_pattern = re.compile(r'static void btn\(int x, int y, int w, int h, const char \*txt, uint16_t bg,\s*uint16_t fg\) \{.*?lcd\.drawString\(txt, x \+ w / 2, y \+ h / 2\);\s*\}', re.DOTALL)
new_btn = """static void btn(int x, int y, int w, int h, const char *txt, uint16_t bg,
                uint16_t fg) {
  auto &lcd = canvas;
  // Button shadow
  if (bg != COL_BG && bg != COL_CARD) {
    lcd.fillRoundRect(x, y + 2, w, h, 6, COL_SHADOW);
  }
  lcd.fillRoundRect(x, y, w, h, 6, bg);
  if (bg == COL_BTN) {
    lcd.drawRoundRect(x, y, w, h, 6, COL_DIVIDER);
  }
  lcd.setFont(&fonts::FreeSans9pt7b);
  lcd.setTextDatum(middle_center);
  lcd.setTextColor(fg, bg);
  lcd.drawString(txt, x + w / 2, y + h / 2 - 1);
}

static void drawShadowCard(int x, int y, int w, int h) {
  canvas.fillRoundRect(x, y+3, w, h, 8, COL_SHADOW);
  canvas.fillRoundRect(x, y, w, h, 8, COL_CARD);
  // canvas.drawRoundRect(x, y, w, h, 8, COL_DIVIDER); // Optional subtle border
}"""

content = old_btn_pattern.sub(new_btn, content)

# Replace standard fillRoundRect cards with drawShadowCard
content = re.sub(r'lcd\.fillRoundRect\(([^,]+?),\s*([^,]+?),\s*([^,]+?),\s*([^,]+?),\s*8,\s*COL_CARD\);', r'drawShadowCard(\1, \2, \3, \4);', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("UI rewrite applied successfully.")
