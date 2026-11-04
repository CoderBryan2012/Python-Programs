import threading, time
from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones
result = 0
stop_event = threading.Event()
options = ["stopwatch", "timer", "time zone"]

def stop_watch():
  global result
  print("Stopwatch started!")
  start_time = time.time()
  while not stop_event.is_set():
    time.sleep(0.05)
    result = time.time() - start_time

def format_date(year, month, day):
  if 11 <= day <= 13:
    suffix = "th"
  else:
    suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
  date_obj = datetime(year, month, day)
  month_str = date_obj.strftime("%b")
  return f"{month_str}. {day}{suffix} {year}"

def time_zone_handler(country):
  zones = sorted(filter(lambda x: country in x, available_timezones()))
  print(f"\nTime zones that match {country}:")
  for element in zones:
    print(element)
  zone_input = input("Which timezone is yours? ")
  zone_now = datetime.now(ZoneInfo(zone_input))
  print(f"\nToday is {format_date(zone_now.year,zone_now.month, zone_now.day)}.")
  print(f"The Time is {zone_now.hour}:{zone_now.minute}:{zone_now.second}.")


print("Welcome to the Clock program!\n")
for i in range(len(options)):
  print(f"{i+1}. {options[i].title()}")

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
  country_input = input("What country are you in? ")
time_zone_handler(country_input)
