# Ez_Ceasar

Đề cho một file python:

```python
import string
import random

flag = "KCSC{s0m3_r3ad4ble_5tr1ng_like_7his}" 

alphabet = string.ascii_letters + string.digits + "!{_}?"
assert all(i in alphabet for i in flag)


for i in range(3):
    k = random.randint(0, len(alphabet))
    alphabet = alphabet[:k] + alphabet[k+1:]

key = random.randint(0, 2**512)

ct = ""
for i in flag:
    ct += (alphabet[(alphabet.index(i) + key) % len(alphabet)])

print(f"{ct=}")

# ct='2V9VnRcNosvgMo4RoVfThg8osNjo0G}mmqmp'
```

Hàm trên sử dụng phương pháp mã hoá Ceasar. Đây là một dạng mật mã thay thế, trong đó mỗi ký tự trên văn bản thô sẽ được thay bằng một ký tự khác có vị trí cách nó 1 khoảng xác định, trong bài này đã có sự thay đổi trong khi đã xóa đi 3 ký tự bất kỳ trong bảng chữ cái  ```abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!{_}?```, nên đầu tiên ta phải tập các alplabet có thể xảy ra sau đó sử dụng vòng lặp để thử các trường hợp và các khóa. Nếu plaintext có "KCSC{" và có độ dài bằng ciphertext thì ta in ra màn hinh. Nhận thấy có nhiều giá trị có 'KCSC{y0u_be4t_My_C3A54R' nên ta lọc tiếp và thêm vào mảng . Cuối cùng ta lọc các giá trị trùng nhau và tìm được flag.

Từ đây mình suy ra script giải bài:

```python
import string
import random

ct='2V9VnRcNosvgMo4RoVfThg8osNjo0G}mmqmp'
alphabet = string.ascii_letters + string.digits + "!{_}?"
lsAlphabet = []
    
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
        if 'KCSC{y0u_be4t_My_C3A54R' in pt and len(pt) == len(ct):
            ls.append(pt)

flag = set(ls)
print(flag)

flag = 'KCSC{y0u_be4t_My_C3A54R_bu7_HoW!!?!}'
```

# Flag

```KCSC{y0u_be4t_My_C3A54R_bu7_HoW!!?!}```
