# AI Impact on Jobs 2030 - Project Structure Plan

The goal of this project is to analyze, predict, and visualize the impact of Artificial Intelligence on various jobs by 2030. The final deliverables will be meaningful and actionable for end-users (e.g., professionals, students, and educators) who want to understand how to prepare for the future job market.

> [!TIP]
> 1. **Target Variable for ML**: Are you more interested in predicting the `AI Impact Level` (Classification task) or the exact number of `Projected Openings (2030)` (Regression task)? I recommend `AI Impact Level` as it often yields better storytelling.
> 2. **Dashboard Scope**: Do you already have a Tableau Public account set up for publishing the dashboard, or would you prefer to host it locally during the presentation?
> 3. **SQL Usage**: The data is currently in pandas. Do you want to export it to a SQLite/PostgreSQL database to demonstrate your SQL skills as part of the graduation requirements?

## Proposed Changes & Project Phases
Based on the merged dataset (`Job_Title`, `Industry`, `AI Impact Level`, `Median Salary`, `Skills`, etc.), here is the step-by-step structure will be followed:

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
- **Interpretability:** Use Feature Importance or SHAP values to explain *why* the model makes certain predictions.

### Phase 4: Dashboarding & Visualization (Tableau)
**Focus:** Creating an interactive, stunning UI for the end-user.
- Export the clean, modeled data to a CSV for Tableau.
- **Dashboard 1: "The State of the Market"**: Overview of current jobs, salaries, and remote work ratios by industry.
- **Dashboard 2: "The 2030 AI Outlook"**: Interactive tool where a user selects their `Industry` or `Job Title` and sees their `AI Impact Level`, projected openings, and which skills they need to learn to stay relevant.
- **Streamlit:** It will demonstrate having valid input from user ,this input can be `Job Title` or `Industry` field of Dream work and it should show the risk analysis and give some recommendations.

## Phase 5: Conclusion
- Write conclusions done 
