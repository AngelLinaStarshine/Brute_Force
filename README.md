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



