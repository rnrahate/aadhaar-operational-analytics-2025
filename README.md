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


🛠️ Technical Stack
Language: Python 3.x

Data Handling: Pandas, NumPy

Visualization: Seaborn, Matplotlib

Dashboarding: Tableau Public (Phase 6)

Version Control: Git & GitHub

📈 Major Discoveries
The Infrastructure Gap: Uttar Pradesh exhibits a severe "Biometric Lag" where demographic demand outpaces physical scanning capacity.

Seasonal Shocks: A predictable 15-20% surge in activity occurs from May to July, correlated with the Indian academic calendar.

Efficiency Bottlenecks: Isolated Pincodes in Telangana and Tamil Nadu with efficiency ratios as low as 1.7%, indicating critical hardware failure or understaffing.

⚙️ How to Run
Clone the repository:
git clone https://github.com/rnrahate_007/uidai_hackathon_2026.git

Place raw CSVs in data/raw/.

Run the notebooks in sequential order (00 through 04).

Refer to reports/findings.md for the full analytical report.

Developed by: rnrahate_007

Context: UIDAI National Hackathon 2026