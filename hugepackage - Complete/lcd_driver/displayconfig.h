// Vordefinierte Displaytypen

#define WINTEK 1
#define TC1602 2
#define _204B 3

#define LCD_BRAND _204B

#define LCD_4X201324 4
#define LCD_2X2X     5
#define LCD_2X16     6

// ----------------------------------------------------------


#if	LCD_BRAND == WINTEK
#define LCD_TYPE LCD_2X2X
#endif

#if	LCD_BRAND == TC1602
#define LCD_TYPE LCD_2X16
#endif

#if	LCD_BRAND == _204B
#define LCD_TYPE LCD_4X201324

#endif

// LCD-DISPLAY-DDRAM setzen

#if   LCD_TYPE == LCD_2X16
#define	LCD_CONTROLLERS 1
#define LCD_ROWS 2
#define LCD_COLS 16
#define LCD_DDRAM_OFFSETS {0x0, 0x40}
#define LCD_DDRAM_WIDTH 0x10
#define LCD_LINE_CONTROLLERS {0, 0}

#elif LCD_TYPE == LCD_2X2X
#define	LCD_CONTROLLERS 2
#define LCD_ROWS 4
#define LCD_COLS 27
#define LCD_DDRAM_OFFSETS {0x0, 0x40, 0x0, 0x40}
#define LCD_DDRAM_WIDTH 0x1b
#define LCD_LINE_CONTROLLERS {0, 0, 1, 1}

#elif LCD_TYPE == LCD_4X201324
#define LCD_CONTROLLERS 1
#define LCD_ROWS 4
#define LCD_COLS 20
#define LCD_DDRAM_OFFSETS {0x0, 0x40, 0x14, 0x54}
#define LCD_DDRAM_WIDTH 0x14
#define LCD_LINE_CONTROLLERS {0, 0, 0, 0}

#endif

