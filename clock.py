import threading
import time
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError, available_timezones

result = 0.0
stop_event = threading.Event()
options = ["stopwatch", "timer", "time zone"]


def stop_watch():
    global result
    print("\nStopwatch started!")
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
    # Case-insensitive search across IANA time zone names
    zones = sorted(z for z in available_timezones() if country.lower() in z.lower())

    if not zones:
        print(f"No timezones were found that match '{country}'.")
        return

    print(f"\nTime zones that match '{country}':")
    for element in zones:
        print(element)

    zone_input = input("\nWhich timezone is yours? ").strip()
    try:
        zone_now = datetime.now(ZoneInfo(zone_input))
        print(f"\nToday is {format_date(zone_now.year, zone_now.month, zone_now.day)}.")
        print(f"The Time is {zone_now.hour:02d}:{zone_now.minute:02d}.")
    except ZoneInfoNotFoundError:
        print(f"Invalid time zone '{zone_input}'. Please copy an exact name from the list.")


def start_program():
    global result
    print("Welcome to the Clock program!\n")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option.title()}")

    try:
        m_choose = int(input("\nPick your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if m_choose == 1:
        result = 0.0
        stop_event.clear()
        thread = threading.Thread(target=stop_watch, daemon=True)
        thread.start()
        input("Press Enter to stop the stopwatch... ")
        stop_event.set()
        thread.join()

        suffix = "" if f"{result:.2f}" == "1.00" else "s"
        print(f"\nStopwatch finished at: {result:.2f} second{suffix}.")
        print("Stopwatch done!")

    elif m_choose == 2:
        try:
            timer_time = int(input("\nHow many seconds should the timer have? "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            return

        if timer_time < 0:
            print("Timer cannot be less than zero.")
        else:
            for t in range(timer_time, 0, -1):
                print(t)
                time.sleep(1)
            print("Time's up!")

    elif m_choose == 3:
        country_input = input("\nWhat country or region are you in? ").strip()
        time_zone_handler(country_input)

    else:
        print("Invalid choice. Please pick 1, 2, or 3.")


if __name__ == "__main__":
    start_program()
