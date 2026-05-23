import math

print("Equations: Arithmetic. Areas, Perimeters")
equation = input("What math equation would you like to try? ").lower()

if equation == "area" or equation ==  "areas":

    print("\n")

    print("Areas: Square / Parallelogram, Triangle / Rhombus, Circle, Semicircle, Quartercircle, Trapezoid / Trapezium and Sector.")
    areas = input("What area would you like to calculate? ").lower()

    if areas == "square" or areas == "rectangle" or areas == "parallelogram":
        base = float(input("What is the base? "))
        height = float(input("What is the height? "))
        result = (base * height)
        print(f"The area of a {areas} with a base of {base} and height of {height} is {result}.")

    elif areas == "triangle" or areas == "rhombus":
        base = float(input("What is the base? "))
        height = float(input("What is the height? "))
        result = (base * height) / 2
        print(f"The area of a {areas} with a base of {base} and height of {height} is {result}.")

    elif areas == "circle":
        radius = float(input("What is the radius? "))
        result = math.pi * (radius ** 2)
        print(f"The area of a {areas} with a radius of {radius} is {result}.")

    elif areas == "semicircle":
        radius = float(input("What is the radius? "))
        result = math.pi * (radius ** 2) / 2
        print(f"The area of a {areas} with a radius of {radius} is {result}.")

    elif areas == "quartercircle":
        radius = float(input("What is the radius? "))
        result = math.pi * (radius ** 2) / 4
        print(f"The area of a {areas} with a radius of {radius} is {result}.")
        
    elif areas == "trapezoid" or areas == "trapezium":
        base1 = float(input("What is the first base? "))
        base2 = float(input("What is the second base? "))
        height = float(input("What is the height? "))
        result = ((base1 + base2) * height) / 2
        print(f"The area of a {areas} with a base of {base1}, {base2} and height of {height} is {result}.")
    
    elif areas == "sector":
        radius = float(input("What is the radius? "))
        angle = float(input("What is the angle? "))
        result = (angle / 360) * math.pi * (radius ** 2)
        print(f"The area of a {angle}-degree sector with a radius of {radius} is: {result}")

    else:
        print("\nInvalid Area.")
        
elif equation == "perimeter":

    print("\n")

    print("Perimeter: Square / Parallelogram, Triangle / Rhombus, Circle, Semicircle, Quartercircle, Trapezoid / Trapezium and Sector.")
    perimeter = input("Which perimeter would you like to calculate?").lower()

    if perimeter == "square" or perimeter == "rhombus":
        side = float(input("What is the side? "))
        result = (side * 4)
        print(f"The perimeter of a {perimeter} with a side length of {side} is {result}.")

    elif perimeter == "triangle":
        side1 = float(input("What is the first side?"))
        side2 = float(input("What is the second side?"))
        base = float(input("What is the base?"))
        result = (side1 + side2 + base)
        print(f"The perimeter of a {perimeter} with a side of {side1}, {side2} and a base of {base} is {result}.")

    elif perimeter == "rectangle" or perimeter == "parallelogram":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        result = 2 * (length + width)
        print(f"The perimeter of a {perimeter} with a length of {length} and a width of {width} is {result}.")

    elif perimeter == "circle":
        radius = float(input("What is the radius? "))
        result = 2 * (math.pi * radius)
        print(f"The perimeter of a {perimeter} with a radius of {radius} is {result}.")


    elif perimeter == "semicircle":
        radius = float(input("What is the radius? "))
        result = (2 * radius) + (math.pi * radius)
        print(f"The perimeter of a {perimeter} with a radius of {radius} is {result}.")


    elif perimeter == "quartercircle":
        radius = float(input("What is the radius? "))
        result =  2 * radius + (math.pi * radius) / 2
        print(f"The perimeter of a {perimeter} with a radius of {radius} is {result}.")

    elif perimeter == "trapezoid" or perimeter == "trapezium":
        base1 =  float(input("What is the first base?"))
        base2 =  float(input("What is the second base?"))
        base3 = float(input("What is the third base?"))
        base4 = float(input("What is the fourth base?"))
        result = (base1 + base2 + base3 + base4)
        print(f"The perimeter of a {perimeter} with a base of {base1}, {base2}, {base3}, {base4} is {result}.")
        
    elif perimeter == "sector":
        radius = float(input("What is the radius? "))
        arc_degrees = float(input("What is the angle degree? "))
        arc_length = (arc_degrees / 360) * (2 * math.pi * radius)
        result = (2 * radius) + arc_length
        print(f"The perimeter of a {arc_degrees}-degree sector with a radius of {radius} is: {result}")
            


elif equation == "arithmetic" or equation == "arith":

    print("\n")
    print("Arithmetic: Addition / Add, Subtraction / Subtract, Multiplication, Multiply, Division / Divide, Exponents / Square, and sqrt / Root.")
    arithmetic = input("Which Arithmetic would you like to calculate? ").lower()

    if arithmetic == "addition" or arithmetic ==  "add":
        num1 = float(input("What is your first number? "))
        num2 = float(input("What is your second number? "))
        result = (num1 + num2)
        print(f"The answer is {result}.")

    elif arithmetic == "subtraction" or arithmetic == "subtract":
        num1 = float(input("What is your first number? "))
        num2 = float(input("What is your second number? "))
        result = (num1 - num2)
        print(f"The answer is {result}.")

    elif arithmetic == "multiplication" or arithmetic == "multiply":
        num1 = float(input("What is your first number? "))
        num2 = float(input("What is your second number? "))
        result = (num1 * num2)
        print(f"The answer is {result}.")

    elif arithmetic == "division" or arithmetic == "divide":
        num1 = float(input("What is your first number? "))
        num2 = float(input("What is your second number? "))
        result = (num1 / num2)
        print(f"The answer is {result}.")

    elif arithmetic == "exponents" or arithmetic == "square":
        num = float(input("What is your number? "))
        square = float(input("What is your square number? "))
        result = (num ** square)
        print(f"The answer is {result}.")
    
    elif arithmetic == "sqrt" or arithmetic == "root":
        num = float(input("What is your number? "))
        sqrt = float(input("What is your square root? "))
        result = (math.sqrt(num))
        print(f"The answer is {result}.")
