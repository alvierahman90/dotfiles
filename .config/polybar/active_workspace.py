#!/usr/bin/env python3

import json
import subprocess

result = subprocess.run(['i3-msg','-t','get_workspaces'], 
        stdout=subprocess.PIPE).stdout.decode('utf-8')
workspaces = json.loads(result)

for i in workspaces:
    if i["focused"]:
        print("Current workspace: {0}".format(i["name"]))
