#include <wiringPi.h>
int main()
{
	wiringPiSetup();
	pinMode(25, OUTPUT);
	for(;;)
	{
		digitalWrite(25, HIGH);
		delay(500);
		digitalWrite(25, LOW);
		delay(500);
	}
}
