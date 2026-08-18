# Data Dictionary

This project uses the `ds_salaries.csv` dataset.

| Field | Meaning |
|---|---|
| `work_year` | Year the salary was reported |
| `experience_level` | Career level: EN = Entry-level, MI = Mid-level, SE = Senior-level, EX = Executive-level |
| `employment_type` | FT = Full-time, PT = Part-time, CT = Contract, FL = Freelance |
| `job_title` | Reported job title |
| `salary` | Reported gross salary in the original currency |
| `salary_currency` | ISO currency code for the original salary |
| `salary_in_usd` | Salary converted to U.S. dollars for comparison |
| `employee_residence` | Country of employee residence |
| `remote_ratio` | Share of remote work: 0 = on-site, 50 = hybrid, 100 = fully remote |
| `company_location` | Country where the employer is located |
| `company_size` | Company size: S = Small, M = Medium, L = Large |

## Interpretation notes

- Salary entries are anonymous and self-reported.
- The dataset should be used to study patterns in the available sample, not to claim a complete picture of the global labor market.
- `salary_in_usd` is the primary field used for cross-country salary comparisons.
- Counts by `job_title` represent records in the dataset, not official market-wide job demand.
