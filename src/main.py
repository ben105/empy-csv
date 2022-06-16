import argparse

from auth import Auth
from datetime import datetime
from datetime import timedelta
from fetch import fetch
from pathlib import Path


parser = argparse.ArgumentParser(description='Process Emporia credentials.')
parser.add_argument('--email', dest='email', help='your Emporia email address', required=True)
parser.add_argument('--password', dest='password', help='your Emporia password', required=True)

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{Path.home()}/Downloads/Emporia Data {timestamp}.csv'

_today = datetime.today()
_before = _today - timedelta(10)

_today_str = _today.strftime('%Y-%m-%d')
_before_str = _before.strftime('%Y-%m-%d')

if __name__ == '__main__':
    args = parser.parse_args()
    emporia_auth = Auth(args.email, args.password)
    fetch(emporia_auth, 'GET', f'https://api.emporiaenergy.com/devices/usage/export?deviceGid=128097&startDate={_before_str}&endDate={_today_str}')
