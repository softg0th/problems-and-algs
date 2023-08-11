#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool cube_checker(int volume, int side) {
    int powered;
    int step;
    step = 3;
    powered = pow(side, step);
    if (powered == volume)
    {
        return true;
    }
    return false;
}

int main()
{
    int volume, side;
    bool result;
    scanf("%d", &volume);
    scanf("%d", &side);
    result = cube_checker(volume, side);
    printf("%s\n", result ? "true":"false");
    return 0;
}