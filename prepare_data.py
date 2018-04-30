import SL
import h5py

f = h5py.File('data.hy', 'a')
f_id = open('id.txt', 'w')
criteria = SL.load_obj('vector_images')
for id in range(len(criteria)):
    criterion = criteria[id]
    irr = criterion[2]
    pixels = criterion[3]
    f_id.write(str(id) + '\n')
    grp = f.create_group(str(id))
    image = grp.create_dataset('image', (40, 40, 1), dtype = 'u1')
    label = grp.create_dataset('label', (4,), dtype = 'b1')
    for i in range(40):
        for j in range(5):
            for k in range(8):
                image[i, j * 8 + k, 0] = pixels[i * 5 + j][k]
    if irr < 0.2:
        label[0] = True
    elif irr < 0.4:
        label[1] = True
    elif irr < 0.6:
        label[2] = True
    else:
        label[3] = True
f_id.close()