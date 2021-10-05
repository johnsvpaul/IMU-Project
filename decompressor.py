import bz2, os, sys, shutil, math
import filecmp

input = "test.csv"
output = input+".bz2"
decomp = "decompressed.csv"

#decompression
with bz2.open(output, 'rb') as f_in:
    with open(decomp, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

decomp_size = os.path.getsize(decomp)
print("Decompressed file Size is :", decomp_size, "bytes")

print(filecmp.cmp(input, decomp, shallow=True))#checks if original file and decompressed file is the same