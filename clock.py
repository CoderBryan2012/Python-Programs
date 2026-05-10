import math, datetime, time

print("Welcome to the Clock program!")
print()
print("1. Stopwatch")
print("2. Timer")
print("3. Time")
m_choose = input("Pick your choice: ")
if m_choose == "1":
    stopWatch_time = int(input("What should the stopwatch end?"))
    for timer in range(stopWatch_time):
        timer = timer + 1
        time.sleep(1)
        print(timer)
    print("Stopwatch done!")
if m_choose == "2":
    timer_time = int(input("How many seconds?"))
    for timer in range(timer_time, 0, -1):
        print(timer)
        time.sleep(1)
    print("Timer done!")
if m_choose == "3":
    print(datetime.datetime.now())
