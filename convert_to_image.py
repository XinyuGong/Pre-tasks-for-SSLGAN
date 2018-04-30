import SL

data = SL.load_obj('vector_result')
images = []
for line in data:
    image = []
    vector = line[3]
    for num in vector:
        row = [] if num != 0 else [127] * 10
        if num != 0:
            smb = 1 if num > 0 else -1
            num *= 100000000000000000000
            for i in range(10):
                tmp = num % 100
                row.append(127 + int(smb * tmp * 1.28))
                num = int(num / 100)
        image.append(row)
    images.append([line[0], line[1], line[2], image])
SL.save_obj(images, 'vector_images')