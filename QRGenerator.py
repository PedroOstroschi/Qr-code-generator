import pyqrcode

url = pyqrcode.create('https://arquivoarquitetura.com/001/')

url.svg ('Utfpr.svg', scale= 8)