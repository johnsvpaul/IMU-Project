import gzip, os, shutil

input = "test.csv"
output = "compressed.csv.gz"
decomp = "new3.csv"
#compressor
with open(input, 'rb') as f_in, gzip.open(output, 'wb') as f_out:
    f_out.writelines(f_in)
#decompressor
with gzip.open(output, 'rb') as f_in:
    with open(decomp, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


#Validate Results:
input_size = os.path.getsize(input)
print("Uncompressed file Size is :", input_size, "bytes")

output_size = os.path.getsize(output)
print("Compressed file Size is :", output_size, "bytes")

#decomp_size = os.path.getsize(decomp)
#print("Decompressed file Size is :", decomp_size, "bytes")

reduction = ((input_size-output_size)/input_size)*100
print("Compression ratio : " + str(reduction) + "%")