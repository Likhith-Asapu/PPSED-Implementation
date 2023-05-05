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

In scheme 1, scheme 2, and secure update files present in the user directory represent the files present in the user computer. Similarly, files present in the server directory represent the files present in the server device. In scheme 2 the files present in the user_mobile device represent the files present in the user's mobile device.


## Usage

All three schemes follow the same procedure of encryption of plain text to cipher text where the plain text files are encrypted and sent to the Server. Then the retrieval algorithm is run where files containing the keyword are retrieved either to the user directory(for scheme 1 and secure update) or user_mobile directory(Scheme 2). These retrieved files can be decrypted using the decryption algorithm.

### Encryption

To run the encrytion code for Scheme 1, run the following command:

```bash
cd Scheme1/
python3 encryption.py
```

The files to be encrypted must be present in the user directory. Enter the path of the file to be encrypted relative to the user directory. The following prompt pops up in running the code. 

```bash
Enter File Name for Encryption: <path of the file to be encrypted relative to user directory>
```

Example:
    
```bash
Enter File Name for Encryption: 2.txt
```

File 1.txt is present in the user directory. Multiple files can be encrypted by running the code multiple times. 

Simlarly to run encryption code for scheme 2 change directory to scheme 2 and run ```python3 encryption.py```.

The encrypted file is present in the Server folder and the corresponding key for that file can be found in the user directory as a .key file.

### Retrieval

To run the retrieval code for any scheme change directory to that scheme folder then run the following command:

```bash
python3 retrieval.py
```

The following prompt pops up in running the code. 

```bash
Enter Keyword: <keyword to be searched>
```

Example:
    
```bash
Enter Keyword: work
```
Output:
```bash
Enter Keyword: work
Retrieved file 2.enc
Retrieved file 3.enc
```

For scheme 1 and secure update these files will be retrieved to the user directory. For scheme 2 these files will be retrieved to the user_mobile directory.

### Decryption

To run the decryption code for any scheme change directory to that scheme folder and ensure that for scheme 1 and secure update the files are present in user directory whereas for scheme 3 they are present in the user_mobile directory. Also make sure that the key for the file is present in the folder as .key file. Run the following command:

```bash
python3 decryption.py
```

The following prompt pops up in running the code. 

```bash
Enter File Name for Decryption: <path of the file to be decrypted relative to user directory>
```

Example:
    
```bash
Enter File Name for Decryption: 2.enc
```
This will use the contents of 2.key as the key to decrypt the file 2.enc.

### Keyword Dictionary

Words can be added to the key word dictionary present in `user/word_indices.json` for each scheme. Maximum size of the keyword dictinoary can be changed by changing the parameter $d$ present in the `imports_and_libraries.py` present in each scheme folder. The maximum number of keywords supported for parameter $d$ is $2^d$.

### Folder Reset

To reset the folder to the original state where none of the files are encypted and the server folder is empty, run the following command:

```bash
python3 clean.py
```

