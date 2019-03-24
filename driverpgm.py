from Extractor import Extractor
import os
datadir = './newdata/'
inputfiles = os.listdir(datadir)
for i in xrange(len(inputfiles)):
    inputfiles[i] = datadir+inputfiles[i]
result = Extractor(inputfiles)
ans = result.getalldiagnosis()
print(ans)
new = []
for i, j in ans.items():
    new += j
for i in new:
    print(i)
