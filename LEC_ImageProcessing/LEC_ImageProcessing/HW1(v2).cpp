#include <iostream>
#include <fstream>
#include <Windows.h>
#include <math.h>

using namespace std;

// Proto type
int smoothRamp(int col);
double equation(int col, double x1, double y1, double x2, double y2);

// Main
int main() {
	int imageSize = 512;
	int bright;

	unsigned char imageBuffer[512][512];

	// 메모리 할당

	for (int col = 0; col < imageSize; col++) {
		bright = smoothRamp(col);
		for (int row = 0; row < imageSize; row++) {
			imageBuffer[row][col] = bright;
		}
	}

	// 파일 저장
	FILE* fp;
	fopen_s(&fp, "HW1-1(v5).raw", "wb");

	fwrite(imageBuffer, sizeof(unsigned char), imageSize * imageSize, fp);
	fclose(fp);

	return 0;
}

int smoothRamp(int col) {
	double brightness;
	if (col < 100)
		brightness = 120;
	else if (col < 200)
		brightness = equation(col, 100, 120, 200, 135);
	else if (col < 280)
		brightness = equation(col, 200, 135, 280, 225);
	else if (col < 300)
		brightness = equation(col, 280, 225, 300, 235);
	else
		brightness = 240;

	return (int)brightness;
}

double equation(int col, double x1, double y1, double x2, double y2) {
	return ((y2 - y1) / (x2 - x1)) * (col - x1) + y1;
}