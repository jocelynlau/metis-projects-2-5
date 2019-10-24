import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(style="whitegrid")

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, confusion_matrix, precision_recall_curve

def print_scores(truth,pred):
    '''
    print key metrics
    '''
    print("Accuracy score:",accuracy_score(truth, pred))
    print("F1 score:",f1_score(truth, pred))
    print("Precision (true + / all predicted +):",precision_score(truth, pred))
    print("Recall (true + / all actual +):",recall_score(truth, pred))
    return


def graph_conf_matrix(matrix):
    '''
    output formatted confusion matrix for specified matrix
    '''
    plt.figure(dpi=150)
    ax = sns.heatmap(matrix, cmap=plt.cm.Blues, annot=True, square=True);
    ax.set_xlabel('Predicted no-show')
    ax.set_ylabel('Actual no-show')
    ax.set_title('Logistic regression confusion matrix')
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)
    return

def graph_prec_recall_curves(threshold_curve,precision_curve,recall_curve):
    '''
    output formatted graph of precision and recall curves
    '''
    plt.figure(dpi=80)
    plt.plot(threshold_curve, precision_curve[1:],label='precision')
    plt.plot(threshold_curve, recall_curve[1:], label='recall')
    plt.legend(loc='lower left')
    plt.xlabel('Threshold (above this probability, label as no-show)');
    plt.title('Precision and Recall Curves');
    return

def graph_roc_auc(fpr,tpr):
    '''
    output formatted graph of ROC
    '''
    plt.plot(fpr, tpr,lw=2)
    plt.plot([0,1],[0,1],c='violet',ls='--')
    plt.xlim([-0.05,1.05])
    plt.ylim([-0.05,1.05])
    
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve for no-show problem');
    return