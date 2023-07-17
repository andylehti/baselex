import string

# Define all possible characters for bases
digits = string.printable

def baselex(number, from_base, to_base):
    if from_base < 2 or from_base > len(digits) or to_base < 2 or to_base > len(digits):
        raise ValueError("Invalid base")

    # Convert the number to base 10
    decimal_num = 0
    for digit in number:
        decimal_num = decimal_num * from_base + digits.index(digit)

    # Convert the decimal number to the target base
    if decimal_num == 0:
        return '0'

    output = ""
    while decimal_num > 0:
        output = digits[decimal_num % to_base] + output
        decimal_num //= to_base

    return output
  
number = '010'
from_base = 2
to_base = 10


# Testing

# Define the range of numbers to convert
start = 1
end = 10000

# Convert and check numbers within the range
for i in range(start, end+1):
    original_number = str(i)
    converted_number = baselex(original_number, 49, 34)
    back_converted_number = baselex(converted_number, 34, 49)
    assert original_number == back_converted_number, f"Error: {original_number} != {back_converted_number}"
print("All tests passed.")
