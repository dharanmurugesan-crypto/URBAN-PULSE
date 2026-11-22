import streamlit as st, plotly.express as px
from common import data,filters,footer
st.title("⏱️ Resolution Analysis")
d=data()
if d is not None:
 d=filters(d)
 if "resolution_hours" in d:
  r=d.resolution_hours.dropna()
  a,b,c=st.columns(3); a.metric("Valid records",f"{len(r):,}"); b.metric("Median",f"{r.median():.2f} hrs" if len(r) else "N/A"); c.metric("Over 72 hours",f"{(r>72).mean()*100:.2f}%" if len(r) else "N/A")
  if len(r):
   st.plotly_chart(px.histogram(d,x="resolution_hours",nbins=30,title="Resolution Time Distribution"),use_container_width=True)
   st.plotly_chart(px.box(d,y="resolution_hours",title="Resolution Time Boxplot"),use_container_width=True)
 if "created_date" in d:
  x=d.dropna(subset=["created_date"]).groupby(d.created_date.dt.date).size().reset_index(name="Requests")
  x.columns=["Date","Requests"]
  st.plotly_chart(px.line(x,x="Date",y="Requests",markers=True,title="Daily Request Trend"),use_container_width=True)
footer()
