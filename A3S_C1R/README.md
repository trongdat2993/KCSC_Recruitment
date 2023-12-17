# A3S_C1R

Đề cho một file python với nội dung như dưới

```python
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random

flag = b'KCSC{s0m3_r3ad4ble_5tr1ng_like_7his}'
nonce = Random.get_random_bytes(8)
countf = Counter.new(64, nonce)
key = Random.get_random_bytes(32)

encrypto = AES.new(key, AES.MODE_CTR, counter=countf)
encrypted = encrypto.encrypt(b"TODO:\n - ADD HARDER CHALLENGE IN CRYPTO\n - ADD FLAG TO THE CHALLENGE\n")

encrypto = AES.new(key, AES.MODE_CTR, counter=countf)
encrypted2 = encrypto.encrypt(flag)

print(f"encrypted: {encrypted.hex()}")
print(f"encrypted2: {encrypted2.hex()}")

# encrypted: 5e07dfa19e2b256c205df16b349c0863a15839d056ada1fb425449f2f9af9563eccca6d15cb01aabbe338c851f7b163982127033787fff49e74e3e09f0aee048a1d5b29f5a
# encrypted2: 410bc8addf6036125f5fe17d4bb61c00ba565a9e71d1bf846f625eeac5bfa972f9e7c4fd60800ac9aa689f9b280f5a09fd3768674401ac60
```

Hàm trên sử dụng phương pháp mã hoá AES, ta thấy tác giả sử dụng AES.MODE_CRT,  AES.MODE_CTR là 1 chế độ hoạt động của AES. Trong chế độ này, 1 tập các khối ngõ vào được gọi là counter được sử dụng để sinh ra 1 tập các giá trị ngõ thông qua 1 thuật toán mã hóa. Sau đó giá trị ngõ ra sẽ XOR với plaintext để được ciphertext và ngược lại xor vs ciphertext đẻ được plaintext. Ta thấy đầu bài đã cho biến encrypted để mã hóa chuỗi 'b"TODO:\n - ADD HARDER CHALLENGE IN CRYPTO\n - ADD FLAG TO THE CHALLENGE\n"' và được bản mã: "5e07dfa19e2b256c205df16b349c0863a15839d056ada1fb425449f2f9af9563eccca6d15cb01aabbe338c851f7b163982127033787fff49e74e3e09f0aee048a1d5b29f5a" nên từ đây ta có thể xor 2 giá trị trên với nhau để tìm được giá trị ngõ. Sau đó sử dụng giá trị ngõ xor với biến encrypted2 để tìm được 

Từ đây mình suy ra script giải bài:

```python
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
from pwn import xor

nonce = Random.get_random_bytes(8)
countf = Counter.new(64, nonce)
key = Random.get_random_bytes(32)

encrypto = AES.new(key, AES.MODE_CTR, counter=countf)
encrypt = '5e07dfa19e2b256c205df16b349c0863a15839d056ada1fb425449f2f9af9563eccca6d15cb01aabbe338c851f7b163982127033787fff49e74e3e09f0aee048a1d5b29f5a'
encrypt_flag = '410bc8addf6036125f5fe17d4bb61c00ba565a9e71d1bf846f625eeac5bfa972f9e7c4fd60800ac9aa689f9b280f5a09fd3768674401ac60'

test = b"TODO:\n - ADD HARDER CHALLENGE IN CRYPTO\n - ADD FLAG TO THE CHALLENGE\n"
encrypt = bytes.fromhex(encrypt)
encrypt_flag = bytes.fromhex(encrypt_flag)
xor1 = xor(test, encrypt)
print(xor(xor1,encrypt_flag))

flag = 'KCSC{A3S_CTR_bU1_K1nd4_3asY_y0u_5h0uld_h4v3_s0lv3d_th1s}'
```

# Flag

```KCSC{A3S_CTR_bU1_K1nd4_3asY_y0u_5h0uld_h4v3_s0lv3d_th1s}```

