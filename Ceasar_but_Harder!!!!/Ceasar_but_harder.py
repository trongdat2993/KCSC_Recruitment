import string
import random

ct='2V9VnRcNosvgMo4RoVfThg8osNjo0G}mmqmp'
alphabet = string.ascii_letters + string.digits + "!{_}?"
lsAlphabet = []
    
#Tìm các tập các alphabet    
for i in range(0, 67):
    for j in range(0, 67):
        for k in range(0, 67):
            alphabet = alphabet[:i] + alphabet[i+1:]
            alphabet = alphabet[:j] + alphabet[j+1:]
            alphabet = alphabet[:k] + alphabet[k+1:]
            lsAlphabet.append(alphabet)
            alphabet = string.ascii_letters + string.digits + "!{_}?"
        alphabet = string.ascii_letters + string.digits + "!{_}?"
    alphabet = string.ascii_letters + string.digits + "!{_}?"

ls = []
for i in lsAlphabet:
    for j in range(0, 67):
        pt = ''
        for k in ct:
            if  k not in i:
                break   
            pt += (i[(i.index(k) - j) % len(i)])
        if 'KCSC{y0u_be4t_My_C3A5' in pt and len(pt) == len(ct):
            ls.append(pt)

flag = set(ls)
print(flag)

flag = [{'KCSC{y0u_be4t_My_C3A54R_bu7_InW!!?!}', 'KCSC{y0u_be4t_My_C3A54R_bu7_IoW!!?!}', 'KCSC{y0u_be4t_My_C3A54R_bu7_HoW!!?!}'}]