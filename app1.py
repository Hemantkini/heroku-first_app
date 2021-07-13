import joblib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title('Patient Hospital Stay Prediction')
# load dataset
df = pd.read_csv('train.csv')

# show the entire dataframe
st.write(df)


# markdown
st.subheader('Making Prediction')
st.markdown('**Please provide patient information**:')  # you can use markdown like this

# load models
tree_clf = joblib.load('2clf-best.pickle')

#user provides inputs

Hospital_code = st.selectbox('Hospital_code', ['1', '2'])
Hospital_type_code = int(st.number_input('Age:', 0, 120, 20))
City_Code_Hospital  = '3'
Hospital_region_code = 'Z'
#Available Extra Rooms in Hospital = int(st.selectbox('Available Extra Rooms in Hospital', ['3']))
Department = 'radiotherapy'
Ward_Type = 'R'
Ward_Facility_Code= 'F'
#Bed Grade = '2'
patientid = '31397'
City_Code_Patient = '7'
#Type of Admission = 'Trauma'
#Severity of Illness = 'Extreme'
#Visitors with Patient = '2'
Age = '51-60'
Admission_Deposit = '4911'


# this is how to dynamically change text
prediction_state = st.markdown('calculating...')

patient= pd.DataFrame(
    {
        'Hospital_code': [Hospital_code],
        'Hospital_type_code': [Hospital_type_code],
	'City_Code_Hospital':  = 3,
	'Hospital_region_code': = [Hospital_region_code] ,
	'Available Extra Rooms in Hospital': = 3,
	'Department': = [Department],
	'Ward_Type': = [Ward_Type],
	'Ward_Facility_Code': [Ward_Facility_Code],
	'Bed Grade': 2,
	'patientid': [patientid],
	'City_Code_Patient': [City_Code_Patient],
	'Type of Admission': 'Trauma',
	'Severity of Illness': 'Extreme',
	'Visitors with Patient': 2,
	'Age': [Age],
	'Admission_Deposit': [Admission_Deposit]


    }
)

y_pred = tree_clf.predict(patient)

if y_pred[0] == 0:
    msg = 'This patient is predicted to stay for: 0-10 days'
else:
    msg = 'This patient is predicted to stay for more than: 0-10 days'

prediction_state.markdown(msg)
