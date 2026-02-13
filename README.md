# Kudaibergenov_Python

QA Automation test task.

## Requirements

- Python 3.11+
- pytest

## Installation

```bash
python -m venv venv
```

Activate the virtual environment:

- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the program

```bash
python main.py
```

The program offers two modes:

- **Mode 1 - Single input:** One value is passed through all three checks independently
- **Mode 2 - Separate inputs:** Each check receives its own dedicated input

### Checks

1. **Check 1** - If the entered number is greater than 7, prints "Hello"
2. **Check 2** - If the entered name matches "John", prints "Hello, John"
3. **Check 3** - Parses input as a numeric array (supports `,` `;` and space separators) and outputs elements that are multiples of 3

## Run tests

```bash
python -m pytest test_main.py -v
```

## Task 2 - Bracket Sequence

Given bracket sequence: `[((())()(())]]`

**2a. Can this sequence be considered correct?**

No. The sequence is not correct. The bracket counts do not match:
- `[` appears 1 time, `]` appears 2 times
- `(` appears 6 times, `)` appears 5 times

**2b. What needs to be changed to make it correct?**

Change the first `]` (position 13) to `)`. This produces `[((())()(()))]` which is a valid bracket sequence.

### Bracket Validator (bonus)

A `validate_brackets(s)` function was written as a bonus solution to Task 2 in a separate file `brackets.py`. It uses a stack-based algorithm to check whether a bracket sequence is valid.

```bash
python brackets.py
```

**Note:** I do not fully understand the stack-based approach yet and plan to study it further. The algorithm was implemented with guidance, and while it works correctly, I want to deepen my understanding of how the stack tracks bracket nesting before I consider this concept fully learned.
