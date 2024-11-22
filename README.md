## Brute Force Attack on AES and 3DES Encryption

This project demonstrates symmetric encryption using AES and 3DES, showcasing how these algorithms encrypt and decrypt data. 
It highlights the vulnerabilities of 3DES, particularly its susceptibility to brute-force attacks, and compares it to the more secure AES algorithm. 

Additionally, this project covers best practices for mitigating attacks on symmetric encryption, key management and proper padding schemes, and demonstrates encryption using different block cipher modes, including CBC (Cipher Block Chaining) and GCM (Galois/Counter Mode). AES in GCM mode is shown to provide both encryption and authentication, ensuring data integrity and confidentiality.

### Features:
- *Symmetric Encryption*: AES and 3DES using CBC and GCM modes.
- *Brute-force Attack Simulation*: Brute-force attacks on both AES and 3DES to highlight vulnerabilities.
- *Countermeasures*: Best practices for key management and encryption security.
- *Encryption Modes*: AES in both CBC and GCM modes.

### Security Countermeasures:
- *Key Derivation*: Using PBKDF2 with salt and multiple iterations to derive secure keys.
- *Authenticated Encryption*: AES-GCM to ensure both confidentiality and data integrity.
- *Key Management Best Practices*: Use of key rotation and secure key storage.

Output: 
AES Encrypted: 08e4263eb50f8e25b82b6d74a909b631e6a2cb9b5735893250018d237f1b6a08ca1dda7b99d9e27919c8620a4b861d27cbb0cb98fe5252779f4fb06371ba61dda95de1b5f8767814ac4a61fb9781f791139ab61fabb1af6cab00f58d1f03bc1f65591d10150e65fd1ea21318fb3cea40c93b15bc9678d7061908495ed667843c
AES Decrypted: Some people call this artificial intelligence, but the reality is this technology will enhance us.
3DES Encrypted: 0054f961371f23fe10f2d864c755466a2d3445a1f7620e9b0da5017f9a4817051f508ba06e021d46092a6096060dd2935a693001f40a29a79e76ea6ab1536e453dcd4e74f11feccae0e83ed7915a8f877d786b44adea1d94f1353edebe5d6b52699b5f0a1fe7e86e36aa64f1a2b09c18
3DES Decrypted: Some people call this artificial intelligence, but the reality is this technology will enhance us.
Attempting brute-force attack on AES...
Time taken for AES brute-force attack: 1.63 seconds
Attempting brute-force attack on 3DES...
Time taken for 3DES brute-force attack: 10.46 seconds

