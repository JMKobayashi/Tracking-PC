import streamlit as st
import pandas as pd
import requests

TRACK_EVENTS_URL = 'https://track-challenge-ucu2fzh5qa-uc.a.run.app/track/events'


def request_api():
    response = requests.get(url=TRACK_EVENTS_URL)

    st.markdown('---')
    st.header('API Response')
    st.text(f'Response status code: {response.status_code}\nResponse Body:')
    df = pd.json_normalize(response.json()).sort_values(by='event_time', ascending=False)
    st.dataframe(df, hide_index=True, column_order=['id', 'request', 'event_time'])


st.markdown(
    '''
    <style>
    .column{
        position: absolute;
        bottom: 0;
        right: 0;
    }
    .stDataFrame{
        width: fit;
    }
    </style>
    ''',
    unsafe_allow_html=True
)
st.header('Show Track Information')
st.text('In this page you can test the fetching of all the documents in database')
col1, col2 = st.columns([3, 1])
col1.text_input('Endpoint URL', value=TRACK_EVENTS_URL, disabled=True)
col2.write('')
col2.write('')
request_button = col2.button('Request')

if request_button:
    request_api()
