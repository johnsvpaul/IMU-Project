import lzhw
import pandas as pd
from sys import getsizeof

gc = pd.read_csv("test.csv")

chunks = gc.shape[0] / 4 ## to have 4 chunks
compressed_chunks = lzhw.CompressedFromCSV("test.csv", chunksize = chunks)