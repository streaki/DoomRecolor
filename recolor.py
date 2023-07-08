#!/usr/bin/env python3

from argparse import Namespace, ArgumentParser, BooleanOptionalAction, REMAINDER
import cv2
from math import ceil
from os import path


def main(args: Namespace) -> None:
    color_image = cv2.imread(args.color_image)
    for filename in args.images:
        value_image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
        # convert both images to HSV
        value_hsv = cv2.cvtColor(value_image, cv2.COLOR_BGR2HSV_FULL)
        color_hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV_FULL)
        # fit the output image to the value image size
        color_hsv = resize_image(color_hsv, value_hsv.shape)
        # trust me it looked like garbage with python's ternary op
        if args.multiply:
            color_hsv[:,:,2] = multiply_value(color_hsv, value_hsv)
        else:
            color_hsv[:,:,2] = value_hsv[:,:,2]
        result = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR_FULL)
        if value_image.shape[2] > 3:
            b, g, r = cv2.split(result)
            _, _, _, a = cv2.split(value_image)
            result = cv2.merge((b, g, r, a))
        cv2.imwrite(path.join(args.output_dir, filename), result)


def multiply_value(img1: cv2.Mat, img2: cv2.Mat) -> cv2.Mat:
    """
    Combine the value channels of two images as if we are multiplying floats of range 0..1

    Step 1: force float conversion by multiplying by 1f
    Step 2: multiply values by each other
    Step 3: floor divide by 255 to get them back into unsigned byte range
    """
    return cv2.multiply(img1[:,:,2] * 1., img2[:,:,2] * 1.) // 255


def resize_image(image: cv2.Mat, dest_size: tuple):
    dest_height, dest_width, _ = dest_size
    # concatenate the image horizontally and vertically x times if it is smaller than the desired output
    image = cv2.hconcat([image] * ceil(dest_width / image.shape[1]))
    image = cv2.vconcat([image] * ceil(dest_height / image.shape[0]))
    # trim it down if it is too large
    return image[:dest_height, :dest_width]



def parse_arguments() -> Namespace:
    parser = ArgumentParser(description='Finds colored shapes')
    parser.add_argument(
        '-c',
        '--color-image',
        type=str,
        required=True,
        help='The image that will transfer its color onto the value images',
    )
    parser.add_argument(
        '-m',
        '--multiply',
        type=bool,
        default=False,
        action=BooleanOptionalAction,
        help="Multiply the two images' values together instead of replacing one with the other",
    )
    parser.add_argument(
        '-o',
        '--output-dir',
        type=str,
        required=True,
        help='The output directory for results',
    )
    parser.add_argument(
        'images',
        nargs=REMAINDER,
        help='Paths to the value images',
    )
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_arguments())
