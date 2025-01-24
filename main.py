# import streamlit as st
# import re

# # Function to clean and normalize WBC input
# def normalize_wbc_input(value, unit="cells/μL"):
#     if isinstance(value, str):
#         value = value.strip()
#         value = re.sub(r'[^\d.]', '', value)
        
#         if value == '':
#             return None
    
#     try:
#         value = float(value)
        
#         if unit == "thousand cells/μL":
#             value = value * 1000
        
#         return value
#     except ValueError:
#         return None

# # Function to analyze and diagnose based on CBC values
# def label_diagnosis(gender, hemoglobin, wbc, platelets):
#     results = {
#         'Hemoglobin': None,
#         'WBC': None,
#         'Platelets': None
#     }
    
#     # Hemoglobin analysis
#     if gender == 'female':
#         if hemoglobin < 12.0:
#             results['Hemoglobin'] = ('Low Hemoglobin', "Increase iron intake. Include foods like spinach, lentils, and red meat. Consult a healthcare provider if symptoms persist.")
#         elif 12.0 <= hemoglobin <= 15.5:
#             results['Hemoglobin'] = None
#         else:
#             results['Hemoglobin'] = ('High Hemoglobin', "High hemoglobin may be due to dehydration, smoking, or other health issues. Consult a doctor for evaluation.")
#     elif gender == 'male':
#         if hemoglobin < 13.5:
#             results['Hemoglobin'] = ('Low Hemoglobin', "Increase iron intake. Include foods like spinach, lentils, and red meat. Consult a healthcare provider if symptoms persist.")
#         elif 13.5 <= hemoglobin <= 17.5:
#             results['Hemoglobin'] = None
#         else:
#             results['Hemoglobin'] = ('High Hemoglobin', "High hemoglobin may be due to dehydration, smoking, or other health issues. Consult a doctor for evaluation.")
    
#     # WBC analysis
#     if wbc is None or wbc <= 0:
#         results['WBC'] = ('Invalid Input', "WBC count cannot be zero or less. Please provide a valid value.")
#     elif wbc < 4.5:
#         results['WBC'] = ('Low WBC Count', "Low WBC count may indicate immune suppression. Seek medical advice for further evaluation.")
#     elif 4.5 <= wbc <= 11:
#         results['WBC'] = None
#     else:
#         results['WBC'] = ('High WBC Count', "High WBC count may indicate an infection. Consult a healthcare provider for further testing.")
    
#     # Platelet analysis
#     if platelets is None or platelets <= 0:
#         results['Platelets'] = ('Invalid Input', "Platelet count cannot be zero or less. Please provide a valid value.")
#     elif platelets < 150000:
#         results['Platelets'] = ('Low Platelets', "Low platelet count may lead to bleeding issues. Seek medical advice for potential causes and treatments.")
#     elif 150000 <= platelets <= 450000:
#         results['Platelets'] = None
#     else:
#         results['Platelets'] = ('High Platelets', "High platelet count can increase clotting risk. Consult a doctor to evaluate the cause and consider treatment options.")
    
#     return results

# # Function to extract parameters from the text file
# def extract_parameters_from_txt(txt_file):
#     parameters = {}

#     with open(txt_file, 'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             line = line.strip()
            
#             match = re.match(r"([a-zA-Z\s]+):\s*(\d+(\.\d+)?)(\s*(\w+))?", line)
            
#             if match:
#                 param = match.group(1).strip().lower()
#                 value = match.group(2)
#                 unit = match.group(5) if match.group(5) else "cells/μL"
                
#                 if param == "hemoglobin" or param == "hgb":
#                     parameters['Hemoglobin'] = float(value)
#                 elif param == "total wbc count" or param == "wbc count":
#                     parameters['WBC'] = normalize_wbc_input(value, unit)
#                 elif param == "platelet count":
#                     parameters['Platelet Count'] = float(value)
    
#     return parameters

# # Streamlit UI
# def main():
#     # Add title
#     st.title("CBC Test Report")  # Title added here

    
#     # File path for automatic reading
#     file_path = r"D:\User\Pinjal\Work\AI_Project\health-prediction-app\modal\found_parameters.txt"
    
#     # Read the file content automatically
#     with open(file_path, "r", encoding="utf-8") as file:
#         txt_content = file.read()
    
#     # Display the content from the predefined file
#     st.text(txt_content)
    
#     # Extract parameters from the file
#     parameters = extract_parameters_from_txt(file_path)
    
#     # Display extracted values
#     st.write("### Extracted Parameters")
#     st.write(parameters)
    
#     # User selects gender
#     gender = st.selectbox("Gender", ["male", "female"])
    
#     # Extract the values for each parameter
#     hemoglobin = parameters.get('Hemoglobin', 0)
#     wbc = parameters.get('WBC', None)
#     platelets = parameters.get('Platelet Count', 0)

#     if wbc is None:
#         st.error("Invalid WBC input. Please check your input format.")  
#         return
    
#     # Perform diagnosis with cleaned values
#     results = label_diagnosis(gender, hemoglobin, wbc, platelets)
    
#     # Check if all values are normal
#     all_normal = True
#     for key, value in results.items():
#         if value is not None:
#             all_normal = False
#             break
    
#     if all_normal:
#         st.success("Your CBC report is within the normal range. Keep up with a healthy lifestyle, balanced diet, and regular health monitoring.")
#     else:
#         # Display diagnosis results if any value is abnormal
#         st.write("### Diagnosis Results")
#         for key, value in results.items():
#             if value is not None:
#                 st.write(f"**{key}:** {value[0]}")
#                 st.write(f"**Suggested Solution:** {value[1]}")

