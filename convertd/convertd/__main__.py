import json
from .cli import get_args, print_help
from .functions import load_data, get_formatter

from colorama import Fore, Style


def main():
    args = get_args()
    filename = args["FILE"]
    outpath = args["OUT"]
    data_format = args["--format"]

    if data_format not in ("json", "csv"):
        print(
            (
                f"{Fore.RED}{Style.BRIGHT}"
                "Unsupported file format: "
                f"{data_format}{Style.RESET_ALL}"
            )
        )
        print_help()
        return

    data = load_data(filename)

    if outpath is None:
        formatter = get_formatter(data_format)
        output = f"{Fore.YELLOW}{formatter(data)}"
        print(output)
    else:
        with open(outpath, "w") as f:
            f.write(data.export(data_format))


if __name__ == "__main__":
    main()
