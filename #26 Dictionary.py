thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

'''
print(type(thisdict))
print(len(thisdict))
print(thisdict["brand"])
print(thisdict["year"])

thisdict.update({"year" : 2000})
print(thisdict)

thisdict.clear()
print(thisdict)

x = thisdict.keys()
y = thisdict.items()
z = thisdict.values()
print(x)
print(y)
print(z)

thisdict["brand"] = "BMW"
print(thisdict)


thisdict["color"] = "red"

#or

thisdict.update({"color": "green"})

print(thisdict)


thisdict.pop("year")

thisdict.popitem()

# del thisdict  # this will through the error because 

thisdict.clear()
print(thisdict)

'''

'''
#loops

for i in thisdict:
    print(i)

for j in thisdict.keys():
    print(j)


for k in thisdict.items():
    print(k)


for l in thisdict.values():
    print(l)


for m, n in thisdict.items():
    print(m,n)

'''

'''
#copy

new_thisdict = thisdict.copy()
print(new_thisdict)

'''
'''
#nested dict

myfamily = {
  "member1" : {
    "name" : "debargha",
    "year" : 2001
  },
  "member2" : {
    "name" : "riya",
    "year" : 1997
  },
  "member3" : {
    "name" : "prabir",
    "year" : 1967
  }
}

print(myfamily)


member1 = {
"name" : "debargha",
"year" : 2001
},
member2 = {
"name" : "riya",
"year" : 1997
},
member3 = {
"name" : "prabir",
"year" : 1967
}

myfamily = {
    "1": member1,
    "2": member2,
    "3": member3,
}

print(myfamily)

'''

myfamily = {
  "member1" : {
    "name" : "debargha",
    "year" : 2001
  },
  "member2" : {
    "name" : "riya",
    "year" : 1997
  },
  "member3" : {
    "name" : "prabir",
    "year" : 1967
  }
}

print(myfamily["member1"]["name"])
print(myfamily["member2"]["year"])

#update
myfamily["member3"].update({"name": "hh"}) 
print(myfamily)
















