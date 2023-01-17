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

int testfileout()
{
	const char filename[]="/tmp/testfile.txt";
	char buf[200];
	FILE * fp;
	int line=0;
	fp=fopen(filename, "r");
	while (fgets(buf, 200, fp)!=NULL) {
		lcdWriteLine(buf, line);
		if (++line>=LCD_ROWS) line=0;
	}
	fclose(fp);
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

int testuart()
{
	char  buf[300];
	int  buf2=0;
	int  lastbuf=0;
	if (INIT_UART()>=0) {;

	while(1) {
		lastbuf=buf2;
		buf2=readUartNonPolling();
		if (buf2>32) {
			printf("%c(%x)\n", buf2, buf2);
			lcdWriteChar(buf2);
		}
		else if (buf2==0xa) {
			printf("LF(%x)", buf2);
			if (lastbuf!=buf2) lcdNewLine();
		}

		/*readStringUartNonPolling(buf, 299);
		printf("%s", buf);
		lcdWriteLine(buf, -1);*/
	}

	CLOSE_UART();
	}

	else {
		printf("UART_INIT_ERROR\n");
		return -1;
	}
}

int primaryLoop()
{
/*	char * flarm;
	flarm=flarmUartGetLine();
	if (flarm!=NULL) flarmParseSentence(flarm);
	free(flarm);*/
	char buf [300];
	if(fgets(buf, 83, stdin)!=NULL) {
		flarmParseSentence(buf);
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
	init4bit(LCD_E2);
	init4bit(LCD_E3);

	if (INIT_UART()>=0) {
		frontendTrafficInfoPage();
		frontendGPSStatusPage();
	}

	CLOSE_UART();

	return 0;

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


/*
	init4bit(LCD_E2);

	send4bit_byte(LCD_E2, 'b', 1, -1);
	send4bit_byte(LCD_E2, 'l', 1, -1);
	send4bit_byte(LCD_E2, 'j', 1, -1);
	send4bit_byte(LCD_E2, 'a', 1, -1);
	send4bit_byte(LCD_E2, 'd', 1, -1);

	send4bit_byte(LCD_E2, CMD_SETDDRAM|0x40, 0, -1);
	send4bit_byte(LCD_E2, 'K', 1, -1);
	send4bit_byte(LCD_E2, 'u', 1, -1);
	send4bit_byte(LCD_E2, 'r', 1, -1);
	send4bit_byte(LCD_E2, 'v', 1, -1);
	send4bit_byte(LCD_E2, 'a', 1, -1);
	send4bit_byte(LCD_E2, CMD_DISPLAY|PAR_DISPLAY_ON|PAR_CURSOR_OFF, 0, -1);
*/



	gpioTerminate();
	return errorcode;
}

