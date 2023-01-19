#include "standard.h"

#define LINE 0
#define COL 1

#define RS(x) x
#define WAITBUSY -1
#define WBUSYNOHANG -2
#define WAITTIME(x) x

#define POSX 0
#define POSY 1

extern const int LCD_EN[];		// Assignments of LCD_EN to Ports ist made in hd44780.h
int		 position[]={0,0};


// returns 0 normally
// returns 1 end of ddram line reached
// returns 2 end of ddram display reached
// returns 4 end of visible line reached
// returns 8 end of visible display reached

int lcdWriteChar(char data)
{
	const int controllerAvail[]=LCD_LINE_CONTROLLERS;
	const int controllerActive=LCD_EN[controllerAvail[position[POSY]]];
	int errorcode;
#ifdef DEBUG
	printf("lcdWriteChar: Sending Character %c -> %d\n", data, controllerActive);
#endif
	switch (data) {
		default:	if (data>0x1F && data<0x7F) {	// omit control characters, only ascii
    					errorcode=send4bit_byte(controllerActive, data, RS(1), WBUSYNOHANG);
				    }
	    			if (errorcode<0) return errorcode;
	    			break;
	}

	if (++position[POSX]>=LCD_DDRAM_WIDTH) {
		position[POSX]=LCD_DDRAM_WIDTH-1;
		if (position[POSY]==(LCD_ROWS-1)) return 2;
		else				  return 1;
	}
	else return 0;
}

int lcdWriteLine(char * data, int line)
{
	const int ddram_offsets[]=LCD_DDRAM_OFFSETS;
	const int controllers[]=LCD_LINE_CONTROLLERS;
	int c;
	int result;

	if (line<0) {
		line=position[POSY];
	}

	if (line<LCD_ROWS) {
		setDDRamAddress(controllers[line], ddram_offsets[line]);
	}

	position[POSX]=0;
	position[POSY]=line;

	for (c=0; c<LCD_DDRAM_WIDTH; c++) {
		if 	(*data>0) result=lcdWriteChar(*(data++));
		else 	result=lcdWriteChar(' ');

		if	(result==0) continue;
		else    return result;
	}

	return 0;
}

char * lcdReadLine(int line)
{
	const int ddram_offsets[]=LCD_DDRAM_OFFSETS;
	const int line_controllers[]=LCD_LINE_CONTROLLERS;
	int address=ddram_offsets[line];
	const int len=LCD_DDRAM_WIDTH;
	int controller;
	char * data;

	if (line>=LCD_ROWS)	return NULL;

	controller=line_controllers[line];
	data=getDDRamData(controller, address, len);
	return data;
}

int lcdBlankLine(int line)
{
	char blanks[LCD_DDRAM_WIDTH+1];
	int i;

	for(i=0; i<LCD_DDRAM_WIDTH; i++) blanks[i]=' ';

	return lcdWriteLine(blanks, line);
}

/* lcdNewLine: 2 Cases:

   Case	1:	posy not yet last row -> shift cursor to next row
   Case 2:	posy already last row -> shift all rows upstairs and cursor on first char

*/

int lcdNewLine() {
	const int ddram_offsets[]=LCD_DDRAM_OFFSETS;
	const int controllers[]=LCD_LINE_CONTROLLERS;
	int errorcode=0;

	if (position[POSY]<(LCD_ROWS-1)) {	// Case 1
		errorcode=setDDRamAddress(controllers[position[POSY]+1], ddram_offsets[position[POSY]+1]);
		if (errorcode==0) {
			position[POSY]++;
			position[POSX]=0;
		} //if
		else {
#ifdef DEBUG
			printf("lcdNewLine: Case1 setDDRamAddress-Error, unkown Display Position\n");
#endif
			return errorcode;
		}
	}
	else {
		lcdInsertLine(position[POSY]);
		errorcode=setDDRamAddress(controllers[position[POSY]], ddram_offsets[position[POSY]]);
		if (errorcode==0) {
			position[POSX]=0;
		} //if
		else {
#ifdef DEBUG
			printf("lcdNewLine: setDDRamAdress-Error, unknown Display Position\n");
#endif
			return errorcode;
		} //else
	} // else

	return errorcode;
}

int lcdInsertLine(int line)
{
	int i;
	// Shiftalgorithm
	if (LCD_ROWS>0) {
		for(i=1; (i<=line && i<LCD_ROWS); i++) {
			lcdMoveLine(i, i-1);
		}
	}
	return 0;
}

int lcdMoveLine(int origin, int destination)
{
	int errorcode=0;
	char *data;
	data=lcdReadLine(origin);
	if (data==NULL) {
		return -1;
	}
	else {
		errorcode= lcdWriteLine(data, destination);
		errorcode+=lcdBlankLine(origin);
		free(data);
	}
	return errorcode;
}

int setDDRamAddress(int controller, int address)
{
	const int CMD_DDRAM=0x80;
	int errorcode;
#ifdef DEBUG
	printf("setDDRamAddress: Set DDram-Address %X on Controller no. %d\n", address, controller);
#endif
	errorcode=send4bit_byte(LCD_EN[controller], (CMD_DDRAM|address), RS(0), -2);
	return errorcode;
}

char * getDDRamData(int controller, int address, int len)
{
	char *data;
	int buf;
	int i;

	data=malloc(len*sizeof(*data));

	setDDRamAddress(controller, address);
	for(i=0; i<len; i++) {
		if (read4bit_byte(LCD_EN[controller], &buf, RS(1), -2)<0) {
			free(data);
			return NULL;
		}
		else *(data+i)=buf;
	}
	return data;
}

int lcdGotoXY(int x, int y) 
{
    const int controllers[]=LCD_LINE_CONTROLLERS;
    const int offsets[]=LCD_DDRAM_OFFSETS;
    int address;
    if (x>=LCD_COLS) return -1;
    if (y>=LCD_ROWS) return -1;

    address=offsets[y]+x;

    position[POSY]=y;
    position[POSX]=x;

    return setDDRamAddress(controllers[y], address);
}

int lcdInstruction(const unsigned char INSTRUCTION)
{
    const int controllers[]=LCD_LINE_CONTROLLERS;
    const int offsets[]=LCD_DDRAM_OFFSETS;
    int i;
    
/*    
int read4bit_byte(int controller, int *data, int rs, int wait_busy)
writeCtrl_waitBusy(data, controller, time_us) send4bit_byte(controller, data, 0, -1);
*/
    for (i=0; i<LCD_CONTROLLERS; i++) {
        if (writeCtrl_waitBusy(INSTRUCTION, i, -1)<0)
            return -1;
    }
    return 0;
}