# # Run the Streamlit app
# if __name__ == "__main__":
#     main()



import streamlit as st
import re

# Function to clean and normalize WBC input
def normalize_wbc_input(value, unit="cells/μL"):
    if isinstance(value, str):
        value = value.strip()
        value = re.sub(r'[^\d.]', '', value)
        
        if value == '':
            return None
    
    try:
        value = float(value)
        
        if unit == "thousand cells/μL":
            value = value * 1000
        
        return value
    except ValueError:
        return None

# Function to analyze and diagnose based on CBC values
def label_diagnosis(gender, hemoglobin, wbc, platelets):
    results = {
        'Hemoglobin': None,
        'WBC': None,
        'Platelets': None
    }
    
    # Hemoglobin analysis
    if gender == 'female':
        if hemoglobin < 12.0:
            results['Hemoglobin'] = ('Low Hemoglobin', "Increase iron intake. Include foods like spinach, lentils, and red meat. Consult a healthcare provider if symptoms persist.")
        elif 12.0 <= hemoglobin <= 15.5:
            results['Hemoglobin'] = None
        else:
            results['Hemoglobin'] = ('High Hemoglobin', "High hemoglobin may be due to dehydration, smoking, or other health issues. Consult a doctor for evaluation.")
    elif gender == 'male':
        if hemoglobin < 13.5:
            results['Hemoglobin'] = ('Low Hemoglobin', "Increase iron intake. Include foods like spinach, lentils, and red meat. Consult a healthcare provider if symptoms persist.")
        elif 13.5 <= hemoglobin <= 17.5:
            results['Hemoglobin'] = None
        else:
            results['Hemoglobin'] = ('High Hemoglobin', "High hemoglobin may be due to dehydration, smoking, or other health issues. Consult a doctor for evaluation.")
    
    # WBC analysis
    if wbc is None or wbc <= 0:
        results['WBC'] = ('Invalid Input', "WBC count cannot be zero or less. Please provide a valid value.")
    elif wbc < 4.5:
        results['WBC'] = ('Low WBC Count', "Low WBC count may indicate immune suppression. Seek medical advice for further evaluation.")
    elif 4.5 <= wbc <= 11:
        results['WBC'] = None
    else:
        results['WBC'] = ('High WBC Count', "High WBC count may indicate an infection. Consult a healthcare provider for further testing.")
    
    # Platelet analysis (Only if platelet data is provided)
    if platelets is not None:
        if platelets < 150000:
            results['Platelets'] = ('Low Platelets', "Low platelet count may lead to bleeding issues. Seek medical advice for potential causes and treatments.")
        elif 150000 <= platelets <= 450000:
            results['Platelets'] = None
        else:
            results['Platelets'] = ('High Platelets', "High platelet count can increase clotting risk. Consult a doctor to evaluate the cause and consider treatment options.")
    
    return results

# Function to extract parameters from the text file
def extract_parameters_from_txt(txt_file):
    parameters = {}

    with open(txt_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            
            match = re.match(r"([a-zA-Z\s]+):\s*(\d+(\.\d+)?)(\s*(\w+))?", line)
            
            if match:
                param = match.group(1).strip().lower()
                value = match.group(2)
                unit = match.group(5) if match.group(5) else "cells/μL"
                
                # Only set the value if the parameter is found
                if param == "hemoglobin" or param == "hgb":
                    parameters['Hemoglobin'] = float(value)
                elif param == "total wbc count" or param == "wbc count":
                    parameters['WBC'] = normalize_wbc_input(value, unit)
                elif param == "platelet count":
                    parameters['Platelet Count'] = float(value)
    
    return parameters

# Streamlit UI
def main():
    # Add title
    st.title("CBC Test Report")  # Title added here

    # File path for automatic reading
    file_path = r"D:\User\Pinjal\Work\AI_Project\health-prediction-app\modal\found_parameters.txt"
    
    # Read the file content automatically
    with open(file_path, "r", encoding="utf-8") as file:
        txt_content = file.read()
    
    # Display the content from the predefined file
    st.text(txt_content)
    
    # Extract parameters from the file
    parameters = extract_parameters_from_txt(file_path)
    
    # Display extracted values
    st.write("### Extracted Parameters")
    st.write(parameters)
    
    # User selects gender
    gender = st.selectbox("Gender", ["male", "female"])
    
    # Extract the values for each parameter
    hemoglobin = parameters.get('Hemoglobin', None)
    wbc = parameters.get('WBC', None)
    platelets = parameters.get('Platelet Count', None)

    # Check if WBC is None
    if wbc is None:
        st.warning("WBC data is missing in the report.")
    
    # Perform diagnosis with cleaned values
    results = label_diagnosis(gender, hemoglobin, wbc, platelets)
    
    # Check if all values are normal
    all_normal = True
    for key, value in results.items():
        if value is not None:
            all_normal = False
            break
    
    if all_normal:
        st.success("Your CBC report is within the normal range. Keep up with a healthy lifestyle, balanced diet, and regular health monitoring.")
    else:
        # Display diagnosis results if any value is abnormal
        st.write("### Diagnosis Results")
        for key, value in results.items():
            if value is not None:
                st.write(f"**{key}:** {value[0]}")
                st.write(f"**Suggested Solution:** {value[1]}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
