'''Encrypt plaintext using Vigenere Cipher with given key'''
def encrypt(plain, key):
    
    #clean plaintext (no spaces, letters only, uppercase)
    plain = "".join(char.upper() for char in plain if char.isalpha())
    
    #clean keyword and convert to numbers
    key = key.upper()
    encoded_key = alphabet_coding(key)
    
    n = len(key)
    chunks = []
    
    #split plaintext into len(key)-sized chunks
    for i in range(0, len(plain), n):
        chunks.append(plain[i:i+n])
    
    encoded_chunks = []
    
    #encode chunks
    for chunk in chunks:
        encoded_chunks.append(alphabet_coding(chunk))
    
    
    #add key to each chunks
    output = []
    
    for i in range(len(encoded_chunks)):
        output.append([x + k for x,k in zip(encoded_chunks[i], encoded_key)])
        
    #decode output
    decoded_output = []
    for word in output:
        decoded_output.append(alphabet_decoding(word))
        
    #return as string
    return ''.join(decoded_output)
    
'''Decrypt ciphertext using Vigenere Cipher with given key'''
def decrypt(cipher, key):
    #clean cipher (no spaces, letters only, lowercase)
    cipher = "".join(char.lower() for char in cipher if char.isalpha())
    
    #clean keyword and convert to numbers
    key = key.lower()
    encoded_key = alphabet_coding(key)
    
    n = len(key)
    chunks = []
    
    #split ciphertext into len(key)-sized chunks
    for i in range(0, len(cipher), n):
        chunks.append(cipher[i:i+n])
        
    encoded_chunks = []
    
    #encode chunks
    for chunk in chunks:
        encoded_chunks.append(alphabet_coding(chunk))
        
    #subtract key to each chunks
    output = []
    
    for i in range(len(encoded_chunks)):
        output.append([y - k for y,k in zip(encoded_chunks[i], encoded_key)])
        
    #decode output
    decoded_output = []
    for word in output:
        decoded_output.append(alphabet_decoding(word))
    
    #return as string
    return ''.join(decoded_output)
    
'''Takes a string and returns its encoding as a list of nums'''
def alphabet_coding(str):
    str = str.upper()
    result = []
    for c in str:
        result.append(ord(c) - ord('A'))
    
    return result

'''Takes list of ints and decodes them into letters'''
def alphabet_decoding(arr):
    result = []
    for num in arr:
        result.append(chr(ord('a') + num%26))
    
    return ''.join(result)

    
if __name__ == '__main__':
    print(alphabet_coding('dog'))
    print(alphabet_decoding([3,14,6]))
    
    
    print(encrypt("Hi, my name is Akhil", 'dog'))
    print(decrypt("kwsbbgpsovoqkwr", 'dog'))