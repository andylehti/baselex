# Baselex
A Python code for converting numbers between different bases. This code supports both conversion from a specified base to specified base and conversion from base specified to a specified base. It also provides an option for handling leading zeroes in the number representation.

## Usage

To use the base conversion code, follow the example below:

```python
number = '010'
from_base_tuple = (2, True)
to_base_tuple = (10, False)

result = baselex(number, from_base_tuple, to_base_tuple)
print(result)  # Output: '2'
```

## Installation and Setup

To use the base conversion code, you need to have Python installed on your system. Additionally, the code requires no external libraries.

1. Clone the repository:
   ```
   git clone https://github.com/andylehti/baselex.git
   ```

2. Navigate to the project directory:
   ```
   cd baselex
   ```

3. Open the code file `baselex.py` in a text editor.

4. Set the `number`, `from_base_tuple`, and `to_base_tuple` variables to your desired values. Example:
   ```python
   number = '010'
   from_base_tuple = (2, True)
   to_base_tuple = (10, False)
   ```

5. Save the file and close the text editor.

6. Run the code from the command line:
   ```
   python3 baselex.py
   ```

7. The result of the base conversion will be displayed in the terminal.

## Work in Progress

Please note that this code is currently a work in progress. There are some aspects that require updating, particularly when the `leading_zeroes` option is set to `False`. The code functions correctly when `leading_zeroes` is `True`, but additional modifications are needed to handle the conversion accurately without leading zeroes.

## Testing

The code includes a testing section that demonstrates various scenarios of base conversion. It generates random numbers within a specified range and tests different base pairs and leading zero configurations. The test results are stored in a dictionary named `results`, which can be accessed for further analysis.

Please note that the testing section is primarily for evaluating the code's functionality and may not reflect the accurate behavior when `leading_zeroes` is set to `False`. Additional testing and modifications are necessary to ensure proper functionality under this configuration.

## Contributions

Contributions to the base conversion code are welcome. If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or raise an issue on the GitHub repository.
