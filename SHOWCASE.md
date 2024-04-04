Here you can see some examples of the generated images. The images are generated with the following parameters:
```bash
python compressor.py test.jpg 15 1 test_compressed.jpg
```
There are always 2 images, the original image and the compressed image. The original image is on the left and the compressed image is on the right.
![image](showcase/0.73artificial.png)
>  This image has a lot of flat colors. Because of this the compression isn't very good. The image is compressed 0.73x the size of the original image.

![image](showcase/1.01leaves_iso_200.png)
> this image has a lot of small details. Because of this the compression better. The image is compressed 1.01x the size of the original image.

![image](showcase/1.08leaves_iso_1600.png)

> This image is almost the same as the previous image but the ISO is higher. Because of this the image is brighter. This doesnt really affect the compression. The image is compressed 1.08x the size of the original image.

![image](showcase/1.15bridge.png)

> This image has a gradient in the sky. This makes the compression artifact more visible. The image is compressed 1.15x the size of the original image.

![image](showcase/1.28big_building.png)

> This image has a lot of small details. If you focuse on the windows you can see that the algorithm removed some unnessary details. The image is compressed 1.28x the size of the original image.

![image](showcase/1.66big_tree.png)

> This image had a lot of small details removed, but the dark parts of the image are really artifacted. The image is compressed 1.66x the size of the original image.

![image](showcase/2.05cathedral.png)
> This image has a clear example of the shortcomings of the algorithm in the dark parts of the image. The image is compressed 2.05x the size of the original image.

![image](showcase/2.18nightshot_iso_100.png)
> This is another example of the shortcomings of the algorithm in the dark parts of the image. but if we would set the MAXSIZE value correctly it would look much better. The image is compressed 2.18x the size of the original image.

![image](showcase/2.25fireworks.png)
> This image has a lot of small details. The image is compressed 2.25x the size of the original image.

![image](showcase/2.28flower_foveon.png)
> Here you can see one of great examples of the selection of important parts of the image. The flower is almost untouched and the background is really compressed. The image is compressed 2.28x the size of the original image.

![image](showcase/2.58hdr.png)
> If this image was shot in better lighting conditions the compression would be much better. But you can still see that the algorithm selected the important parts of the image. The image is compressed 2.58x the size of the original image.

![image](showcase/3.63nightshot_iso_1600.png)
> This image looks great even though it is compressed 3.63x the size of the original image. There are some artifacts but they are not really visible.

![image](showcase/4.39spider_web.png)
> This is a example of a bad image for this compression algorithm. Because the important part of the image is very small it gets almost completly removed. The image is compressed 4.39x the size of the original image.

![image](showcase/6.55deer.png)
> The head of the deer is almost untouched. The background is really compressed. If we would finetune the input settings, we could remove the artifacting on the neck The image is compressed 6.55x the size of the original image.