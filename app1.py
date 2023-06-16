import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

web_apps = st.sidebar.selectbox("Select Web Apps",
                                ("Exploratory Data Analysis", ""))


if web_apps == "Exploratory Data Analysis":

  uploaded_file = st.sidebar.file_uploader("Choose a file")

  if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    show_df = st.checkbox("Show Data Frame", key="disabled")

    if show_df:
      st.write(df)

    column_type = st.sidebar.selectbox('Select Data Type',
                                       ("Numerical", "Categorical", "Bool", "Date"))
    
    st.markdown('Rows: ' + str(len(df)))
    st.markdown('Columns: ' + str(len(df.columns)))
    st.markdown('Numeric variables: ' + str(len(df.select_dtypes(['number']).columns)))
    st.markdown('Categorical variables: ' + str(len(df.select_dtypes(['object']).columns)))
    st.markdown('Boolean variables: ' + str(len(df.select_dtypes(['boolean']).columns)))

    if column_type == "Numerical":
      numerical_column = st.sidebar.selectbox(
          'Select a Column', df.select_dtypes(include=['int64', 'float64']).columns)

      st.header('Five-number summary')
      st.table(df[numerical_column].describe().loc[['min', '25%', '50%', '75%', 'max']])


      # histogram
      choose_color = st.color_picker('Pick a Color', "#783198")
      choose_opacity = st.slider(
          'Color Opacity', min_value=0.0, max_value=1.0, step=0.05)

      hist_bins = st.slider('Number of bins', min_value=5,
                            max_value=150, value=30)
      hist_title = st.text_input('Set Title', 'Histogram')
      hist_xtitle = st.text_input('Set numerical x-axis Title', numerical_column)

      fig, ax = plt.subplots()
      ax.hist(df[numerical_column], bins=hist_bins,
              edgecolor="black", color=choose_color, alpha=choose_opacity)
      ax.set_title(hist_title)
      ax.set_xlabel(hist_xtitle)
      ax.set_ylabel('Count')

      st.pyplot(fig)
      filename = "plot.png"
      fig.savefig(filename,dpi = 300)
      
      with open("plot.png", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
        )
    
    if column_type == "Categorical":
      categorical_column = st.sidebar.selectbox(
          'Select a Column', df.select_dtypes(include=['object']).columns)
      
      choose_color = st.color_picker('Pick a Color', "#783198")
      choose_opacity = st.slider(
          'Color Opacity', min_value=0.0, max_value=1.0, step=0.05)
      h = df[categorical_column].value_counts()
      #st.markdown(h)

      bar_title = st.text_input('Set Title', 'Bar Plot')
      bar_xtitle = st.text_input('Set categorical x-axis Title', categorical_column)

      fig, ax = plt.subplots()
      ax.bar(x = h.index.tolist(), height = h,
              edgecolor="black", color=choose_color, alpha=choose_opacity)
      
      ax.set_title(bar_title)
      ax.set_xlabel(bar_xtitle)
      ax.set_ylabel('Count')


      st.pyplot(fig)
      filename = "plot.png"
      fig.savefig(filename,dpi = 300)

      # Display the download button
      with open("plot.png", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
        )
    if column_type == "Boolean":
      boolean_column = st.sidebar.selectbox(
          'Select a Column', df.select_dtypes(include=['boolean']).columns)
      
      choose_color = st.color_picker('Pick a Color', "#783198")
      choose_opacity = st.slider(
          'Color Opacity', min_value=0.0, max_value=1.0, step=0.05)
      h = df[boolean_column].value_counts()
      #st.markdown(h)

      bar_title = st.text_input('Set Title', 'Bar Plot')
      bar_xtitle = st.text_input('Set boolean x-axis Title', boolean_column)

      fig, ax = plt.subplots()
      ax.bar(x = h.index.tolist(), height = h,
              edgecolor="black", color=choose_color, alpha=choose_opacity)
      
      ax.set_title(bar_title)
      ax.set_xlabel(bar_xtitle)
      ax.set_ylabel('Count')

      
      st.pyplot(fig)
      filename = "plot.png"
      fig.savefig(filename,dpi = 300)

      # Display the download button
      with open("plot.png", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
        )
