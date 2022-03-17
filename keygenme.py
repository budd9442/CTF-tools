#https://play.picoctf.org/practice/challenge/121?page=2

import hashlib
key = [hashlib.sha256(b'GOUGH').hexdigest()[i] for i in [4,5,3,6,2,7,1,8]]
s="picoCTF{1n_7h3_|<3y_of_" + ''.join([((str(k))) for k in key] ) + "}"
print(s)