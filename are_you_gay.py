'''
home-made r u gay quiz. in progress...
'''

import streamlit as st
import matplotlib.pyplot as plt
from gay_options import *

st.title("Are you gay?")
st.write("let's see...")
user_score = 0

if 'stage' not in st.session_state:
    st.session_state.stage = 0
    st.session_state.q_index = 0
    st.session_state.selection = 0
    st.write(f'User Score: {user_score}')

def set_state(i):
    st.session_state.stage = i

def next_question():
    st.session_state.q_index += 1
    st.session_state.stage = 2

def handle_response():
    st.write('test')

# State 1
if st.session_state.stage == 0:
    st.button('start Quiz! xD', on_click=set_state, args=[1])

# State 2
if st.session_state.stage >= 1:
    name = st.text_input('Enter your name: ', on_change=set_state, args=[2])

# State 3
if st.session_state.stage == 2:
    st.write(f'well hello, {name}!')
    
    if(st.session_state.q_index < len(questions)):
        st.session_state.selection = st.selectbox(questions[st.session_state.q_index], answers[st.session_state.q_index])
        if(st.session_state.selection == None):
            st.write("pls select something")
        else:
            st.write(f'u selected {st.session_state.selection}')
            selection_index = answers[st.session_state.q_index].index(st.session_state.selection)
            st.write(f'that gets you {weights[selection_index]} points!!!!!')
        st.button("Next Question", on_click=next_question)

    else:
        st.write("all done")

# Restart
if st.session_state.stage > 3:
    st.button('Start Over', on_click=set_state, args=[0])

# # for later, making pi chart
# labels = ['Gay', 'not Gay']
# sizes = [50, 50]
# ax.pie(sizes, labels=labels, autopct='%1.1f%%')
# ax.axis('equal')
# st.pyplot(fig)