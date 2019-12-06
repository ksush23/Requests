import requests
import re

#getting names of domain

link = "http://pastebin.com/raw/hfMThaGb"#input()
text = requests.get(link).text
pattern = r"(?:<a[^>]*href=)(?:\'|\"|)?(?:(?:\w+|\-):\/\/)?((?:\w+(?:\.|\-))+\w+)"
l = []
for i in re.findall(pattern, text):
    if i not in l:
        l.append(i)

l.sort()
for i in l:
    print(i)


#finding whether link can be reached from given by 2 clicks

res1 = requests.get(input())
link = input()
result = False

for l in re.findall(r"<a href=\"(.*)\"", res1.text):
    res2 = requests.get(l)
    if res2.status_code == 200:
        for u in re.findall(r"<a href=\"(.*)\"", res2.text):
            if link == u:
                result = True
                break
        if result:
            break

if result:
    print("Yes")
else:
    print("No")


#getting picture by link

res = requests.get("https://cdn.imgbin.com/13/3/7/imgbin-logo-queen-black-and-white-queen-queen-illustration-4qxZPHVCuPEJAXfCPDMASijmk.jpg")
print(res.status_code)
print(res.headers['Content-Type'])

print(res.content)

with open("queen.png", "wb") as f:
    f.write(res.content)