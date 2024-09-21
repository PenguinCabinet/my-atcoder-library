import os

for e in os.listdir("test"):
    os.system("python -B test/" + e)
