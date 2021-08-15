import plotly_express as px
import csv 

with open("data.csv")as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()