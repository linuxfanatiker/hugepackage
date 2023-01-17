#include "standard.h"

#define BFLG_ERROR_TIMEOUT -1

const int LCD_EN[]=LCD_EN_ORDER;

int set_Pinmodes()
{
	const int output[]={LCD_D4, LCD_D5, LCD_D6, LCD_D7, LCD_E1, LCD_E2, LCD_E3, LCD_RS, LCD_RW, -1};
	int i;
	int errorcode=0;

	for (i=0; output[i]!=-1; i++) {
		gpioSetMode(output[i], PI_OUTPUT);
		gpioWrite(output[i], 0);
	}
	return errorcode;
}

int send4bit_byte(int controller, int data, int rs, int wait_busy)
{
	int errorcode;

	errorcode=send4bit_nibble(controller, (data>>4), rs, wait_busy);		// Sending MSB-Nibble
	if (errorcode<0) {
#ifdef DEBUG
		printf("send4bit_byte Error on upper nibble: %d\n", errorcode);
#endif
		return -1;
	}

	errorcode=send4bit_nibble(controller, data, rs, wait_busy);			// Sending LSB-Nibble
	if (errorcode<0) {
#ifdef DEBUG
		printf("send4bit_byte Error on lower nibble: %d\n", errorcode);
#endif
		return -1;
	}
	return 0;
}

int send4bit_nibble(int controller, int nibble, int rs, int wait_busy)
{
	const int busymax=100;
	int i=0;
	int ac;

	// Send Low Nibble
	// Check Busy
	if (wait_busy<0) {
		while(check_busyflag(controller, &ac)==BUSY) {
			gpioDelay(1);
			if (wait_busy==-2 && i++>=busymax) {
#ifdef DEBUG
				printf("send4bit_nibble: BusyTimeout ERROR\n");
#endif
				return BFLG_ERROR_TIMEOUT;
			} // if
		} // while
	} // if
	else gpioDelay(wait_busy);

	gpioWrite(LCD_RS, rs);
	gpioWrite(LCD_RW, 0);
	gpioWrite(LCD_D4,  (nibble    &1));
	gpioWrite(LCD_D5, ((nibble>>1)&1));
	gpioWrite(LCD_D6, ((nibble>>2)&1));
	gpioWrite(LCD_D7, ((nibble>>3)&1));

	gpioWrite(controller, 1);
	gpioDelay(LCD_MIN_WAIT);
	gpioWrite(controller, 0);
//	gpioDelay(LCD_MIN_WAIT);

	return ac;
}

int read4bit_byte(int controller, int *data, int rs, int wait_busy)
{
	int errorcode;
	int buf;

	errorcode=read4bit_nibble(controller, &buf, rs, -2);		// Sending MSB-Nibble
	if (errorcode<0) {
#ifdef DEBUG
		printf("read4bit_byte Error on upper nibble: %d\n", errorcode);
#endif
		return -1;
	}
	*data=buf<<4;

	errorcode=read4bit_nibble(controller, &buf, rs, 1);			// Sending LSB-Nibble
	if (errorcode<0) {
#ifdef DEBUG
		printf("read4bit_byte Error on lower nibble: %d\n", errorcode);
#endif
		return -1;
	}
	*data|=buf;
	return 0;
}

int read4bit_nibble(int controller, int * nibble, int rs, int wait_busy)
{
	const int busymax=100;
	int i=0;
	int ac;
	// Send Low Nibble
	// Check Busy
	if (wait_busy<0) {
		while(check_busyflag(controller, &ac)==BUSY) {
			gpioDelay(1);
			if (wait_busy==-2 && i++>=busymax) {
#ifdef DEBUG
				printf("send4bit_nibble: BusyTimeout ERROR\n");
#endif
				return BFLG_ERROR_TIMEOUT;
			} // if
		} // while
	} // if
	else gpioDelay(wait_busy);


	gpioSetMode(LCD_D7, PI_INPUT);
	gpioSetMode(LCD_D6, PI_INPUT);
	gpioSetMode(LCD_D5, PI_INPUT);
	gpioSetMode(LCD_D4, PI_INPUT);

	gpioWrite(LCD_RS, rs);
	gpioWrite(LCD_RW, 1);

	gpioWrite(controller, 1);
	gpioDelay(LCD_MIN_WAIT);

	*nibble =gpioRead(LCD_D4);
	*nibble|=gpioRead(LCD_D5)<<1;
	*nibble|=gpioRead(LCD_D6)<<2;
	*nibble|=gpioRead(LCD_D7)<<3;

	gpioWrite(controller, 0);
	//gpioDelay(LCD_MIN_WAIT);

	gpioSetMode(LCD_D7, PI_OUTPUT);
	gpioSetMode(LCD_D6, PI_OUTPUT);
	gpioSetMode(LCD_D5, PI_OUTPUT);
	gpioSetMode(LCD_D4, PI_OUTPUT);

	gpioWrite(LCD_D7, 0);
	gpioWrite(LCD_D6, 0);
	gpioWrite(LCD_D5, 0);
	gpioWrite(LCD_D4, 0);

	return 0;
}

