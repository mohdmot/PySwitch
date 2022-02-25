# PySwitch
### Sample Tool To Make Switch in Python
#### By : [@zaky](https://instagram.com/zaky1_mohammed)
# Import -
#### This is Not a Pip Library , You Have To Use one of This Methods :
### Method 1:
Import it Within Read The Code From Github Raw :
```py
import requests
exec(requests.get('https://raw.githubusercontent.com/Zaky202/PySwitch/main/PySwitch.py').text)
```
#
### Method 2:
Download [PySwitch.py](https://github.com/Zaky202/PySwitch/blob/main/PySwitch.py) in Current Path of Your Script And Import it :
```py
from PySwitch import *
```
# Usage -
```py
data='instagram'
switch(data,{
    case('twitter'):lambda:print('This is Twitter'),
    case('whatsapp'):lambda:print('This is Whatsapp'),
    case('instagram'):lambda:print('This is Instagram'),
    default():lambda:print('Somthing Else')
})
```
### You Can Use Functions Too !!
```py
def Func () :
  print('This is Twitter')

case('twitter') : Func
```
