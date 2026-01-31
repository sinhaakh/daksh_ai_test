# daksh_ai_test
testing ai in coding

## Features

### double.py
A Python script that takes a number as input and prints its double.

**Features:**
- **Number Input**: Accepts numeric input and calculates the double of the number
- **Input Validation**: Validates that the input is a valid number. If invalid, prompts the user to enter a number again
- **Timeout Reminder**: If no input is received for 15 seconds, displays a reminder message
- **Auto-Exit**: If no input is received for 30 seconds after the reminder (45 seconds total), the program automatically exits
- **Continuous Loop**: Continuously prompts for numbers until timeout or manual exit (Ctrl+C)

**Usage:**
```bash
python double.py
```

**Example:**
```
Enter a number: 5
The double of 5.0 is 10.0

Enter a number: 3.5
The double of 3.5 is 7.0

Enter a number: 
Please enter a number (you have 30 more seconds)...
```

**Requirements:**
- Python 3.x
- Standard library only (no external dependencies)
