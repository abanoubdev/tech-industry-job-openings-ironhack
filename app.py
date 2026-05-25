import streamlit as st
import pandas as pd
import joblib
from pandas.api.types import is_numeric_dtype
import os

# Set page config
st.set_page_config(page_title="AI Risk Predictor", page_icon="🤖", layout="centered")

# Determine the absolute path to the directory where app.py lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load everything using absolute paths to prevent FileNotFoundError
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
    job_title = st.selectbox("Select Job Title", df['Job_Title'].sort_values().unique())
with col2:
    location = st.selectbox("Select Location", df['Location'].sort_values().unique())

st.write("---")

if st.button("Predict AI Impact Risk", type="primary"):
    
    subset = df[(df['Job_Title'] == job_title) & (df['Location'] == location)]
    if subset.empty:
        subset = df[df['Job_Title'] == job_title]

    input_data = {}
    
    # Extract median/mode for all features based on the filtered subset
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
        st.write("---")
        
        if prediction_text == 'High':
            risk_score = 90
        elif prediction_text == 'Moderate':
            risk_score = 50
        else:
            risk_score = 10

        st.metric(label="Predicted AI Automation Risk Level", value=prediction_text, delta=f"{risk_score}% Risk Score", delta_color="inverse")
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
                
        global_remote = df['Remote_Work_Ratio'].mean()
        job_remote = input_data['Remote_Work_Ratio']
        
        remote_df = pd.DataFrame({
            "Metric": ["Global Average", f"Your Role"],
            "Remote Work Ratio": [global_remote, job_remote]
        }).set_index("Metric")
            
        if job_remote > global_remote:
            remote_text = f"Your role has a **{job_remote:.0f}%** remote work ratio, which is higher than the global average of **{global_remote:.0f}%**. Because your work is highly digitized and done through a screen, it is structurally easier for an AI to learn and automate."
        else:
            remote_text = f"Your role has a **{job_remote:.0f}%** remote work ratio, which is lower than the global average of **{global_remote:.0f}%**. Roles that require physical presence are generally safer from AI."
            
        st.info(remote_text)
            
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
