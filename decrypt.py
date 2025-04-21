from Crypto.Cipher import AES
import base64

# Texto cifrado (base64)
encrypted = base64.b64decode("BQO5l5Kj9MdErXx6Q6AGOw==")

# Clave
key = "c4scadek3y654321".encode('utf-8')  # 16 bytes

# IV fijo
iv = "1tdyjCbY1Ix49842".encode('utf-8')  # 16 bytes

# Crear el cifrador AES en modo CBC
cipher = AES.new(key, AES.MODE_CBC, iv)

# Descifrar
decrypted = cipher.decrypt(encrypted)

# Quitar el padding PKCS7
pad_len = decrypted[-1]
if 1 <= pad_len <= 16 and all(b == pad_len for b in decrypted[-pad_len:]):
    decrypted = decrypted[:-pad_len]
    print("Contraseña descifrada:", decrypted.decode('utf-8'))
else:
    print("Padding inválido, bytes crudos:", decrypted.hex())
