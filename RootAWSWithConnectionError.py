import pandas as pd
from sqlalchemy import create_engine


data = pd.read_csv("startup.csv")

engine = create_engine('mysql+mysqlconnector://root:Suyash%401985@ec2-18-188-248-131.us-east-2.compute.amazonaws.com:3306/startup', echo=False)

data.to_sql(name="startupdata", con=engine, index=False, if_exists="replace")

print("Records Updated")
