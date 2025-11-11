#https://goheels.com/sports/mens-basketball/roster

import pandas as pd

roster = ["Evans", "High", "Brown"]
player = {"Last Name": roster,
        "First Name": ["Kyan","Zayden", "James"], 
        "Height": ["602", "610", "610"],
        "Weight": ["175", "230", "240"]}
data = pd.DataFrame(player)
print(data)
