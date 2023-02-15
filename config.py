particle = dict(
    size = 1,
    # size of the dust particle, minecraft accepts int <1;4>

    count = 1,
    # sets the number of particles in each segment

    type = "force",
    # sets the variant of the particle (normal/force)
)
placement = dict(
    spacing = 0.002,
    # sets the spacing between all pixels

    orientation = "xz",
    # sets the orientation of the image
)
compression = dict(
    color_compression = 40,
    # sets the maximum difference in the avarage of all colors in the square 

    min_pixel_size = 4
    #sets the size of the smallest square possible 
)