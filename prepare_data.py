"""
Read, transform and reshape images
"""

import time
import sys
import os
import math
from skimage import io, transform

def prepare(source, size, count, is_train):
    """
    Read images of [count] quantity from [source] and resize them to [size]*[size]
    then reshape matrix to vector
    """
    lines = []
    cat = dog = 0
    for root, dirs, files in os.walk(source):
        for name in files:
            if cat + dog > count:
                break
            sys.stderr.write("Preparing {}...\n".format(name))
            img = io.imread(os.path.join(root, name))
            img = transform.resize(img, (size, size))
            img = img.reshape(1, size * size * 3)[0]
            if "cat" in name:
                label = "1"
                cat += 1
            else:
                label = "0"
                dog += 1
            fmt = lambda num: str(math.trunc(num * 10000))
            if is_train:
                line = "{}\t{}\n".format(",".join(map(fmt, img)), label)
            else:
                line = ",".join(map(fmt, img)) + "\n"
            lines.append(line)
    sys.stdout.writelines(lines)
    if is_train:
        sys.stderr.writelines("\nCats: {}\tDogs: {}\n".format(cat, dog))

if __name__ == "__main__":
    T = time.time()
    SOURCE = sys.argv[1]
    SIZE = int(sys.argv[2])
    COUNT = int(sys.argv[3])
    IS_TRAIN = sys.argv[4] == "y"
    prepare(SOURCE, SIZE, COUNT, IS_TRAIN)
    sys.stderr.write("Time: {:.3f} seconds\n".format(time.time() - T))
