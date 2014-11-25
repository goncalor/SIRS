# characters usable in URLs

from pprint import pprint

usable_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&'()*+,;="

l = []

for c in usable_chars:
  l.append(hex(ord(c)))

l.sort()
print l
#pprint(l)