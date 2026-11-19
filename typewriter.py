import time
def typewriter(text, delay=0.03):
    """Typewriter function, created to make text look more dynamic."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay * 6 if char == "." else delay)
    print()
