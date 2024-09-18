import numpy as np
import math

#Problem 1
def get_bits(number):
    """For a NumPy quantity, return bit representation
    
    Inputs:
    ------
    number : NumPy value
        value to convert into list of bits
        
    Returns:
    -------
    bits : list
       list of 0 and 1 values, highest to lowest significance
    """
    bytes = number.tobytes()
    bits = []
    for byte in bytes:
        bits = bits + np.flip(np.unpackbits(np.uint8(byte)), np.uint8(0)).tolist()
    return list(reversed(bits))


for value in [100.98763]:
    bitlist=get_bits(np.float32(value))
    sign = bitlist[0]
    exponent = bitlist[1:9]
    mantissa = bitlist[9:32]
    template = """{value} decimal ->
       sign = {sign} 
       exponent = {exponent} 
       mantissa = {mantissa}"""
    print(template.format(value=value, sign=sign, exponent=exponent, mantissa=mantissa))
    e10 = np.array([ ee * 2**(7-indx) for indx, ee in zip(range(8), bitlist[1:9])], dtype=np.int32).sum() - 127
    print("Exponent of {value}: {exponent} --> {e10}".format(value=value, exponent=bitlist[1:9], e10=e10))
    print("Mantissa of {value}: {mantissa}".format(value=value, mantissa=bitlist[9:]))
    mantis=float(1)
    for bitnum in range(len(mantissa)):
     mantis=mantis + mantissa[bitnum]*np.power(float(2), -bitnum-1)
     print('bitnum '+str(bitnum))
     print('bitlistbitnum '+str(mantissa[bitnum]))
     print('mantis'+str(mantis))
     number=np.float64(64)*np.float64(mantis)
     print('number: ' +str(number))
     diff=number-np.float64(100.98763)
     print("diff: " +str(diff))



#Problem 2

x=np.float32(1)
y=np.float32(.0000001)
z=x+y
print(z)

x2=np.float64(1)
y2=np.float32(.000000000000001)
z2=x2+y2
print(z2)



a=np.float32(100000000000000000000000000000000000000)
b=np.float64(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
c=np.float32(.000000000000000000000000000000000000000000001)
d=np.float64(.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
print(a)
print(b)
print(c)
print(d)
