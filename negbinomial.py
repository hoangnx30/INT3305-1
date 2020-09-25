import math


def prob(n, p, r):
    return math.comb(n - 1, n - r) * (p ** r) * ((1 - p) ** (n - r))


def infoMeasure(n, p, r):
    return -1 * math.log2(prob(n, p, r))

'''
    Tổng Pr(1) + Pr(2) + ... bằng 1.
    Dãy c_{N} = Pr(1) + Pr(2) + ... + Pr(N) là một dãy dương, tăng và có giới hạn bằng 1.
    Do đó khi N càng lớn thì a_{N} càng xấp xỉ 1. Như vậy hàm sumProb cho phép kiểm tra
    tổng xác suất của biến ngẫu nhiên nhị thức âm bằng 1.
'''
def sumProb(N, p, r):
    return sum(prob(i, p, r) for i in range(r, N + 1))
    

'''
    Xét dãy H_{N} = (-Pr(1) log Pr(1)) + (-Pr(2) log Pr(2)) + ...
    H_{N} là một dãy dương, tăng và có giới hạn là entropy của biến ngẫu nhiên nhị thức âm
    Do đó khi N càng lớn, hàm approxEntropy sẽ tiến đến entropy của biến ngẫu nhiên nhị thức âm và hàm này có thể dùng để tính xấp xỉ entropy
'''
def approxEntropy(N, p, r):
    return sum(prob(i, p, r) * infoMeasure(i, p, r) for i in range(r, N + 1))

print(math.comb(4, 3))