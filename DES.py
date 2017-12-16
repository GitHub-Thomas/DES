InitialPermutation = [58,50,42,34,26,18,10,2,
                      60,52,44,36,28,20,12,4,
                      62,54,46,38,30,22,14,6,
                      64,56,48,40,32,24,16,8,
                      57,49,41,33,25,17,9,1,
                      59,51,43,35,27,19,11,3,
                      61,53,45,37,29,21,13,5,
                      63,55,47,39,31,23,15,7]

InitialPermutation_1 = [40,8,48,16,56,24,64,32,
                        39,7,47,15,55,23,63,31,
                        38,6,46,14,54,22,62,30,
                        37,5,45,13,53,21,61,29,
                        36,4,44,12,52,20,60,28,
                        35,3,43,11,51,19,59,27,
                        34,2,42,10,50,18,58,26,
                        33,1,41,9,49,17,57,25]

ExpansionPermutation = [32,1,2,3,4,5,
                        4,5,6,7,8,9,
                        8,9,10,11,12,13,
                        12,13,14,15,16,17,
                        16,17,18,19,20,21,
                        20,21,22,23,24,25,
                        24,25,26,27,28,29,
                        28,29,30,31,32,1]

sbox1 = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
         0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
         4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
         15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]

sbox2 = [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
         3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
         0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
         13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]

sbox3 = [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
         13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
         13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
         1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

sbox4 = [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
         13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
         10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
         3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]

sbox5 = [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
         14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
         4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
         11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]

sbox6 = [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
         10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
         9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
         4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

sbox7 = [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
         13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
         1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
         6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]

sbox8 = [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
         1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
         7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
         2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]

Permutation = [16,7,20,21,29,12,28,17,
               1,15,23,26,5,18,31,10,
               2,8,24,14,32,27,3,9,
               19,13,30,6,22,11,4,25]

PermutationChoose1 = [57,49,41,33,25,17,9,
                      1,58,50,42,34,26,18,
                      10,2,59,51,43,35,27,
                      19,11,3,60,52,44,36,
                      63,55,47,39,31,23,15,
                      7,62,54,46,38,30,22,
                      14,6,61,53,45,37,29,
                      21,13,5,28,20,12,4]

PermutationChoose2 = [14,17,11,24,1,5,3,28,
                      15,6,21,10,23,19,12,4,
                      26,8,16,7,27,20,13,2,
                      41,52,31,37,47,55,30,40,
                      51,45,33,48,44,49,39,56,
                      34,53,46,42,50,36,29,32]

BitsRotated = "1122222212222221"

def change(str):
    result = ""
    for i in range(0,8):
        k = ord(str[i])
        str1 = bin(k)
        j = len(str1)
        str2 = str1[2:j]
        result = result + str2.zfill(7) + "0"
    return(result)

def doPermutation(text,Permutation,num):
    result = ""
    for i in range(0,num):
        result = result + text[Permutation[i]-1]
    return(result)

def moveTheKey(key,rotate,times):
    result = ""
    i = int(rotate[times-1])
    for j in range(0,28):
        result = result + key[(j+i)%28]
    for j in range(0,28):
        result = result + key[(j+i)%28+28]
    return(result)

def SboxPermutation(sbox,text):
    row = int(text[0])*2 + int(text[5])
    col = int(text[1])*8 + int(text[2])*4 + int(text[3])*2 + int(text[4])
    num = sbox[row*16+col]
    result1 = bin(num)
    i = len(result1)
    result2 = result1[2:i]
    result = result2.zfill(4)
    return(result)

def doSboxPermutation(text):
    result1 = SboxPermutation(sbox1,text[0:6])
    result2 = SboxPermutation(sbox2,text[6:12])
    result3 = SboxPermutation(sbox3,text[12:18])
    result4 = SboxPermutation(sbox4,text[18:24])
    result5 = SboxPermutation(sbox5,text[24:30])
    result6 = SboxPermutation(sbox6,text[30:36])
    result7 = SboxPermutation(sbox7,text[36:42])
    result8 = SboxPermutation(sbox8,text[42:48])
    result = result1 + result2 + result3 + result4 + result5 + result6 + result7 + result8
    return(result)

def doExclusiveOr(a,b,num):
    result = ""
    for i in range(0,num):
        a1 = int(a[i])
        b1 = int(b[i])
        r1 = a1 ^ b1
        result =result + str(r1)
    return(result)

def doCreateKey(key,times):
    Keys = []
    for i in range(0,times):
        key = moveTheKey(key,BitsRotated,i+1)
        key_PC2 = doPermutation(key,PermutationChoose2,48)
        Keys.append(key_PC2)
    return(Keys)
    
def doWheel(text,key):
    text_l = text[0:32]
    text_r = text[32:64]
    result_text_l = text_r
    textAfterExpansion = doPermutation(text_r,ExpansionPermutation,48)
    textAfterExclusiveOr = doExclusiveOr(textAfterExpansion,key,48)
    textAfterSboxPermutation = doSboxPermutation(textAfterExclusiveOr)
    textAfterPermutation = doPermutation(textAfterSboxPermutation,Permutation,32)
    result_text_r = doExclusiveOr(text_l,textAfterPermutation,32)
    result = result_text_l + result_text_r
    return(result)

def doEncrypt(text,key,times):
    result = ""
    Keys = doCreateKey(key,times)
    for i in range(0,times):
        text = doWheel(text,Keys[i])
    text_l = text[0:32]
    text_r = text[32:64]
    result = text_r + text_l
    return(result)

def doDecrypt(text,key,times):
    result = ""
    Keys = doCreateKey(key,times)
    for i in range(0,times):
        text = doWheel(text,Keys[times-i-1])
    text_l = text[0:32]
    text_r = text[32:64]
    result = text_r + text_l
    return(result)

OriginalText_1 = input("Input the text:")
while(len(OriginalText_1)%8 != 0):
    OriginalText_1 = OriginalText_1 + "0"

OriginalKey = input("Input the key:")
ChangedKey = change(OriginalKey)
Key_PC1 = doPermutation(ChangedKey,PermutationChoose1,56)

Num = input("Input how many time you want to encrypt the text:")
Times = int(Num)

Cipher = ""
CipherReal = ""

for i in range (0,int(len(OriginalText_1)/8)):
    l = int(8 * i)
    r = int(8 * i + 8)
    OriginalText = OriginalText_1[l:r]
    ChangedText = change(OriginalText)
    Text_IP = doPermutation(ChangedText,InitialPermutation,64)
    result = doEncrypt(Text_IP,Key_PC1,Times)
    CipherText = doPermutation(result,InitialPermutation_1,64)
    Cipher = Cipher + CipherText

print("The Cipher is:",Cipher)
