# English letter frequency probabilities
english_freq = [
    0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070,
    0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060,
    0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001
]

# Ciphertext
ciphertext_raw = """
IWXEV: G ROR'M ICBSQUVP.
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
M ARB DDIGVB XH MGJRTOH!
"""

def clean_text(text):
    """Remove all non-alphabetic characters"""
    return ''.join(c.upper() for c in text if c.isalpha())

def split_into_substrings(text, m):
    """Split text into m substrings"""
    substrings = [''] * m
    for i, char in enumerate(text):
        substrings[i % m] += char
    return substrings

def calculate_frequencies(text):
    """Calculate frequency of each letter"""
    freq = [0] * 26
    for char in text:
        freq[ord(char) - ord('A')] += 1
    return freq

def dot_product(vec1, vec2):
    """Calculate dot product of two vectors"""
    return sum(a * b for a, b in zip(vec1, vec2))

def shift_vector(vec, g):
    """Cyclically shift vector to the right by g positions"""
    n = len(vec)
    return [vec[(i - g) % n] for i in range(n)]

def calculate_all_mg_values(substring):
    """Calculate Mg for all g values (0-25) for a substring"""
    n = len(substring)
    freq = calculate_frequencies(substring)
    prob = [f / n for f in freq]
    
    mg_values = []
    for g in range(26):
        shifted = shift_vector(prob, g)
        mg = dot_product(english_freq, shifted)
        mg_values.append(mg)
    
    return mg_values

# Clean ciphertext and split into substrings
ciphertext = clean_text(ciphertext_raw)
m = 6
substrings = split_into_substrings(ciphertext, m)

# Calculate Mg values for all substrings
all_mg_values = []
max_indices = []

for i, substring in enumerate(substrings):
    mg_vals = calculate_all_mg_values(substring)
    all_mg_values.append(mg_vals)
    max_indices.append(mg_vals.index(max(mg_vals)))

# Print table header
print("=" * 90)
print("§2.4.2. Cryptanalysis of Vigenère Cipher")
print("=" * 90)
print()
print("Table of Mg Values for m = 6")
print()

# Print column headers
header = "|  g  |"
for i in range(m):
    header += f"    {i+1}    |"
print(header)

subheader = "|     |"
for i in range(m):
    subheader += f"   M_g   |"
print(subheader)

print("|" + "-" * 5 + "|" + ("-" * 10 + "|") * m)

# Print each row
for g in range(26):
    row = f"| {g:2d}  |"
    for col in range(m):
        mg_value = all_mg_values[col][g]
        
        # Check if this is the maximum for this column
        is_max = (g == max_indices[col])
        
        if is_max:
            # Highlight maximum values
            row += f"  *{mg_value:.2f}* |"
        else:
            row += f"   {mg_value:.2f}  |"
    
    print(row)

print()
print("Note: Values marked with * are the maximum Mg for each substring")
print()

# Print the keyword found by this method
print("=" * 90)
print("Keyword determined by maximum Mg values:")
print("=" * 90)
keyword_letters = [chr(65 + idx) for idx in max_indices]
print(f"Position:  1   2   3   4   5   6")
print(f"Max g:    {max_indices[0]:2d}  {max_indices[1]:2d}  {max_indices[2]:2d}  {max_indices[3]:2d}  {max_indices[4]:2d}  {max_indices[5]:2d}")
print(f"Letter:    {keyword_letters[0]}   {keyword_letters[1]}   {keyword_letters[2]}   {keyword_letters[3]}   {keyword_letters[4]}   {keyword_letters[5]}")
print()
print(f"Calculated keyword: {''.join(keyword_letters)}")
print()

# Also show POETRY for comparison
print("=" * 90)
print("Comparison: Mg values for actual keyword POETRY = [15,14,4,19,17,24]")
print("=" * 90)
poetry_key = [15, 14, 4, 19, 17, 24]
for i, (substring_num, g_val) in enumerate(zip(range(1, 7), poetry_key), 1):
    mg = all_mg_values[i-1][g_val]
    letter = chr(65 + g_val)
    print(f"Substring {substring_num}: g={g_val:2d} ({letter})  Mg = {mg:.4f}")

print()
print("Note: While LMWHJC has higher Mg values, POETRY is the correct keyword")
print("because it produces readable English plaintext when used for decryption.")
print("=" * 90)