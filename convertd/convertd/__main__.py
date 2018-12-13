import json
from .cli import get_args, print_help

from colorama import Fore
from tablib import Dataset

def main():
    args = get_args()
    filename = args['FILE']
    outpath = args['OUT']
    data_format = args['--format']

    if data_format not in ('json', 'csv'):
        print(f'Unsupported file format: {data_format}')
        print_help()
        return

    with open(filename) as f:
        raw = f.read()
        data = Dataset().load(raw)

    if outpath is None:
        if data_format == 'csv':
            output = f'{Fore.YELLOW}{str(data)}'
            print(output)
        else: #if default or json
            output = f'{Fore.YELLOW}{json.dumps(data.dict, indent=4)}'
            print(output)
    else:
        with open(outpath, 'w') as f:
            f.write(data.export(data_format))
         


if __name__ == '__main__':
    main()
