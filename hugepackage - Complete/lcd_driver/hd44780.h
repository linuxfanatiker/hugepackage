#define HUGEPACKAGE

#ifdef HUGEPACKAGE
#define LCD_D4 6
#define LCD_D5 13
#define LCD_D6 19
#define LCD_D7 26
#define LCD_E1 21
#define LCD_E2 21
#define LCD_E3 21
#define LCD_EN_ORDER {LCD_E1, LCD_E2, LCD_E3}
#define LCD_RS 16
#define LCD_RW 20
#endif

#ifdef FLARM
#define LCD_D4 7
#define LCD_D5 8
#define LCD_D6 25
#define LCD_D7 11
#define LCD_E1 10
#define LCD_E2 18
#define LCD_E3 24
#define LCD_EN_ORDER {LCD_E3, LCD_E2, LCD_E3}
#define LCD_RS 9
#define LCD_RW 4
#endif

// minimum time for waiting after instructions in usec
// increase value, if raspberry to quick for lcd-driver
#define LCD_MIN_WAIT 50

#define BUSY 1
#define IDLE 0


/* AVR-LCD Compatibility */

#define writeCtrl_waitTime(data, controller, time_us) send4bit_byte(controller, data, 0, time_us)
#define writeCtrl_waitBusy(data, controller, time_us) send4bit_byte(controller, data, 0, -1)
#define writeData_waitBusy(data, controller) send4bit_byte(controller, data, 1, -1)

int set_Pinmodes(void);
int startup_LCD(void);

int send4bit_byte(int, int, int, int);
int send4bit_nibble(int, int, int, int);
int read4bit_byte(int, int *, int, int);
int read4bit_nibble(int, int *, int, int);

int check_busyflag(int, int *);

void init4bit(int controller);
