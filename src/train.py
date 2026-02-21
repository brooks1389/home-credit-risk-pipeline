import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score


def main():
    print("Loading data...")

    df = pd.read_csv("data/application_train.csv")

    print("Data shape:", df.shape)

    # Drop rows with missing target
    df = df.dropna(subset=["TARGET"])

    # Simple numeric feature selection
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    numeric_cols.remove("TARGET")

    X = df[numeric_cols].fillna(0)
    y = df["TARGET"]

    print("Splitting data...")
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training logistic regression...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    preds = model.predict_proba(X_val)[:, 1]
    auc = roc_auc_score(y_val, preds)

    print(f"Validation AUC: {auc:.4f}")


if __name__ == "__main__":
    main()