import math

def prob(n, p):
    return ((1-p) ** (n-1)) * p


def infoMeasure(n, p):
    return -1 * math.log2(prob(n, p))


def subProb(N, p):
    return sum(prob(i, p) for i in range(1, N + 1))


def approxEntropy(N, p):
    return sum(prob(i, p) * infoMeasure(i, p) for i in range(1, N + 1))
