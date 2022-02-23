# PySwitch
### Sample Tool To Make Switch in Python
#### By : [@zaky](https://instagram.com/zaky1_mohammed)
# Import -
### This is Not a Pip Library , You Have To Import it Within Read The Code From Github Raw :
```
import requests
exec(requests.get('https://raw.githubusercontent.com/Zaky202/PySwitch/main/PySwitch.py').text)
```
# Usage -
```
data='instagram'
switch(data,{
    case('twitter'):lambda:print('This is Twitter'),
    case('whatsapp'):lambda:print('This is Whatsapp'),
    case('instagram'):lambda:print('This is Instagram'),
    default():lambda:print('Somthing Else')
})
```
### You Can Use Functions Too !!
```
def Func () :
  print('This is Twitter')

case('twitter') : Func
```
