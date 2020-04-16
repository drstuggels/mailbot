# noahmail
#### introduction
The most simple way to describe this: Python Email Confirmation Link Scraper
So the idea is to use this if you want to register an account with a bot and you need to confirm an email without any UI. This is very simple and should maybe only be used if you're a beginner or you just want something simple. There is only one function. Anyway here's how to use it:
#### Prerequisites
The only package you need to install is [urlextract](https://pypi.org/project/urlextract/).
```
pip install urlextract
```
#### Installing
Just download the **noahmail.py** file and put it in your own project folder.
[This is a direct link](https://github.com/drstuggels/noahmail/blob/master/noahmail.py)
#### How to use
Import it:
```python
from noahmail import connectAndGetLinks
```
Use it somewhere
```python
connectAndGetLinks(mailserver, emailuser, emailpassword, refresh interval)
```
It will return an **array** of links found in the newest email. It might take a while (so dont worry), but it's the fastest way to do this™.
##### Example
```python
all_urls = connectAndGetLinks('example.mailserver.com','user1@exaple.com','password123', 5)
confirmation_url = all_urls[6]
print("You need to go to",confirmation_url,"to confirm your account!")
```
## Please contribute
Please contribute and help me make this better. It's a not-so-well documented subject and it took me a while to figure it out how to do it. It's guaranteed to have bugs so be carefull.
