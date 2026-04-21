from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
LOCAL_PATH = DATA_DIR / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
REMOTE_URL = "https://raw.githubusercontent.com/treselle-systems/customer_churn_analysis/master/WA_Fn-UseC_-Telco-Customer-Churn.csv"

if LOCAL_PATH.exists():
    df = pd.read_csv(LOCAL_PATH)
else:
    df = pd.read_csv(REMOTE_URL)

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.drop(columns=["customerID"]).dropna()
df["Churn"] = (df["Churn"] == "Yes").astype(int)

out_dir = Path(__file__).resolve().parents[1] / "data" / "processed"
out_dir.mkdir(parents=True, exist_ok=True)
df.to_csv(out_dir / "telco_churn_clean.csv", index=False)

print("Saved cleaned data to", out_dir / "telco_churn_clean.csv")
