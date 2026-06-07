# ⚡ Hybrid Streaming Pipeline (Crypto Data Engineering System)

## 📌 Overview

This project simulates a hybrid data engineering system that processes crypto market data using batch-style ETL pipelines and streaming-inspired workflows.

It demonstrates how financial data can be ingested, transformed, and converted into trading signals using automated pipelines.

---

## 🏗️ System Architecture

```text
Crypto Market Data Source
↓
Python Extraction Layer (scripts/extract.py)
↓
Signal Generation Layer (scripts/crypto_signal.py)
↓
Trading Signal Processing (scripts/trading_signals.py)
↓
PostgreSQL Database (SQL Layer)
↓
Airflow Orchestration (crypto_pipeline.py DAG)
↓
Scheduled Pipeline Execution

```

---

## ⚙️ Components

### 📥 Data Extraction Layer
- Simulates or fetches crypto market data
- Prepares structured input for downstream processing

---

### 📊 Signal Generation Layer
- Computes crypto trading signals
- Applies rule-based or statistical transformations

---

### 📈 Trading Signal Layer
- Converts signals into structured outputs
- Prepares data for storage and analytics

---

### 🧠 Orchestration Layer (Airflow)
- Automates pipeline execution using DAGs
- Handles task dependencies and scheduling
- Ensures reproducibility of workflows

---

## 🧰 Tech Stack

- Python (Data Processing)
- SQL (Data Storage)
- PostgreSQL (Database Layer)
- Apache Airflow (Workflow Orchestration)
- Docker (Containerization)

---

## 🔄 Pipeline Flow

Crypto Data → Extraction → Signal Generation → Trading Logic → Database → Airflow Scheduling

---

## 🚀 Outcome

This project demonstrates a hybrid data engineering pipeline combining:

- Batch-style ETL processing
- Streaming-inspired financial data workflows
- Automated orchestration using Airflow
- Structured trading signal generation

It simulates real-world fintech data engineering systems used in trading analytics platforms.
