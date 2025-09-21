# from functools import lru_cache
from functools import cache

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import sys

# @lru_cache(maxsize=None)
# @@@ lru_cache의 메모리 사이즈를 제한하지 않을 경우(maxsize=None)는 그냥 메모리 사이즈 제한 없는 cache를 사용할 것
@cache
def binomial_probability(n: int, p: float, k: int):
    '''
    B(n,p)의 random variable X에 대해 P(X=k)를 구하는 함수
    '''
    if not n > 0:
        raise Exception("n must be an integer greater than 0")
    
    if not 0 <= p <= 1:
        raise Exception("p(float) must be in the interval [0, 1]")
    
    if not 0 <= k <= n:
        raise Exception("k must be an integer such that 0 <= k <= n")
    
    if k == 0:
        return (1-p)**n
    
    return (p/(1-p)) * ((n-k+1)/(k)) * binomial_probability(n, p, k-1)

@cache
def binomial_prob_less_than_and_equal(n: int, p: float, k: int):
    '''
    B(n,p)의 random variable X에 대해 P(X<=k)를 구하는 함수
    '''
    if not n > 0:
        raise Exception("n must be an integer greater than 0")
    
    if not 0 <= p <= 1:
        raise Exception("p(float) must be in the interval [0, 1]")
    
    if not 0 <= k <= n:
        raise Exception("k must be an integer such that 0 <= k <= n")
    
    result = 0

    for i in range(k+1):
        result += binomial_probability(n, p, i)

    return result


def main():
    print("Hello from probability-statistics-practice!")

    # args = sys.argv[1:] # sys.argv[0]은 실행 스크립트의 이름 (main.py)
    # @@@ flag를 제외한 argument들만 args에 저장
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    # print(args)
    
    if not args:
        print("n, p not provided - will plot B(16,0.5) as default")
        n = 16
        p = 0.5
    else:
        try:
            n = int(args[0])
            p = float(args[1])
        except Exception as e:
            raise e

    result = []
    result_cum = [] 

    for i in range(n+1):
        cur = binomial_probability(n, p, i)
        cur_cum = binomial_prob_less_than_and_equal(n, p, i)
        # print(f"P(X = {i}), given B({n}, {p}), is {cur}")
        # print(f"P(X <= {i}), given B({n}, {p}), is {cur_cum}")

        result.append(cur)
        result_cum.append(cur_cum)

    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax1.bar([i for i in range(n+1)], result)
    ax2.bar([i for i in range(n+1)], result_cum)

    plt.show()

if __name__ == "__main__":
    main()
