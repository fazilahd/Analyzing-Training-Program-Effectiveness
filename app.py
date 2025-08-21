import streamlit as st
import pandas as pd
from PIL import Image

st.title("GTS Training Program Effectiveness Dashboard")

# Load data
employment = pd.read_csv("employment_by_training_program.csv")
cert_feedback = pd.read_csv("completion_certification_feedback.csv")
training_corr = pd.read_csv("training_feature_correlation.csv")
skill_completed = pd.read_csv("skill_ratings_completed.csv")

# Show key metrics
st.header("Key Metrics")
st.write("Top 5 Training Programs by Job Placements")
st.dataframe(employment.sort_values("n_placements", ascending=False).head(5))

# Show images/charts
st.header("Visualizations")

st.subheader("Placements by Program")
st.image("placements_by_program.png")

st.subheader("Median Salary by Program")
st.image("median_salary_by_program.png")

st.subheader("Median Time to Employment by Program")
st.image("median_time_to_employment_by_program.png")

st.subheader("Certification Rate (Popular Programs)")
st.image("certification_rate_popular_programs_5.png")

st.subheader("Skill Improvement (Line Chart)")
st.image("skill_improvement_linechart.png")

st.subheader("Correlation Heatmap")
st.image("correlation_heatmap.png")

st.subheader("Certification Rate by Content Area")
st.image("segmentation_cert_rate_content.png")

st.subheader("Certification Rate by Duration")
st.image("segmentation_cert_rate_duration.png")

st.subheader("Certification Rate by Training Type")
st.image("segmentation_cert_rate_type.png")

st.subheader("Average Salary by Content Area")
st.image("segmentation_salary_content.png")

st.subheader("Average Salary by Duration")
st.image("segmentation_salary_duration.png")

st.subheader("Average Salary by Training Type")
st.image("segmentation_salary_type.png")

st.subheader("Skill Ratings for Users Who Completed Training (Top 5 Skills)")
st.image("skill_ratings_completed_bar.png")

st.subheader("Skill Ratings for Users Who Did Not Complete Training (Top 5 Skills)")
st.image("skill_ratings_not_completed_bar.png")

st.subheader("Average Trainer Rating for Top 10 Training Programs (≥5 Enrollments)")
st.image("trainer_rating_popular_programs_5.png")

# Show data tables
st.header("Explore Data")
tab = st.selectbox("Choose a table to view:", [
    "Employment by Training Program",
    "Certification & Feedback",
    "Skill Ratings (Completed)"
])
if tab == "Employment by Training Program":
    st.dataframe(employment)
elif tab == "Certification & Feedback":
    st.dataframe(cert_feedback)
elif tab == "Skill Ratings (Completed)":
    st.dataframe(skill_completed)

st.write("For more analysis, see the full report.")