# my-fake-useragent
generate your random fake useragent.


## TODO
version_ranget filter


## description:
create your fake useragent

## install

    python setup.py install

or

    pip install my_fake_useragent


## usage

```python

from my_fake_useragent import UserAgent

ua = UserAgent(family='chrome')

res = ua.random()

```

### family参数可用：
可以设置列表还匹配多种情况

- chrome
- firefox
- edge
- ie
- opera
- safari

### os_family参数可用：
可以设置列表还匹配多种情况
- android
- windows
- linux
- mac
- ios
- chrome os

### phone参数可用：
- None 不过滤
- True 要求是移动端

- False 要求不是移动端

移动端的判据如下：
如果device family检测到：

```python
[
    'BlackBerry',
    'BlackBerry 9700',
    'BlackBerry 9800',
    'Generic Feature Phone',
    'Generic Smartphone',
    'Generic Tablet',
    'HTC Desire',
    'HTC DesireHD A9191',
    'HTC DesireS S510e',
    'HTC DesireZ A7272',
    'HTC HD2_T8585',
    'HTC IncredibleS S710e',
    'HTC Legend',
    'HTC P715a',
    'HTC Pyramid',
    'HTC Sensation',
    'HTC Vision',
    'LG-L160L',
    'LG-LU3000',
    'LG-P505R',
    'Nintendo Wii',
    'Nokia 2730c-1',
    'SprintPPC-6700',
    'SprintPPC-6700)',
    'SprintPPC-i830',
    'SprintSCH-i320',
    'SprintSCH-i830',
    'SprintSPH-ip320',
    'SprintSPH-ip830w',
    'T-Mobile myTouch 3G Slide',
    'iPad',
    'iPhone',
    'iPod']
```

则认为是移动端，同时还补充 认为 android操作系统和ios操作系统也是移动端。


一个符合过滤例子如下：

要求 linux操作系统的的chrome 浏览器:

```python
from my_fake_useragent import UserAgent
ua = UserAgent(family='chrome', os_family='linux')
```

## CHANGELOG
### 0.1.1
this module does not need any third module at all.

### 0.1.0
init


