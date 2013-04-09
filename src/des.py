import os
import binascii
import struct
from os.path import join, getsize

class DES(object):
    
    __ip = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7,
    ]
    
    __ip1 = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,  
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,  
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25,
    ]

    __p = [  
        16, 7, 20, 21,
        29, 12, 28, 17,  
        1, 15, 23, 26,
        5, 18, 31, 10,  
        2, 8, 24, 14,
        32, 27, 3, 9,  
        19, 13, 30, 6,
        22, 11, 4, 25,  
    ]  

    __e = [  
        32, 1, 2, 3, 4, 5,  
        4, 5, 6, 7, 8, 9,  
        8, 9, 10, 11, 12, 13,  
        12, 13, 14, 15, 16, 17,  
        16, 17, 18, 19, 20, 21,  
        20, 21, 22, 23, 24, 25,  
        24, 25, 26, 27, 28, 29,  
        28, 29, 30, 31, 32, 1,  
    ]

    __s = [  
        [  
        'e', '4', 'd', '1', '2', 'f', 'b', '8', '3', 'a', '6', 'c', '5', '9', '0', '7',  
        '0', 'f', '7', '4', 'e', '2', 'd', '1', 'a', '6', 'c', 'b', '9', '5', '3', '8', 
        '4', '1', 'e', '8', 'd', '6', '2', 'b', 'f', 'c', '9', '7', '3', 'a', '5', '0',  
        'f', 'c', '8', '2', '4', '9', '1', '7', '5', 'b', '3', 'e', 'a', '0', '6', 'd', 
        ],  
        [  
        'f', '1', '8', 'e', '6', 'b', '3', '4', '9', '7', '2', 'd', 'c', '0', '5', 'a',  
        '3', 'd', '4', '7', 'f', '2', '8', 'e', 'c', '0', '1', 'a', '6', '9', 'b', '5',  
        '0', 'e', '7', 'b', 'a', '4', 'd', '1', '5', '8', 'c', '6', '9', '3', '2', 'f',  
        'd', '8', 'a', '1', '3', 'f', '4', '2', 'b', '6', '7', 'c', '0', '5', 'e', '9',  
        ],  
        [  
        'a', '0', '9', 'e', '6', '3', 'f', '5', '1', 'd', 'c', '7', 'b', '4', '2', '8',  
        'd', '7', '0', '9', '3', '4', '6', 'a', '2', '8', '5', 'e', 'c', 'b', 'f', '1',  
        'd', '6', '4', '9', '8', 'f', '3', '0', 'b', '1', '2', 'c', '5', 'a', 'e', '7',  
        '1', 'a', 'd', '0', '6', '9', '8', '7', '4', 'f', 'e', '3', 'b', '5', '2', 'c',  
        ],  
        [  
        '7', 'd', 'e', '3', '0', '6', '9', 'a', '1', '2', '8', '5', 'b', 'c', '4', 'f',  
        'd', '8', 'b', '5', '6', 'f', '0', '3', '4', '7', '2', 'c', '1', 'a', 'e', '9',  
        'a', '6', '9', '0', 'c', 'b', '7', 'd', 'f', '1', '3', 'e', '5', '2', '8', '4',  
        '3', 'f', '0', '6', 'a', '1', 'd', '8', '9', '4', '5', 'b', 'c', '7', '2', 'e',  
        ],  
        [  
        '2', 'c', '4', '1', '7', 'a', 'b' ,'6', '8', '5', '3', 'f', 'd', '0', 'e', '9', 
        'e', 'b', '2', 'c', '4', '7', 'd', '1', '5', '0', 'f', 'a', '3', '9', '8', '6',  
        '4', '2', '1', 'b', 'a', 'd', '7', '8', 'f', '9', 'c', '5', '6', '3', '0', 'e',  
        'b', '8', 'c', '7', '1', 'e', '2', 'd', '6', 'f', '0', '9', 'a', '4', '5', '3', 
        ],  
        [  
        'c', '1', 'a', 'f', '9', '2', '6', '8', '0', 'd', '3', '4', 'e', '7', '5', 'b',   
        'a', 'f', '4', '2', '7', 'c', '9', '5', '6', '1', 'd', 'e', '0', 'b', '3', '8',  
        '9', 'e', 'f', '5', '2', '8', 'c', '3', '7', '0', '4', 'a', '1', 'd', 'b', '6',  
        '4', '3', '2', 'c', '9', '5', 'f', 'a', 'b', 'e', '1', '7', '6', '0', '8', 'd',  
        ],  
        [  
        '4', 'b', '2', 'e', 'f', '0', '8', 'd', '3', 'c', '9', '7', '5', 'a', '6', '1',  
        'd', '0', 'b', '7', '4', '9', '1', 'a', 'e', '3', '5', 'c', '2', 'f', '8', '6',  
        '1', '4', 'b', 'd', 'c', '3', '7', 'e', 'a', 'f', '6', '8', '0', '5', '9', '2',  
        '6', 'b', 'd', '8', '1', '4', 'a', '7', '9', '5', '0', 'f', 'e', '2', '3', 'c',  
        ],  
        [  
        'd', '2', '8', '4', '6', 'f', 'b', '1', 'a', '9', '3', 'e', '5', '0', 'c', '7',  
        '1', 'f', 'd', '8', 'a', '3', '7', '4', 'c', '5', '6', 'b', '0', 'e', '9', '2',  
        '7', 'b', '4', '1', '9', 'c', 'e', '2', '0', '6', 'a', 'd', 'f', '3', '5', '8',  
        '2', '1', 'e', '7', '4', 'a', '8', 'd', 'f', 'c', '9', '0', '3', '5', '6', 'b',  
        ],  
    ] 
    
    __k1 = [  
        57, 49, 41, 33, 25, 17, 9,  
        1, 58, 50, 42, 34, 26, 18,  
        10, 2, 59, 51, 43, 35, 27,  
        19, 11, 3, 60, 52, 44, 36,  
        63, 55, 47, 39, 31, 23, 15,  
        7, 62, 54, 46, 38, 30, 22,  
        14, 6, 61, 53, 45, 37, 29,  
        21, 13, 5, 28, 20, 12, 4,  
    ]
    
    __k2 = [  
        14, 17, 11, 24, 1, 5, 3, 28,  
        15, 6, 21, 10, 23, 19, 12, 4,  
        26, 8, 16, 7, 27, 20, 13, 2,  
        41, 52, 31, 37, 47, 55, 30, 40,  
        51, 45, 33, 48, 44, 49, 39, 56,  
        34, 53, 46, 42, 50, 36, 29, 32,  
    ]  
    
    __k = [
        1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1,
    ]
    
    __hex_bin = {  
        '0':'0000', '1':'0001', '2':'0010', '3':'0011',  
        '4':'0100', '5':'0101', '6':'0110', '7':'0111',  
        '8':'1000', '9':'1001', 'a':'1010', 'b':'1011',  
        'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111',  
        ' ':'0000'  
    }

    __hex1_bin = {
        '0000':'0', '0001':'1', '0010':'2', '0011':'3',
        '0100':'4', '0101':'5', '0110':'6', '0111':'7',
        '1000':'8', '1001':'9', '1010':'a', '1011':'b',
        '1100':'c', '1101':'d', '1110':'e', '1111':'f',
    }
    
    
    def __init__(self):
        pass
        
    def uncode(self, data):
        recnewkey = []
        iptmp = bintmp = ''
        l = r = ''
        key ='0011000100110010001100110011010000110101001101100011011100111000'
        hextmp = binascii.b2a_hex(data)
        for i in range(0, 16):
            bintmp += self.__hex_bin[hextmp[i]]
        for i in range(0, 64):
            iptmp += bintmp[self.__ip[i] - 1]
        for i in range(0, 32):
            l += iptmp[i]
            r += iptmp[i + 32]
        tmp1 = tmp2 = ''
        for j in range(0, 28):
            tmp1 += key[self.__k1[j] - 1]
            tmp2 += key[self.__k1[j + 28] - 1]
        for i in range(0, 16):
            newkey = ''
            newtmp1 = newtmp2 = ''
            newtmp1 += tmp1[self.__k[i]:28]
            newtmp1 += tmp1[0:self.__k[i]]
            newtmp2 += tmp2[self.__k[i]:28]
            newtmp2 += tmp2[0:self.__k[i]]
            tmp1 = newtmp1
            tmp2 = newtmp2
            combine = newtmp1 + newtmp2
            for j in range(0, 48):
                newkey += combine[self.__k2[j] - 1]
            recnewkey += [newkey]
        for i in range(0, 16):
            newr = ''
            for j in range(0, 48):
                newr += r[self.__e[j] - 1]
            afterf = ''
            for j in range(0, 8):
                row = 0
                col = ((ord(newr[j * 6]) - 48) ^ (ord(recnewkey[15 - i][j * 6]) - 48)) * 2
                col += ((ord(newr[j * 6 + 5]) - 48) ^ (ord(recnewkey[15 - i][j * 6 + 5])) - 48)
                for m in range(1, 5):
                    row += ((ord(newr[j * 6 + m]) - 48) ^ (ord(recnewkey[15 - i][j * 6 + m]) - 48)) * (2 ** (4 - m))
                afterf += self.__hex_bin[self.__s[j][col * 16 + row]]
            afterp = ''
            for j in range(0, 32):
                afterp += afterf[self.__p[j] - 1]
            tmp = ''
            for j in range(0, 32):
                tmp += chr(((ord(afterp[j]) - 48) ^ (ord(l[j]) - 48)) + 48)
            l = r
            r = tmp
        befip = r + l
        res = ''
        for i in range(0, 64):
            res += befip[self.__ip1[i] - 1]
        return res

    def encode(self, data):
        iptmp = bintmp = ''
        l = r = ''
        key ='0011000100110010001100110011010000110101001101100011011100111000'
        hextmp = binascii.b2a_hex(data)
        for i in range(0, 16):
            bintmp += self.__hex_bin[hextmp[i]]
        for i in range(0, 64):
            iptmp += bintmp[self.__ip[i] - 1]
        for i in range(0, 32):
            l += iptmp[i]
            r += iptmp[i + 32]
        tmp1 = tmp2 = ''
        for j in range(0, 28):
            tmp1 += key[self.__k1[j] - 1]
            tmp2 += key[self.__k1[j + 28] - 1]
        for i in range(0, 16):
            newkey = ''
            newtmp1 = newtmp2 = ''
            newtmp1 += tmp1[self.__k[i]:28]
            newtmp1 += tmp1[0:self.__k[i]]
            newtmp2 += tmp2[self.__k[i]:28]
            newtmp2 += tmp2[0:self.__k[i]]
            tmp1 = newtmp1
            tmp2 = newtmp2
            combine = newtmp1 + newtmp2
            for j in range(0, 48):
                newkey += combine[self.__k2[j] - 1]
            newr = ''
            for j in range(0, 48):
                newr += r[self.__e[j] - 1]
            afterf = ''
            for j in range(0, 8):
                row = col = 0
                col = ((ord(newr[j * 6]) - 48) ^ (ord(newkey[j * 6]) - 48)) * 2
                col += ((ord(newr[j * 6 + 5]) - 48) ^ (ord(newkey[j * 6 + 5])) - 48)
                for m in range(1, 5):
                    row += ((ord(newr[j * 6 + m]) - 48) ^ (ord(newkey[j * 6 + m]) - 48)) * (2 ** (4 - m))
                afterf += self.__hex_bin[self.__s[j][col * 16 + row]]
            afterp = ''
            for j in range(0, 32):
                afterp += afterf[self.__p[j] - 1]
            tmp = ''
            for j in range(0, 32):
                tmp += chr(((ord(afterp[j]) - 48) ^ (ord(l[j]) - 48)) + 48)
            l = r
            r = tmp
        befip = r + l
        res = ''
        for i in range(0, 64):
            res += befip[self.__ip1[i] - 1]
        return res

    def input_uncode(self, parent, filename1, filename2):
        f1 = open(filename1, 'rb')
        parent.report.insertPlainText('Read ' + filename1 + ' successfully.\n')
        f1.seek(0)
        f2 = open(filename2, 'wb')
        parent.report.insertPlainText('Create ' + filename2 + ' successfully.\n')
        strlength = f1.read(8)
        length, = struct.unpack('Q', strlength)
        val = length
        parent.report.insertPlainText('Unencrypt...\n')
        while True:
            parent.pbar.setValue(100 - length * 100 / val)
            data_string = f1.read(8)
            if length >= 8:
                temp = self.uncode(data_string)
                hextemp = ''
                for i in range(0, 16):
                    fourbit = ''
                    for j in range(0, 4):
                        fourbit += temp[i * 4 + j]
                    hextemp += self.__hex1_bin[fourbit]
                writedata = binascii.a2b_hex(hextemp)
                f2.write(writedata)
            else:
                temp = self.uncode(data_string)
                hextemp = ''
                for i in range(0, 16):
                    fourbit = ''
                    for j in range(0, 4):
                        fourbit += temp[i * 4 + j]
                    hextemp += self.__hex1_bin[fourbit]
                writedata = binascii.a2b_hex(hextemp)
                for i in range(0, length):
                    f2.write(writedata[i])
                break
            length -= 8
        parent.report.insertPlainText('Unencrypt has been done.\n')
        parent.pbar.setValue(100)
    
    def input_encode(self, parent, filename1, filename2):
        val = 0
        f1 = open(filename1, 'rb')
        parent.report.insertPlainText('Read ' + filename1 + ' successfully.\n')
        f1.seek(0)
        f2 = open(filename2, 'wb')
        parent.report.insertPlainText('Create ' + filename2 + ' successfully.\n')
        length = getsize(filename1)
        f2.write(struct.pack('Q', length))
        parent.report.insertPlainText('Encrypt...\n')
        while True:
            val += 8
            parent.pbar.setValue(val * 100 / length)
            data_string = f1.read(8)
            if len(data_string) == 8:
                temp = self.encode(data_string)
                hextemp = ''
                for i in range(0, 16):
                    fourbit = ''
                    for j in range(0, 4):
                        fourbit += temp[i * 4 + j]
                    hextemp += self.__hex1_bin[fourbit]
                writedata = binascii.a2b_hex(hextemp)
                f2.write(writedata)
            else:
                while(len(data_string) < 8):
                    data_string += '0'
                temp = self.encode(data_string)
                for i in range(0, 16):
                    fourbit = ''
                    for j in range(0, 4):
                        fourbit += temp[i * 4 + j]
                    hextemp += self.__hex1_bin[fourbit]
                writedata = binascii.a2b_hex(hextemp)
                f2.write(writedata)
                break
        parent.report.insertPlainText('Encrypt has been done.\n')
        parent.pbar.setValue(100)
