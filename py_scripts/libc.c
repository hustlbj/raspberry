#include <unistd.h>
#include <sys/time.h>
void _n10us_delay(int n)
{
	int i = 0;
	int round = 450*n;
	while (i < 400)
		i ++;
}

void main()
{
	struct timeval start, end;
	int i = 0;
	gettimeofday(&start, 0);
	_n10us_delay(1);
	gettimeofday(&end, 0);
	printf("usec: %d-%d=%d\n", end.tv_usec, start.tv_usec, end.tv_usec-start.tv_usec);
}
