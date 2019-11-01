"""
Note this file contains _NO_ flask functionality.
Instead it makes a file that takes the input dictionary Flask gives us,
and returns the desired result.

This allows us to test if our modeling is working, without having to worry
about whether Flask is working. A short check is run at the bottom of the file.
"""

import pickle
import numpy as np
import datetime as dt
import pandas as pd
import calendar


with open("static/models/appt_model.pkl", "rb") as f:
    appt_model = pickle.load(f)

feature_names = appt_model.feature_names
neighborhoods = appt_model.neighborhood_names

site_dict = ['Age','Public Assistance','Alcoholism','Receives SMS',
            'Neighborhood','Reschedule','Follow-Up','Prior Appointment Count','Prior No-Show Count',
            'Scheduling Date','Appointment Date']
site_default = [0,0,0,0,0,0,0,0,0,'11/01/2019','11/15/2019']

def make_prediction(feature_dict):
    """
    Input:
    feature_dict: a dictionary of the form {"feature_name": "value"}

    Function makes sure the features are fed to the model in the same order the
    model expects them.

    Output:
    Returns (x_inputs, probs) where
      x_inputs: a list of feature values in the order they appear in the model
      probs: a list of dictionaries with keys 'name', 'prob'
    """
    x_input = [
        feature_dict.get(name,site_default[i]) for i,name in enumerate(site_dict)
    ]

    #initialize new datapoint and map to actual feature names
    a = np.array([[0]]*82)
    a = pd.DataFrame(a.T,columns=feature_names)
    a['Age2'] = feature_dict.get('Age',0)
    a['Scholarship'] = feature_dict.get('Public Assistance',0)
    a['Alcoholism'] = feature_dict.get('Alcoholism',0)
    a['SMS_received'] = feature_dict.get('Receives SMS',0)
    a['Reschedule'] = feature_dict.get('Reschedule',0)
    a['Follow_up'] = feature_dict.get('Follow-Up',0)
    a['prior_appt_count'] = feature_dict.get('Prior Appointment Count',0)
    a['prior_no_show_count'] = feature_dict.get('Prior No-Show Count',0)
    #neighborhood
    a['Reschedule'] = feature_dict.get('Reschedule',0)
    #schedule day of week
    sched_weekday = dt.datetime.weekday(dt.datetime.strptime(feature_dict.get('Scheduling Date','11/01/2019'), '%m/%d/%Y'))
    if sched_weekday==2:
        a['SchedDayofWeek_Tuesday']=1
    elif sched_weekday==3:
        a['SchedDayofWeek_Wednesday']=1
    elif sched_weekday==4:
        a['SchedDayofWeek_Thursday']=1
    elif sched_weekday==5:
        a['SchedDayofWeek_Friday']=1
    elif sched_weekday==6:
        a['SchedDayofWeek_Saturday']=1
    #appointment day of week
    appt_weekday = dt.datetime.weekday(dt.datetime.strptime(feature_dict.get('Appointment Date','11/15/2019'), '%m/%d/%Y'))
    if appt_weekday==2:
        a['ApptDayofWeek_Tuesday']=1
    elif appt_weekday==3:
        a['ApptDayofWeek_Wednesday']=1
    elif appt_weekday==4:
        a['ApptDayofWeek_Thursday']=1
    elif appt_weekday==5:
        a['ApptDayofWeek_Friday']=1
    #appointment day diff
    a['DayDiff2'] = min((dt.datetime.strptime(feature_dict.get('Appointment Date','05/30/2019'), '%m/%d/%Y')-dt.datetime.strptime(feature_dict.get('Schedule Date','05/01/2019'), '%m/%d/%Y')).days,60)

    pred_probs = appt_model.predict_proba(a.values).flat
    probs = round(pred_probs[1],2)
    # probs = [{'name': appt_model.target_names[index], 'prob': round(pred_probs[index],2)}
    #          # for index in np.array(pred_probs)[::-1]]
    #          for index in np.argsort(pred_probs)[::-1]]

    return (x_input, probs)


# This section checks that the prediction code runs properly
# To run, type "python predictor_api.py" in the terminal.
#
# The if __name__='__main__' section ensures this code only runs
# when running this file; it doesn't run when importing
if __name__ == '__main__':
    from pprint import pprint
    print("Checking to see what setting all params to 0 predicts")
    features = {f: '0' for f in feature_names}
    print('Features are')
    pprint(features)

    x_input, probs = make_prediction(features)
    print(f'Input values: {x_input}')
    print('Output probabilities')
    pprint(probs)
