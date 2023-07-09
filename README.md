## DoomRecolor

A script for quick palette swapping of images.
Originally intended to use with Doom graphics.

### Usage

Designed to be rand from commend line. To invoke, run:

```bash
python3 recolor.py [-h] -c COLOR_IMAGE [-m [MULTIPLY]] -o OUTPUT_DIR [VALUE_IMAGES...]
```

Options and parameters:
- `-h` — displays a help text.
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
- `VALUE_IMAGES` a space-separated/wildcarded list of images that will be used as value inputs
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
