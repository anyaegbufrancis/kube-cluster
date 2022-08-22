#!/usr/bin/python3

import os
cmd = [
 "ansible-playbook template_play1.yaml -v", 
 "ansible-playbook template_play2.yaml -v", 
 "ansible-playbook template_play3.yaml -v",
 "ansible-playbook template_play4.yaml -v",
 "ansible-playbook template_play5.yaml -v"
  ]
for command in cmd:
  os.system(command)
