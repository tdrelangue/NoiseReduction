from os import walk
from Reduce import reduce

mypath = "Noisy"
returnPath = "Quiet"
files = []
for (_, _, filenames) in walk(mypath):
    files.extend(filenames)

for file in files:
    reduce(mypath, file, returnPath)
