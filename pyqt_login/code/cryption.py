from pyDes import *

#mode 加解密模式
#modus ecb or cbc模式
#input 原始数据，可以说密文也可以是明文
#key 密钥
#iv 初始向量
def des_algorithm(mode, modus, input, key, iv):
    if len(key) == 8: #single_des
        if modus == 'ecb': #ecb
            MYDES = des(key, CBC, b'\0\0\0\0\0\0\0\0', pad=None, padmode=PAD_NORMAL)
        else:
            MYDES = des(key, CBC, iv, pad=None, padmode=PAD_NORMAL)
    elif len(key) == 16 or len(key) == 24: #triple_des
        if modus == 'ecb':  # ecb
            MYDES = triple_des(key, CBC, b'\0\0\0\0\0\0\0\0', pad=None, padmode=PAD_NORMAL)
        else:
            MYDES = triple_des(key, CBC, iv, pad=None, padmode=PAD_NORMAL)


    if mode == 'encrypt':  # 加密模式
        data = input
        data = data.encode(encoding='utf-8')
        cipher = MYDES.encrypt(data)
        return cipher
    else:
        data = input
        mystr = MYDES.decrypt(data)
        mystr = mystr.decode(encoding = 'utf-8')#gb2312
        return mystr

#数据异或校验
def XOR(data, datalen):
    sum = 0
    for i in range(datalen):
        sum ^= data[i]
    return sum



#测试用
'''
data = '12345678'
cipher = b'\x5B\x91\x18\xB4\x1D\xF8\xC8\x87'
key = b'\x31\x31\x31\x31\x31\x31\x31\x31\x32\x32\x32\x32\x32\x32\x32\x32'
test = des_algorithm('encrypt', 'ecb', data, key, 'null')
test1 = des_algorithm('decrypt', 'ecb', cipher, key, 'null')
print(test)
print(test1)

datalen = 8
data = b'\x01\x02\x03\x04\x05\x06\x07\x08'
lrc = XOR(data, datalen)
print(lrc)
'''