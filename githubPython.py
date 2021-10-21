import requests
headers = {'Authorization': "Token " + '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'}
url = "https://api.github.com/repos/YuriZhdanov/gitTest/git/refs/heads"
branches = requests.get(url, headers=headers).json()
branch, sha = branches[-1]['ref'], branches[-1]['object']['sha']
res = requests.post('https://api.github.com/repos/YuriZhdanov/gitTest/git/refs', json={
    "ref": "refs/heads/newbranch",
    "sha": sha
}, headers=headers)
print(res.content)