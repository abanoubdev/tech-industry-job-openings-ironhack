# AI Impact on Jobs 2030 - Project Structure Plan

The goal of this project is to analyze, predict, and visualize the impact of Artificial Intelligence on various jobs by 2030. The final deliverables will be meaningful and actionable for end-users (e.g., professionals, students, and educators) who want to understand how to prepare for the future job market.

## User Review Required

> [!IMPORTANT]
> Please review this proposed project structure. We can adjust the focus based on what you find most interesting or what you think will wow your Ironhack audience the most!

## Open Questions

> [!TIP]
> 1. **Target Variable for ML**: Are you more interested in predicting the `AI Impact Level` (Classification task) or the exact number of `Projected Openings (2030)` (Regression task)? I recommend `AI Impact Level` as it often yields better storytelling.
> 2. **Dashboard Scope**: Do you already have a Tableau Public account set up for publishing the dashboard, or would you prefer to host it locally during the presentation?
> 3. **SQL Usage**: The data is currently in pandas. Do you want to export it to a SQLite/PostgreSQL database to demonstrate your SQL skills as part of the graduation requirements?

## Proposed Changes & Project Phases

Based on the merged dataset (`Job_Title`, `Industry`, `AI Impact Level`, `Median Salary`, `Skills`, etc.), here is the step-by-step structure we will follow:

### Phase 1: Exploratory Data Analysis (EDA) & Data Cleaning
**Focus:** Understanding the data and finding initial trends.
- **Data Cleaning:** Handle any missing values or anomalies in the merged dataset.
- **Univariate Analysis:** Look at the distribution of salaries, remote work ratios, and job openings.
- **Bivariate Analysis:** 
  - How does `AI Impact Level` vary across different `Industries`?
  - Is there a correlation between `Median Salary` and `AI Impact Level`?
  - What are the top skills associated with jobs that have a "High" AI Impact?

### Phase 2: Feature Engineering & Preprocessing
**Focus:** Preparing data for Machine Learning.
- **Create New Features:** For example, `Job_Growth` = `Projected Openings (2030)` - `Job Openings (2024)`.
- **Encoding Categorical Variables:** Convert `Industry`, `Required Education`, and `Job_Title` into numerical formats suitable for modeling (e.g., One-Hot Encoding, Label Encoding).
- **Scaling:** Standardize numerical features like `Median Salary` and `Experience Required`.

### Phase 3: Machine Learning Modeling
**Focus:** Predicting which jobs will be most impacted by AI.
- **Model Selection:** Train Classification models (e.g., Random Forest, XGBoost, Logistic Regression) to predict the `AI Impact Level`.
- **Model Evaluation:** Use metrics like Accuracy, Precision, Recall, and F1-Score.
- **Interpretability (Crucial for audiences!):** Use Feature Importance or SHAP values to explain *why* the model makes certain predictions. For example, "Jobs requiring Skill_4 and Bachelor's degrees have a 70% higher chance of being highly impacted by AI."

### Phase 4: Dashboarding & Visualization (Tableau)
**Focus:** Creating an interactive, stunning UI for the end-user.
- Export the clean, modeled data to a CSV for Tableau.
- **Dashboard 1: "The State of the Market"**: Overview of current jobs, salaries, and remote work ratios by industry.
- **Dashboard 2: "The 2030 AI Outlook"**: Interactive tool where a user selects their `Industry` or `Job Title` and sees their `AI Impact Level`, projected openings, and which skills they need to learn to stay relevant.

### Phase 5: Storytelling & Final Presentation
**Focus:** Synthesizing the technical work into a compelling narrative for your graduation.
- Formulate 3-5 key actionable takeaways (e.g., "The future is remote and requires XYZ skills", or "Healthcare is the safest industry from AI replacement").

## Verification Plan

### Automated/Technical Verification
- Validate ML model performance using cross-validation to ensure it doesn't overfit.
- Verify data integrity after feature engineering (ensure no data leakage).

### Manual Verification
- Review the Tableau dashboard to ensure all filters and tooltips work correctly and the design is premium and user-friendly.
- Do a dry run of the insights to ensure they sound logical and impactful.
