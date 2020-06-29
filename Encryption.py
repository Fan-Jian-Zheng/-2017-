#coding=utf-8

from Crypto.Cipher import AES
import base64

class ENCRYTION(object):

    def __init__(self, s_content="jiamineirong", s_keyword=b"vip"):

        self.s_content = s_content
        self.s_keyword = s_keyword

    def Encode(self):
        #进行加密算法，模式ECB模式，把叠加完16位的秘钥传进来
        aes = AES.new(pad_key(self.s_keyword), AES.MODE_ECB)
        #加密内容,此处需要将字符串转为字节
        text = self.s_content
        #进行内容拼接16位字符后传入加密类中，结果为字节类型
        encrypted_text = aes.encrypt(pad(text))
        encrypted_text = base64.b64encode(encrypted_text)
        return encrypted_text

    def Decode(self):
        self.s_content = base64.b64decode(self.s_content)
        try:
            aes = AES.new(pad_key(self.s_keyword), AES.MODE_ECB)
            #此处是为了验证是否能将字节转为字符串后，进行解密成功
            text = self.s_content
            #用aes对象进行解密，将字节类型转为str类型，错误编码忽略不计
            de = str(aes.decrypt(text),encoding='utf-8',errors="ignore")
            #获取str从0开始到文本内容的字符串长度。
            try:
                # print(de.rstrip())
                return de.rstrip()
            except Exception as e:
                return "password is wrong"            
        except Exception as e:
            print(e)
            return "password is wrong"

        
def pad(text):
    #加密内容需要长达16位字符，所以进行空格拼接
    while len(text) % 16 != 0:
        text += b' '
    return text

def pad_key(key):
    #加密秘钥需要长达16位字符，所以进行空格拼接
    while len(key) % 16 != 0:
        key += b' '
    return key


def AutoTest():
    # 'auto-test for ... library'
    # ----待加密内容：--------------
    wati_encode = "Fan_Xu_Yang"
    key_word    = "vip2379"
    wati_encode = wati_encode.encode()
    key_word    = key_word.encode()
    # ----加密：--------------
    ps = ENCRYTION(wati_encode, key_word)
    content = ps.Encode()
    # ------使用base64编码方式进行编码：-------
    # content = base64.b64encode(content)

    # ----------加密内容存储到txt文档-------
    with open("record.txt","w") as f:
        f.write(content.decode())
    # ----------解析txt文档中的内容：-------
    with open("record.txt","r+") as f:
        record_content = f.read()

    # ------使用base64编码方式进行解码：---
    # record_content = base64.b64decode(record_content)
    # ----解密：--------------
    key_word = "vip2379"
    key_word = key_word.encode()
    ps2 = ENCRYTION(record_content, key_word)
    content2 = ps2.Decode()


    print("decode content :")
    print(content2)    

'auto-test scripts'
if __name__ == '__main__':
    try:
        AutoTest()
    except KeyboardInterrupt:
        print('\n\n(Exit)')
    except:
        import traceback
        print('\n\n', traceback.format_exc())