int check_busyflag(int controller_enable, int * pAc)
{
	int busyFlagLevel;

	gpioSetMode(LCD_D7, PI_INPUT);			// Set D7 for input
	gpioSetMode(LCD_D6, PI_INPUT);			// Set D6 for input
	gpioSetMode(LCD_D5, PI_INPUT);			// Set D5 for input
	gpioSetMode(LCD_D4, PI_INPUT);			// Set D4 for input

	gpioWrite(LCD_RS, 0);				// RS 0
	gpioWrite(LCD_RW, 1);				// RW 1
	gpioWrite(controller_enable, 1);		// ENABLE
	gpioDelay(LCD_MIN_WAIT);			// Wait some usec
	busyFlagLevel	 =gpioRead(LCD_D7);			// Read busyFlag
	*pAc 		 =gpioRead(LCD_D6)<<6;			// Read AC upper nibble
	*pAc		|=gpioRead(LCD_D5)<<5;
	*pAc		|=gpioRead(LCD_D4)<<4;
	gpioWrite(controller_enable, 0);		// DISABLE
	gpioDelay(LCD_MIN_WAIT);

	gpioWrite(LCD_RS, 0);				// RS 0
	gpioWrite(LCD_RW, 1);				// RW 1
	gpioWrite(controller_enable, 1);		// ENABLE
	gpioDelay(LCD_MIN_WAIT);			// Wait some usec
	*pAc|=gpioRead(LCD_D7)<<3;			// Read busyFlag
	*pAc|=gpioRead(LCD_D6)<<2;			// Read AC upper nibble
	*pAc|=gpioRead(LCD_D5)<<1;
	*pAc|=gpioRead(LCD_D4);
	gpioWrite(controller_enable, 0);		// DISABLE
//	gpioDelay(LCD_MIN_WAIT);
	gpioWrite(LCD_RW, 0);				// RW to default LOW
	gpioSetMode(LCD_D7, PI_OUTPUT);			// D7 to default OUTPUT
	gpioSetMode(LCD_D6, PI_OUTPUT);			// D6 to default OUTPUT
	gpioSetMode(LCD_D5, PI_OUTPUT);			// D5 to default OUTPUT
	gpioSetMode(LCD_D4, PI_OUTPUT);			// D4 to default OUTPUT
	gpioWrite(LCD_D7, 0);				// All data to default Low
	gpioWrite(LCD_D6, 0);
	gpioWrite(LCD_D5, 0);
	gpioWrite(LCD_D4, 0);

#ifdef DEBUG
	if (busyFlagLevel==BUSY) printf("Controller ist Busy\n");
	else			 printf("Controller ist idle\n");
#endif

	return busyFlagLevel;
}

/* Init and Set LCD in 4 Bit Mode */
void init4bit(int controller)
{
	gpioDelay(15000);							// Wait at least 15ms
	send4bit_nibble(controller, 0b00000011, 0, LCD_MIN_WAIT);		// Send D5 D4
	gpioDelay(6000);
	send4bit_nibble(controller, 0b00000011, 0, LCD_MIN_WAIT);		// Send D5 D4
	gpioDelay(200);
	send4bit_nibble(controller, 0b00000011, 0, LCD_MIN_WAIT);		// Send D5
	send4bit_nibble(controller, 0b00000010, 0, -2);				// Erste Funkion mit Busy Flag

	send4bit_byte(controller,   0b00101000, 0, -2);		// Zeilen und Character Setzen
	send4bit_byte(controller,   0b00001101, 0, -2);		// Display an, Cursor blink
	send4bit_byte(controller,   0b00000110, 0, -2);		// Set Increment
	send4bit_byte(controller,   0b00000001, 0, -2);		// Clear Screen

	gpioDelay(10000);
}
