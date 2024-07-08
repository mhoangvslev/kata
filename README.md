# kata

## Usage

```bash
python main.py <number> # Any number
python test.py # Test suites
```

## Some explanations
I first wrote a rushed version using just lists.

The idea is to simulate how humans do it:
- Break the number by thousand lexemes, 
- Break each thousand lexeme into Hundred, Ten and Unit lexeme
- Pronounce each lexeme along with it power of thousand

The final submission uses Strategy pattern where different lexeme has different implementation for `__str__()`. 

## Disclaimer
Copilot was used solely to complete code lines.