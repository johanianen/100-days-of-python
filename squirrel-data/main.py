import pandas as pd
data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

len(data[data["Primary Fur Color"] == "Gray"])

squirrel_dict = {
    "Fur color":["Gray",
                 "Cinnamon",
                  "Black"],

    "Number":[len(data[data["Primary Fur Color"] == "Gray"]),
             len(data[data["Primary Fur Color"] == "Cinnamon"]), 
             len(data[data["Primary Fur Color"] == "Black"])] 
}

squirrel_df = pd.DataFrame(squirrel_dict)
squirrel_df.to_csv("./squirrel_fur_count.csv")