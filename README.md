# 🇮🇳 Aadhaar Operational Analytics: 2025 Performance Review

## 📌 Project Overview
This repository contains a comprehensive data engineering and analytics pipeline for the UIDAI (Aadhaar) dataset of 2025. The project transitions from raw, fragmented CSV data to a unified master dataset, uncovering critical operational bottlenecks, "Biometric Deserts," and seasonal system strains across India.

### 🚀 Key Highlights
* **Scale:** Processed and merged ~4.9 million records across three disparate data silos.
* **Integrity:** Implemented a pre-merge aggregation strategy to eliminate Cartesian product errors and maintain 100% data accuracy.
* **Actionability:** Identified specific high-strain Pincodes (e.g., 501158) requiring immediate infrastructure audits.

---

## 📂 Project Structure
```text
uidai_hackathon_2026/
├── data/
│   ├── raw/               # Original UIDAI CSVs (Git Ignored)
│   └── processed/         # Cleaned & Master datasets
├── notebooks/             # Step-by-step Jupyter Workflows
│   ├── 00_data_quality.ipynb
│   ├── 01_eda.ipynb
│   ├── 02_feature_eng_and_merge.ipynb
│   ├── 03_analysis.ipynb
│   └── 04_visualizations.ipynb
├── reports/
│   ├── figures/           # Exported Python Visualizations
│   └── findings.md        # Detailed phase-by-phase insights
├── src/                   # Production-grade Python scripts
│   ├── config.py          # State mappings & path variables
│   └── utils.py           # Reusable processing functions
└── README.md


---

## 🛠️ Technical Stack
- **Language:** Python 3.x  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  
- **Dashboarding:** Tableau Public (Phase 6)  
- **Version Control:** Git & GitHub  

---

## 📈 Key Findings

### 1. Infrastructure Gap
- States like **Uttar Pradesh** show a strong biometric lag  
- Demand significantly exceeds available scanning infrastructure  

### 2. Seasonal Demand Surge
- A **15–20% spike** in Aadhaar activity is observed between **May–July**  
- Likely linked to the academic admission cycle  

### 3. Efficiency Bottlenecks
- Certain pincodes in **Telangana** and **Tamil Nadu** show efficiency as low as **~1.7%**  
- Indicates potential:
  - Hardware failures  
  - Operator shortages  
  - Process inefficiencies  

---

## ⚙️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/rnrahate_007/uidai_hackathon_2026.git
cd uidai_hackathon_2026