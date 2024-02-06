#This script about list down the GitHub pull request of a repo
"""
1.Request
2.API(url)---->Pull
3.JSon--->Dictionary
4.Print (list of usernames)
"""

import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_detail = response.json()

for element in range(len(complete_detail)):
    print(complete_detail[element]["user"]["login"])





