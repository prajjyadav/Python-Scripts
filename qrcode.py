import pyqrcode

w = input("Enter link: ")
url = pyqrcode.create(w)
url.svg("qrcode.svg", scale=10)








'''
Conditions:
	1)pip install [pyqrcode](https://pypi.org/project/PyQRCode/)
'''
