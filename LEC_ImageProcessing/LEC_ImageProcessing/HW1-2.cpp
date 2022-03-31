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

	unsigned char imageBuffer[512][512];


	FILE* rawfile;
	fopen_s(&rawfile, "HW1-1.raw", "rb");
	fread(imageBuffer, sizeof(char), imageSize * imageSize, rawfile);

	// ��Ʈ�� ��� �߰�
	char inputImage[50] = "lena_bmp_512x512_new.bmp";
	FILE* infile;

	fopen_s(&infile, inputImage, "rb"); // "Read Binary"

	BITMAPFILEHEADER HF; //�������� ����(C�� ����Ǿ� ����)
	BITMAPINFOHEADER IF; //�������� ����
	RGBQUAD hRGB[256];

	fread(&HF, sizeof(BITMAPFILEHEADER), 1, infile);
	fread(&IF, sizeof(BITMAPINFOHEADER), 1, infile);
	fread(hRGB, sizeof(RGBQUAD), 256, infile);

	// BMP�� ����
	FILE* outfile;
	fopen_s(&outfile, "HW1-2.bmp", "wb");
	fwrite(&HF, sizeof(BITMAPFILEHEADER), 1, outfile);
	fwrite(&IF, sizeof(BITMAPINFOHEADER), 1, outfile);
	fwrite(hRGB, sizeof(RGBQUAD), 256, outfile);
	fwrite(imageBuffer, sizeof(unsigned char), imageSize * imageSize, outfile);
	fclose(rawfile);
	fclose(outfile);

	return 0;
}