import os
import binascii
import struct
import DES_IN_CPP
from os.path import join, getsize

class DES(object):
    
    def __init__(self):
        pass

    def input_uncode(self, parent, filename1, filename2):

        #Read input file
        f1 = open(unicode(filename1), 'rb')
        #Report text to UI
        parent.report.insertPlainText('Read ' + filename1 + ' successfully.\n')
        f1.seek(0)

        #Create output file
        f2 = open(unicode(filename2), 'wb')
        #Report text to UI
        parent.report.insertPlainText('Create ' + filename2 + ' successfully.\n')

        #Get the length of output file
        strlength = f1.read(8)
        length, = struct.unpack('Q', strlength)
        val = length
        #Report text to UI
        parent.report.insertPlainText('Unencrypt...\n')

        #Unencrypt data every 1024*1024-bit string or string that has less characters and can be divided exactly by eight 
        while True:
            #Change the value of qbar
            parent.pbar.setValue(100 - length * 100 / val)
            if length >= 1024 * 1024:
                data_string = f1.read(1024 * 1024)
                length -= 1024 * 1024
                temp = DES_IN_CPP.Unencrypt(data_string)
                f2.write(temp)
            else:
                getnum = ((int)(length / 8) + 1) * 8
                data_string = f1.read(getnum)
                temp = DES_IN_CPP.Unencrypt(data_string)
                f2.write(temp[:length])
                length = 0
                break
                
        #Report text to UI
        parent.report.insertPlainText('Unencrypt has been done.\n')
        #Change the value of qbar
        parent.pbar.setValue(100)
    
    def input_encode(self, parent, filename1, filename2):
        val = 0
        #Read input file
        f1 = open(unicode(filename1), 'rb')
        parent.report.insertPlainText('Read ' + filename1 + ' successfully.\n')
        f1.seek(0)
    
        #Create output file
        f2 = open(unicode(filename2), 'wb')
        parent.report.insertPlainText('Create ' + filename2 + ' successfully.\n')
        
        #Get the length of input file
        length = getsize(unicode(filename1))
        f2.write(struct.pack('Q', length))
        #Report text to UI
        parent.report.insertPlainText('Encrypt...\n')
        
        #Encrypt data every 1024*1024-bit string or string that has less characters and can be divided exactly by eight 
        while True:
            #Change the value of qbar
            parent.pbar.setValue(100 * val / length)
            if length - val >= 1024 * 1024:
                readlen = 1024 * 1024
                data_string = f1.read(readlen)
                val += 1024 * 1024
                temp = DES_IN_CPP.Encrypt(data_string)
                f2.write(temp)
            else:
                readlen = ((int)((length - val) / 8) + 1) * 8
                data_string = f1.read(length - val)
                #Make the length of string that can be divided exactly by eight
                for i in range(length - val, readlen):
                    data_string += '0'
                temp = DES_IN_CPP.Encrypt(data_string)
                val += readlen
                f2.write(temp)
                break
                    
        #Report text to UI
        parent.report.insertPlainText('Encrypt has been done.\n')
        #Change the value of qbar
        parent.pbar.setValue(100)
