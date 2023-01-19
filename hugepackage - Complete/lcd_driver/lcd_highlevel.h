int lcdWriteChar(char);
int lcdWriteLine(char*, int);
char * lcdReadLine(int);
int lcdBlankLine(int);
int lcdNewLine(void);
int lcdInsertLine(int);
int lcdMoveLine(int, int);
int setDDRamAddress(int, int);
char * getDDRamData(int, int, int);
int lcdGotoXY(int, int);
int lcdInstruction();
#ifdef LCDEMU
    int lcd_emu_out();
#endif

#define LCD_INSTR_CLRSCR  0x01
#define LCD_INSTR_CURSON  0x0F
#define LCD_INSTR_CURSOFF 0x0D

