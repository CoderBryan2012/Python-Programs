import threading, datetime, time

result = 0
stop_event = threading.Event()

def stop_watch():
  global result
  print("Stopwatch started!")
  start_time = time.time()
  while not stop_event.is_set():
    time.sleep(0.05)
    result = time.time() - start_time

print("Welcome to the Clock program!\n")
print("1. Stopwatch")
print("2. Timer")
print("3. Time")

m_choose = int(input("Pick your choice: "))

if m_choose == 1:
  result = 0
  stop_event.clear()
  thread = threading.Thread(target=stop_watch, daemon=True)
  thread.start()
  input("Press Enter to stop the stopwatch...")
  stop_event.set()
  thread.join()

  print(f"\nTime: {result:.2f}")
  print("Stopwatch done!")

if m_choose == 2:
    timer_time = int(input("How many seconds?"))
    for timer in range(timer_time, 0, -1):
        print(timer)
        time.sleep(1)
    print("Timer done!")
    
if m_choose == 3:
    print(datetime.datetime.now())
