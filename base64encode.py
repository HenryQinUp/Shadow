import base64
with open("jiedian.txt") as f:
    data = f.read() #需要加密的内容
code = base64.b64encode(data)
with open("jiedian.txt", "w") as out_file:
    out_file.write(code)
