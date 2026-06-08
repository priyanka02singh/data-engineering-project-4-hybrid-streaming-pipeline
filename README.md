# ⚡ Project 4: Crypto Data Engineering Pipeline (Batch ETL + Orchestration)

## 📌 Overview

This project simulates a crypto data engineering pipeline that processes market data using a structured batch ETL workflow orchestrated with Apache Airflow.

It demonstrates how raw financial market data can be ingested, transformed, and converted into structured datasets and trading signals for downstream analytics.

This pipeline reflects real-world fintech data engineering workflows, where scheduled jobs process financial data for reporting and decision-making systems.

---

## 🎯 Business Problem

Financial markets generate continuous streams of price and trading data, but organizations often need:

- Cleaned and structured historical datasets
- Derived trading indicators
- Scheduled processing workflows
- Reliable storage for analytics and reporting

Raw market data cannot be directly used for decision-making due to noise, inconsistency, and lack of structure.

### This project solves:
- How to extract and structure raw crypto market data
- How to generate meaningful trading signals from raw inputs
- How to automate ETL workflows using orchestration tools
- How to store processed data for analytics use cases

---

## 🏗️ System Architecture

```text
Crypto Market Data Source
        ↓
Python Extraction Layer (extract.py)
        ↓
Data Transformation Layer (signal generation)
        ↓
Trading Signal Engine (rule-based computations)
        ↓
PostgreSQL Database (structured storage)
        ↓
Apache Airflow DAG (pipeline orchestration)
        ↓
Scheduled Batch Execution
```

---

## 🔄 Data Flow
- Crypto market data is extracted using Python scripts
- Raw data is cleaned and normalized
- Feature engineering is applied to generate trading signals
- Signals are transformed into structured records
- Data is stored in PostgreSQL for querying and analysis
- Airflow orchestrates the entire pipeline using scheduled DAG runs

---

## 📦 Data Processing Stages
### 1. Data Extraction Layer
- Simulates or fetches crypto market data
- Standardizes raw input format
- Prepares data for transformation

### 2. Signal Generation Layer
- Computes trading indicators from price movements
- Applies rule-based transformations (e.g., trend signals)
- Produces structured signal outputs

### 3. Trading Signal Processing Layer
- Converts computed signals into final dataset format
- Ensures consistency for storage and analytics

### 4. Storage Layer (PostgreSQL)
- Stores processed trading signals
- Enables structured querying for analysis and reporting

### 5. Orchestration Layer (Airflow)
- Automates execution using DAG-based workflows
- Manages task dependencies
- Ensures reproducibility of pipeline runs
- Schedules periodic batch processing jobs

---

## 🧰 Tech Stack

- Python → Data extraction & transformation
- SQL → Data storage & querying
- PostgreSQL → Relational database for structured data
- Apache Airflow → Workflow orchestration
- Docker → Local environment setup

---

## ⚙️ Key Engineering Concepts
### 1. Batch ETL Pipeline Design

The system follows a structured ETL flow:

- Extract → Transform → Load

### 2. Workflow Orchestration

Airflow manages pipeline execution:

- Defines task dependencies
- Automates scheduled runs
- Ensures repeatability and reliability

### 3. Data Transformation Logic

The system applies:

- Cleaning of raw market data
- Feature engineering for trading signals
- Structured formatting for storage

### 4. Modular Pipeline Design

Each stage is independently defined:

- Extraction layer
- Transformation layer
- Storage layer
- Orchestration layer

---

## ⚠️ Limitations & Trade-offs
- No real-time streaming (batch-only system)
- No external market API integration (simulated/controlled data)
- No advanced ML-based prediction models
- No distributed computing layer (single-node setup)

These simplifications were intentional to focus on core ETL and orchestration concepts.

---

## 🔗 Connection to Full Data Platform (Projects 5 & 6)

This project represents the batch processing layer in a larger data ecosystem:

- Project 4 → Batch ETL + orchestration
- Project 5 → Real-time streaming pipeline (Kafka)
- Project 6 → Data warehouse + analytics platform

Together, they simulate a modern end-to-end data engineering ecosystem (batch + streaming + analytics).

---

## ▶️ How to Run
```bash
# Start Airflow environment
docker-compose up

# Run extraction script
python extract.py

# Run transformation pipeline
python crypto_signal.py

# Trigger Airflow DAG
airflow dags trigger crypto_pipeline
```
---

## 📊 Output Examples
- Cleaned crypto market dataset
- Generated trading signal dataset
- Structured PostgreSQL tables
- Scheduled pipeline execution logs from Airflow

---

## 💡 Key Learnings
- Batch ETL pipeline design (Extract → Transform → Load)
- Data pipeline orchestration using Airflow
- Financial data transformation logic
- Structured data modeling for analytics
- Building modular and maintainable data workflows
