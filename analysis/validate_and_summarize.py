"""Reproducible validation and summary analysis for the Power BI salary dashboard."""

from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "ds_salaries.csv"


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    required = {
        "work_year", "experience_level", "employment_type", "job_title",
        "salary", "salary_currency", "salary_in_usd", "employee_residence",
        "remote_ratio", "company_location", "company_size",
    }
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    print("DATA QUALITY CHECKS")
    print(f"Rows: {len(df):,}")
    print(f"Duplicate rows: {df.duplicated().sum():,}")
    print(f"Missing values: {int(df.isna().sum().sum()):,}")
    print(f"Years: {df['work_year'].min()}–{df['work_year'].max()}")
    print(f"Unique job titles: {df['job_title'].nunique():,}")
    print(f"Employee countries: {df['employee_residence'].nunique():,}")

    print("\nSALARY SUMMARY (USD)")
    print(df["salary_in_usd"].describe().round(0).to_string())

    exp_order = ["EN", "MI", "SE", "EX"]
    exp = (
        df.groupby("experience_level")["salary_in_usd"]
        .agg(records="size", median_salary="median", average_salary="mean")
        .reindex(exp_order)
        .round(0)
    )
    print("\nBY EXPERIENCE LEVEL")
    print(exp.to_string())

    remote = (
        df.groupby("remote_ratio")["salary_in_usd"]
        .agg(records="size", median_salary="median", average_salary="mean")
        .round(0)
    )
    print("\nBY REMOTE RATIO")
    print(remote.to_string())

    roles = (
        df.groupby("job_title")["salary_in_usd"]
        .agg(records="size", median_salary="median", average_salary="mean")
        .query("records >= 20")
        .sort_values("median_salary", ascending=False)
        .head(10)
        .round(0)
    )
    print("\nTOP ROLES BY MEDIAN SALARY (minimum 20 records)")
    print(roles.to_string())

    years = (
        df.groupby("work_year")["salary_in_usd"]
        .agg(records="size", median_salary="median", average_salary="mean")
        .round(0)
    )
    print("\nBY WORK YEAR")
    print(years.to_string())


if __name__ == "__main__":
    main()
