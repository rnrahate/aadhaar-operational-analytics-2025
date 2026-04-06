# 🇮🇳 Aadhaar Operational Analytics: 2025 Performance Review

> A comprehensive data engineering and analytics pipeline built on UIDAI's 2025 dataset — transitioning raw, fragmented CSVs into a unified master dataset to uncover critical operational bottlenecks, **Biometric Deserts**, and seasonal system strains across India.

<br>

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Key Highlights](#-key-highlights)
- [Project Structure](#-project-structure)
- [Technical Stack](#️-technical-stack)
- [Pipeline Workflow](#-pipeline-workflow)
- [Key Findings](#-key-findings)
- [How to Run](#️-how-to-run)
- [Results & Reports](#-results--reports)
- [Contributing](#-contributing)

---

## 🔍 Project Overview

The **Aadhaar system** generates millions of authentication and enrollment records daily across thousands of centers in India. This project ingests, cleans, merges, and analyzes that data to surface actionable infrastructure insights for UIDAI stakeholders.

The pipeline handles three disparate data silos, resolves Cartesian product errors via pre-merge aggregation, and produces a clean master dataset ready for both Python-based analysis and Tableau dashboarding.

---

## 🚀 Key Highlights

| Metric | Value |
|--------|-------|
| 📦 Records Processed | ~4.9 million across 3 data silos |
| ✅ Data Accuracy | 100% maintained via pre-merge aggregation |
| 🔴 High-Strain Pincode Identified | 501158 (Telangana) — flagged for immediate audit |
| 📉 Minimum Efficiency Found | ~1.7% in specific Telangana & Tamil Nadu pincodes |
| 📈 Seasonal Spike | 15–20% activity surge between May–July |

---

## 📂 Project Structure

```
uidai_hackathon_2026/
├── data/
│   ├── raw/                        # Original UIDAI CSVs (Git Ignored)
│   └── processed/                  # Cleaned & Master datasets
│
├── notebooks/                      # Step-by-step Jupyter Workflows
│   ├── 00_data_quality.ipynb       # Null checks, dtype audits, anomaly flags
│   ├── 01_eda.ipynb                # Exploratory Data Analysis
│   ├── 02_feature_eng_and_merge.ipynb  # Pre-merge aggregation & master join
│   ├── 03_analysis.ipynb           # Bottleneck & efficiency analysis
│   └── 04_visualizations.ipynb     # Chart generation & export
│
├── reports/
│   ├── figures/                    # Exported Python visualizations (.png / .svg)
│   └── findings.md                 # Detailed phase-by-phase analytical insights
│
├── src/                            # Production-grade Python scripts
│   ├── config.py                   # State mappings, path variables & constants
│   └── utils.py                    # Reusable preprocessing & helper functions
│
└── README.md
```

---

## 🛠️ Technical Stack

| Category | Tools |
|----------|-------|
| **Language** | Python 3.10+ |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Dashboarding** | Tableau Public (Phase 6) |
| **Notebook Environment** | Jupyter Lab / Notebook |
| **Version Control** | Git & GitHub |

---

## 🔄 Pipeline Workflow

```
Raw CSVs (3 silos)
        │
        ▼
[ 00 ] Data Quality Audit
        │  Null detection, dtype fixes, outlier flagging
        ▼
[ 01 ] Exploratory Data Analysis
        │  Distributions, correlations, state-level summaries
        ▼
[ 02 ] Feature Engineering & Master Merge
        │  Pre-merge aggregation → eliminates Cartesian product errors
        │  Produces: master_dataset.csv
        ▼
[ 03 ] Operational Analysis
        │  Efficiency scoring, bottleneck pincode detection
        │  Biometric Desert mapping
        ▼
[ 04 ] Visualizations & Reporting
        │  Heatmaps, time-series plots, pincode drill-downs
        ▼
[ 05 ] Tableau Dashboard (Phase 6)
```

---

## 📈 Key Findings

### 1. 🏜️ Biometric Desert — Infrastructure Gap

States like **Uttar Pradesh** exhibit a pronounced **biometric lag**, where authentication demand significantly outpaces available scanning infrastructure. These regions are classified as *Biometric Deserts* — areas where citizens face disproportionately high failure or wait rates due to hardware scarcity.

**Recommendation:** Prioritize mobile enrollment unit deployment and operator capacity expansion in high-lag districts.

---

### 2. 📅 Seasonal Demand Surge (May–July)

A consistent **15–20% spike** in Aadhaar authentication activity is observed between May and July each year, strongly correlated with:
- College & school admission cycles
- Government scholarship disbursements
- Agricultural subsidy renewals

**Recommendation:** Pre-position additional infrastructure and temporary operators at high-volume centers before May each year.

---

### 3. ⚙️ Efficiency Bottlenecks

Specific pincodes in **Telangana** and **Tamil Nadu** recorded efficiency rates as low as **~1.7%**, pointing to one or more of:

- 🔧 Hardware failures (biometric scanner degradation)
- 👤 Operator shortages or inadequate training
- 🔄 Process inefficiencies (queue management, network latency)

**Flagged Pincode for Immediate Audit:** `501158` (Telangana)

---

## ⚙️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/rnrahate/uidai_hackathon_2026.git
cd uidai_hackathon_2026
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Raw Data

Place the original UIDAI CSV files inside `data/raw/`. These files are `.gitignore`d and must be sourced separately.

### 5. Run Notebooks in Order

```bash
jupyter lab
```

Execute notebooks sequentially:

```
00_data_quality.ipynb  →  01_eda.ipynb  →  02_feature_eng_and_merge.ipynb  →  03_analysis.ipynb  →  04_visualizations.ipynb
```

---

## 📊 Results & Reports

- Processed master dataset → `data/processed/master_dataset.csv`
- All figures exported to → `reports/figures/`
- Phase-by-phase narrative insights → [`reports/findings.md`](reports/findings.md)
- Tableau dashboard → *(Coming in Phase 6 — link will be added here)*

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add: your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
  Built with 🔥 by <a href="https://github.com/rnrahate">Aryan Rahate</a> &nbsp;|&nbsp;
  <a href="https://linkedin.com/in/aryan-rahate">LinkedIn</a>
</div>