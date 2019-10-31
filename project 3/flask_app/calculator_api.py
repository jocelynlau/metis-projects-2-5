"""
Note this file contains _NO_ flask functionality.
Instead it makes a file that takes the input dictionary Flask gives us,
and returns the desired result.

This allows us to test if our modeling is working, without having to worry
about whether Flask is working. A short check is run at the bottom of the file.
"""

import pickle
import numpy as np
from sklearn.metrics import confusion_matrix

with open("static/models/appt_model2.pkl", "rb") as f:
    appt_model = pickle.load(f)
with open("static/models/X_test.pickle", "rb") as f:
    X_test = pickle.load(f)
with open("static/models/y_test.pickle", "rb") as f:
    y_test = pickle.load(f)

input_names = ["Total Number of Appointments","Intervention Cost ($)",
               "Appointment Cost ($)","Threshold"]
input_defaults = [1000,10,30,0.5]

def calculate_int(input_dict):
    """
    Input:
    input_dict: a dictionary of the form {"input":"value"}

    Function takes in the inputs and applies cost calculation

    Output:
    Returns:
    Expected cost
    """
    i_input = [
        float(input_dict.get(inp, input_defaults[i])) for i,inp in enumerate(input_names)
    ]

    y_pred_prob = appt_model.predict_proba(X_test.values)[:,1] > i_input[3]
    a = confusion_matrix(y_test, y_pred_prob)
    tot_a = len(y_test)

    TP = a[1,1]/tot_a #true positives - Predicted no-shows, actual no-shows
    FP = a[0,1]/tot_a #false positives - Predicted no-shows, actual shows
    FN = a[1,0]/tot_a #false negatives - Predicted shows, actual no-shows
    TN = a[0,0]/tot_a #true negatives - Predicted shows, actual shows

    matrix = [TP,FP,FN,TN]
    matrix.append(np.sum(matrix))
    appts = [m*i_input[0] for m in matrix] #appointment counts
    appts.append(np.sum(appts))

    # appointment gain/loss in do-nothing scenario
    do_nothing = [(appts[0]*i_input[2])+(appts[2]*i_input[2]),
                  (appts[1]*i_input[2])+(appts[3]*i_input[2])
                 ] #cost of no-shows, cost of shows
    do_nothing.append(-do_nothing[0]+do_nothing[1])

    # intervention cost for predicted no-shows
    int_cost = [(appts[0]*i_input[1]),
                  (appts[1]*i_input[1])
                 ]  # intervention cost for TPs and FPs
    int_cost.append(int_cost[0]+int_cost[1])

    # appointment gain/loss in scenario
    cost_w_int = [(appts[0]*i_input[2]),(appts[1]*i_input[2]),
                  (appts[2]*i_input[2]),(appts[3]*i_input[2])
                  ]
    cost_w_int.append(cost_w_int[0]+cost_w_int[1]-cost_w_int[2]+cost_w_int[3])

    # total gain/loss in scenario
    tot_cost_w_int = [(cost_w_int[0]-int_cost[0]),cost_w_int[1]-int_cost[1],
                      -cost_w_int[2],cost_w_int[3]
                      ] # appt gain/loss - int for predicted Ps, appt gain/loss for predicted Ns
    tot_cost_w_int.append(np.sum(tot_cost_w_int))

    matrix = [x.round(2) for x in matrix]
    do_nothing = [x.round(2) for x in do_nothing]
    appts = [int(x.round(0)) for x in appts]
    int_cost = [x.round(2) for x in int_cost]
    cost_w_int = [x.round(2) for x in cost_w_int]
    tot_cost_w_int = [x.round(2) for x in tot_cost_w_int]

    return i_input, matrix, appts, do_nothing, int_cost, cost_w_int, tot_cost_w_int


# This section checks that the prediction code runs properly
# To run, type "python predictor_api.py" in the terminal.
#
# The if __name__='__main__' section ensures this code only runs
# when running this file; it doesn't run when importing
# if __name__ == '__main__':
    # from pprint import pprint
    # print("Checking to see what setting all params to 0 predicts")
    # features = {f: '0' for f in feature_names}
    # print('Features are')
    # pprint(features)
    #
    # x_input, probs = make_prediction(features)
    # print(f'Input values: {x_input}')
    # print('Output probabilities')
    # pprint(probs)
