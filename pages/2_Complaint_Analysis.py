import streamlit as st, plotly.express as px
from common import data,filters,footer
st.title("📊 Complaint Analysis")
d=data()
if d is not None:
 d=filters(d)
 if "complaint_type" in d:
  x=d.complaint_type.fillna("Unspecified").value_counts().head(10).rename_axis("Complaint Type").reset_index(name="Requests")
  st.plotly_chart(px.bar(x,x="Requests",y="Complaint Type",orientation="h",title="Top 10 Complaint Types"),use_container_width=True)
 if "status" in d:
  x=d.status.fillna("Unspecified").value_counts().rename_axis("Status").reset_index(name="Requests")
  st.plotly_chart(px.pie(x,names="Status",values="Requests",title="Status Distribution"),use_container_width=True)
footer()
