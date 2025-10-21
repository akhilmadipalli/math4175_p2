'''Encrypt plaintext using Vigenere Cipher with given key'''  
def encrypt(plain, key):
    plain = "".join(char.upper() for char in plain if char.isalpha())
    key = key.upper()
    
    
    return ''.join(
        chr(((ord(plain[i]) - ord('A') + ord(key[i % len(key)]) - ord('A')) % 26) + ord('A'))
        for i in range(len(plain))
    )

'''Decrypt ciphertext using Vigenere Cipher with given key'''
def decrypt(cipher, key):
    cipher = cipher.lower()
    key = key.lower()
    
    return ''.join(chr(((ord(cipher[i]) + ord('a') - ord(key[i % len(key)]) - ord('a')) % 26) + ord('a'))
                   for i in range(len(cipher))
                   )
    
if __name__ == '__main__':
    print(encrypt('Hi, my name is Akhil', 'dog'))
    print(decrypt('kwsbbgpsovoqkwr', 'dog'))