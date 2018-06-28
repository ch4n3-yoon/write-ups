#include <stdio.h>

int main()
{
	char input[31] = "f9+qH,8?#qN9W5T6l]KY=VU?]VYgUk";
	char v15[] = "Marri4g3";
	char v16[] = "ApPLeS0da";
	char v18[] = "crypt4Nalysis";

	int i, j, k, l, m, n;

	for ( n = 0; n <= 14; ++n )
    		input[n + 15] -= 15;

	for ( m = 0; m <= 5; ++m )
    		input[m + 9] += 8;

	for ( l = 0; l <= 8; ++l )
    		input[l] += 10;

	for ( k = 0; k <= 12; ++k )
    		input[k + 17] ^= v18[k];

	for ( j = 0; j <= 7; ++j )
    		input[j + 9] ^= v15[j];

	for ( i = 0; i <= 8; ++i )
    		input[i] ^= v16[i];


	printf("%s",input);
}
