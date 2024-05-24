# key='H9n&S@oGohGpV6d7'.encode('utf-8')
# iv='5150956153345366'.encode('utf-8')


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from common.readYaml import env_config, data_config

key_en = env_config()['key']
iv_en = env_config()['iv']


def aes_encry(plaintext):
    # 密钥需要是 16（AES-128）、24（AES-192）或 32（AES-256）字节长
    key = key_en.encode('utf-8')

    # 初始化向量（IV）需要和块大小相同，对于 AES 来说是 16 字节
    iv = iv_en.encode('utf-8')

    # 创建一个 AES cipher 对象，使用 CBC 模式
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 加密前需要对明文进行填充
    padded_data = pad(plaintext.encode('utf-8'), AES.block_size)

    # 执行加密
    ciphertext = cipher.encrypt(padded_data)

    # 将 IV 和密文连接起来，以便在解密时可以使用 IV
    encrypted_data = iv + ciphertext
    # print(encrypted_data)

    # 打印加密后的数据
    # print("Encrypted Data:", encrypted_data.hex())
    return encrypted_data.hex()


def aes_decry(encrypted_hex_string):
    # 解密过程
    # 将十六进制字符串转换回字节序列
    encrypted_data = bytes.fromhex(encrypted_hex_string)

    # 假设你已经有了密钥和IV，这些应该是加密时使用的相同值
    key = key_en.encode('utf-8')

    # 初始化向量（IV）需要和块大小相同，对于 AES 来说是 16 字节
    iv = iv_en.encode('utf-8')
    ciphertext = encrypted_data[AES.block_size:]  # 实际的密文是IV之后的部分

    # 创建AES cipher对象用于解密
    decipher = AES.new(key, AES.MODE_CBC, iv)

    # 执行解密
    decrypted_data = decipher.decrypt(ciphertext)

    # 如果加密时使用了填充，则需要去除填充
    try:
        decrypted_data = unpad(decrypted_data, AES.block_size)
    except ValueError:
        # print("解密失败：可能是密钥或IV不正确，或者数据已损坏")
        decrypted_data = None

    # 如果原始明文是文本，将字节序列解码为字符串
    if decrypted_data is not None:
        decrypted_text = decrypted_data.decode('utf-8')  # 假设明文是UTF-8编码的文本
        # print("解密后的明文:", decrypted_text)
        return decrypted_text

# aes_encry('@#')
# aes_decry('35313530393536313533333435333636f85b708dbec91bc906f1463ecc510d54')
