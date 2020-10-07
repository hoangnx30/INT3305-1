import math


def prob(n, p, N):
	return math.comb(N, n) * (p ** N)


def infoMeasure(n, p, N):
    return -1 * math.log2(prob(n, p, N))


'''
    Biến ngẫu nhiên nhị thức chỉ có hữu hạn symbol, tổng xác suất của tất cả các symbol này bằng 1.
    => hàm sumProb cho phép kiểm tra tổng xác suất của biến ngẫu nhiên nhị thức bằng 1.
'''
def sumProb(N, p):
    return sum(prob(i, p, N) for i in range(1, N + 1))

'''
    Các symbol của biến ngẫu nhiên nhị thức là hữu hạn, do đó entropy cũng hữu hạn (bị chặn trên)
    Khi N càng lớn thì approxEntropy(N, p) càng xấp xỉ với entropy nên hàm này cho phép tính xấp xỉ entropy.
'''
def approxEntropy(N, p):
    return sum(prob(i, p, N) * infoMeasure(i, p, N) for i in range(1, N + 1))

