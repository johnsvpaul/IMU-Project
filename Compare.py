import filecmp
  
f1 = "2018-09-19-03_57_11_VN100.csv"
f2 = "DecryptedFile.csv"
  
# shallow comparison
result = filecmp.cmp(f1, f2)
print(result)
# deep comparison
result = filecmp.cmp(f1, f2, shallow=False)
print(result)