import parser
from sys import argv
# i want to show the awesome zen python message


def main(argvs):

    # lets create some esolang
    # setup registers
    a = 0
    x = 0
    y = 0

    # create the stack
    stack = [0]

    parser.parse(a, x, y, stack)

    input("")
    return 0


if __name__ == "__main__":
    exit(main(argv))
