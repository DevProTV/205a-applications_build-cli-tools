from textwrap import dedent
from .functions import get_args, normalize_url

import requests
from colorama import Fore



def main():
    args = get_args()
    url = normalize_url(args.url)
    try:
        res = requests.get(url)
        if res.status_code != 200:
            print(f'{Fore.RED}The website {args.url} is down...')
        else:
            print(f'{Fore.GREEN}The website {args.url} is up!')
    except requests.exceptions.ConnectionError as e:
        message = '\n'.join(
                (f'{Fore.YELLOW}Could not connect to {args.url}.',
                'Check your url and try again.')
            )
        print(message)
    
if __name__ == '__main__':
    main()
