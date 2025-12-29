# Demo Script – Feeder Demand Forecasting & Peak Load Detection

This demo script provides a clear, interview-ready walkthrough of the project.
It is aligned with:
- The three Jupyter notebooks
- The refactored `src/` modules
- The saved outputs in `outputs/plots` and `outputs/metrics`

---

## 🎯 Demo Objective (30–60 seconds)

> “This project demonstrates how short-term electricity demand can be forecasted
> and how abnormal peak loads can be detected in distribution systems using
> real-world utility data.”

---

## 1️⃣ Dataset & Problem Context (1 minute)

- **Dataset**: Short-term Electricity Load Forecasting (Panama)
- **Resolution**: Hourly
- **Target variable**: National electricity demand (`nat_demand` / `DEMAND`)
- **Assumption**: National demand is used as a proxy for feeder-level load due to data confidentiality

Explain briefly:
- Weather drivers: temperature, humidity, wind speed, precipitation
- Calendar drivers: holidays and school periods
- Real-world motivation: overload prevention, short-term dispatch, demand response

---

## 2️⃣ Exploratory Data Analysis (Notebook 01) – 1 minute

Open: `notebooks/01_eda_and_peak_analysis.ipynb`

Explain:
- Daily and weekly load patterns
- Hour-of-day demand behavior
- Impact of holidays and school periods
- Statistical peak definition using the 95th percentile

Show saved plots:
- `outputs/plots/hourly_load_profile.png`
- `outputs/plots/average_hourly_demand.png`
- `outputs/plots/peak_load_visualization.png`

Key takeaway:
> “The data shows strong seasonality and calendar-driven effects,
> which validates the use of lagged, weather, and calendar features.”

---

## 3️⃣ Short-Term Load Forecasting (Notebook 02) – 2 minutes

Open: `notebooks/02_forecasting_model.ipynb`

Explain:
- Use of official dataset-provided rolling train–test splits
- Feature set:
  - Weekly demand lags
  - Moving averages
  - Calendar indicators
  - Weather variables
- Model choice: Gradient Boosting Regressor

Show:
- Forecast vs actual plot from `outputs/plots/forecast_vs_actual.png`
- Metrics from `outputs/metrics/forecast_metrics.csv`

Mention:
- MAE and RMSE as evaluation metrics
- Suitability for 24–72 hour operational forecasting

---

## 4️⃣ Peak Load & Anomaly Detection (Notebook 03) – 1 minute

Open: `notebooks/03_peak_detection.ipynb`

Explain:
- Residual-based detection logic:
  - Residual = Actual demand − Forecasted demand
- Peaks identified as extreme positive residuals (95th percentile)

Show:
- `outputs/plots/detected_peaks.png`
- `outputs/metrics/peak_detection_summary.csv`

Key takeaway:
> “This approach detects abnormal demand events that deviate from expected
> behavior and can act as early warnings for feeder overload risk.”

---

## 5️⃣ Modular Code Structure (`src/`) – 1 minute

Briefly show the `src/` folder:

- `data_loader.py` – dataset loading utilities
- `model.py` – forecasting model definition and training
- `evaluation.py` – MAE and RMSE metrics
- `peak_detection.py` – residual-based peak detection
- `feature_checks.py` – EDA support functions

Emphasize:
> “The logic is modular and reusable, similar to production ML pipelines.”

---

## 6️⃣ Closing Summary (30 seconds)

> “This project combines time-series forecasting and anomaly detection to solve
> a real operational problem faced by distribution utilities.
> The same pipeline can be directly applied to feeder-level monitoring.”

Optional mention:
- Future extensions: LSTM models, probabilistic forecasting, feeder-wise deployment

---

## ⏱️ Total Demo Time
**~7 minutes** (ideal for interviews and portfolio walkthroughs)
