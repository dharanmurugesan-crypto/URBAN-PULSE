import streamlit as st
from common import data,filters,footer
st.title("📋 Data Explorer")
d=data()
if d is not None:
 d=filters(d)
 st.dataframe(d.head(500),use_container_width=True)
 st.download_button("Download filtered CSV",d.to_csv(index=False).encode("utf-8"),"urban_pulse_filtered.csv","text/csv")
footer()
