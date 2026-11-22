import streamlit as st
from common import data, filters, footer
import plotly.express as px
st.set_page_config(page_title="URBAN PULSE", page_icon="🏙️", layout="wide")
st.title("🏙️ URBAN PULSE")
st.subheader("Citizen Complaint Intelligence & Resolution Analytics")
df=data()
if df is not None:
    d=filters(df)
    n=len(d); s=d.status.fillna("").str.lower() if "status" in d else None
    closed=int((s=="closed").sum()) if s is not None else 0
    opened=int((s=="open").sum()) if s is not None else 0
    r=d.resolution_hours.dropna() if "resolution_hours" in d else []
    a,b,c,e,f=st.columns(5)
    a.metric("Total Requests",f"{n:,}"); b.metric("Recorded Closure",f"{closed/n*100:.2f}%" if n else "0%")
    c.metric("Open Requests",f"{opened:,}"); e.metric("Median Resolution",f"{r.median():.2f} hrs" if len(r) else "N/A")
    f.metric("Over 72 Hours",f"{(r>72).mean()*100:.2f}%" if len(r) else "N/A")
    x,y=st.columns(2)
    if "borough" in d:
        x.subheader("Requests by Borough"); x.bar_chart(d.borough.fillna("Unspecified").value_counts())
    if "complaint_type" in d:
        y.subheader("Top Complaint Types"); y.bar_chart(d.complaint_type.value_counts().head(10))
    st.info("Use the sidebar to open the four detailed analyst pages.")
footer()
