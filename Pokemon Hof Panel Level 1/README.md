# Pokemon Hof Panel Level 1

Mở ```http://103.162.14.116:10003/``` và nhập ký tự ```abc```  sau đó web hiện lên:

![](https://github.com/trongdat2993/KCSC_Recruitment/blob/main/Pokemon%20Hof%20Panel%20Level%201/Image/1.png)

Ta mở source code ```champ.php``` ra thì thấy code:

![](https://github.com/trongdat2993/KCSC_Recruitment/blob/main/Pokemon%20Hof%20Panel%20Level%201/Image/2.png)

Dễ thấy code sử dụng Cookie Value để check flag. Để lấy được flag thì giá trị ```isChampion($user)``` phải bằng true.
Mở Inspect để lấy giá trị Cookie và decrypt base64: 

![](https://github.com/trongdat2993/KCSC_Recruitment/blob/main/Pokemon%20Hof%20Panel%20Level%201/Image/3.png)

Sửa đoạn ```b:0``` thành ```b:1``` ,encrypt giá trị Cookie vừa sửa sau đó gán lại giá trị vào Cookie Value thì ta lấy được flag:

![](https://github.com/trongdat2993/KCSC_Recruitment/blob/main/Pokemon%20Hof%20Panel%20Level%201/Image/4.png)

# Flag

```KCSC{n0w_y0u_kn0w_s3r1al1z3_f0m4rt}```

