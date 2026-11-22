import streamlit as st, plotly.express as px
from common import data,filters,footer
st.title("📍 Geographic Analysis")
d=data()
if d is not None:
 d=filters(d)
 if "borough" in d:
  x=d.borough.fillna("Unspecified").value_counts().rename_axis("Borough").reset_index(name="Requests")
  st.plotly_chart(px.bar(x,x="Borough",y="Requests",title="Requests by Borough"),use_container_width=True)
  st.dataframe(x,use_container_width=True)
footer()
