import base64
from Cryptodome.Cipher import AES

with open("jiedian0.txt") as f:
    data = f.read() #需要加密的内容
# 密钥（key）, 密斯偏移量（iv） CBC模式加密


def AES_Decrypt(key, data):
  vi = '0000000000000000'
  data = data.encode('utf8')
  encodebytes = base64.decodebytes(data)
  # 将加密数据转换位bytes类型数据
  cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
  text_decrypted = cipher.decrypt(encodebytes)
  unpad = lambda s: s[0:-s[-1]]
  text_decrypted = unpad(text_decrypted)
  # 去补位
  text_decrypted = text_decrypted.decode('utf8')
  return text_decrypted


key = '8YfiQ8wrkziZ5YFa' #自己密钥

text_decrypted = AES_Decrypt(key, data)
with open("jiedian", "w") as out_file:
    out_file.write(text_decrypted)
