# PPSED-Implementation

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This Repository contains the implementation of Privacy Preserving Keyword Searches on Remote Encrypted Data (PPSED) Protocol. The schemes implemented in this repo can be found in this paper: [https://eprint.iacr.org/2004/051.pdf](https://eprint.iacr.org/2004/051.pdf) 

## Requirements

- Python 3.10 or greater
- nltk
- glob
- shutil
- secrets

## Folder Structure

```
PPSED-Implementation
├───Scheme1
│   ├───user
│   ├───server
│   └───Scheme1 related files
├───Scheme2
│   ├───user
│   ├───user_mobile
│   ├───server
│   └───Scheme2 related files
├───SecureUpdate
│   ├───user
│   ├───server
│   └───SecureUpdate related files
├───file_decryption.py
├───file_encryption.py
├───README.md
├───one_time_pad.py
└───pseudo_random.py
```

In scheme 1, scheme 2, and secure update files present in the user directory represent the files present in the user computer. Similarly, files present in the server directory represent the files present in the server device. In scheme 2 the files present in the the user_mobile device represent the files present in the user's mobile device.


## Usage

### Scheme 1

To run the code for Scheme 1, run the following command:

```bash
$ cd Scheme1/
$ python3 encryption.py
```

make sure that the files to be encrypted are present in the user directory. Enter the path of the file to be encrypted relative to user directory 

```bash
cd Scheme1/
python3 encryption.py
```



