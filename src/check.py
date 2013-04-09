import os
import binascii
from os.path import join, getsize

class main(object):
    
    def check(self, parent, filename1, filename2):
        
        f1 = open(filename1, 'rb')
        parent.report.insertPlainText('Read ' + filename1 + ' successfully.\n')
        f1.seek(0)
        f2 = open(filename2, 'rb')
        parent.report.insertPlainText('Read ' + filename2 + ' successfully.\n')
        f2.seek(0)

        length = getsize(filename1)
        parent.report.insertPlainText('Checking...\n')

        if getsize(filename1) != getsize(filename2):
            parent.pbar.setValue(100)
            parent.report.insertPlainText('Check has been done.\n')
            return False
        else:
            flag = True
            for i in range (0, length):
                parent.pbar.setValue((i + 1) * 100 / length)
                l1 = f1.read(1)
                l2 = f2.read(1)
                if l1 != l2:
                    flag = False
                    break
            parent.report.insertPlainText('Check has been done.\n')
            parent.pbar.setValue(100)
            if flag == True:
                return True
            else:
                return False
