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
#ifdef LCDEMU
    int lcd_emu_out();
#endif

