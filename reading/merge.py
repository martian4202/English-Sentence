import sys
from collections import OrderedDict

def run():
    mapping = OrderedDict()
    with open(sys.argv[1]) as ielts:
        n = 0
        while True:
            line = ielts.readline()
            if not line:
                break
            line = line.strip('\n')
            mapping[line] = n
            n += 1
    diff = OrderedDict()
    with open(sys.argv[2]) as toefl:
        n = 0
        while True:
            line = toefl.readline()
            if not line:
                break
            line = line.strip('\n')
            if line not in mapping:
                diff[line] = n
            n += 1
    words = list(mapping.keys())
    for k, v in diff.items():
        words.insert(v, k)
    for w in words:
        print(w)

if __name__ == "__main__":
    run()