import streamlit as st
import numpy as np
import plotly.express as px

def generate_gaussian_mode(mean, variance, num_of_samples):
    cov_matirx = [[variance, 0], [0, variance]]
    samples = np.random.multivariate_normal(mean, cov_matirx, num_of_samples)
    return samples

def generate_class_data(num_of_modes, samples_per_mode):
    all_samples = []
    for _ in range(num_of_modes):
        mean = np.random.uniform(-5, 5, 2) # center
        variance = np.random.uniform(0.05, 0.2) # spread
        samples = generate_gaussian_mode(mean, variance, samples_per_mode)
        all_samples.append(samples)
    return np.vstack(all_samples)

st.title("Gaussian Data Generator and Visualiser")

st.sidebar.header("Settings")
num_of_modes_class_0 = st.sidebar.number_input("Number of Modes for Class 0", min_value=1, max_value=10, value=1)
num_of_modes_class_1 = st.sidebar.number_input("Number of Modes for Class 1", min_value=1, max_value=10, value=1)
samples_per_mode = st.sidebar.number_input("Number of Samples per Mode", min_value=10, max_value=1000, value=100)

if st.sidebar.button("Generate Data"):
    class_0_data = generate_class_data(num_of_modes_class_0, samples_per_mode)
    class_1_data = generate_class_data(num_of_modes_class_1, samples_per_mode)

    class_0_df = {"x": class_0_data[:,0], "y": class_0_data[:,1], "class": "Class 0"}
    class_1_df = {"x": class_1_data[:,0], "y": class_1_data[:,1], "class": "Class 1"}

    import pandas as pd
    data_df = pd.DataFrame(class_0_df)._append(pd.DataFrame(class_1_df))

    fig = px.scatter(data_df, x="x", y="y", color="class", title="Generated Gaussian Data")
    st.plotly_chart(fig)

