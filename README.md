# UKCS Oil Production Forecasting with Walk-Forward Machine Learning

**Level 2 — Intermediate Data-Science Portfolio Project**

An independent, reproducible forecasting project built from public NSTA/PPRS monthly production data. It uses leakage-safe lag and rolling features, a dedicated 2023 tuning window, a locked 24-month walk-forward evaluation, and a transparent 2026 uncertainty band.
## Author

**Dr Khaldoun Shaker**  
Petroleum & Reservoir Engineer | Energy Data Analytics  
Edinburgh, United Kingdom  

Built as an independent professional portfolio project to apply my petroleum
and reservoir engineering experience to energy-data problems using Python,
SQL and machine learning. I reviewed the engineering assumptions, analytical
workflow, results and limitations.

© 2026 Khaldoun Shaker. All rights reserved.
## Headline result

| Model | MAE (m³) | RMSE (m³) | MAPE |
|---|---:|---:|---:|
| **Random Forest** | **48,203.71** | 60,515.59 | 25.06% |
| Ridge | 48,951.61 | **56,731.40** | **24.50%** |
| Last value | 52,389.83 | 76,298.07 | 26.22% |
| Seasonal naive | 64,092.62 | 73,758.73 | 29.97% |

Random Forest is the MAE champion, improving on the last-value baseline by approximately 8%. Ridge remains competitive and performs better on RMSE and MAPE, so the result is reported as a trade-off rather than an absolute victory.

![Walk-forward model comparison](outputs/charts/02_walk_forward_predictions.png)

## Time-aware design

- **2021–2022:** initial history and supervised training examples
- **2023:** hyperparameter selection only
- **2024–2025:** locked expanding-window evaluation
- **2026:** recursive forecast after refitting on all available observations

Predictors include time, cyclical month encoding, lags 1/2/3/6/12, rolling means 3/6/12, and trailing six-month volatility. Every feature for month `t` uses information available before `t`.

## Repository structure

```text
.
├── data/
│   ├── raw/                         # Complete reproducible NSTA extract
│   └── processed/                   # Validated series and model features
├── docs/                            # Bilingual methodology and report
├── models/                          # Ridge, Random Forest, and metadata
├── outputs/
│   ├── charts/                      # Five portfolio-ready figures
│   └── tables/                      # Tuning, evaluation, forecast, drift
├── src/                             # Independent modular pipeline
├── tests/                           # Automated validation and leakage tests
├── DATA_SOURCE.md
├── MODEL_CARD.md
├── run_project.py
└── requirements.txt
```

## Run the full project

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run_project.py
python -m unittest discover -s tests -v
```

Expected champion: `random_forest`. Random seed 42 is fixed for reproducibility.

## Main outputs

- `data/processed/model_features.csv`
- `outputs/tables/hyperparameter_tuning_2023.csv`
- `outputs/tables/walk_forward_predictions_2024_2025.csv`
- `outputs/tables/model_metrics_2024_2025.csv`
- `outputs/tables/forecast_2026_with_interval.csv`
- `outputs/tables/random_forest_feature_importance.csv`
- `models/random_forest_final.joblib`
- `models/ridge_final.joblib`

## Responsible interpretation

The 2026 range is based on the empirical 90th percentile of prior absolute errors; it is not a formally calibrated probability interval. This portfolio model omits operational drivers and must not be used for reserves, engineering, safety, investment, or production-planning decisions. See [MODEL_CARD.md](MODEL_CARD.md).

---

## الملخص العربي

هذا هو **المشروع الثاني – المستوى الثاني (المتوسط)**. يبني 12 خاصية زمنية من البيانات السابقة فقط، ويستخدم سنة 2023 لاختيار إعدادات النماذج، ثم ينفذ 24 اختباراً متحركاً من يناير 2024 إلى ديسمبر 2025.

حققت Random Forest أفضل MAE، بينما حقق Ridge نتائج أفضل في RMSE وMAPE. يحتوي المشروع أيضاً على توقعات 2026 ونطاق خطأ تجريبي، وخمسة رسوم، ونموذجين محفوظين، وتقارير واختبارات كاملة. النتائج تعليمية ولا تمثل توقعاً هندسياً أو تجارياً.

