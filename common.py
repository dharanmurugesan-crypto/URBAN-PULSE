import os, streamlit as st, pandas as pd, psycopg2
@st.cache_resource
def conn():
    pw=os.getenv("DB_PASSWORD")
    if not pw:
        try: pw=st.secrets["DB_PASSWORD"]
        except Exception: st.error("Set DB_PASSWORD as an environment variable or in .streamlit/secrets.toml."); st.stop()
    return psycopg2.connect(host="localhost",database="urban_pulse_db",user="postgres",password=pw,port="5432")
@st.cache_data(ttl=300)
def data():
    try:
        d=pd.read_sql_query("SELECT * FROM service_requests;",conn())
        if "created_date" in d: d["created_date"]=pd.to_datetime(d["created_date"],errors="coerce")
        return d
    except Exception as ex: st.error(f"Database error: {ex}"); st.stop()
def filters(d):
    st.subheader("🔎 Filters")
    a,b,c=st.columns(3)
    sel={}
    for col,box in [("borough",a),("complaint_type",b),("status",c)]:
        vals=sorted(d[col].dropna().astype(str).unique()) if col in d else []
        sel[col]=box.selectbox(col.replace("_"," ").title(),["All"]+vals)
    for col in ["borough","complaint_type","status"]:
        if sel[col]!="All" and col in d: d=d[d[col].astype(str)==sel[col]]
    if "created_date" in d and d.created_date.notna().any():
        lo,hi=d.created_date.min().date(),d.created_date.max().date()
        dates=st.date_input("Created Date Range",(lo,hi),min_value=lo,max_value=hi)
        if len(dates)==2: d=d[d.created_date.dt.date.between(*dates)]
    st.caption(f"Showing {len(d):,} records")
    return d
def footer(): st.markdown("---"); st.caption("URBAN PULSE | Citizen Complaint Intelligence & Resolution Analytics")
