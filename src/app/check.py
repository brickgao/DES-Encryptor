import os
import binascii
import DES_IN_CPP
from os.path import join, getsize

class main(object):
    
    def check(self, parent, filename1, filename2):
        
        f1 = open(unicode(filename1), 'rb')
        parent.report.insertPlainText('Read ' + filename1 + ' successfully.\n')
        f1.seek(0)
        f2 = open(unicode(filename2), 'rb')
        parent.report.insertPlainText('Read ' + filename2 + ' successfully.\n')
        f2.seek(0)

        length = getsize(unicode(filename2))
        parent.report.insertPlainText('Checking...\n')

        if getsize(unicode(filename2)) != getsize(unicode(filename2)):
            parent.pbar.setValue(100)
            parent.report.insertPlainText('Check has been done.\n')
            return False
        else:
            flag = True
            val = 0
            while True:
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
            parent.report.insertPlainText('Check has been done.\n')
            parent.pbar.setValue(100)
            if flag == True:
                return True
            else:
                return False
