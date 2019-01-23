import random
import urllib.request

def download_img(url):
    num=random.randint(1,1000)
    name=str(num)+".jpg"

    urllib.request.urlretrieve(url,name)

download_img("https://instagram.fnbo2-1.fna.fbcdn.net/vp/4de2e7fde8b4a0b98c2fac71512b96d8/5B813722/t51.2885-19/s150x150/30856093_213656679225134_1137011197690773504_n.jpg")