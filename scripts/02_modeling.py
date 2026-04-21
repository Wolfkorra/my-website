from pathlib import Path
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_validate, StratifiedKFold
from sklearn.linear_model import LogisticRegression

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "processed" / "telco_churn_clean.csv"
df = pd.read_csv(DATA_PATH)

X = df.drop(columns="Churn")
y = df["Churn"]

numeric_features = X.select_dtypes(include=["number"]).columns.tolist()
categorical_features = X.select_dtypes(exclude=["number"]).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
            ]),
            numeric_features,
        ),
        (
            "cat",
            Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ]),
            categorical_features,
        ),
    ]
)

model = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("model", LogisticRegression(max_iter=2000)),
    ]
)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=4025)
scores = cross_validate(
    model,
    X,
    y,
    cv=cv,
    scoring={"roc_auc": "roc_auc", "accuracy": "accuracy"},
    n_jobs=-1,
)

print("Mean ROC-AUC:", scores["test_roc_auc"].mean())
print("Mean accuracy:", scores["test_accuracy"].mean())
