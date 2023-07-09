## DoomRecolor

A script for quick palette swapping of images.
Originally intended to use with Doom graphics.
Requires Python 3 and OpenCV 2 (`opencv-python`) library to run.

### Usage

Designed to be rand from commend line. To invoke, run:

```bash
python3 path/to/recolor.py [-h] -c COLOR_IMAGE [-m [MULTIPLY]] -o OUTPUT_DIR [VALUE_IMAGES...]
```

Options and parameters:
- `-h` — displays a help text. _Optional parameter._
- `-m [MULTIPLY]` — multiply flag and optional brightness scale.
Multiplies the value channels of the color image and the value image together,
instead of replacing the former's value with the latter.
Acts as if the value is a floating point number in range 0..1.
If used without specifying brightness, it will scale the brightness down to unsigned byte range,
usually resulting in the image being really dim.
Can optionally be supplied a brightness parameter (as a number in range 0..255).
A brightness value of 128 will result in an imagle half as dark as without brightness correction.
_Optional parameter with optional value._
- `-o OUTPUT_DIR` — directory to which output the results.
As this script is intended for batch processing, it's assumed that the outputs have the value images' filenames,
and are saved to a different directory.
**Mandatory parameter.**
- `-c COLOR_IMAGE` — the image whose color (H and S channels) will be used.
**Mandatory parameter.**
- `VALUE_IMAGES` — a space-separated/wildcarded list of images that will be used as value inputs
(V and alpha channels).

### Doom graphics workflow
- open a WAD with graphics in SLADE
- select some graphics, right-click and pick _Graphics -> export as PNG_
- use the script on the exported graphics
- optionally tweak them by hand in grhaphics edition software
- drag and drop the files into your own WAD in SLADE
- right-click your imported graphics, pick _Graphics -> convert to..._
- select either _Doom gfx (paletted)_ or _Doom flat (paletted)_ depending on what you need
- hit _Convert All_

###  Examples

Say, you have the below couple images prepared, along with an `out` directory.

![image](https://github.com/streaki/DoomRecolor/assets/65075598/fd08483d-a889-4de2-adb8-56d0adf2456d)

#### Example 1:
You want to have blue versions of the `MWALL` patches, and output them to the `out` directory.
In order to do it, run:
```bash
python3 path/to/recolor.py -c COMP03_2.png -o out MWALL4_2.png MWALL5_1.png
```
And here's the results, inside the `out` directory:

![image](https://github.com/streaki/DoomRecolor/assets/65075598/6e95217c-9335-4fe0-9432-fa5b203e2baf)

#### Example 2:
Now, you want a wooden looking version of the `MWALL` patches, and output them to the `out` directory.
You want to preserve the wooden texture along with the monster faces, so instead of overriding the value,
you pick the `-m` (multiply) option, with brightness correction set to 130, as the input images are pretty dark:
```bash
python3 path/to/recolor.py -c WALL40_1.png -o out -m 130 MWALL*.png
```
Here's the woodmarble abominations that it deposits in the `out` directory:

![image](https://github.com/streaki/DoomRecolor/assets/65075598/099636a1-23eb-4284-9a86-e19e7673d4df)

### Gallery
![doom08](https://github.com/streaki/DoomRecolor/assets/65075598/d0793959-bc9a-4d03-9ea7-73fcf4f466bf)

