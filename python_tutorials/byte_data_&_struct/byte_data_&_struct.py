from struct import *        # here * means import all. struct is modeule that deals with the bytes conversion of all
                            #  all data types and its reverse
packed_data = pack('iif', 3, 6 ,9.81 )          # here in pack you have first provide the format of the data that is
                                                # needed to be packed ,as here data is integer ,integer  and float
                                                # so the format is 'iif' , no. of int = no. of i
                                                # no. of float = no. of f
print(packed_data)

print(calcsize('i'))
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# to get the data into human readable form , use unpack
real_data = unpack('iif',packed_data)
print(real_data)

print(unpack('iif',b'\x03\x00\x00\x00\x06\x00\x00\x00\xc3\xf5\x1cA'))