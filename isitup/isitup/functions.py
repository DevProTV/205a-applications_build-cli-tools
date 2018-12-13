import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Check the status of a website")
    parser.add_argument('url', type=str, help="url of the site to check")
    return parser.parse_args()


def normalize_url(url):
    if 'https://' not in url or 'http://' not in url:
        return f'http://{url}'
    else:
        return url


