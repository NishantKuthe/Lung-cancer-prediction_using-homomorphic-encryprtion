# from msilib.schema import File
from PIL import Image
import numpy as np

import ImageCryptography as IC
import Paillier as Pa

publicKey, privateKey = Pa.generate_keys()
print(publicKey.__repr__())

im = Image.open(r"C:\Users\saura\Desktop\Homomorphic\Homomorphic-Image_Encryption-main\test-images\lena512gray.bmp")
# im.show()

encrypt_image = IC.ImgEncrypt(publicKey,im)
inc_bright = IC.homomorphicBrightness(publicKey,encrypt_image,30)
im = IC.ImgDecrypt(publicKey,privateKey,inc_bright)
im.save("encrypted-images/test4.png")
im.show()
ij = IC.saveEncryptedImg(inc_bright,"test4.png")