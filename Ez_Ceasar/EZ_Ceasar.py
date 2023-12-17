import string
ct='ldtdMdEQ8F7NC8Nd1F88CSF1NF3TNdBB1O'
flag = ""
alphabet = string.ascii_letters + string.digits + "!{_}?"
Key = 42
pt = ''
for j in ct:
    pt += (alphabet[(alphabet.index(j) - Key) % len(alphabet)])

print(pt)
    
flag = "KCSC{C3as4r_1s_Cl4ss1c4l_4nd_C00l}"