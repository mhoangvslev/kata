from parser.Number import Number     
import sys

def main(input_number):
    number = Number(input_number)
    print(f"French: {str(number)}")

if __name__ == "__main__":
    # call main with args
    args = sys.argv[1:]
    input_number = int(args[0])
    main(input_number)
