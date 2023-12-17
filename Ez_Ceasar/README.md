# Ez_Ceasar

Đề cho một file python:

```python
import string
import random

alphabet = string.ascii_letters + string.digits + "!{_}?"

flag = 'KCSC{s0m3_r3ad4ble_5tr1ng_like_7his}'
assert all(i in alphabet for i in flag)

key = random.randint(0, 2**256)

ct = ""
for i in flag:
    ct += (alphabet[(alphabet.index(i) + key) % len(alphabet)])

print(f"{ct=}")

# ct='ldtdMdEQ8F7NC8Nd1F88CSF1NF3TNdBB1O'
```

Hàm trên sử dụng phương pháp mã hoá Ceasar. Đây là một dạng mật mã thay thế, trong đó mỗi ký tự trên văn bản thô sẽ được thay bằng một ký tự khác có vị trí cách nó 1 khoảng xác định, vì kí tự đầu tiên của flag là 'K' còn kí tự đầu của cyphertext là 't', nên từ đó ta có thể tìm được Key.

Bảng chữ cái dựa theo đề bài là ```abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!{_}?```, từ đó suy ra Key mã hoá là 42

Từ đây mình suy ra script giải bài:

```python
import string
ct='ldtdMdEQ8F7NC8Nd1F88CSF1NF3TNdBB1O'
flag = ""
alphabet = string.ascii_letters + string.digits + "!{_}?"
Key = 42
pt = ''
for j in ct:
    pt += (alphabet[(alphabet.index(j) - Key) % len(alphabet)])

print(pt)
```

# Flag

```KCSC{C3as4r_1s_Cl4ss1c4l_4nd_C00l}```
