import zlib

original_data = open('test.csv', 'rb').read()
compressed_data = zlib.compress(original_data, zlib.Z_BEST_COMPRESSION)

compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))

print('Compressed: %d%%' % (100.0 * compress_ratio))