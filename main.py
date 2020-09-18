#! /usr/bin/env python3

import os

config_available = [x.split('config_')[1] for x in os.listdir(os.path.expanduser('~/.config/gcloud/configurations'))]
active_config = ''
with open(os.path.expanduser('~/.config/gcloud/active_config'), 'r') as f:
    active_config = f.readline()

new_config = config_available[(config_available.index(active_config) + 1) % len(config_available)]

with open(os.path.expanduser('~/.config/gcloud/active_config'), 'w') as f:
    f.write(new_config)

if os.path.isfile(os.path.expanduser('~/.kube/config')):
    with open(os.path.expanduser('~/.kube/config'), "r") as f:
        lines = f.readlines()
    with open(os.path.expanduser('~/.kube/config'), "w") as f:
        for line in lines:
            if not line.__contains__("access-token:"):
                f.write(line)

print('Current config is now: ' + new_config)
