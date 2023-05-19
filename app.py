import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


# PAGE TITLE
st.set_page_config( page_title = "EDA - Exploratory Data Analysis App",
                    page_icon = ":bar_chart:" , 
                    layout = 'wide')

# TITLE OF THE APP
st.title(":bar_chart: EDA Application")



# CUSTOM CSS :
with open('style.css') as css :
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)



# UPLOAD CSV FILE HERE :
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)""")


# PANDAS PROFILING REPORT :
if uploaded_file is not None:

    @st.cache_data
    
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    
    df = load_csv()
    
    pr = ProfileReport(df, explorative=True)
    
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    
    st_profile_report(pr)

else:
    
    st.info('Awaiting for CSV file to be uploaded.')
    
    if st.button('Press to use Example Dataset'):

        # EXAMPLE DATA
        @st.cache_data

        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['col_1', 'col_2', 'col_3', 'col_5', 'col_6']
            )
            return a
        
        df = load_data()

        pr = ProfileReport(df, explorative=True)

        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')

        st_profile_report(pr)