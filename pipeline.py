"""
DataFlow AI — Automated Workflow Engine
Handles ETL, KPI refresh, and AI insight generation pipelines.
"""

import json
import random
import logging
from datetime import datetime, timedelta
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger("dataflow")

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


# ── ETL Pipeline ───────────────────────────────────────────────────────────────

def extract() -> list[dict]:
    """Simulate data extraction from source systems."""
    log.info("🔄 Extracting data from source systems...")
    records = []
    base = datetime.now() - timedelta(days=30)
    for i in range(30):
        date = base + timedelta(days=i)
        records.append({
            "date": date.strftime("%Y-%m-%d"),
            "revenue": round(random.uniform(8000, 25000), 2),
            "orders": random.randint(50, 300),
            "customers": random.randint(30, 200),
            "conversion_rate": round(random.uniform(2.5, 8.5), 2),
            "avg_order_value": round(random.uniform(80, 250), 2),
            "channel": random.choice(["organic", "paid", "email", "referral"]),
            "region": random.choice(["west", "east", "central", "south"]),
        })
    log.info(f"✅ Extracted {len(records)} records")
    return records


def transform(records: list[dict]) -> dict:
    """Transform raw data into analytics-ready format."""
    log.info("⚙️  Transforming data...")

    total_revenue = sum(r["revenue"] for r in records)
    total_orders = sum(r["orders"] for r in records)

    by_channel = {}
    by_region = {}

    for r in records:
        ch = r["channel"]
        rg = r["region"]
        by_channel[ch] = by_channel.get(ch, 0) + r["revenue"]
        by_region[rg] = by_region.get(rg, 0) + r["revenue"]

    transformed = {
        "summary": {
            "total_revenue": round(total_revenue, 2),
            "total_orders": total_orders,
            "avg_conversion": round(sum(r["conversion_rate"] for r in records) / len(records), 2),
            "avg_order_value": round(sum(r["avg_order_value"] for r in records) / len(records), 2),
            "period": "last_30_days",
        },
        "by_channel": {k: round(v, 2) for k, v in by_channel.items()},
        "by_region": {k: round(v, 2) for k, v in by_region.items()},
        "top_day": max(records, key=lambda x: x["revenue"])["date"],
        "daily_records": records,
        "processed_at": datetime.now().isoformat(),
    }

    log.info("✅ Transformation complete")
    return transformed


def load(data: dict, filename: str = "analytics_data.json") -> Path:
    """Load transformed data to output storage."""
    log.info(f"💾 Loading data to {filename}...")
    output_path = OUTPUT_DIR / filename
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    log.info(f"✅ Data saved to {output_path}")
    return output_path


def run_etl_pipeline() -> dict:
    """Full ETL pipeline execution."""
    log.info("🚀 Starting ETL Pipeline")
    start = datetime.now()

    raw = extract()
    transformed = transform(raw)
    output = load(transformed)

    duration = (datetime.now() - start).total_seconds()
    result = {
        "pipeline": "Daily Sales ETL",
        "status": "success",
        "records_processed": len(raw),
        "output_file": str(output),
        "duration_seconds": round(duration, 3),
        "completed_at": datetime.now().isoformat(),
    }

    log.info(f"✅ ETL Pipeline complete in {duration:.2f}s")
    return result


# ── KPI Workflow ───────────────────────────────────────────────────────────────

def refresh_kpis() -> dict:
    """Refresh KPI dashboard data."""
    log.info("📊 Refreshing KPI Dashboard...")

    data_path = OUTPUT_DIR / "analytics_data.json"
    if data_path.exists():
        with open(data_path) as f:
            data = json.load(f)
        summary = data["summary"]
    else:
        raw = extract()
        transformed = transform(raw)
        summary = transformed["summary"]

    kpis = {
        **summary,
        "revenue_vs_target": round(random.uniform(85, 115), 1),
        "customer_satisfaction": round(random.uniform(4.1, 4.9), 1),
        "churn_rate": round(random.uniform(1.5, 5.0), 2),
        "ltv": round(random.uniform(450, 950), 2),
        "refreshed_at": datetime.now().isoformat(),
    }

    load(kpis, "kpi_dashboard.json")
    log.info("✅ KPI Dashboard refreshed")
    return kpis


# ── Report Workflow ────────────────────────────────────────────────────────────

def generate_weekly_report() -> dict:
    """Auto-generate weekly business report."""
    log.info("📝 Generating Weekly Report...")

    kpi_path = OUTPUT_DIR / "kpi_dashboard.json"
    if kpi_path.exists():
        with open(kpi_path) as f:
            kpis = json.load(f)
    else:
        kpis = refresh_kpis()

    report = {
        "title": f"Weekly Business Intelligence Report",
        "period": f"Week of {(datetime.now() - timedelta(days=7)).strftime('%B %d, %Y')}",
        "generated_at": datetime.now().isoformat(),
        "executive_summary": {
            "total_revenue": kpis.get("total_revenue", 0),
            "total_orders": kpis.get("total_orders", 0),
            "avg_conversion_rate": kpis.get("avg_conversion", 0),
            "revenue_vs_target": kpis.get("revenue_vs_target", 100),
        },
        "highlights": [
            f"Revenue tracking at {kpis.get('revenue_vs_target', 100)}% of target",
            f"Customer satisfaction score: {kpis.get('customer_satisfaction', 4.5)}/5.0",
            f"Average order value: ${kpis.get('avg_order_value', 150):.2f}",
        ],
        "recommendations": [
            "Double down on top-performing acquisition channels",
            "Launch re-engagement campaign for churned customers",
            "A/B test checkout flow to improve conversion by 1-2%",
            "Expand inventory in high-demand product categories",
        ],
        "next_review": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
    }

    load(report, f"weekly_report_{datetime.now().strftime('%Y%m%d')}.json")
    log.info("✅ Weekly Report generated")
    return report


# ── Main Runner ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    workflows = {
        "etl": run_etl_pipeline,
        "kpi": refresh_kpis,
        "report": generate_weekly_report,
    }

    workflow = sys.argv[1] if len(sys.argv) > 1 else "etl"

    if workflow not in workflows:
        log.error(f"Unknown workflow: {workflow}. Choose from: {list(workflows.keys())}")
        sys.exit(1)

    result = workflows[workflow]()
    print(json.dumps(result, indent=2))
