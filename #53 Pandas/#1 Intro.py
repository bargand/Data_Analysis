import pandas as pd

print(pd.__version__)


data = {
    "car": ["BMW", "Mer", "Toy"],
    "Index": [1,2,3]
}

print(pd.DataFrame(data))