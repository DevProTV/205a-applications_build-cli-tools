import requests
from colorama import Fore
from .functions import get_args

def normalize_url(url):
    if 'https://' not in url or 'http://' not in url:
        return f'http://{url}'
    else:
        return url

def main():
    args = get_args()
    url = normalize_url(args.url)
    res = requests.get(url)
    if res.status_code != 200:
        print(f'{Fore.RED}The website {args.url} is down...')
    else:
        print(f'{Fore.GREEN}The website {args.url} is up!')


if __name__ == '__main__':
    main()
