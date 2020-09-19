import math

math.f
def prob(n, p, N):
	return math.comb(N, n) * (p ** N)


def infoMeasure(n, p, N):
    return -1 * math.log2(prob(n, p, N))

def subProb(N, p):
    return sum(prob(i, p, N) for i in range(1, N + 1))

def approxEntropy(N, p):
    return sum(prob(i, p, N) * infoMeasure(i, p, N) for i in range(1, N + 1))

