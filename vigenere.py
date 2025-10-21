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
    return ''.join(decoded_output)
    

'''Takes a string and returns its encoding as a list'''
def alphabet_coding(str):
    coding = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 
        'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 
        'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
        }
    result = []
    for c in str:
        result.append(coding[c])
    return result

'''Takes list of ints and decodes them into letters'''
def alphabet_decoding(arr):
    coding = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}
    result = []
    for num in arr:
        result.append(coding[num%26])
    return ''.join(result)
    
if __name__ == '__main__':
    print(encrypt('Hi, my name is Akhil', 'dog'))