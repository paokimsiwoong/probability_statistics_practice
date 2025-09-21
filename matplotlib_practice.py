import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    print("Hello from probability-statistics-practice!")

    print(f'numpy version : {np.__version__}') # version check
    print(f'matplotlib version : {mpl.__version__}') # version check

    fig = plt.figure(figsize=(12,6))
    fig.set_facecolor('red')
    ax1 = fig.add_subplot(1, 2, 1)
    # (전체행수, 전체 열수, index)
    ax2 = fig.add_subplot(122)

    x = [1,2,3]
    plt.plot(x)
    # plt.plot은 마지막에 추가된 ax에 자동으로 그리기

    ax1.plot([1, 1, 1]) # 파랑
    ax1.plot([1, 2, 3]) # 주황
    ax1.plot([3, 3, 3]) # 초록
    # ax 객체 지정 후 plot

    plt.show()


if __name__ == "__main__":
    main()
