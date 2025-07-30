import pandas as pd

data={
    "Car": ["BMW", "Mer", "Hero"],
    "Price": [90, 80, 10]
}

'''
My_Ver = pd.DataFrame(data)
print(My_Ver)
'''

'''
if we declare the index name then we do this
'''
My_Ver = pd.DataFrame(data, index=["x", "y", "z"])

print(My_Ver)

print(My_Ver.loc["x"]) # to locate a specific indexing with index name



'''
if we not declare the index name then we can do this
'''
My_Ver = pd.DataFrame(data)
print(My_Ver.loc[[0]])



