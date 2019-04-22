
import numpy
import sys, os
from collections import Counter

vocab = set(line.strip() for line in open(sys.argv[1], 'rU'))
print('len(vocab)', len(vocab))

intersect = set()
f = open(sys.argv[2], 'w')
for line in open('/home/kitsing/corpora/glove.6B.300d.txt', 'rU'):
    word = line.strip().split()[0]
    if word in vocab:
        intersect.add(word)
        print(line.strip(), file=f)
print(len(intersect))

for w in vocab - intersect:
    embedding = ' '.join([str('%.6f'%x) for x in numpy.random.normal(size=300)])
    print(w, embedding, file=f)

f.close()
