import subprocess
import os.path
import time

x = 1

while (x < 3):
 
 fn = "output" + str(x) + ".csv"

 subprocess.call('python3 imu.py ' + fn , shell = True) #Sensehat
 
 
 while not os.path.exists(fn):                       #compression
     time.sleep(1)
 
 if os.path.isfile(fn):
  subprocess.call('python3 compressor.py '+ fn  , shell = True)
     
 else:
  raise ValueError("%s isn't a file!" % fn) 

 fn2 = "output" + str(x) + ".csv.bz2"
 

 while not os.path.exists(fn2):                       #encryption
  time.sleep(1)
    
 if os.path.isfile(fn2):
  subprocess.call('python3 Encrypt.py '+fn2  , shell = True)
        
 else:
  raise ValueError("%s isn't a file!" % fn2)  
                              
 x = x + 1
 
 print("DONE");
