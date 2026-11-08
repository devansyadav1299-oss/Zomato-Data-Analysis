# 📊 Zomato Location & Performance Analysis: Consumer Insights Engine

[![Python Version](https://shields.io)](https://python.org)
[![Data Pipeline](https://shields.io)](https://pydata.org)
[![Data Visualization](https://shields.io)](https://pydata.org)

## 🎯 Business Context & Core Objectives

Consumer behavioral shifts within aggregate logistics spaces like Zomato dictate revenue optimizations for restaurant owners.

This project delivers an end-to-end data cleaning, processing, and exploratory data analysis (EDA) pipeline that transforms raw commercial tracking fields into actionable optimization matrices. It maps dining trends, evaluates order channel efficiencies, and isolates low-penetration targets for marketing interventions.

---

## 🚀 Key Strategic Insights Summary

- **Dominant Market Segment:** **Dining** constitutes the vast majority of consumer engagement footprint, leading overall transaction counts.
- **Volume Drivers:** **Dining** venues hold the largest aggregate customer attention, capturing **20,363 aggregate votes**.
- **Ecosystem Performance Baseline:** Most platforms settle securely in the **3.5 to 4.0 out of 5.0 rating band**.
- **Average Ticket Size:** Couples ordering food online demonstrate a mean basket spend of **\$510.34 per transaction**.
- **Channel Performance Premium:** Food services offering **Online Ordering** capture a statistically significant premium on review metrics over offline alternatives.
- **Target Promotion Opportunity:** **Dining establishments** present the highest non-digital footprint, identifying them as prime candidates for target integration offers.

---

## ⚙️ Engineering & Analytics Pipeline

### 1. Ingestion & Structured Cleaning

- Isolated string fragments to unpack historical objects (`4.1/5`) into low-overhead 64-bit float indices.
- Stripped mathematical commas out of monetary vectors to maintain integer format consistency.
- Evaluated missing value null distributions across feature vectors to verify clean database structures.

### 2. Multi-Plot Statistical Visualizations

- Developed custom matrices mapping order fulfillment types across business classifications.
- Visualized outlier boundaries on review distributions using explicit hue variables via Seaborn boxplots.

---

## 🗂️ Production Repository Architecture

```text
Zomato-Data-Analysis/
├── data/                               # Source storage directory
│   └── Zomato data .csv
├── notebooks/                          # Development notebook tracks
│   └── Zomato_Data_Analysis.ipynb
├── requirements.txt                    # App dependency schema
└── README.md                           # Documentation Portfolio
```

---

## 💻 Installation & Local Reproducibility

1. Clone this repository to your workstation directory:

   ```bash
   git clone https://github.com
   cd Zomato-Data-Analysis
   ```

2. Establish an isolated virtual environment and initialize dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Launch your notebook runtime:
   ```bash
   jupyter notebook notebooks/Zomato_Data_Analysis.ipynb
   ```

---

👨‍💻 **Developed by Devans yadav** @www.linkedin.com/in/
devansyadav1299
