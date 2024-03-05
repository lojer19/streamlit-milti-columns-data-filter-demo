import pandas as pd
import streamlit as st

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter the data by:", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            user_input = right.multiselect( 
                f"Values for {column}",
                    df[column].unique(),
                    default = None,
            )
            df = df[df[column].isin(user_input)]
    return df

def main():
    # Hide the error on the streamlit web GUI
    st.set_option('deprecation.showfileUploaderEncoding', True)
    
    st.title("Data Filter")
    
    # File upload
    excel_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])
    
    if excel_file is not None: 
        # Select the row containing the column titles
        title_row = st.number_input("Enter the row number containing column titles:", min_value=1, value=1)
        
        # Read the Excel file
        data = pd.read_excel(excel_file, skiprows=title_row-1)
        
        # Extract the column names from the selected row
        column_names = data.columns
        
        filtered_data = filter_dataframe(data)
        st.write(filtered_data)

if __name__ == "__main__":
    main()