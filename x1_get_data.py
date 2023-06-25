
import pandas as pd

# Download the zipped dataset
train = pd.read_csv("https://raw.githubusercontent.com/jasonchanhku/mlops_tracking/main/data/train.csv")
test = pd.read_csv("https://raw.githubusercontent.com/jasonchanhku/mlops_tracking/main/data/test.csv")


train.to_csv("./train.csv", index=False)
test.to_csv("./test.csv", index=False)

print('\nAll files are being extracted.')
