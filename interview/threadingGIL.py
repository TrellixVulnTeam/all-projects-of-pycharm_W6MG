'''single threading'''
# import time
# from threading import Thread
# COUNT = 50000000
# def countdown(n):
#     while n>0:
#         n = n - 1
# start = time.time()
# countdown(COUNT)
# end = time.time()
# print(end - start)

import time
from threading import Thread
COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown,args=(COUNT//2,))
t2 = Thread(target=countdown,args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(end-start)


