def typewriter(text, delay=0.03):
    """Typewriter function, created to make text look more dynamic."""
    for char in text:
        if char == ".":
            print(char, end="", flush=True)
            time.sleep(delay * 6)
        else:
            print(char, end="", flush=True)
            time.sleep(delay)
    print()
