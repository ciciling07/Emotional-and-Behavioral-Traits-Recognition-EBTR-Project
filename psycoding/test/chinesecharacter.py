# encoding:utf-8

"""
test for chinese character encoding problem.
"""
with open('tmpdata.txt','rb') as f:
    line = f.readline()
    print(line)
    with open('tmptmpdata.txt','wb') as f1:
        f1.write(line.decode('unicode_escape').encode('utf8'))