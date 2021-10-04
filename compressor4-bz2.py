import bz2, os, sys, shutil, math
import filecmp

input = "test.csv"
output = input+".bz2"
decomp = "decompressed.csv"

#compression
with open(input, mode="rb") as fin, bz2.open(output, "wb") as fout:
    fout.write(fin.read())

#decompression
with bz2.open(output, 'rb') as f_in:
    with open(decomp, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


#Validate Results:
input_size = os.path.getsize(input)
print("Uncompressed file Size is :", input_size, "bytes")

output_size = os.path.getsize(output)
print("Compressed file Size is :", output_size, "bytes")

decomp_size = os.path.getsize(decomp)
print("Decompressed file Size is :", decomp_size, "bytes")

reduction = round(((input_size-output_size)/input_size)*100)
print("Compression ratio : " + str(reduction) + "%")

print(filecmp.cmp(input, decomp, shallow=True))#checks if original file and decompressed file is the same