import streamlit as st

# Function to label condition based on Hemoglobin, WBC, and Platelet Count and provide interactive solutions
def label_diagnosis(gender, hemoglobin, wbc, platelets):
    if (gender == 'female' and hemoglobin < 12.0) or (gender == 'male' and hemoglobin < 13.8):
        return 'Fatigue (Low Hemoglobin)', "Consider increasing iron intake. Foods like spinach, lentils, and red meat are good sources of iron. Consult a healthcare provider if symptoms persist."
    elif wbc > 10000:
        return 'Infection (High WBC)', "A high WBC count may indicate an infection. Consult a healthcare provider for further testing and treatment."
    elif platelets < 150000:
        return 'Bleeding Risk (Low Platelets)', "Low platelet count may lead to bleeding issues. Seek medical advice for potential causes and treatments."
    elif platelets > 450000:
        return 'Bleeding Risk (High Platelets)', "High platelets can increase clotting risk. Consult a doctor to evaluate the cause and consider treatment options."
    return 'Normal', "CBC values are within the normal range. Maintain a healthy lifestyle and regular check-ups."

# Streamlit UI
def main():
    st.title("CBC Report Diagnosis")

    # User inputs for all CBC parameters
    gender = st.selectbox('Gender', ['male', 'female'])
    hemoglobin = st.number_input('Hemoglobin (g/dL)', min_value=0.0, max_value=30.0, value=13.0)
    wbc = st.number_input('White Blood Cells (cells/mcL)', min_value=0, max_value=30000, value=7000)
    platelets = st.number_input('Platelet Count (cells/mcL)', min_value=10000, max_value=1000000, value=250000)

    # Diagnosis button
    if st.button('Get Diagnosis'):
        # Store the diagnosis result in session_state to maintain state across reruns
        diagnosis, solution = label_diagnosis(gender, hemoglobin, wbc, platelets)
        st.session_state['diagnosis'] = diagnosis
        st.session_state['solution'] = solution

    # Check if a diagnosis is stored in session_state
    if 'diagnosis' in st.session_state:
        st.write(f"### Diagnosis: {st.session_state['diagnosis']}")
        st.write(f"### Suggested Solution: {st.session_state['solution']}")

        # Interactive follow-up questions based on diagnosis
        follow_up_question(st.session_state['diagnosis'])

# Follow-up questions based on the diagnosis
def follow_up_question(diagnosis):
    if diagnosis == 'Fatigue (Low Hemoglobin)':
        fatigue_symptoms = st.radio("Are you feeling unusually tired or weak?", ['Yes', 'No'], key='fatigue')
        if fatigue_symptoms == 'Yes':
            st.write("Consider iron-rich foods like spinach, lentils, and red meat. Iron supplements may also help. Consult a healthcare provider.")
        else:
            st.write("Try maintaining a diet rich in vitamins and minerals. Ensure adequate sleep and regular exercise to boost energy levels.")

    elif diagnosis == 'Infection (High WBC)':
        infection_symptoms = st.radio("Do you have symptoms like fever, chills, or body aches?", ['Yes', 'No'], key='infection')
        if infection_symptoms == 'Yes':
            st.write("High WBC count may indicate an infection. Visit a healthcare provider for diagnosis and treatment.")
        else:
            st.write("Stay hydrated, maintain good hygiene, and monitor for any future symptoms. Follow up with your doctor if needed.")

    elif diagnosis == 'Bleeding Risk (Low Platelets)':
        bleeding_symptoms = st.radio("Are you experiencing easy bruising, nosebleeds, or prolonged bleeding?", ['Yes', 'No'], key='low_platelets')
        if bleeding_symptoms == 'Yes':
            st.write("Low platelets can cause bleeding issues. Seek immediate medical advice for further testing.")
        else:
            st.write("Focus on a balanced diet with foods that support platelet production, like leafy greens, citrus fruits, and berries. Regular check-ups are recommended.")

    elif diagnosis == 'Bleeding Risk (High Platelets)':
        clotting_symptoms = st.radio("Are you experiencing unusual clotting, swelling, or pain in your limbs?", ['Yes', 'No'], key='high_platelets')
        if clotting_symptoms == 'Yes':
            st.write("High platelets may increase the risk of clotting. Consult a healthcare provider for proper evaluation and potential treatment.")
        else:
            st.write("Maintain an active lifestyle, stay hydrated, and avoid smoking. Regular blood tests can help monitor platelet levels.")

    elif diagnosis == 'Normal':
        st.write("You're in good health! Keep up with a healthy lifestyle, balanced diet, and regular health monitoring.")

# Run the app
if __name__ == "__main__":
    main()
