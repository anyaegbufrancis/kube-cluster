#!/usr/bin/python3

import os
cmd = [
 "ansible-playbook template_play1.yaml -v", 
 "ansible-playbook template_play2.yaml -v", 
 "ansible-playbook other_plays.yaml -v"
  ]
for command in cmd:
  os.system(command)

print("Playbook run completed!!")
