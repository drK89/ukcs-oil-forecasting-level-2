# Model Card | بطاقة النموذج

## Intended purpose

An intermediate portfolio forecasting system that demonstrates leakage-safe feature engineering, separate hyperparameter tuning, expanding-window evaluation, reproducible model persistence, and uncertainty communication for monthly UKCS production data.

## Inputs and engineered features

The models use only information available before each predicted month: time index, cyclical month encodings, lags 1/2/3/6/12, rolling means over 3/6/12 months, and a trailing six-month standard deviation.

## Development design

- 2021–2022: initial history and supervised training rows
- 2023: walk-forward hyperparameter tuning only
- 2024–2025: locked 24-month walk-forward evaluation
- 2026: recursive portfolio forecast after refitting on all available observations

The final comparison includes last-value, seasonal-naive, tuned Ridge, and tuned Random Forest models. Random seed 42 is fixed.

## Results

Random Forest ranked first by MAE at **48,203.71 m³**, narrowly ahead of Ridge at **48,951.61 m³** and ahead of last value at **52,389.83 m³**. The result should be treated cautiously because the series is small and volatile.

## Uncertainty

The 2026 band adds and subtracts the empirical 90th percentile of the champion model's 2024–2025 absolute walk-forward errors (**106,918.42 m³**). It is a transparent error band, not a formally calibrated probabilistic prediction interval.

## Limitations and prohibited use

- One field and only 60 monthly observations
- Recursive multi-step errors can accumulate
- No operational, well, maintenance, pressure, weather, price, or intervention variables
- Impurity-based feature importance is descriptive and not causal
- Not for reserves, investment, production planning, safety, or engineering decisions

## العربية

هذا نموذج متوسط المستوى يطبق خصائص زمنية لا تستخدم المستقبل، وضبط إعدادات منفصل على 2023، واختباراً متحركاً على 2024–2025. فازت Random Forest بفارق محدود، ولذلك لا يجوز المبالغة في النتيجة. نطاق 2026 هو نطاق خطأ تجريبي للتوضيح وليس ضماناً إحصائياً أو توقعاً هندسياً.

