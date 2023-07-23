#include <reg51.h>
sbit SW = P2 ^ 7;
void MSDelay(unsigned int value)
{
    unsigned int x, y;
    for (x = 0; x < 1275; x++)
        for (y = 0; y < value; y++)
            ;
}
void main()
{
    SW = 1;
    while (1)
    {
        if (SW == 0)
        {
            P1 = 0x66;
            MSDelay(50);
            P1 = 0xCC;
            MSDelay(50);
            P1 = 0x99;
            MSDelay(50);
            P1 = 0x33;
            MSDelay(50);
        }
        else
        {
            P1 = 0x66;
            MSDelay(50);
            P1 = 0x33;
            MSDelay(50);
            P1 = 0x99;
            MSDelay(50);
            P1 = 0xCC;
            MSDelay(50);
        }
    }
}