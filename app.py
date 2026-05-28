import streamlit as st
import pandas as pd
import joblib
from pandas.api.types import is_numeric_dtype
import os

st.set_page_config(page_title="AI Risk Predictor", page_icon="🤖", layout="centered")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_assets():
    model = joblib.load(os.path.join(BASE_DIR, 'DataSet/model/xgb_boosting_model.pkl'))
    encoders = joblib.load(os.path.join(BASE_DIR, 'DataSet/Encoder/label_encoders.pkl'))
    scaler = joblib.load(os.path.join(BASE_DIR, 'DataSet/Scaler/scaler.pkl'))
    df = pd.read_csv(os.path.join(BASE_DIR, 'DataSet/cleaned_job_data.csv'))
    return model, encoders, scaler, df

try:
    model, encoders, scaler, df = load_assets()
except Exception as e:
    st.error(f"Error loading model assets. Error: {e}")
    st.stop()

st.title("🤖 Tech Industry AI Risk Predictor")
st.markdown("Select a **Job Title** and **Location** below. Our Machine Learning model will predict how likely this role is to be impacted by AI by the year 2030.")

col1, col2 = st.columns(2)
with col1:
    tech_jobs = df[~df['Job_Title'].str.contains('Lawyer', case=False, na=False)]['Job_Title'].sort_values().unique()
    job_title = st.selectbox("Select Job Title", tech_jobs)
with col2:
    location = st.selectbox("Select Location", df['Location'].sort_values().unique())

st.write("---")

if st.button("Predict AI Impact Risk", type="primary"):
    
    subset = df[(df['Job_Title'] == job_title) & (df['Location'] == location)]
    if subset.empty:
        subset = df[df['Job_Title'] == job_title]

    input_data = {}
    for col in df.columns:
        if col == 'AI_Impact_Level': 
            continue
        if is_numeric_dtype(df[col]):
            input_data[col] = subset[col].median()
        else:
            input_data[col] = subset[col].mode()[0]
            
    input_data['Job_Title'] = job_title
    input_data['Location'] = location
    
    input_df = pd.DataFrame([input_data])
    
    for col in encoders.keys():
        if col in input_df.columns and col != 'AI_Impact_Level':
            le = encoders[col]
            if input_df[col].iloc[0] in le.classes_:
                input_df[col] = le.transform(input_df[col])
            else:
                input_df[col] = 0 
                
    scale_cols = scaler.feature_names_in_
    input_df[scale_cols] = scaler.transform(input_df[scale_cols])
    
    try:
        model_input = input_df[model.feature_names_in_]
        prediction_num = model.predict(model_input)[0]
        prediction_text = encoders['AI_Impact_Level'].inverse_transform([prediction_num])[0]
        
        st.subheader("Prediction Result:")
        # Determine numerical score and dynamic color for the visual progress bar
        if prediction_text == 'High':
            risk_score = 90
            d_color = "inverse" # Streamlit 'inverse' makes positive numbers Red
        elif prediction_text == 'Moderate':
            risk_score = 50
            d_color = "off"     # Streamlit 'off' makes the text Gray
        else:
            risk_score = 10
            d_color = "normal"  # Streamlit 'normal' makes positive numbers Green

        st.metric(label="Predicted AI Automation Risk Level", value=prediction_text, delta=f"{risk_score}% Risk Score", delta_color=d_color)
        st.progress(risk_score)
        
        if prediction_text == 'High':
            st.error(f"🚨 **High Risk of AI Disruption**")
            st.warning("**Actionable Recommendation:** Upskill in AI tools immediately. Pivot to roles requiring high human empathy, strategic decision-making, or complex physical manipulation.")
        elif prediction_text == 'Moderate':
            st.warning(f"⚠️ **Moderate AI Impact**")
            st.info("**Actionable Recommendation:** Learn to use AI as a 'Copilot'. Your job will change significantly, but you will not be replaced if you adapt your workflows.")
        else:
            st.success(f"✅ **Low AI Impact (Highly Secure)**")
            st.success("**Actionable Recommendation:** Your role is structurally secure from automation. Continue focusing on the deeply human aspects of your job (leadership, creativity, strategy).")
                
        # --- Meaningful Analytics Charts ---
        st.write("---")
        st.subheader("📊 Why did you get this score?")
        st.markdown("We compared your specific role against the global tech industry averages to see exactly why the Machine Learning model flagged it.")
        
        col_chart1, col_chart2 = st.columns(2)
        
        global_remote = df['Remote_Work_Ratio'].mean()
        job_remote = input_data['Remote_Work_Ratio']
        
        remote_df = pd.DataFrame({
            "Metric": ["Global Average", "Your Role"],
            "Remote Work (%)": [global_remote, job_remote]
        }).set_index("Metric")
        
        with col_chart1:
            st.markdown("**Remote Work Vulnerability**")
            st.bar_chart(remote_df, color="#ff7f0e")

        global_salary = df['Median_Salary_(USD)'].mean()
        job_salary = input_data['Median_Salary_(USD)']
        
        salary_df = pd.DataFrame({
            "Metric": ["Global Average", "Your Role"],
            "Salary (USD)": [global_salary, job_salary]
        }).set_index("Metric")
        
        with col_chart2:
            st.markdown("**Financial Incentive to Automate**")
            st.bar_chart(salary_df, color="#1f77b4")
            
        # Dynamic Text that aligns with the AI's actual prediction
        if prediction_text == 'Low':
            if job_remote > global_remote:
                remote_text = f"Your role has a high remote work ratio (**{job_remote:.0f}%**), which usually increases AI risk. However, our model determined that the complex, deeply human requirements of your specific role completely override this vulnerability, keeping your job highly secure!"
            else:
                remote_text = f"Your role has a remote work ratio of **{job_remote:.0f}%**, which is lower than the global average. This requirement for physical presence is one of the key reasons our model marked your job as highly secure from AI!"
        elif prediction_text == 'High':
            if job_remote > global_remote:
                remote_text = f"Your role has a **{job_remote:.0f}%** remote work ratio, which is higher than the global average. Because your work is highly digitized and done through a screen, it is a massive factor in why our model flagged this role as High Risk."
            else:
                remote_text = f"Despite having a lower-than-average remote work ratio (**{job_remote:.0f}%**), our model flagged this role as High Risk due to other extreme vulnerabilities, such as the high financial incentive to automate it."
        else:
            # Moderate
            if job_remote > global_remote:
                remote_text = f"Your role has a **{job_remote:.0f}%** remote work ratio, which is higher than average. This digitization pushes your role into the Moderate Risk category, meaning you will likely need to adapt and use AI as a copilot."
            else:
                remote_text = f"Your remote work ratio is **{job_remote:.0f}%**. While your physical presence provides some security, other factors in the data pushed your role into Moderate Risk, meaning your daily workflows will still be heavily impacted by AI."
            
        st.info(remote_text)
            
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
