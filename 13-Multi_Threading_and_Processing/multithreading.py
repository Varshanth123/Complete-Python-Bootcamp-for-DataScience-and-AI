'''Multithreading

When to use Multi-threading
-> I/O-bound tasks: Tasks that spend more time waiting for I/O operations(eg., file operations,network requests).
-> Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.
'''

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'Number:{i}')

def print_letter():
    for letter in 'abcde':
        time.sleep(2)
        print(f'Letter:{letter}')


# Create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)


t=time.time()
## lets start the thread 
t1.start()
t2.start()

### wait for the threads to complete 
## .join()= threading module forces the program to pause and wait for a specific thread to finish its execution before allowing the rest of the code to continue.
t1.join()
t2.join()
finished_time=time.time()-t
print(finished_time)

'''
OutPut:
Number:0
Letter:a
Letter:b
Number:1
Letter:c
Number:2
Letter:d
Number:3
Letter:e
Number:4
10.005400657653809
'''