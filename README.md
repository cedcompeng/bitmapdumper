# Bitmap Dumper for ePaper Code

The Python script generates code for a 208 x 112 pixel monochrome Splash screen bitmap as used in the [E-paper Shield Kit](https://www.crowdsupply.com/soniktech/e-paper-shield-kit)

## Getting Started

The E-paper software can be found at [github.com/pdp7/TeensyEpaperShield](https://github.com/pdp7/TeensyEpaperShield)

The script requires Python 2.7 and a bitmap editor to draw the image.

### Bitmap Setup

The bitmap must be drawn mirrored and on it's side to form a 112 x 208 pixel images. To create readable text, the text has to be mirrored then rotated clockwise.

Save the bitmap in monochrome format as a 112 x 208 pixel image.

## Usage

Type the following to generate ```output.c``` from the source bitmap ```logo.bmp```:

```
python bitmapdumper.py logo.bmp > output.c
```

## Acknowledgments

Thanks Jarek at [soniktech.com](http://soniktech.com/) for crowd funding the E-paper adapter board and making the code available.

This script is provided by [Cedric Computer Engineering](http://www.cedric.com.au/)
