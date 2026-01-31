#parser means it reads the values in terminal and arguments are values inside the terminal.
#help is not imp but useful for user it helps when user entered help in terminal
import argparse
parser=argparse.ArgumentParser(description="enter colour")
parser.add_argument("--colour",choices=["red","blue","green"],help=("choose any colour"))
arg=parser.parse_args()
print("you choosed:",arg.colour)
