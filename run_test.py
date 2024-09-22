import os
import subprocess

flags = True
for e in os.listdir("test"):
    code = subprocess.call("python -B test/" + e, shell=True)
    if code != 0:
        flags = False

if not flags:
    raise AssertionError
