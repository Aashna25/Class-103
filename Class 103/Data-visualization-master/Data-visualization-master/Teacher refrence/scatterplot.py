import pandas as pd
import plotly.express as px

df = pd.read_csv("C:\Users\anil1299\Desktop\WhiteHat.jr\Class 103\Data-visualization-master\Data-visualization-master\Teacher refrence\data.csv")
fig = px.scatter(df, x="Population", y="Per capita",
	          size="Percentage",color="Country",
                   size_max=60)
fig.show()
