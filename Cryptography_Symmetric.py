import time
from Crypto.Cipher import AES, DES3
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def secure_key(password, salt, key_len=32, iterations=100000):
    return PBKDF2(password.encode(), salt, dkLen=key_len, count=iterations)

def aes_encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return cipher.iv + ct_bytes

def aes_decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    ct = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ct), AES.block_size)
    return decrypted.decode()

def des3_encrypt(plain_text, key):
    cipher = DES3.new(key, DES3.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), DES3.block_size))
    return cipher.iv + ct_bytes

def des3_decrypt(ciphertext, key):
    iv = ciphertext[:DES3.block_size]
    ct = ciphertext[DES3.block_size:]
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ct), DES3.block_size)
    return decrypted.decode()

def brute_aes(ciphertext, key_space):
    print("Attempting brute-force attack on AES...")
    start_time = time.time()

    for key_candidate in key_space:
        try:
            cipher = AES.new(key_candidate, AES.MODE_CBC)
            decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
            if decrypted == b"Some people call this artificial intelligence, but the reality is this technology will enhance us.":
                print(f"AES Key found: {key_candidate.hex()}")
                break
        except ValueError:
            continue

    print(f"Time taken for AES brute-force attack: {time.time() - start_time:.2f} seconds")

def brute_3des(ciphertext, key_space):
    print("Attempting brute-force attack on 3DES...")
    start_time = time.time()

    for key_candidate in key_space:
        try:
            cipher = DES3.new(key_candidate, DES3.MODE_CBC)
            decrypted = unpad(cipher.decrypt(ciphertext), DES3.block_size)
            if decrypted == b"Some people call this artificial intelligence, but the reality is this technology will enhance us.":
                print(f"3DES Key found: {key_candidate.hex()}")
                break
        except ValueError:
            continue

    print(f"Time taken for 3DES brute-force attack: {time.time() - start_time:.2f} seconds")

def main():
    password = "ghbgsvg5674++-dfj=!?f"
    salt = get_random_bytes(16)
    key = secure_key(password, salt)

    plaintext = "Some people call this artificial intelligence, but the reality is this technology will enhance us."

    aes_key = get_random_bytes(32)
    aes_ciphertext = aes_encrypt(plaintext, aes_key)
    print(f"AES Encrypted: {aes_ciphertext.hex()}")
    decrypted_aes = aes_decrypt(aes_ciphertext, aes_key)
    print(f"AES Decrypted: {decrypted_aes}")

    des3_key = get_random_bytes(24) 
    des3_ciphertext = des3_encrypt(plaintext, des3_key)
    print(f"3DES Encrypted: {des3_ciphertext.hex()}")
    decrypted_des3 = des3_decrypt(des3_ciphertext, des3_key)
    print(f"3DES Decrypted: {decrypted_des3}")

    key_space_aes = [get_random_bytes(32) for _ in range(100000)] 
    brute_aes(aes_ciphertext, key_space_aes)

    key_space_3des = [get_random_bytes(24) for _ in range(100000)] 
    brute_3des(des3_ciphertext, key_space_3des)

if __name__ == "__main__":
    main()
