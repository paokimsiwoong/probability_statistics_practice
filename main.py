# from functools import lru_cache
from functools import cache

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

    for i in range(7):
        print(f"P(X = {i}), given B(6, 0.4), is {binomial_probability(6, 0.4, i)}")
        print(f"P(X <= {i}), given B(6, 0.4), is {binomial_prob_less_than_and_equal(6, 0.4, i)}")




if __name__ == "__main__":
    main()
