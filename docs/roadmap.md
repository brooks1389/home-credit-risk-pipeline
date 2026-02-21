# Home Credit Risk Modeling Pipeline

## Goal
Build a production-style credit risk modeling pipeline using the Home Credit Kaggle dataset, ending with a deployed Streamlit policy simulator.

Time budget: ~10 hours/week  
Target duration: 12 weeks

---

## Final Deliverables
1) Public GitHub repo with reproducible pipeline, documentation, and model card  
2) Public Streamlit app that:
   - trains/loads a model
   - lets users adjust PD threshold
   - shows approval rate, default rate among approved, expected loss
   - shows SHAP-based explanations (summary + one example applicant)

---

## Week-by-week roadmap

### Weeks 1–2: Foundation + Baseline
**Build**
- Project skeleton and environment
- Load `application_train.csv`
- Baseline Logistic Regression
- LightGBM model
- Evaluation: ROC + AUC + calibration

**Definition of done**
- `python -m src.train` runs end-to-end and outputs metrics.

---

### Weeks 3–5: Multi-table feature engineering
Add one table per week (aggregate to applicant level, merge back, retrain, measure lift):
- Week 3: `bureau.csv` (+ `bureau_balance.csv` optional)
- Week 4: `previous_application.csv`
- Week 5: `installments_payments.csv`

**Definition of done**
- Modular feature builders exist under `src/features/`
- Model trains on merged features and metrics are logged.

---

### Weeks 6–7: Model maturity + explainability
**Build**
- Light hyperparameter tuning (small grid)
- Feature importance review + leakage checks
- SHAP summary plot + basic per-applicant explanation
- Stability check across folds

**Definition of done**
- A short `docs/model_report.md` explaining top drivers and caveats.

---

### Weeks 8–9: Policy simulator (product layer)
**Build**
- Policy simulation function:
  - approval rate at threshold
  - default rate among approved
  - expected loss using fixed LGD/EAD defaults
- Streamlit MVP UI with threshold slider + charts

**Definition of done**
- Local Streamlit app works and updates metrics interactively.

---

### Weeks 10–12: Deployment + polish
**Build**
- Streamlit app deployed publicly
- README rewritten with setup + run instructions
- Architecture diagram + model card (limitations, ethics, leakage risks)

**Definition of done**
- Public URL + clean repo that someone else can run.