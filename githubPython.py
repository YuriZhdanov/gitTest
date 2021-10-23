import requests
import os
import subprocess
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', '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')

owner = "kaltura"
# repo = input('What is your repo? ')
# branche = input('What is your branche? ')
# filename = input('What is your filename? ')

repo = 'platform-install-packages'
branche = '9.13'
filename = input('What is your filename? ')

params = {
    "state": "open",
}
headers = {'Authorization': f'token {token}'}

query_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{filename}"
r = requests.get(query_url, headers=headers, params=params)

fileinfo = r.json()
if fileinfo['download_url']:
    f = requests.get(fileinfo['download_url'], headers=headers, params=params)
    filecontents = f.text
    print('\n---------------------------------- file contents ----------------------------------')
    pprint(filecontents)