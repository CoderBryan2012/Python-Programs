import time

def loading_bar(bars, delay):
    print("Loading..." )
    for i in range(1, bars):
        print("█", end="", flush=True)
        time.sleep(delay)
    print("100%")
    
loading_bar(5, 0.5)
