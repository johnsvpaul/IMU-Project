import zipfile, os, time


file = "data.csv"
archive = "compressed_data_1.zip"

with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write(file)

print(f"Uncompressed size: {os.stat(file).st_size}")

print(f"Compressed size: {os.stat(archive).st_size}")
