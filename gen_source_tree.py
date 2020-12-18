TREE=open("source_tree.txt").read()

import os
for line in TREE.split("\n"):
    if len(line.strip()) == 0:
        continue
    d = os.path.dirname(line)
    pth = os.path.join("STree",d)
    if not os.path.isdir(pth):
        os.makedirs(pth)
    with open(os.path.join("STree",line),"w") as f:
        f.write("dummy")
