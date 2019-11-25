import pandas as pd
df = pd.read_csv('cars.csv')

a = df.iloc[:5, [1,3,5,7,9,11]]
print(a,'\n')
b = df[df['Model'] == 'Mazda RX4']
print(b,'\n')
c = df.loc[[23], ['Model','cyl']]
print(c,'\n')
d = df.loc[[1, 28, 18], ['Model','cyl','gear']]
print(d)
