import base64
from Cryptodome.Cipher import AES

with open("jiedian.txt") as f:
    data = f.read() #需要加密的内容
data1 = data.decode('utf8')
code = base64.b64encode(data1)
data2 = code.encode('utf8')
with open("jiedian.txt", "w") as out_file:
    out_file.write(code)
