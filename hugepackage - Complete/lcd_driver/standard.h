//#define DEBUG
#define NCURSES

#define SIMULATION_FACTOR 8

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef OUTPUT_LCD
    #ifdef RASPBERRY	
        #include <pigpio.h>
    	#include "hd44780.h"
    	#include "lcd_highlevel.h"
    #elif defined LCDEMU
    	#include "lcd_highlevel.h"
    #else
        #error "OUTPUT not defined"
    #endif
	#include "displayconfig.h"
#endif
#include <unistd.h>
#include <termios.h>
#include <fcntl.h>
#include <time.h>
#include "flarm.h"
#include "frontend.h"
#include "main.h"
#include "uart.h"
#include "fileio.h"
