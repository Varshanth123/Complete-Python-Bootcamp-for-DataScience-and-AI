## Multiprocessing with Process PoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f'{number} square: {number*number}'

numbers=[1,2,3,4,5,6,7,8,9,10]

if __name__=='__main__':
    with ProcessPoolExecutor(max_workers=3) as executor: # creates 3 concurent
        results=executor.map(square_number,numbers)

    for result in results:
        print(result)

'''
OutPut:
1 square: 1
2 square: 4
3 square: 9
4 square: 16
5 square: 25
6 square: 36
7 square: 49
8 square: 64
9 square: 81
10 square: 100
'''