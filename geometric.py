import math

def prob(n, p):
    return ((1-p) ** (n-1)) * p


def infoMeasure(n, p):
    return -1 * math.log2(prob(n, p))


'''
    Tổng Pr(1) + Pr(2) + ... = 1
    Dãy a_{N} = Pr(1) + Pr(2) + ... + Pr(N) là một dãy dương, tăng và có giới hạn bằng 1
    Vậy nên khi N càng lớn thì a_{N} càng xấp xỉ 1.
'''
def sumProb(N, p):
    return sum(prob(i, p) for i in range(1, N + 1))

'''
    Xét dãy H_{N} = (-Pr(1) log Pr(1)) + (-Pr(2) log Pr(2)) + ...
    H_{N} là một dãy dương, tăng và có giới hạn là entropy của biến ngẫu nhiên hình học.
    Vậy nên khi N càng lớn, hàm approxEntropy sẽ tiến đến entropy.
'''
def approxEntropy(N, p):
    return sum(prob(i, p) * infoMeasure(i, p) for i in range(1, N + 1))
