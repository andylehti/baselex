import string
digits = string.printable

def baselex(number, from_base_tuple, to_base_tuple):
    from_base, from_base_leading_zeroes = from_base_tuple
    to_base, to_base_leading_zeroes = to_base_tuple

    if from_base < 2 or from_base > len(digits) or to_base < 2 or to_base > len(digits):
        raise ValueError("Invalid base")

    # Convert the number to base 10
    if from_base_leading_zeroes:
        decimal_num = 0
        for digit in number:
            decimal_num = decimal_num * from_base + digits.index(digit)
    else:
        decimal_num = 0
        for i, digit in enumerate(reversed(number)):
            decimal_num += digits.index(digit) * (from_base ** i)

    # Convert the decimal number to the target base
    if decimal_num == 0:
        return '0'

    if to_base_leading_zeroes:
        output = ""
        while decimal_num > 0:
            output += digits[decimal_num % to_base]
            decimal_num //= to_base
        return output[::-1]  # reverse the string
    else:
        output = ""
        while decimal_num > 0:
            output = digits[decimal_num % to_base] + output
            decimal_num //= to_base
        return output
import random

## REMINDER THAT THIS CODE IS NOT WELL TESTED YET, AND THERE ARE ERRORS WITH THE LEADING ZEROES CURRENTLY:

# Example usage
number = '010'
from_base_tuple = (2, True)
to_base_tuple = (10, False)

# Conversion from one base to another
converted_result = baselex(number, from_base_tuple, to_base_tuple)
print(f"{number} in base {from_base_tuple[0]} with leading zeroes {from_base_tuple[1]} converted to base {to_base_tuple[0]} with leading zeroes {to_base_tuple[1]}: {converted_result}")

# Conversion from one base to another
converted_back = baselex(converted_result, to_base_tuple, from_base_tuple)
print(f"{converted_result} in base {to_base_tuple[0]} with leading zeroes {to_base_tuple[1]} converted back to base {from_base_tuple[0]} with leading zeroes {from_base_tuple[1]}: {converted_back}")

###### BELOW THIS LINE IS FOR TESTING PURPOSES

# Define the range of numbers to convert
start = 38453
end = 47832857553263475735

# Define the number of random numbers to generate
num_samples = 1

# Generate the random numbers
random_numbers = [random.randint(start, end) for _ in range(num_samples)]

# Define the base pairs to test
base_pairs = [
    (from_base, to_base)
    for from_base in range(2, len(digits)+1)  # from base 2 to max base
    for to_base in range(2, len(digits)+1)  # to base 2 to max base
]

# Define the leading zero configurations to test
leading_zero_configs = [
    (from_base_leading_zeroes, to_base_leading_zeroes)
    for from_base_leading_zeroes in [False, True]
    for to_base_leading_zeroes in [False, True]
]

# Initialize a dictionary to store the test results
results = {}

# Test all combinations of base pairs and leading zero configurations
for base_pair in base_pairs:
    for leading_zero_config in leading_zero_configs:
        # Initialize counters for passed and failed tests
        num_passed = 0
        num_failed = 0

        # Convert each random number and then convert it back
        for number in random_numbers:
            try:
                # Convert the number to a string in the from_base
                number_str = baselex(str(number), (base_pair[0], leading_zero_config[0]), (10, False))

                # Convert the number to the to_base and then convert it back to the from_base
                converted_back_str = baselex(
                    baselex(number_str, (base_pair[0], leading_zero_config[0]), (base_pair[1], leading_zero_config[1])),
                    (base_pair[1], leading_zero_config[1]),
                    (base_pair[0], leading_zero_config[0])
                )

                # Check if the original number and the converted back number are equal
                if int(number_str, base_pair[0]) == int(converted_back_str, base_pair[0]):
                    num_passed += 1
                else:
                    num_failed += 1
            except:
                num_failed += 1

        # Store the test results
        results[(base_pair, leading_zero_config)] = (num_passed, num_failed)

results
