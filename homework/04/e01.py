#list
mylist = ["moi", "hei", "ciao"]
mylist.append("ok")
print(mylist)
mylist.pop(0)
mylist.remove("hei")
print(mylist)
mylist[1] = "hei hei"
print(mylist)

#tuple
mytuple = ("moi", "hei", "ciao")
try:
    mytuple.append("tuple")
    mytuple.remove("moi")
    mytuple[1] = "heihei"
except:
    print("you cannot add new items to tuple")
print(mytuple)

#set
myset = {"moikka","heippa","terve"}
myset.add("hejsan")
print(myset)
myset.add("moikka")
print("you cannot add duplicate items to a set")
myset.remove("hejsan")
print(myset)

#dictionary
mydict = {
    "key1": "love",
    "key2": "blue sky",
    "key3": "green meadows"
}
mydict["key4"] = "summer cottage"
mydict.pop("key3")
mydict["key4"] = "sunny beach"
print(mydict)