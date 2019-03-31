#-*- coding:utf-8 -*-

key = ['s','f','o','t','d','o','g','.']

def en_code(passwd:str)->str:
    str_len = len(passwd)
    l=[]
    for i in range(str_len):
        l.append(chr(ord(passwd[i])^ord(key[i&7])))
    if '\r' in ''.join(l) or '\n' in ''.join(l):
        return 'non_compliant_agreement_eof'
    else:
        return ''.join(l)

def de_code(passwd:str)->str:
    str_len = len(passwd) 
    l=[]
    for i in range(str_len):
        l.append(chr(ord(passwd[i])^ord(key[i&7])))
    return ''.join(l)
