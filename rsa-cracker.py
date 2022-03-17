from calendar import c
from factordb.factordb import FactorDB
def crackRSA(c,n,e):
    f= FactorDB(n)
    p,q = f.connect()
    ph = (p-1)*(q-1)
    d = pow(e,-1,ph)  # gmpy2.invert(e, ph)
    plaintext = pow(c,d,n)
    return bytearray.fromhex(format(plaintext, 'x')).decode()


#https://play.picoctf.org/practice/challenge/162 

c=240986837130071017759137533082982207147971245672412893755780400885108149004760496
n=831416828080417866340504968188990032810316193533653516022175784399720141076262857
e=65537

print(crackRSA(c,n,e))