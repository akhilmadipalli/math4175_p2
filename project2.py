'''Author: Akhil Madipalli'''

#global freq table
freq = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070,
0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060,
0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]

'''Project 2b'''
def project2():
    # Open output file
    with open('output.txt', 'w') as f:
        raw_cipher = """IWXEV: G ROR'M ICBSQUVP.
        YIWM R JXBI MF QPM M'F CGKWRZ,
        KFPH M'F EMI OQHEE IVI WVYS.
        HLHLEW W'Q ZVRIWRZ DMGS JHIETHJNC
        YCR QBOCS IT BE RWS LXRB.
        X USM LQTR XH DW PFXAIGIWW,
        MF KN RIGKSGSW B'D PTGMZECS.
        W GTE KPBEZV KN PMYFAPZW,
        ULR VCH B DGHG QR DGCR.
        JHI QDAIMZKT W GTE'R GSQXDZTF
        AAVL X GXTEB PH XAV DDCX HW RWS WMRGGG,
        MY Z KJGX ZF SE TSK JMBSXAZLV
        CV ARTT W NNJR RCQX UMLB JKFK IVIKV.
        YCR FXWMGS XAV DGWHZV QD CJMVL,
        BM THFP BWRW ZQ UWPEVB LWXA UMJPX,
        ARTT Z NNJR EIX YFMS OATP,
        MG VEOV G RCQX KM IOOX JMBS SNK.
        YCR XAVPT'G XBDCH KLXE GI WW WRPZ
        KMMY KN BMZYRROT HE KN VITU,
        G SCR'M BLDK MY Z'K GSXBIGCU,
        SK ASHH KXKRXBK HLR DT FXU.
        QD, WJ BK'Q BM XNIL IC AKZRT MSN,
        KFTFI'L EM CSIW WMG UIMKGCU WHIC,
        X AER KFXBO MYYI W LTMC LFMMKCC,
        ORW UMC'H ATER IC FX R ZDFI.
        LF PTAIFSCG HLTK G ACZX PMJ,
        ORW NGHV XARR NCY PVPT BITI.
        LDK MM'J LTOVEP KPWP MZKT
        GS FLQI GER XMDRFRV BTOV.
        AVPT W WMRLS PILZBT HLX DYXZ FHO,
        UXHL T WYRS WH MCGM VXU,
        GCGXXRB DT QTZJXBK RFS BM PXKRTF,
        M ARB DDIGVB XH MGJRTOH!"""

        #clean cipher text
        cipher = "".join(char.lower() for char in raw_cipher if char.isalpha())
        
        '''Part 1: Index of Coincedences'''
        #Step(1): m = 5
        y_5 = split_into_substrings(cipher, 5)
        ic = []
        for substring in y_5:
            ic.append(index_of_coincedence(substring))
        f.write("Step 1 (m = 5): Print index of coincedence of each substring\n" + ", ".join(str(val) for val in ic) + "\n\n")
        
        #Step(2): m = 6
        y_6 = split_into_substrings(cipher, 6)
        ic = []
        for substring in y_6:
            ic.append(index_of_coincedence(substring))
        f.write("Step 2 (m = 6): Print index of coincedence of each substring\n" + ", ".join(str(val) for val in ic) + "\n\n")

        
        #Step(3): m = 7
        y_7 = split_into_substrings(cipher, 7)
        ic = []
        for substring in y_7:
            ic.append(index_of_coincedence(substring))
        f.write("Step 3 (m = 7): Print index of coincedence of each substring\n" + ", ".join(str(val) for val in ic) + "\n\n")
        
        f.write("This verifies that m = 6 is the correct guess, since the IC of the substrings when the ciphertext is split into 6-letter chunks most closely aligns the IC of English plaintext (0.065)\n\n")

        #generate q vectors for y_6 (m = 6)
        qs = [q_vec(y_i) for y_i in y_6]

        #create list of q vectors after shifts
        v_gs = []
        for q in qs:
            v_g_i = []
            #shift from 0 to 25
            for g in range(26):
                v_g_i.append(generate_v_g(q, g))
            v_gs.append(v_g_i)
        
        #calculate M_g for all subtrings y_i
        M_gs = []
        for q_all_shifts in v_gs:
            M_g_yi = []
            for q_shifted in q_all_shifts:
                M_g_yi.append(dot_product(freq,q_shifted))
            M_gs.append(M_g_yi)
        
        # Create table with M_g values
        f.write("Table of M_g values for each substring and shift:\n")
        f.write("=" * 100 + "\n")
        f.write(f"{'g':<5} {'y1':<15} {'y2':<15} {'y3':<15} {'y4':<15} {'y5':<15} {'y6':<15}\n")
        f.write("=" * 100 + "\n")
        
        for g in range(26):
            row = f"{g:<5} "
            for i in range(6):
                row += f"{M_gs[i][g]:<15.6f} "
            f.write(row + "\n")
        
        f.write("=" * 100 + "\n\n")
        
        #Decode key using max vals of M_g in each y_i
        key = ""
        for M_g_values in M_gs:
            best_shift = M_g_values.index(max(M_g_values))
            key += chr(best_shift + ord('A'))

        f.write(f"Key: {key}\n\n")

        # Decrypt the cipher
        plaintext = decrypt(cipher, key)
        
        #Formatted plaintext
        formatted = """Title: I can't remember.
Just a line to say I'm living,
That I'm not among the dead.
Though I'm getting more forgetful
And mixed up in the head.
I got used to my arthritis,
To my dentures I'm resigned.
I can manage my bifocals,
But God I miss my mind.
For sometimes I can't remember
When I stand at the foot of the stairs,
If I must go up for something
Or have I just come down from there.
And before the fridge so often
My poor mind is filled with doubt,
Have I just put food away or
Have I come to take some out.
And there's times when it is dark
With my nightcap on my head,
I don't know if I'm retiring
Or just getting out of bed.
So if it's my turn to write you
There's no need for getting sore.
I may think that I have written
And don't want to be a bore.
So remember that I love you,
And wish that you were near.
Now it's nearly mailtime
So must say goodbye dear.
Here I stand beside the mailbox
With a face so very red,
Instead of mailing you my letter
I had opened it instead."""
        
        f.write("Decrypted Plaintext (Not Formatted):\n")
        f.write("=" * 100 + "\n")
        f.write(plaintext + "\n")
        f.write("=" * 100 + "\n\n")
        
        f.write("Decrypted Plaintext (Formatted):\n")
        f.write("=" * 100 + "\n")
        f.write(formatted + "\n")
        f.write("=" * 100 + "\n")

    print("Output written to output.txt")

    
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

'''find dot product of vectors x and y'''
def dot_product(x,y):
    return sum(a*b for a,b in zip(x,y))

'''get frequency of all 26 letters in str'''
def get_freq(str):
    str = str.upper()
    freq = [0] * 26
    
    for i in range(len(str)):
        freq[(ord(str[i]) - ord('A'))%26] += 1
        
    return freq

'''right shift q by g'''
def generate_v_g(q, g):
    return [q[(i + g)%26] for i in range(26)]

'''generate q vector of y_i'''
def q_vec(y_i):
    N = len(y_i)
    
    frequencies = get_freq(y_i)
    
    q = [f/N for f in frequencies]
    
    return q
    
'''Calculate index of coincedence of given string (Prob two randomly selected characters in x are equal)'''
def index_of_coincedence(x):
    n = len(x)
    frequencies = get_freq(x)
    return sum(f * (f - 1) for f in frequencies) / (n * (n - 1))


'''Split text into m substrings (y1,y2,...,y_m)'''      
def split_into_substrings(str, m):
    substrings = [''] * m
    for i, char in enumerate(str):
        substrings[i % m] += char
    return substrings

if __name__ == '__main__':
    project2()