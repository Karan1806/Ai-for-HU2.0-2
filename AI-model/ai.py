# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 17:51:19 2023

@author: Rajiv Arora
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:\Users\Rajiv Arora\Desktop\Ai-for-HU2.0-2\AI-model\saved models\diabetes_model.sav', 'rb'))





# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')