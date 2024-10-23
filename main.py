import streamlit as st
import pandas as pd
import time

# text element
st.text("This is a text")
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("This is a super fashion")
st.markdown("""THIS IS A MARKDOWN""")
st.latex("\int")
st.json("""{"data":"This is streamlit"}""")
st.code("""
System.out.println("hello streamlit");
        """,language="java",line_numbers=True)

# Error Element
st.success("This is success")
st.error("This is error")
st.exception("TypeError")
st.warning("warning")

# Input Widget
firstName=st.text_input("First Name")
password=st.text_input("Password",type='password')
message=st.text_area("Message")
date=st.date_input("Date")
appointment=st.time_input("appointment")
age=st.number_input("age",step=1)
gender=st.radio("Gender",["Male","Female"])
enable=st.toggle("Enable Picker")
level=st.checkbox("Level")

# Sliders & Selectors
countries=st.selectbox("Countries",["India","Africa","America","China","Uruguay"])
programming_lang=st.multiselect("Programming",["Python","GoLLang","java","Javascript","C++"])
rating= st.slider("Rating",0,10)
ranking=st.select_slider("Ranking",["Junior Dev","Middle Dev","Senior Dev"])

st.divider()
if enable: 
    st.write(f"Details: {firstName},{password}")
    color=st.color_picker("Pick a Color")
    st.write(color)
    
# Data Elements
def loadData(data)-> pd.DataFrame:
    return pd.read_csv(data)

df=loadData("survey.csv")
st.dataframe(df)
st.table(df.head(2))

edited_data=st.data_editor(df)
# st.json(df.to_json())

# Connection to DB
# st.connection()

# Media Elements 
img=st.image("pic.jpeg","Image in Streamlit")
# audio_file=open("intro.mp3")
# st.audio(audio_file.read())

# VIDEO
# st.video()
if st.button("Take a Picture"):
    pic=st.camera_input("Take a picture")
    with open("someimg","wb") as f:
        f.write(pic.getbuffer())

# Download and Upload
file_upload=st.file_uploader("Upload CSV",type="csv")
if file_upload:
    st.write(pd.read_csv(file_upload))

st.download_button("download","pic.jpeg")

# Status Elements
if st.button("Compete"):
    with st.spinner("Thinking..."):
        time.sleep(5)
        st.write("Hello")
        
    # with st.progress("progression"):
    #     time.sleep(2)
    #     st.write("Hiii")
    
    st.toast("This is a toast")
    
# Chat Elements (LLM UI)
# Type writer effect
def stream_data(data,delay: float=0.2):
    for word in data.split():
        yield word+" "
        time.sleep(delay)
        
prompt=st.chat_input("Ask something")
if prompt:
    with st.chat_message("user"):
        st.write(f"You typed {prompt}")
    
    with st.spinner("Thinking ...."):
        time.sleep(0.02)
        response=f"some random test for streamlist"
        st.write_stream(stream_data(response))
        
# Streaming response
# Generator
# Some text
response=f"some random test for streamlist"
if st.button("StreamTest"):
    st.write_stream(stream_data(response))


st.divider()
# Layout
# Tabs
home_tab,about_tab=st.tabs(["Home","About"])

with home_tab:
    st.subheader("This is a home tab")

with about_tab:
    st.subheader("This is a about tab") 
    st.dataframe(df)
    
# Columns
col1,col2,col3=st.columns(3)

# Context Manager approach
with col1:
    st.title("This is first column")

col2.dataframe(df)

col3.image("pic.jpeg",use_column_width=True)

# Container
container=st.container(border=True)
container.write("Some container")

row1=st.columns(3)
row2=st.columns(3)

for col in row1+row2:
    tile=col.container(height=120)
    tile.title(":balloon:")
    
# Expander and Popover
with st.expander("Expander"):
    st.dataframe(df)
    
with st.popover("Popover"):
    st.image("pic.jpeg")
    
# Plots
# st.area_chart(df,x="") 