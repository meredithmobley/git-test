#https://goheels.com/sports/mens-basketball/roster

import pandas as pd

roster = ["Evans", "High", "Brown"]
for player in roster:
    print (player)

data = pd.DataFrame(roster)
print(data)
