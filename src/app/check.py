import os
import binascii
import DES_IN_CPP
from os.path import join, getsize

class main(object):
    
    def check(self, parent, filename1, filename2):
        
        #Read input file
        f1 = open(unicode(filename1), 'rb')
        #Report text to UI
        parent.report.insertPlainText('Read ' + filename1 + ' successfully.\n')
        f1.seek(0)

        #Read input file
        f2 = open(unicode(filename2), 'rb')
        #Report text to UI
        parent.report.insertPlainText('Read ' + filename2 + ' successfully.\n')
        f2.seek(0)

        #Get the size of f2
        length = getsize(unicode(filename2))
        #Report text to UI
        parent.report.insertPlainText('Checking...\n')

        #Check the length of f1 and f2 is same or not
        if getsize(unicode(filename2)) != getsize(unicode(filename2)):
            parent.pbar.setValue(100)
            parent.report.insertPlainText('Check has been done.\n')
            return False
        else:
            #Check data every 1024*1024-bit string or string that has less characters
            flag = True
            val = 0
            while True:
                #Change the value of qbar
                parent.pbar.setValue(val * 100 / length)
                if length - val >= 1024 * 1024:
                    l1 = f1.read(1024 * 1024)
                    l2 = f2.read(1024 * 1024)
                    val += 1024 * 1024
                    if DES_IN_CPP.Check(l1, l2, 1024 * 1024) == 0:
                        flag = False
                else:
                    l1 = f1.read(length - val)
                    l2 = f2.read(length - val)
                    if DES_IN_CPP.Check(l1, l2, length - val) == 0:
                        flag = False
                    break
            
            #Report text to UI
            parent.report.insertPlainText('Check has been done.\n')
            #Change the value of qbar
            parent.pbar.setValue(100)
    
            #Return the value that respresent two files is same or not
            if flag == True:
                return True
            else:
                return False
