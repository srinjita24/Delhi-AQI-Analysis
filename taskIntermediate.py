import pandas as pd

url = "https://drive.google.com/uc?id=1DqkaLn2MDOZwXKoZgqaPdpSWE4sMJOSu&export=download"
df = pd.read_csv(url)

print(df.head())

