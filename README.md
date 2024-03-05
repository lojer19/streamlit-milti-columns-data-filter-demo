# Multi-columns Data Filter Using Streamlit in Python
 This repository contains a Python script that allows you to filter data in an Excel file using Streamlit, a web application framework for Python. The script utilizes the pandas library for data manipulation.

## Requirements
* Python 3

## Installation

1. Clone the repository:

```bash
git clone https://github.com/lojer19/streamlit-multi-columns-data-filter-demo.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage
1. Run the script:
```python
streamline run filter.py
```
2. The Streamlit web application will open in your browser.
3. Click on the "Upload Excel file" button and select an Excel file (.xlsx or .xls) containing the data you want to filter.
4. Enter the row number that contains the column titles in the Excel file. This row will be skipped when reading the data.
5. The script will display a multi-select dropdown for each column in the dataset. Select the values you want to filter by for each column.
6. The filtered data will be displayed below the filters.

## Contributing

Pull requests are welcome.


## License
[MIT](https://choosealicense.com/licenses/mit/)
