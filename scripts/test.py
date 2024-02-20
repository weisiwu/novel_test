import os
from pathlib import *

basePath = Path(__file__).parent
txt = basePath / "test.txt"
resultPath = basePath / "result_raw.txt"

with open(txt, "r", encoding="utf8") as f:
    result = []
    for line in f.readlines():
        lineLen = len(line)
        if lineLen >= 40 and lineLen <= 45:
            result.append(line)

with open(resultPath, "w", encoding="utf8") as f:
    for line in result:
        f.write("%s" % line)

    print("finish")
