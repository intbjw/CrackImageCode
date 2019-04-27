# import tesserocr
# from PIL import Image
#
# image = Image.open('code2.jpg')
# result = tesserocr.image_to_text(image)
# print(result)
import requests

url = 'http://111.198.29.45:45464/login.php'

username = 'c3tlwDmIn23'
password = '1qazWSXED56yhn8ujm9olk81wdfTG'

payloads = { 'username':username, 'password':password }

r = requests.post(url, data = payloads)
print (r.text[-29:])
