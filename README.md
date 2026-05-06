# Pulse_IQ
# ⚡ DataFlow AI — Business Intelligence & Analytics Platform

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Claude AI](https://img.shields.io/badge/Claude_AI-Powered-FF6B35?style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-3_Workflows-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An AI-powered Business Intelligence platform with automated ETL pipelines, KPI dashboards, and an intelligent analytics assistant — all running on automated GitHub Actions workflows.**

[Features](#-features) • [Workflows](#-automated-workflows) • [API](#-api-endpoints) • [Setup](#-setup) • [Tech Stack](#-tech-stack)

</div>

---

## 🎯 What is DataFlow AI?

DataFlow AI is a production-ready **Business Intelligence & Analytics API** that combines:

- 🤖 **AI Analytics Assistant** — powered by Claude AI for natural language data insights
- 🔄 **Automated ETL Pipelines** — daily data extraction, transformation, and loading
- 📊 **KPI Dashboard Engine** — real-time business metrics refresh
- 📝 **Auto Report Generation** — weekly BI reports generated automatically
- ⚙️ **3 GitHub Actions Workflows** — fully automated CI/CD and data pipelines

---

## ✨ Features

### 🤖 AI Analytics Assistant
Ask business questions in plain English and get data-driven answers:
```
"What are my top performing channels?"
"Where should I focus my marketing budget?"
"Analyze my conversion rate trends"
```

### 🔄 Automated Data Workflows
Three fully automated GitHub Actions pipelines running on schedule:

| Workflow | Schedule | What It Does |
|---|---|---|
| 🔄 Daily ETL | Every day 6AM UTC | Extract → Transform → Load sales data |
| 📊 KPI Refresh | Every 30 minutes | Refresh all dashboard KPIs |
| 📝 Weekly Report | Every Monday 8AM | Auto-generate BI report |

### 📊 Analytics Dashboard
Real-time metrics across:
- Revenue trends & growth rates
- Order volume & conversion rates
- Channel performance (organic, paid, email, referral)
- Regional breakdowns (west, east, central, south)
- Customer LTV & churn analysis

---

## ⚙️ Automated Workflows

### 1. 🔄 Daily ETL Pipeline (`.github/workflows/daily_etl.yml`)
```yaml
Trigger: Daily at 6AM UTC + manual dispatch
Steps:
  1. Extract data from source systems
  2. Transform & aggregate metrics
  3. Load to output storage
  4. Refresh KPI dashboard
  5. Upload artifacts to GitHub
```

### 2. 📝 Weekly Report Generator (`.github/workflows/weekly_report.yml`)
```yaml
Trigger: Every Monday at 8AM UTC + manual dispatch
Steps:
  1. Run ETL pipeline
  2. Generate executive summary
  3. Build recommendations
  4. Save report as artifact (90-day retention)
```

### 3. ✅ CI Pipeline (`.github/workflows/ci.yml`)
```yaml
Trigger: Every push to main/develop + pull requests
Steps:
  1. Lint code with Ruff
  2. Run pytest test suite
  3. Test all 3 workflow scripts
  4. Validate API endpoints
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | API homepage |
| `GET` | `/health` | Health check |
| `POST` | `/chat` | 🤖 AI Analytics Assistant |
| `GET` | `/analytics/sales` | Sales data (configurable days) |
| `GET` | `/analytics/kpis` | KPI summary dashboard |
| `POST` | `/analytics/insights` | AI-generated data insights |
| `POST` | `/report/generate` | Auto-generate BI report |
| `GET` | `/workflows/status` | Pipeline status monitor |

### Example: Chat with AI Assistant
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What are my top performing channels?", "context": "sales analytics"}'
```

### Example: Get KPI Dashboard
```bash
curl http://localhost:8000/analytics/kpis?days=30
```

### Example: Generate Report
```bash
curl -X POST http://localhost:8000/report/generate \
  -H "Content-Type: application/json" \
  -d '{"title": "Q1 Report", "metrics": ["total_revenue", "total_orders"], "period": "last_30_days"}'
```

---

## 🚀 Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/dataflow-ai.git
cd dataflow-ai

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables (optional — runs in demo mode without)
echo "ANTHROPIC_API_KEY=your_key_here" > .env

# 5. Run the API
uvicorn app.main:app --reload

# 6. Run a workflow manually
python workflows/pipeline.py etl    # Run ETL
python workflows/pipeline.py kpi    # Refresh KPIs
python workflows/pipeline.py report # Generate report

# 7. Run tests
pytest tests/ -v
```

Visit **http://localhost:8000/docs** for interactive API documentation.

---

## 📁 Project Structure

```
dataflow-ai/
│
├── app/
│   └── main.py               # FastAPI app — all API endpoints + AI assistant
│
├── workflows/
│   └── pipeline.py           # ETL, KPI refresh, report generation
│
├── .github/
│   └── workflows/
│       ├── daily_etl.yml     # Daily automated ETL pipeline
│       ├── weekly_report.yml # Weekly BI report generator
│       └── ci.yml            # CI/CD — lint, test, validate
│
├── tests/
│   └── test_api.py           # pytest test suite
│
├── outputs/                  # Generated data files (gitignored)
├── requirements.txt
└── README.md
```

---

## 🤖 Tech Stack

| Layer | Technology |
|---|---|
| **API Framework** | FastAPI |
| **AI Assistant** | Claude AI (Anthropic) |
| **Automation** | GitHub Actions (3 workflows) |
| **Data Processing** | Python, JSON |
| **Testing** | pytest, httpx |
| **Linting** | Ruff |
| **Runtime** | Python 3.12 |

---

## 📊 Sample Output

```json
{
  "kpis": {
    "total_revenue": 412847.32,
    "total_orders": 4821,
    "avg_conversion_rate": 5.43,
    "avg_order_value": 156.23,
    "revenue_growth": 12.4,
    "customer_satisfaction": 4.7,
    "churn_rate": 2.3
  },
  "period": "last_30_days"
}
```

---

## 🗺️ Roadmap

- [ ] PostgreSQL integration for persistent storage
- [ ] Slack notifications on workflow completion
- [ ] Power BI / Tableau dashboard integration
- [ ] Real-time WebSocket data streaming
- [ ] Multi-tenant support with API key auth
- [ ] Dockerize for one-command deployment

---

## 🙋 Author

**Sumanth [Last Name]**
MS Business Analytics — University of North Texas

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/yourprofile)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github)](https://github.com/yourusername)

---



---

<div align="center">
Built with ⚡ to showcase automated AI-powered analytics workflows.
</div>
