def invert_image(image):
    for ix, _ in enumerate(image):
        image[ix] = image[ix][::-1]
    image = image[::-1]
    return image
    

image = [[1,2,3], [4,5,6], [7,8,9]]
print(invert_image(image))