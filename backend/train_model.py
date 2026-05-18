import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
import joblib

df = pd.read_csv('churnx_dataset.csv')

# CLEANING
df = df[df['monthly_charges'] >= 0]
df = df[df['tenure_months'] < 120]

# FEATURES
X = df[['tenure_months','monthly_charges','support_tickets','last_login_days']]
y = df['churn'].map({'Yes': 1, 'No': 0})

# SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# MODEL
model = GradientBoostingClassifier(n_estimators=200)
model.fit(X_train, y_train)

# EVAL
preds = model.predict_proba(X_test)[:,1]
print("AUC:", roc_auc_score(y_test, preds))

# SAVE
joblib.dump(model, "model.pkl")