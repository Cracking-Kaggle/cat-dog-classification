"""
Read, transform and reshape images
"""

import time
import sys
import os
import math
from skimage import io, transform

def prepare(source, count):
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
            if "cat" in name:
                label = "1"
                cat += 1
            else:
                label = "0"
                dog += 1
            fmt = lambda num: str(math.trunc(num * 10000))
            lines.append(label + "\n")
    sys.stdout.writelines(lines)
    sys.stderr.writelines("\nCats: {}\tDogs: {}\n".format(cat, dog))

if __name__ == "__main__":
    T = time.time()
    SOURCE = sys.argv[1]
    COUNT = int(sys.argv[2])
    prepare(SOURCE, COUNT)
    sys.stderr.write("Time: {:.3f} seconds\n".format(time.time() - T))
