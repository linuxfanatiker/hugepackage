#include "standard.h"

/* Optimized for 4x20 DISPLAY */

int frontendInit()
{
    #ifdef RASPBERRY
	if (gpioInitialise()<0) {
		printf("gpioInitialise returned error\n");
		return -1;
	}
	else {
		#ifdef DEBUG
		printf("gpioInitialise OK\n");
		#endif
	}
    #else
    #endif

    // Initialize 2 Display-Controllers
    #ifndef LCDEMU
	init4bit(LCD_E1);
	init4bit(LCD_E2);
//    init4bit(LCD_E3);
    #endif
    return 0;
}

int frontendExit()
{
    return 0;
}

int frontendMain()
{
    int key;
	while (1) {
/*        key=getch();
        switch(key) {
            case 'x':   return 0;
            case ERR:   
            default:    break;
        }*/
		frontendGPSStatusPage();
        #ifdef LCDEMU
            lcd_emu_out();
                    printf("End emuout\n");

        #endif
		primaryLoop();
	}
    return -1;
}


int frontendGPSStatusPage()
{
	/*char * line[]={ "GPS Status Page    ",
			"Satellites Rx: %d",
			"%.7s %8s",
			"GPS:%d Baro:%dft" }*/
	char buf[21];
	int satellites=0;
	double latDeg=0;
	double longDeg=0;
	char latNS=0;
	char longEW=0;
	double gpsAlt=0;
	double baroAlt=0;

	lcdWriteLine("GPS Status Page", 0);

//	while(1) {
    {
		if (satellites!=flarmStatus.satellites) {
			satellites=flarmStatus.satellites;
			sprintf(buf, "Satellites: %d", satellites);
			lcdWriteLine(buf, 1);
		}
		if (latDeg!=flarmPosition.latDeg ||
			longDeg!=flarmPosition.longDeg ||
			latNS!=flarmPosition.latNS ||
			longEW!=flarmPosition.longEW) {

			latDeg=flarmPosition.latDeg;
			longDeg=flarmPosition.longDeg;
			latNS=flarmPosition.latNS;
			longEW=flarmPosition.longEW;

			sprintf(buf, "%c%06.1f %c%07.1f", latNS, latDeg, longEW, longDeg);
			lcdWriteLine(buf, 2);
		}
		if (gpsAlt!=flarmPosition.gpsAltitude ||
			baroAlt!=flarmPosition.baroAltitude) {
			gpsAlt=flarmPosition.gpsAltitude;
			baroAlt=flarmPosition.baroAltitude;
			//printf ("GPS-Altitude: %f %c\n", flarmPosition.gpsAltitude, flarmPosition.gpsAltitude_unit);


			sprintf(buf, "GPS %.0lf%c Baro %.0lf%c", gpsAlt, flarmPosition.gpsAltitude_unit, baroAlt, flarmPosition.baroAltitude_unit);
			lcdWriteLine(buf, 3);
		}
	}
	return 0;
}

int frontendTrafficInfoPage()
{
	char buf[21];


	lcdWriteLine("Traffic Info", 0);


	while (1) {
//		if (rx!=flarmStatus.rx) {
//			rx=flarmStatus.rx;
			sprintf(buf, "Currently %d a/c", flarmStatus.rx);
			lcdWriteLine(buf, 1);
//		}
	} // while (1)
	return 0;
}

void printDEBUG(const char * data, ...)
{
}
