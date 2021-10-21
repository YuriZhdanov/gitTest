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

query_url = f"https://api.github.com/repos/{owner}/{repo}/commits?path={filename}&sha={branche}"
params = {
    "state": "open",
}
headers = {'Authorization': f'token {token}'}

r = requests.get(query_url, headers=headers, params=params)

commitList = r.json()

print(f"sha: {commitList[0]['sha']}")
