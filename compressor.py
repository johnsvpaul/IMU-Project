import bz2, os, sys, shutil, math
import filecmp
import sys

parameter = sys.argv[1]
input = parameter
output = input+".bz2"



#compression
with open(input, mode="rb") as fin, bz2.open(output, "wb") as fout:
    fout.write(fin.read())



#Validate Results:
input_size = os.path.getsize(input)
print("Uncompressed file Size is :", input_size, "bytes")

output_size = os.path.getsize(output)
print("Compressed file Size is :", output_size, "bytes")



reduction = round(((input_size-output_size)/input_size)*100)
print("Compression ratio : " + str(reduction) + "%")

