# wordlesolver
Written with Python 3.9

## How to use
Wordle Solver is a command line application. Run

```commandline
python3 solver.py
```

or

```commandline
python3 solver.py true
```

to use the list of words used in the original Wordle game.

To enter your guess, use this format `word:symbols`

The symbols available are the following:
* `_`: correct letter, correct position
* `?`: Correct letter, incorrect position
* `*`: Incorrect letter

Example: `piano:_**_?`

To exit the application you can either type `exit` in the console or fill in the correct word like this: `piano:_____`.
