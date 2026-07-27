import numpy as np
import pandas as pd

df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

df_clean = df.drop(columns=["EmployeeCount", "StandardHours", "Over18"])
df_clean["Attrition_Flag"] = df_clean["Attrition"].apply(
    lambda x: 1 if x == "Yes" else 0
)

role_medians = df_clean.groupby("JobRole")["MonthlyIncome"].transform("median")
df_clean["Comp_Parity_Index"] = (
    df_clean["MonthlyIncome"] / role_medians
).round(2)

df_clean["Risk_Overtime"] = df_clean["OverTime"].apply(
    lambda x: 30 if x == "Yes" else 0
)
df_clean["Risk_Satisfaction"] = df_clean["JobSatisfaction"].apply(
    lambda x: 20 if x <= 2 else 0
)
df_clean["Risk_Promotion"] = df_clean["YearsSinceLastPromotion"].apply(
    lambda x: 20 if x >= 3 else 0
)
df_clean["Risk_Pay"] = df_clean["Comp_Parity_Index"].apply(
    lambda x: 30 if x < 0.9 else 0
)

df_clean["Flight_Risk_Score"] = (
    df_clean["Risk_Overtime"]
    + df_clean["Risk_Satisfaction"]
    + df_clean["Risk_Promotion"]
    + df_clean["Risk_Pay"]
)

df_final = df_clean.drop(
    columns=[
        "Risk_Overtime",
        "Risk_Satisfaction",
        "Risk_Promotion",
        "Risk_Pay",
    ]
)

df_final.to_csv("data/Enterprise_Talent_Intelligence.csv", index=False)

print(
    "Success! Processed dataset generated at: data/Enterprise_Talent_Intelligence.csv"
)
