'''
Multiprocessing
----------------

-> it allows the processes that run in parallel

when to use
-> CPU-Bound Tasks - Tasks that are heavy on CPU usage(e.g., mathematical computations,data processing)
->Parallel execution - want to use Multiple cores of the CPU
'''

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'{i}^2 = {i*i}')

def cude_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f'{i}^3 = {i*i*i}')

if __name__=='__main__': # entry poin
    # create 2 process
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cude_numbers)


    # start 2 process
    t=time.time()
    p1.start()
    p2.start()

    # wait for the process to complete
    p1.join()
    p2.join()
    finished_time=time.time()-t
    print(finished_time)

'''
OutPut:

0^2 = 0
0^3 = 0
1^2 = 1
1^3 = 1
2^2 = 4
3^2 = 9
2^3 = 8
4^2 = 16
3^3 = 27
4^3 = 64
7.882741212844849
'''
