# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 07:53:34 2021

@author: harishs
"""
import threading
import xml.etree.ElementTree as ET

def baseelement():
    tree = ET.parse('C:\\Users\\harishs\\.spyder-py3\\practice\\Simple-XML-file-for-student-details.xml')
    root = tree.getroot()
    print('\nParsed XML doc {0}\nThe Root: {1}'.format(tree, root.tag))
    
    x = []
    
    for vchild in root.findall('student'):
        vbranch = vchild.find('branch').text
        x.append(vbranch)

    print(x)
    return x

def towrite():
    root = ET.Element('branch')
    tree = ET.ElementTree(root)

    y = baseelement()

    print(y)
    
    file = open('branch.txt','w')

    for i in y:
        print(i)
        vnewelement = ET.Element('subject')
        vnewsubelement = ET.SubElement(vnewelement,'dept')
        vnewsubelement.text = i
        print(i)
        root.append(vnewelement)
        tree.write('branch.xnl')
        
        str = 'subject'+'|'+i+'|'+'dept'
        print(str)
        file.write(str)
        
        print('updated sucessfully')
        
        
        
towrite()


#def main():
# #     print('main thread starts...')
# #     vthread1 = threading.Thread(target = showsquare, args = (10,))
# #     vthread2 = threading.Thread(target = showcube, args = (10,))
# #     print('Child thread starts...')
# #     vthread1.start()
# #     vthread2.start()
# #     print('Main thread is waiting for child threads!\n')
# #     vthread1.join()
# #     vthread2.join()
# #     print('\nMain thread ends..')
    
# # main()
    

