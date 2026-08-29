# Team-Collabration-Project
To create a practice repository and practice collabrations and features on **github**\
##Features✨
  - Add, subtract, multiply, and divide two numbers
  - Handles invalid number input gracefully (won't crash)
  - Handles division by zero
  - Keeps running until you choose to quit
### Requirement
**- Python 3.x (no external libraries needed)

## How to Run

```bash
python simple_calculator.py
```

## Usage

1. Run the program.
2. Enter the first number when prompted (or type `quit` to exit).
3. Enter an operator: `+`, `-`, `*`, or `/`.
4. Enter the second number.
5. The result is printed, and the program asks for the next calculation.

### Example

```
=== Simple Calculator ===
Operations: + - * /
Type 'quit' to exit

Enter first number (or 'quit'): 10
Enter operator (+, -, *, /): +
Enter second number: 5
Result: 15.0

Enter first number (or 'quit'): quit
Goodbye!
```

## Code Structure

| Function      | Description                                |
|---------------|---------------------------------------------|
| `add(a, b)`      | Returns the sum of two numbers           |
| `subtract(a, b)` | Returns the difference of two numbers    |
| `multiply(a, b)` | Returns the product of two numbers       |
| `divide(a, b)`   | Returns the quotient, or an error message if dividing by zero |
| `main()`         | Runs the interactive command-line loop   |

## Concepts Practiced

- Variables
- Functions
- Conditional statements (`if` / `elif` / `else`)
- `while` loops
- Basic input/output
- Exception handling (`try` / `except`)

## Possible Extensions

- Add a power/exponent operator (`**`)
- Add a running history of past calculations
- Support more advanced operations (square root, modulo, etc.)
- Add unit tests for each function**
