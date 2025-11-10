#https://goheels.com/sports/mens-basketball/roster

import pandas as pd

roster = ["Evans", "High", "Brown"]
player = {"Last Name": roster}
data = pd.DataFrame(player)
print(data)
