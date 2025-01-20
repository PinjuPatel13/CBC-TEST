import streamlit as st

# Function to analyze and diagnose based on CBC values
def label_diagnosis(gender, hemoglobin, wbc, platelets):
    # Results dictionary to hold outputs for each parameter
    results = {
        'Hemoglobin': None,
        'WBC': None,
        'Platelets': None
    }
    
    # Hemoglobin analysis
    if (gender == 'female' and hemoglobin < 12.0):
        results['Hemoglobin'] = ('Fatigue (Low Hemoglobin)', "Increase iron intake. Include foods like spinach, lentils, and red meat. Consult a healthcare provider if symptoms persist.")
    elif (gender == 'male' and hemoglobin < 13.8):
        results['Hemoglobin'] = ('Fatigue (Low Hemoglobin)', "Increase iron intake. Include foods like spinach, lentils, and red meat. Consult a healthcare provider if symptoms persist.")
    elif (gender == 'female' and hemoglobin > 15.5) or (gender == 'male' and hemoglobin > 17.5):
        results['Hemoglobin'] = ('High Hemoglobin', "High hemoglobin may be due to dehydration, smoking, or other health issues. Consult a doctor for evaluation.")
    
    # WBC analysis
    if wbc <= 0:
        results['WBC'] = ('Invalid Input', "WBC count cannot be zero or less. Please provide a valid value.")
    elif wbc > 10000:
        results['WBC'] = ('Infection (High WBC)', "High WBC count may indicate an infection. Consult a healthcare provider for further testing.")
    elif wbc < 4000:
        results['WBC'] = ('Low WBC Count', "Low WBC count may indicate immune suppression. Seek medical advice for further evaluation.")
    
    # Platelet analysis
    if platelets <= 0:
        results['Platelets'] = ('Invalid Input', "Platelet count cannot be zero or less. Please provide a valid value.")
    elif platelets < 150000:
        results['Platelets'] = ('Bleeding Risk (Low Platelets)', "Low platelet count may lead to bleeding issues. Seek medical advice for potential causes and treatments.")
    elif platelets > 450000:
        results['Platelets'] = ('Bleeding Risk (High Platelets)', "High platelet count can increase clotting risk. Consult a doctor to evaluate the cause and consider treatment options.")
    
    return results

# Streamlit UI
def main():
    st.title("CBC Report Diagnosis")

    # User inputs for all CBC parameters
    gender = st.selectbox('Gender', ['male', 'female'])
    hemoglobin = st.number_input('Hemoglobin (g/dL)', min_value=0.0, max_value=30.0, value=13.0)
    wbc = st.number_input('White Blood Cells (cells/mcL)', min_value=0, max_value=30000, value=7000)
    platelets = st.number_input('Platelet Count (cells/mcL)', min_value=0, max_value=1000000, value=250000)

    # Diagnosis button
    if st.button('Get Diagnosis'):
        results = label_diagnosis(gender, hemoglobin, wbc, platelets)
        st.session_state['results'] = results

    # Display results
    if 'results' in st.session_state:
        st.write("### Diagnosis and Suggested Solutions:")
        results = st.session_state['results']
        
        # Flag to check if all parameters are normal
        all_normal = True
        
        # Display results for each parameter
        if results['Hemoglobin']:
            diagnosis, solution = results['Hemoglobin']
            st.write(f"**Hemoglobin Diagnosis:** {diagnosis}")
            st.write(f"**Suggested Solution:** {solution}")
            all_normal = False
        if results['WBC']:
            diagnosis, solution = results['WBC']
            st.write(f"**WBC Diagnosis:** {diagnosis}")
            st.write(f"**Suggested Solution:** {solution}")
            all_normal = False
        if results['Platelets']:
            diagnosis, solution = results['Platelets']
            st.write(f"**Platelets Diagnosis:** {diagnosis}")
            st.write(f"**Suggested Solution:** {solution}")
            all_normal = False
        
        # If all parameters are normal
        if all_normal:
            st.write("### Diagnosis: Normal")
            st.write("Your CBC report is within the normal range. Keep up with a healthy lifestyle, balanced diet, and regular health monitoring.")

# Run the app
if __name__ == "__main__":
    main()
