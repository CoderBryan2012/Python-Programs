import threading, datetime, time

result = 0
stop_event = threading.Event()
options = ["stopwatch", "timer", "time"]

def date(year, month, day):
  if 11 <= day <= 13:
    suffix = "th"
  else:
    suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
  date_obj = datetime.datetime(year, month, day)
  month_str = date_obj.strftime("%b")
  return f"{month_str}. {day}{suffix} {year}"

def stop_watch():
  global result
  print("Stopwatch started!")
  start_time = time.time()
  while not stop_event.is_set():
    time.sleep(0.05)
    result = time.time() - start_time

print("Welcome to the Clock program!\n")
for i in range(len(options)):
  print(f"{i+1}. {options[i].capitalize()}")

m_choose = int(input("Pick your choice: "))

if m_choose == 1:
  result = 0
  stop_event.clear()
  thread = threading.Thread(target=stop_watch, daemon=True)
  thread.start()
  input("Press Enter to stop the stopwatch...")
  stop_event.set()
  thread.join()

  suffix = "" if f"{result:.2f}" == "1.00" else "s"
  print(f"\nStopwatch finished at: {result:.2f} second{suffix}.")
  print("Stopwatch done!")

if m_choose == 2:
    timer_time = int(input("How many seconds should the timer have? "))
    for timer in range(timer_time, 0, -1):
        print(timer)
        time.sleep(1)
    print("Time's up!")

if m_choose == 3:
  time = datetime.datetime.now()
  print(f"\nToday is {date(time.year,time.month, time.day)}")
