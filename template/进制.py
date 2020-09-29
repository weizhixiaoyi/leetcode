# -*- coding:utf-8 -*-

# 十进制
# 二进制转十进制
print(int('1001', 2))
# 十六进制转十进制
print(int('0xf', 16))
# 八进制转十进制
print(int('12', 8), end='\n\n')

# 二进制: 先转到十进制, 再通过bin转成二进制
# 十进制转二进制
print(bin(15))
# 十六进制转二进制
print(bin(int('0xf', 16)), end='\n\n')

# 十六进制: 先转到十进制, 再通过hex转成十六进制
# 十进制转16进制
print(hex(15))
# 二进制转16进制
print(hex(int('1001', 2)), end='\n\n')

# 八进制: 先赚到十进制, 再通过oct转到八进制
# 十进制转八进制
print(oct(15))
# 二进制转8进制
print(oct(int('1010', 2)))
