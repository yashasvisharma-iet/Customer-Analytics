# Customer Support Analytics & SLA Optimization

## 📌 Overview
Analyzed 1000+ customer support tickets to identify key drivers of SLA breaches and customer satisfaction.

Built an end-to-end analytics pipeline using Python (Pandas) and Tableau to transform raw data into actionable business insights.

---

## ⚙️ Tech Stack
- Python (Pandas)
- Tableau Cloud
- SQL (for KPI logic)
- Jupyter Notebook

---

## 📊 Key KPIs
- SLA Breach Rate: 45.33%
- Avg Resolution Time: 45.79 hrs
- Avg CSAT Score: 3.16

---

## 🔍 Key Insights

- Delayed first responses increase SLA breach rate from **42% → 60%**
- Longer resolution times reduce CSAT (**correlation: -0.26**)
- Chat and Email channels show higher SLA breaches
- Slow tickets (>24 hrs) have significantly lower CSAT (~2.84)

---

## 📈 Dashboard
👉 View Dashboard:

![Dashboard Preview](ss.png)

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python src/app.py