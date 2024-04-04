import cv2
import numpy as np
import argparse
import time
import os
import math

# this function is recursive
# if that image has every pixel with the color +-N% same as the avarage color it fills the intire square with that color
# if not it splits the square into 4 smaller squares and calls itself on them
# the function returns the image with the squares filled
def compress(img: np.ndarray, color_compression: int, min_pixel_size: int, max_pixel_size: int) -> np.ndarray:
    # get the avarage color of the square
    avg_color = np.median(img, axis=(0, 1))
    # get the maximum difference in the avarage of all colors in the square
    max_diff = color_compression * 255 / 100
    # get the size of the square
    size_X = img.shape[0]
    size_Y = img.shape[1]
    # check if the square is smaller than the smallest square possible
    if size_X <= min_pixel_size or size_Y <= min_pixel_size:
        # fill the square with the avarage color
        if not (size_X >= max_pixel_size or size_Y >= max_pixel_size):
            img[:, :] = avg_color
            return img
    # check if every pixel in the square has the color +-N% same as the avarage color
    if np.all(np.abs(img - avg_color) < max_diff):
        # fill the square with the avarage color
        img[:, :] = avg_color
        return img
    # split the square into 4 smaller squares
    half_X = size_X // 2
    half_Y = size_Y // 2
    # call the function on the 4 smaller squares
    img[:half_X, :half_Y] = compress(img[:half_X, :half_Y], color_compression, min_pixel_size)
    img[:half_X, half_Y:] = compress(img[:half_X, half_Y:], color_compression, min_pixel_size)
    img[half_X:, :half_Y] = compress(img[half_X:, :half_Y], color_compression, min_pixel_size)
    img[half_X:, half_Y:] = compress(img[half_X:, half_Y:], color_compression, min_pixel_size)
    return img

def main(args):
    timenow = time.perf_counter()
    img = cv2.imread(args.image_path)
    img = compress(img, args.color_compression, args.min_pixel_size, args.max_pixel_size)
    if args.output_path:
        cv2.imwrite(args.output_path, img)
    if args.display:
        cv2.imshow("image", img)
        cv2.waitKey(0)
    
    if args.verbose:
        print(f"Time: {time.perf_counter() - timenow} seconds")
        print(f"Compression ratio: {os.path.getsize(args.image_path) / os.path.getsize(args.output_path)}x smaller than the original file")
    print(f"Compressed file saved to {args.output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Image Compression')
    parser.add_argument('image_path', type=str, help='Path to the image file') # Done
    parser.add_argument('color_compression', type=int, default=20, help='Color compression percentage') # Done
    parser.add_argument('min_pixel_size', type=int, default=12, help='Minimum pixel size') # Done
    parser.add_argument('output_path', type=str, help='Path to the output file') # Done
    parser.add_argument('-m' '--max_pixel_size', type=int, default=math.inf, help='Maximum pixel size') # Done
    parser.add_argument('-d', '--display', action='store_true', help='Display the compressed image') # Done
    parser.add_argument('-v', '--verbose', action='store_true', help='Display verbose information') # Done
    parser.add_argument('--version', action='version', version='%(prog)s 2.0') # Done
    args = parser.parse_args()

    main(args)
