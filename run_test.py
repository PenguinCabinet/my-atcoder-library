import os
import subprocess

for e in os.listdir("test"):
    subprocess.call("python -B test/" + e, shell=True)
