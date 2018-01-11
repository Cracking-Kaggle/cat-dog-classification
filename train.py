"""
Load features from file, train and produce model
"""

import time
import sys
from sklearn.linear_model import LogisticRegression

def train(data, size):
    """
    Read features from file, train and output model
    """
    datafile = open(data, 'r')
    feas = []
    labels = []
    cnt = 0
    while True:
        line = datafile.readline()
        if not line:
            break
        parts = line.strip().split("\t")
        assert len(parts) == 2
        fmt = lambda num: int(num) / 10000.0
        fea = list(map(fmt, parts[0].split(",")))
        label = int(parts[1])
        feas.append(fea)
        labels.append(label)
        cnt += 1
        if cnt > size:
            break
    datafile.close()
    classifier = LogisticRegression()
    classifier.fit(feas, labels)
    sys.stdout.write(",".join(map(str, list(classifier.coef_[0]))))
    sys.stdout.write("\n" + str(classifier.intercept_[0]))

if __name__ == "__main__":
    T = time.time()
    DATA = sys.argv[1]
    SIZE = int(sys.argv[2])
    train(DATA, SIZE)
    sys.stderr.write("Time: {:.2f} seconds\n".format(time.time() - T))
