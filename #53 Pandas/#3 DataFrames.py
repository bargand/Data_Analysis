import pandas as pd

data={
    "Car": ["BMW", "Mer", "Hero"],
    "Price": [90, 80, 10]
}

'''
My_Ver = pd.DataFrame(data)
print(My_Ver)
'''
My_Ver = pd.DataFrame(data, index=["x", "y", "z"])

print(My_Ver)

print(My_Ver.loc["x"]) # to locate a specific indexing