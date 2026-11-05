import math
import inspect

areas = {
    "square": lambda s: s*s,
    "rectangle": lambda b,h: b*h,
    "parallelogram": lambda b,h: b*h,
    "triangle": lambda b,h: 0.5 * b*h,
    "circle": lambda r: math.pi * r * r,
    "rhombus": lambda d1,d2: 0.5 * d1*d2,
    "semicircle": lambda r: 0.5 * math.pi * r * r,
    "quartercircle": lambda r: 0.25 * math.pi * r * r,
    "trapezoid": lambda b1, b2, h: ((b1 + b2) * h) / 2,
    "trapezium": lambda b1, b2, h: ((b1 + b2) * h) / 2,
    "sector": lambda r, a: (a / 360) * math.pi * (r * r),
}

perimeters = {
    "square": lambda s: s*4,
    "rhombus": lambda s: s * 4,
    "rectangle": lambda l,w: 2 * (l+w),
    "parallelogram": lambda l,w: 2 * (l+w),
    "triangle": lambda s1,s2,b: s1 + s2 + b,
    "circle": lambda r: 2 * (math.pi * r),
    "semicircle": lambda r: (2 * r) + (math.pi * r),
    "quartercircle": lambda r: 2 * r + (math.pi * r) / 2,
    "trapezoid": lambda b1, b2, b3, b4 : b1 + b2 + b3 + b4,
    "trapezium": lambda b1, b2, b3, b4 : b1 + b2 + b3 + b4,
    "sector": lambda r, a_d: (2 * r) + ((a_d / 360) * (2 * math.pi * r)),
}

print("Equations: Arithmetic. Areas, Perimeters")
equation = input("What math equation would you like to try? (Type 'area' or 'perimeter'): ").lower()

# Determine which dictionary to use based on user input
if "area" in equation:
    target_dict = areas
    mode = "Area"
elif "perimeter" in equation or "circumference" in equation:
    target_dict = perimeters
    mode = "Perimeter"
else:
    print("Invalid choice. Please choose either 'area' or 'perimeter'.")
    exit()

print(f"\nAvailable shapes for {mode}:")
print(" | ".join([shape.capitalize() for shape in target_dict.keys()]))

shape_choice = input(f"\nWhat {mode.lower()} would you like to calculate? ").lower()

if shape_choice in target_dict:
    func = target_dict[shape_choice]
    
    sig = inspect.signature(func)
    args = []
    
    print(f"\nPlease enter the measurements for a {shape_choice}:")
    for param in sig.parameters.keys():
        val = float(input(f"Enter value for {param}: "))
        args = args + [val]
        
    result = func(*args)
    print(f"\nThe {mode.lower()} of the {shape_choice} is: {result:.2f}")
else:
    print(f"\nError: {mode} of '{shape_choice}' could not be found.")
