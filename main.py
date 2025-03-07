import streamlit as st
import random
import time
import requests

st.title('Money Making Machine')
def generate_money():
    return random.randint(1, 1000)

st.subheader('Instant Cash Generator')
if st.button('Generate Money'):
    st.write(f'Counting Your Money...')
    time.sleep(5)
    amount = generate_money()
    st.success(f'You have generated ${amount}')


def fetch_side_hustle():
    try:
        response = requests.get('http://127.0.0.1:8000/side_hustles?api_key=123456789')
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return ('Freelancing')
        
    except:
        return ('Something went wrong')
    
st.subheader('Side Hustle Ideas')
if st.button('Generate Hustle'):
    hustle = fetch_side_hustle()
    st.success(f'Your side hustle is: {hustle}') 




def fetch_money_quote():
    try:
        response = requests.get('http://127.0.0.1:8000/money_quotes?api_key=123456789')
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
        else:
            return ('Money is not everything')
        
    except:
        return ('Something went wrong')
    

st.subheader('Money Making Motivation')
if st.button('Get Inspired'):
    quote = fetch_money_quote()
    st.info(quote)