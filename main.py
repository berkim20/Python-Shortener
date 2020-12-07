import pyshorteners

link = input("Enter your link: ")
shortener = pyshorteners.Shortener()
x = shortener.tinyurl.short(link)
print(x)