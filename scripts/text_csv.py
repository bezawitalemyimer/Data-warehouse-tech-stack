import pandas as pd

read_file = pd.read_csv (r'/Users/bez/Desktop/Data/I80_davis.txt')
read_file.to_csv (r'/Users/bez/Desktop/Data/I80_davis.csv', index=None)