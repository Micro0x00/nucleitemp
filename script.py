import sys
import os
for repo in open("nuclie.txt"):
    os.system(f"git clone {repo}")
