<h1>EEE3097S Design Project</h1>

## Features
- Write IMU data to CSV files
- Compress CSV files using BZ2 compression (& decompression)
- Encrypt CSV file using AES encryption (& decryption)



## Prerequisites

- Python3
- python-imaging
- python-smbus
- pycryptodome
- Internet connection

## Installation

sudo apt-get install python-pip 
sudo pip install RPi.GPIO
sudo pip install spidev
sudo apt-get install python-imaging
sudo apt-get install python-smbus
sudo pip install pycryptodome


## Included Files
<table>
	
  <tr>
    <th>File</th>
    <th>Explaination</th>
  </tr>
	
  <tr>
    <td>System.py</td>
    <td>Encompasses imu.py, compressor.py and Encrypt.py and runs each of them one after the other, checking to see if the correct output file has first been created</td>
  </tr>
	 <tr>
    <td>imu.py</td>
    <td>Reads sensor data from the IMU and writes it directly to a CSV file </td>
  </tr>
  <tr>
    <td>compressor.py</td>
    <td>Compresses the CSV file containing the IMU data. The compression used is BZip2 (BZ2)</td>
  </tr>
	 <tr>
    <td>Encrypt.py</td>
    <td>Encrypts the compressed CSV file. Uses AES encryption</td>
  </tr>
	 <tr>
    <td>Decrypt.py</td>
    <td>Decryptes the encrypted and compressed file</td>
  </tr>
		 <tr>
    <td>decompressor.py</td>
    <td>Decompresses the compressed file </td>
  </tr>
	 <tr>
    <td>Compare.py</td>
    <td>Compares the original file to the output file </td>
  </tr>
	

  
</table>

## Attributions



## Author
Johns Paul
Divyan Chetty

## License
[MIT](https://choosealicense.com/licenses/mit/)
