import random

from pyDatalog import pyDatalog


pyDatalog.create_terms("Average, N, Sum, RndSum")
Sum[N] = N + Sum[N - 1]
Sum[0] = 0
print(Sum[88] == N)

Average[N] = Sum[N] / N
print(Average[88] == N)

RndSum[N] = random.randint(0, 100) + RndSum[N - 1]
RndSum[N] = random.randint(0, 100)

print(RndSum[45] == N)

_rndSum = [random.randint(0, 100) for x in range(0, 100)]
_rndSum.sort()

print((_rndSum[48] + _rndSum[49]) / 2)

