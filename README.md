# VoidHub API Wrapper

VoidHub's API accessible from Python!

## Installation

Install VAW using these Commands:

    pip install git+https://github.com/voidhubapp/vaw

## Quick Start
VAW v1 allows getting Posts and Communities using the `/v/<community>/json` Endpoint.  

Since VAW can be hosted virtually anywhere, on creating the Instance, you must specify the base URL, defaulting to localhost.

```py
from vaw import VoidHub

vh = VoidHub("http://voidhub.xyz")
iama = vh.community("iama")
print(iama.name)
for post in iama.posts:
    print(post.title)
```