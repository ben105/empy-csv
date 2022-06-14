import argparse

from auth import Auth
from datetime import datetime
from fetch import fetch
from pathlib import Path


parser = argparse.ArgumentParser(description='Process Emporia credentials.')
parser.add_argument('--email', dest='email', help='your Emporia email address', required=True)
parser.add_argument('--password', dest='password', help='your Emporia password', required=True)

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{Path.home()}/Downloads/Emporia Data {timestamp}.csv'

if __name__ == '__main__':
    args = parser.parse_args()
    emporia_auth = Auth(args.email, args.password)
    resp = fetch(emporia_auth, 'GET', '')

    with open(filename, 'wb') as csv_file:
        csv_file.write(resp.content)
