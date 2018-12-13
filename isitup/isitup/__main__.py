import argparse
import requests
from colorama import Fore

def get_args():
    parser = argparse.ArgumentParser(description="Check the status of a website")
    parser.add_argument('url', type=str, help="url of the site to check")
    return parser.parse_args()

def main():
    args = get_args()
    res = requests.get(args.url)
    if res.status_code != 200:
        print(f'{Fore.RED}The website {args.url} is down...')
    else:
        print(f'{Fore.GREEN}The website {args.url} is up!')


if __name__ == '__main__':
    main()
