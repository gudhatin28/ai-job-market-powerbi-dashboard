# AI & Data Science Salary Intelligence Dashboard

**Power BI case study | 3,755 real-world salary records | 2020–2023**

An end-to-end business intelligence project that turns public AI, ML, and Data Science salary submissions into an interactive compensation analysis. The project focuses on the questions an analyst would need to answer before making claims about pay, experience, geography, remote work, and role representation.

![Dashboard overview](overview.png)

## Executive Summary

This project demonstrates more than dashboard formatting. It shows the workflow behind an analyst deliverable: understanding the source, defining fields, checking data quality, choosing defensible metrics, building interactive Power BI views, and documenting limitations so the results are not overstated.

The dataset contains **3,755 anonymous salary records from 2020–2023**. Because these are self-reported salary observations rather than a census of job postings, record counts are treated as **dataset representation**, not market-wide job demand.

## Business Questions

1. How does compensation differ across experience levels?
2. Which roles show the strongest salary levels in the available sample?
3. How do on-site, hybrid, and fully remote records compare?
4. How does compensation vary by company size?
5. How are salary observations distributed geographically?
6. How did salary patterns and role representation change from 2020–2023?

## Analytical Approach

**1. Source assessment** — Reviewed the dataset structure, salary fields, categorical codes, geography fields, and reporting period.

**2. Data preparation** — Used standardized USD salary (`salary_in_usd`) for cross-currency comparisons and interpreted coded fields for experience level, employment type, remote ratio, and company size.

**3. Data validation** — Added a reproducible Python validation script that checks required columns, row counts, duplicate rows, missing values, year coverage, category coverage, and salary summaries.

**4. Analysis** — Compared compensation by experience, role, work arrangement, company size, year, and geography. For role-level salary ranking, the reproducible analysis applies a minimum-record threshold to reduce misleading conclusions from very small groups.

**5. Visualization** — Built three Power BI pages for executive overview, salary analysis, and global/work-arrangement trends.

**6. Interpretation** — Documented the limits of self-reported salary data and avoided treating record frequency as official labor-market demand.

## Dashboard

### 1. Job Market Overview
High-level view of salary observations, average compensation, role representation, and experience-level patterns.

![Job Market Overview](overview.png)

### 2. Salary Analysis
Role, experience, company-size, and salary-distribution analysis designed for compensation comparison.

![Salary Analysis](Salary_Analysis.png)

### 3. Global Trends
Geographic, remote-work, and year-over-year views of the available salary observations.

![Global Trends](Global_Trends.png)

## Reproducible Validation

The Power BI file is the primary deliverable, but the repository also includes a lightweight Python analysis so reviewers can inspect the data logic without opening Power BI.

Run:

```bash
pip install -r requirements.txt
python analysis/validate_and_summarize.py
```

The script reports:

- dataset size, duplicate count, and missing-value count
- year and geographic coverage
- salary distribution in USD
- salary summaries by experience level and remote-work ratio
- role-level salary rankings with a minimum sample-size rule
- annual salary summaries

## Repository Structure

```text
ai-job-market-powerbi-dashboard/
├── AI_Data_Science_Salary_Dashboard.pbix   # Power BI report
├── ds_salaries.csv                         # analysis dataset
├── overview.png                            # dashboard preview
├── Salary_Analysis.png                     # dashboard preview
├── Global_Trends.png                       # dashboard preview
├── DATA_DICTIONARY.md                      # field definitions + interpretation notes
├── requirements.txt                        # Python dependency
└── analysis/
    └── validate_and_summarize.py            # reproducible validation + summary analysis
```

## Dataset

**Source:** aijobs.net Global AI/ML/Data Science Salary Index  
**Source repository:** https://github.com/foorilla/ai-jobs-net-salaries  
**License:** CC0 / Public Domain  
**Records used:** 3,755  
**Period:** 2020–2023

Key fields include `work_year`, `experience_level`, `employment_type`, `job_title`, `salary_in_usd`, `employee_residence`, `remote_ratio`, `company_location`, and `company_size`.

See [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) for definitions and interpretation notes.

## Tools & Skills Demonstrated

**Power BI** — dashboard design, interactive analysis, KPI presentation, visual storytelling  
**Python / pandas** — data validation, grouped analysis, reproducible checks  
**Data Analysis** — salary comparison, segmentation, descriptive statistics, sample-size awareness  
**Business Intelligence** — question framing, metric interpretation, executive-facing reporting  
**Data Communication** — documentation, limitations, and defensible conclusions

## Data Limitations

The salary submissions are anonymous and self-reported. They may contain selection bias and do not represent every AI/Data Science professional or employer. Differences between groups should therefore be interpreted as patterns in this dataset, not causal effects or definitive market benchmarks. Counts by job title represent observations in the sample and should not be described as official job demand.

---

**Portfolio focus:** Business Intelligence · Data Analysis · Power BI · Python · Data Visualization
