import pandas as pd
df = pd.read_csv('cars.csv')
x = df[:5]
y = df[-5:]
print(x,y)
