from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional
import httpx
import json
import os
import random
from datetime import datetime, timedelta

app = FastAPI(
    title="DataFlow AI",
    description="AI-Powered Business Intelligence & Analytics Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")


# ── Models ─────────────────────────────────────────────────────────────────────

class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = "business analytics"

class AnalyticsRequest(BaseModel):
    dataset: str
    question: str

class ReportRequest(BaseModel):
    title: str
    metrics: list[str]
    period: str = "last_30_days"


# ── Mock Data Generator ────────────────────────────────────────────────────────

def generate_sales_data(days: int = 30) -> list[dict]:
    data = []
    base = datetime.now() - timedelta(days=days)
    for i in range(days):
        date = base + timedelta(days=i)
        data.append({
            "date": date.strftime("%Y-%m-%d"),
            "revenue": round(random.uniform(8000, 25000), 2),
            "orders": random.randint(50, 300),
            "customers": random.randint(30, 200),
            "conversion_rate": round(random.uniform(2.5, 8.5), 2),
            "avg_order_value": round(random.uniform(80, 250), 2),
        })
    return data


def generate_kpi_summary(data: list[dict]) -> dict:
    total_revenue = sum(d["revenue"] for d in data)
    total_orders = sum(d["orders"] for d in data)
    avg_conversion = sum(d["conversion_rate"] for d in data) / len(data)
    avg_aov = sum(d["avg_order_value"] for d in data) / len(data)
    prev_revenue = total_revenue * random.uniform(0.85, 0.95)

    return {
        "total_revenue": round(total_revenue, 2),
        "total_orders": total_orders,
        "avg_conversion_rate": round(avg_conversion, 2),
        "avg_order_value": round(avg_aov, 2),
        "revenue_growth": round(((total_revenue - prev_revenue) / prev_revenue) * 100, 2),
        "top_day": max(data, key=lambda x: x["revenue"])["date"],
        "peak_revenue": round(max(d["revenue"] for d in data), 2),
    }


# ── Routes ─────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html><body style="font-family:monospace;background:#0a0a0a;color:#00ff88;padding:40px">
    <h1>⚡ DataFlow AI — API Running</h1>
    <p>Visit <a href="/docs" style="color:#00aaff">/docs</a> for full API documentation</p>
    <ul>
        <li>POST /chat — AI Analytics Assistant</li>
        <li>GET  /analytics/sales — Sales Dashboard Data</li>
        <li>GET  /analytics/kpis — KPI Summary</li>
        <li>POST /analytics/insights — AI-Generated Insights</li>
        <li>POST /report/generate — Auto-Generate Reports</li>
        <li>GET  /workflows/status — Workflow Pipeline Status</li>
    </ul>
    </body></html>
    """


@app.post("/chat")
async def chat_with_ai(request: ChatRequest):
    """AI Analytics Assistant powered by Claude."""
    if not ANTHROPIC_API_KEY:
        # Demo mode — return mock response
        responses = [
            f"Based on your {request.context} data, I can see strong growth trends in Q1. Revenue is up 18% compared to the previous period, driven primarily by increased conversion rates and higher average order values.",
            f"Analyzing your {request.context} metrics — your top performing segment shows a 23% uplift. I recommend focusing budget allocation on high-converting channels to maximize ROI.",
            f"Your {request.context} data reveals an interesting pattern: weekday performance outpaces weekends by 34%. Consider shifting campaign timing to capitalize on peak engagement windows.",
        ]
        return {
            "response": random.choice(responses),
            "model": "demo-mode",
            "context": request.context,
            "timestamp": datetime.now().isoformat()
        }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 500,
                "system": f"You are DataFlow AI, an expert business intelligence and analytics assistant. Context: {request.context}. Be concise, data-driven, and actionable.",
                "messages": [{"role": "user", "content": request.message}]
            },
            timeout=30
        )

    data = response.json()
    return {
        "response": data["content"][0]["text"],
        "model": data["model"],
        "context": request.context,
        "timestamp": datetime.now().isoformat()
    }


@app.get("/analytics/sales")
async def get_sales_data(days: int = 30):
    """Get sales analytics data."""
    data = generate_sales_data(days)
    return {
        "period": f"last_{days}_days",
        "data": data,
        "generated_at": datetime.now().isoformat()
    }


@app.get("/analytics/kpis")
async def get_kpis(days: int = 30):
    """Get KPI summary dashboard."""
    data = generate_sales_data(days)
    kpis = generate_kpi_summary(data)
    return {
        "period": f"last_{days}_days",
        "kpis": kpis,
        "generated_at": datetime.now().isoformat()
    }


@app.post("/analytics/insights")
async def get_ai_insights(request: AnalyticsRequest):
    """Generate AI-powered insights from your data."""
    insight_request = ChatRequest(
        message=f"Dataset: {request.dataset}. Question: {request.question}. Provide 3 specific, actionable insights.",
        context="business analytics insights"
    )
    return await chat_with_ai(insight_request)


@app.post("/report/generate")
async def generate_report(request: ReportRequest):
    """Auto-generate a business intelligence report."""
    data = generate_sales_data(30)
    kpis = generate_kpi_summary(data)

    report = {
        "title": request.title,
        "period": request.period,
        "generated_at": datetime.now().isoformat(),
        "executive_summary": f"Performance report for {request.title} covering {request.period}.",
        "metrics": {},
        "recommendations": [
            "Increase investment in top-performing channels by 20%",
            "Optimize conversion funnel — focus on checkout abandonment",
            "Expand customer retention programs targeting high-LTV segments",
        ]
    }

    for metric in request.metrics:
        if metric in kpis:
            report["metrics"][metric] = kpis[metric]

    return report


@app.get("/workflows/status")
async def get_workflow_status():
    """Get status of all automated data workflows."""
    workflows = [
        {
            "name": "Daily Sales ETL",
            "status": "✅ Success",
            "last_run": (datetime.now() - timedelta(hours=2)).isoformat(),
            "next_run": (datetime.now() + timedelta(hours=22)).isoformat(),
            "records_processed": random.randint(5000, 15000),
        },
        {
            "name": "KPI Dashboard Refresh",
            "status": "✅ Success",
            "last_run": (datetime.now() - timedelta(minutes=30)).isoformat(),
            "next_run": (datetime.now() + timedelta(minutes=30)).isoformat(),
            "records_processed": random.randint(100, 500),
        },
        {
            "name": "AI Insights Generator",
            "status": "🔄 Running",
            "last_run": (datetime.now() - timedelta(minutes=5)).isoformat(),
            "next_run": (datetime.now() + timedelta(hours=6)).isoformat(),
            "records_processed": random.randint(1000, 3000),
        },
        {
            "name": "Weekly Report Generator",
            "status": "⏳ Scheduled",
            "last_run": (datetime.now() - timedelta(days=7)).isoformat(),
            "next_run": (datetime.now() + timedelta(days=1)).isoformat(),
            "records_processed": 0,
        },
    ]
    return {
        "total_workflows": len(workflows),
        "active": sum(1 for w in workflows if "Running" in w["status"]),
        "successful": sum(1 for w in workflows if "Success" in w["status"]),
        "workflows": workflows,
        "checked_at": datetime.now().isoformat()
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "ai_enabled": bool(ANTHROPIC_API_KEY),
        "timestamp": datetime.now().isoformat()
    }
