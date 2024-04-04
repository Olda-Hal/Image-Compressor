# Compression Algorithm: HalALG
this compression algorithm is a simple compression algorithm used for images. It is a lossy compression algorithm that uses custom process to remove unncesary details. This algorithm is not suitable for text files.

# How to use
1. Clone the repository
2. Run the following command in the terminal
```bash
pip install -r requirements.txt
```
3. Run the following command in the terminal
```bash
python compressor.py INPUT_FILE_PATH MAX_DIFFERENCE MIN_PIXEL_SIZE OUTPUT_FILE_PATH
```
you can learn more about the parameters by running the following command
```bash
python compressor.py -h
```
4. The compressed image will be saved in the output file path

# Example
```bash
python compressor.py test.jpg 10 10 test_compressed.jpg
```
# Showcase
You can see some examples of the generated images in the [showcase](SHOWCASE.md) with some short descriptions about the images.

# How it works
this algorithm is a recursive algorithm that works as follows:
splits the image into 4 quadrants and calculates the average color of each quadrant. Then it compares every pixel in the quadrant with the average color of the quadrant. If the difference between the pixel color and the average color is less than the MAX_DIFFERENCE on all pixels in the quadrant, the quadrant will be replaced with the avarage color of the quadrant. If there is a pixel that has a difference greater than the MAX_DIFFERENCE, the quadrant will be split into 4 quadrants and the process will be repeated. The process will be repeated until the quadrant size is less or equal than the MIN_PIXEL_SIZE. 

# Advantages and Disadvantages
- this algorithm is lossy
- this algorithm is not suitable for text files
- this algorithm wont loose details in parts of the image that have a lot of details but removes them in parts that have less details
- this algorithm may compress the image to a very small size
