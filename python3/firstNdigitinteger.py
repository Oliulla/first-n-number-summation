# First n number sum
try:
    n = int(input("Enter your number?: "))
    sum = (n * (n+1)) / 2
    print(f"Your first {n} number summation is: {sum}")
except ValueError:
    print("""
    Invalid Value.
    please, try with valid value.
    Keep Support, Thank you.
    """)