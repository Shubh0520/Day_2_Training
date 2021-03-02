import pandas as pd

states = {"MH": {"name": "Maharashtra", "population": "124862220", "rank": "3rd"},
          "UP": {"name": "Uttar Pradesh", "population": "199812341", "rank": "4th"},
          "RJ": {"name": "Rajasthan", "population": "81032689", "rank": "1st"}
          }

df = pd.DataFrame(states)
df.to_csv('IndianStates.csv', index=False)
read_csv = pd.read_csv('IndianStates.csv', sep=",")
print(read_csv)