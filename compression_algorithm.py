import cv2
import numpy as np
import pandas as pd
import config


def write_into_file(avg_color,x,y,height,width,writer):
    r_custom = round(avg_color[2]/255, 3)
    g_custom = round(avg_color[1]/255, 3)
    b_custom = round(avg_color[0]/255, 3)
    particle_size = config.particle["size"]
    particle_type = config.particle["type"]
    spacing = config.placement["spacing"]
    particle_count = round((width*height*config.particle["count"]*config.placement["spacing"])/particle_size) + 1
    square_width = round((width/2)*spacing,3)
    square_height = round((height/2)*spacing,3)
    dimension_1 = round((x)*spacing,3)
    dimension_2 = round((y)*spacing,3)

    if config.placement["orientation"] == "xz":
        writer.write(f"particle dust {r_custom} {g_custom} {b_custom} {particle_size} ~{dimension_1} ~ ~{dimension_2} {square_width} 0 {square_height} 0 {particle_count} {particle_type}\n")

    if config.placement["orientation"] == "xy":
        writer.write(f"particle dust {r_custom} {g_custom} {b_custom} {particle_size} ~{dimension_1} ~{dimension_2} ~ {square_width} {square_height} 0 0 {particle_count} {particle_type}\n")

    if config.placement["orientation"] == "yz":
        writer.write(f"particle dust {r_custom} {g_custom} {b_custom} {particle_size} ~ ~{dimension_1} ~{dimension_2} 0 {square_width} {square_height} 0 {particle_count} {particle_type}\n")


def process_image(image_path, min_square_size, color_range):
    final_particles = 0
    # Load image
    image = cv2.imread(image_path)
    # Initialize dataframe to store square information
    df = pd.DataFrame(columns=['x', 'y', 'width', 'height', 'color'])
    # Initialize starting x, y, width, and height
    x, y, width, height = (0, 0, image.shape[1], image.shape[0])
    # Initialize stack to store squares that need further processing
    squares = [(x, y, width, height)]
    with open("result.mcfunction", "w") as mcfunction:
        while squares:
            x, y, width, height = squares.pop()
            if width <= min_square_size or height <= min_square_size:
                img = image[y:y+height, x:x+width]
                avg_color = np.mean(img, axis=(0,1))
                write_into_file(avg_color,x,y,height,width,mcfunction)
                df = pd.concat([df, pd.DataFrame([{'x': x, 'y': y, 'width': width, 'height': height, 'color': avg_color}])], ignore_index=True)
                continue
            img = image[y:y+height, x:x+width]
            avg_color = np.mean(img, axis=(0,1))
            if width < min_square_size or height < min_square_size or not np.any(np.abs(img - avg_color) > color_range):
                write_into_file(avg_color,x,y,height,width,mcfunction)
                df = pd.concat([df, pd.DataFrame([{'x': x, 'y': y, 'width': width, 'height': height, 'color': avg_color}])], ignore_index=True)
            else:
                for i in range(2):
                    for j in range(2):
                        new_x = x + (i * (width // 2))
                        new_y = y + (j * (height // 2))
                        new_width = width // 2
                        new_height = height // 2
                        squares.append((new_x, new_y, new_width, new_height))
    # create new image
    new_image = np.copy(image)
    compression_result = 0
    for _, row in df.iterrows():
        cv2.rectangle(new_image, (row['x'], row['y']), (row['x']+row['width'], row['y']+row['height']), row['color'], -1)
        compression_result+=1
    print(f"Final Compression resulted in {compression_result} commands")
    cv2.imwrite("output.png", new_image)

# Example usage

process_image('image.png', config.compression["min_pixel_size"], config.compression["color_compression"])