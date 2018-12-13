from .cli import get_args

from colorama import Fore

def main():
    args = get_args()
    print(args)


if __name__ == '__main__':
    main()
