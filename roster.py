#https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": ["Evans", "High", "Brown", "Dixon", "Young", "Denis", "Davis", "Trimble", "Wilson", "Powell"],
        "First Name": ["Kyan","Zayden", "James", "Derek", "Jaydon", "Isaiah", "Elijah", "Seth", "Caleb", "Jonathan"], 
        "Height": [74, 82, 82, 77, 76, 76, 77, 77, 82, 78],
        "Weight": [175, 230, 240, 200, 200, 180, 205, 200, 215, 190]}
data = pd.DataFrame(player)

#bmi = weight in kg/ heights in meters squared

data["BMI"] = (data["Weight"]/2.205)/((data["Height"]/39.37)**2)

print(data)

data.to_csv("bmi.csv")