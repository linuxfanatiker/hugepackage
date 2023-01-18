#include "standard.h"

extern const int LCD_EN[];

int testeditor(int rows)
{
	int i;
	char buf[100];

	printf ("Displaytyp %d, Reihen: %d, Spalten: %d\n", LCD_TYPE, LCD_ROWS, LCD_COLS);

	for (i=0; i<rows; i++)
	{
		printf("\n%d. Zeile: ", i+1);
		fgets(buf, 100, stdin);
		lcdWriteLine(buf, i);
	}

	return 0;
}

int teststdin()
{
	const int trunc=0;
	char buf[200];
	int result;
	while (fgets(buf, 200, stdin)!=NULL) {
		if (result==2) lcdNewLine();
		result=lcdWriteLine(buf+trunc, -1);
		if (result<2 && result>=0) lcdNewLine();
		gpioDelay(5000);
	}
	return 0;
}

int primaryLoop()
{
	char buf [300];
	if(fgets(buf, 83, stdin)!=NULL) {
//		flarmParseSentence(buf);
		gpioDelay(2000);
	}
}

int main(void)
{
	int errorcode=0;
	if (gpioInitialise()<0) {
		printf("gpioInitialise returned error\n");
		return -1;
	}
	else {
		#ifdef DEBUG
		printf("gpioInitialise OK\n");
		#endif
	}

	init4bit(LCD_E1);



	lcdWriteLine("Hallo", 0);
	lcdWriteLine("Jan", 1);

	sleep(5);

	lcdWriteLine("Hallo", 1);
	lcdWriteLine("Martin", 0);


	sleep(5);

	lcdWriteLine("Hallo", 0);
	lcdWriteLine("Jan", 1);

	while(1) teststdin();



//	init4bit(LCD_E2);
//	init4bit(LCD_E3);
/*
	{
		char *data;
		int i,z;
		teststdin();
		testeditor(6);
		for (z=0; z<LCD_ROWS; z++) {
			printf("\"");
				data=lcdReadLine(z);
				for (i=0; i<LCD_DDRAM_WIDTH; i++) printf("%c", *(data+i));
				free(data);
			printf("\"\n");
		}
	}



	init4bit(LCD_E1);

	send4bit_byte(LCD_E1, 'b', 1, -1);
	send4bit_byte(LCD_E1, 'l', 1, -1);
	send4bit_byte(LCD_E1, 'j', 1, -1);
	send4bit_byte(LCD_E1, 'a', 1, -1);
	send4bit_byte(LCD_E1, 'd', 1, -1);
*/

	return errorcode;
}

