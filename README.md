# 🏙️ URBAN PULSE
### Citizen Complaint Intelligence & Resolution Analytics

**URBAN PULSE** is a data analytics project that explores citizen complaints and service requests using Python, Pandas, PostgreSQL, SQL, and Streamlit.

The project focuses on understanding complaint patterns, analysing resolution performance, and presenting useful insights through an interactive dashboard.

## 🎯 Project Objectives

- Analyse citizen complaint patterns and distribution.
- Identify complaint categories with high request volumes.
- Compare complaint resolution performance.
- Examine geographic and time-based complaint trends.
- Present key performance indicators through an interactive dashboard.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas & NumPy | Data cleaning and manipulation |
| PostgreSQL | Database storage |
| SQL | Data querying and analysis |
| Matplotlib, Seaborn & Plotly | Data visualization |
| Streamlit | Interactive dashboard |

## 📂 Dataset

**Source:** NYC 311 Service Requests

[NYC Open Data – 311 Service Requests](https://data.cityofnewyork.us/Social-Services/311-Service-Requests/erm2-nwe9)

The project uses a snapshot of 100,000 recently created service requests, covering November 4–13, 2026.

## ⚙️ Project Workflow

1. **Data Collection:** Retrieve service request records from the NYC Open Data API.
2. **Data Cleaning:** Handle missing values, duplicates, date formats, and invalid resolution durations.
3. **Feature Engineering:** Create resolution hours and additional date-based columns.
4. **Exploratory Data Analysis:** Examine complaint distributions, trends, and resolution times.
5. **Database Management:** Store and query cleaned records using PostgreSQL.
6. **Dashboard Development:** Build an interactive, multi-page Streamlit application.

## 📊 Dashboard Features

The dashboard includes:

- **Overview Dashboard:** Key performance indicators and complaint summaries.
- **Geographic Analysis:** Complaint distribution across boroughs.
- **Complaint Analysis:** Complaint category and status analysis.
- **Resolution Analysis:** Resolution time distribution and delayed complaints.
- **Data Explorer:** Browse complaint records.

### Key Performance Indicators

1. Total Complaints
2. Closure Rate
3. Open Complaints
4. Median Resolution Time
5. Percentage of Resolved Complaints Taking More Than 72 Hours

## 📈 Sample Findings

Based on the analysed 100,000-record snapshot:

- Brooklyn recorded the highest complaint volume.
- Thursday had the highest number of complaints among weekdays.
- 10 AM was the busiest hour in the dataset.
- Median resolution time was approximately 2.45 hours.
- Approximately 5.12% of valid resolution records took more than 72 hours.

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/dharanmurugesan-crypto/URBAN-PULSE.git
cd URBAN-PULSE
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Create or configure the PostgreSQL database:

- Database: `urban_pulse_db`
- Table: `service_requests`

Set your database password using the `DB_PASSWORD` environment variable, or configure Streamlit secrets locally.

For Windows PowerShell:

```powershell
$env:DB_PASSWORD = "YOUR_POSTGRES_PASSWORD"
```

Make sure your PostgreSQL server is running and the required table is populated before starting the dashboard.

### 5. Run the application

```bash
python -m streamlit run app.py
```

## ⚠️ Limitations

- The analysis covers a 10-day data snapshot and may not represent long-term trends.
- Missing closure dates affect resolution-time calculations.
- Citizen complaints represent reported issues, not necessarily the complete extent of city problems.
- Recorded complaint closure does not necessarily indicate citizen satisfaction.

## 👨‍💻 Author

**Dharan Murugesan**

GitHub: [dharanmurugesan-crypto](https://github.com/dharanmurugesan-crypto)

---

*This project was developed as part of a learning journey in data analytics and AIML.*
