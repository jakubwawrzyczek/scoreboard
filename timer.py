import time

start_time = time.time()
while True:
    curr_time = time.time()
    timer = open('timer.txt', 'w')
    timer.write(str(round((curr_time - start_time) // 60)).zfill(2) + ':' + str(round(((curr_time - start_time) % 60))).zfill(2))
    timer.close()
    time.sleep(1)
    