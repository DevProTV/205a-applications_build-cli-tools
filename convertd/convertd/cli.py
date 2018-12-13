from docopt import docopt

USAGE = """CONVERTD CLI
Usage:
    convertd [--format=<format>] FILE [OUT]
    convertd -h | --help
    convertd -v | --version

Arguments:
    FILE input file containing the data
    OUT output filename to place the converted data

Options:
    -h --help           Show this screen.
    -v --version        Show version.
    --format=<format>   Output format (json,csv) [default: json].
"""


def get_args():
    return docopt(USAGE, version="convertd 0.1.0")


def print_help():
    print(USAGE)
