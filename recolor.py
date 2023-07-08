#!/usr/bin/env python3

from argparse import Namespace, ArgumentParser, BooleanOptionalAction, REMAINDER
import cv2


def main(args: Namespace) -> None:
    # print(args.images)
    # print(args.color_image)
    # print(args.multiply)
    color_image = cv2.imread(args.color_image)
    for filename in args.images:
        value_image = cv2.imread(filename)
        # convert both images to HSV
        value_hsv = cv2.cvtColor(value_image, cv2.COLOR_BGR2HSV_FULL)
        color_hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV_FULL)
        # trust me it looked like garbage with python's ternary op
        if args.multiply:
            color_hsv[:,:,2] = multiply_value(color_hsv, value_hsv)
        else:
            color_hsv[:,:,2] = value_hsv[:,:,2]
        result = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR_FULL)
        cv2.imshow('foo', result)
        cv2.waitKey()


def multiply_value(img1: cv2.Mat, img2: cv2.Mat) -> cv2.Mat:
    """
    Combine the value channels of two images as if we are multiplying floats of range 0..1

    Step 1: force float conversion by multiplying by 1f
    Step 2: multiply values by each other
    Step 3: floor divide by 255 to get them back into unsigned byte range
    """
    return cv2.multiply(img1[:,:,2] * 1., img2[:,:,2] * 1.) // 255


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
        help="Multiply the color image's value by value images' values together instead of replacing it",
    )
    parser.add_argument(
        'images',
        nargs=REMAINDER,
        help='Paths to the value images',
    )
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_arguments())
