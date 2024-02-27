import numpy as np
import pandas as pd
import json
from flask import Flask, render_template, request ,jsonify
app = Flask(__name__)

from joblib import load
model = load(r'C:\Users\Aakash\Documents\codes\EPICS\epics_model.joblib')

with open(r'C:\Users\Aakash\Documents\codes\EPICS\disease_data.json', 'r') as file:
    disease_data = json.load(file)


@app.route('/')
def helloworld():
    d="Select your symptoms and predict your illness"
    return render_template('index.html',you="",result="",details=d)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    pred = data.get('pred')
    print(pred)

    pred_2d=[pred]

    col_names=['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']

    col_names = pd.Index(col_names)

    row_df = pd.DataFrame(pred_2d, columns=col_names)

    output = model.predict(row_df) 
    predicted_disease=output[0]
    print(predicted_disease)

    disease_details = get_disease_details(predicted_disease)
    
    return jsonify({'result': predicted_disease,
                    'details': disease_details})

#input_string.replace(" ", "").lower()

def get_disease_details(dis):
    for i in disease_data['diseases']:
        if i['disease_name'].replace(" ", "").lower() == dis.replace(" ", "").lower():
            return i['details']
    return "Info not available"


    #return output[0]
    #return render_template('index.html', result=output[0])
    #session['pred_2d'] = pred_2d
    #return jsonify({'pred_2d': pred_2d})
    #return pred

# @app.route('/login',methods = ['POST'])
# def login():
#     pred_2d = session.get('pred_2d', None)  
#     col_names = pd.Index(col_names
#     row_df = pd.DataFrame(pred_2d, columns=col_names)
#     output = model.predict(row_df) 
#     print(output)
#     return render_template('index.html', y=output)

if __name__ == '__main__':
    app.run()