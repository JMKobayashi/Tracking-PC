import streamlit as st
import requests
TRACK_URL = 'https://track-challenge-ucu2fzh5qa-uc.a.run.app/track'


def request_api():
    response = requests.post(url=TRACK_URL)

    st.markdown('---')
    st.header('API Response')
    st.text(f'Response status code: {response.status_code}\nResponse Body:')
    st.json(response.json())


st.markdown(
    '''
    <style>
    .column{
        position: absolute;
        bottom: 0;
        right: 0;
    }
    </style>
    ''',
    unsafe_allow_html=True
)
st.header('Create Track Information')
st.text('On this page, you can experiment with creating a Track document in the database.')
col1, col2 = st.columns([3, 1])
col1.text_input('Endpoint URL', value=TRACK_URL, disabled=True)
col2.write('')
col2.write('')
request_button = col2.button('Request')

if request_button:
    request_api()
