import math


def prob(n, p, r):
    return math.comb(n - 1, n - r) * (p ** r) * ((1 - p) ** (n - r))


def infoMeasure(n, p, r):
    return -1 * math.log2(prob(n, p, r))

'''

'''
def subProb(N, p, r):
    return sum(prob(i, p, r) for i in range(r, N + 1))


def approxEntropy(N, p, r):
    return sum(prob(i, p, r) * infoMeasure(i, p, r) for i in range(r, N + 1))


