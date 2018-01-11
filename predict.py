"""
Load model from file and predict with it
"""

import time
import sys
import math
import numpy as np

def predict(model, test):
    modelfile = open(model, 'r')
    coef = list(map(float, modelfile.readline().strip().split(",")))
    b = float(modelfile.readline().strip())
    modelfile.close()
    w = np.matrix(coef)
    testfile = open(test, 'r')
    feas = []
    while True:
        line = testfile.readline()
        if not line:
            break
        fmt = lambda num: int(num) / 10000.0
        fea = list(map(fmt, line.split(",")))
        feas.append(fea)
    testfile.close()
    predicts = []
    for fea in feas:
        x = np.matrix(fea)
        prod = w.dot(x.T) + b
        predict = 1 / (1 + math.exp(-prod))
        predicts.append(predict)
    fmt = lambda p: str(p) + "\n"
    sys.stdout.writelines(list(map(fmt, predicts)))

if __name__ == "__main__":
    T = time.time()
    MODEL = sys.argv[1]
    TEST = sys.argv[2]
    predict(MODEL, TEST)
    sys.stderr.write("Time: {:.3f} seconds\n".format(time.time() - T))
