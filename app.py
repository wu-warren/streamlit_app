import streamlit as st

st.title('title of your application')
st.markdown('*italic*')
st.markdown('this is **bold text**')

st.sidebar.title('title of sidebar')
st.sidebar.markdown('markdown **text** in the *sidebar*')

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
    st.markdown('this is markdown **text**')

agree_sidebar = st.sidebar.checkbox('sidebar checkbox')
if agree_sidebar:
    st.sidebar.write('side bar checked')