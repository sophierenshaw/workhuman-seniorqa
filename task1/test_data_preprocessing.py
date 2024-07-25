import pandas as pd
import numpy as np

from .data_preprocessing import drop_columns,clean_null_values,  clean_duplicate_values, to_lower_case, remove_special_characters

def test_drop_columns():
    # Create a sample DataFrame for testing
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

    # Define the columns to drop
    columns_to_drop = ['B', 'C']

    # Call the drop_columns function
    result = drop_columns(data, columns_to_drop)

    # Check if the dropped columns are no longer present in the DataFrame
    assert 'B' not in result.columns
    assert 'C' not in result.columns

    # Check if the remaining column is still present in the DataFrame
    assert 'A' in result.columns

    # Check if the shape of the DataFrame is correct after dropping columns
    assert result.shape == (3, 1)

def test_clean_null_values():
    # Create a sample DataFrame for testing
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, np.nan, 6], 'C': [np.nan, 8, 9]})

    # Call the clean_null_values function
    result = clean_null_values(data)

    # Check if rows with null values are printed
    assert result.shape[0] == 1

    # Check if null values are removed from the DataFrame
    assert result.isnull().sum().sum() == 0

    # Check if the shape of the DataFrame is correct after removing null values
    assert result.shape == (1, 3)

def test_clean_duplicate_values():
    # Create a sample DataFrame for testing
    data = pd.DataFrame({'A': ['order', 'technical', 'order'], 'B': ['help','power','help'], 'C': ['okay', 'button', 'okay']})

    # Call the clean_duplicate_values function
    result = clean_duplicate_values(data)

    # Check if duplicate rows are printed
    assert result.shape[0] == 2

    # Check if duplicate values are removed from the DataFrame
    assert result.duplicated().sum() == 0

    # Check if the shape of the DataFrame is correct after removing duplicate values
    assert result.shape == (2, 3)

def test_to_lower_case():
    # Create a sample DataFrame for testing
    data = pd.DataFrame({'A': ['Order', 'HELP'], 'B': ['Technical', 'SUPPORT']})

    # Call the to_lower_case function
    result = to_lower_case(data)

    # Check if the values in columns are converted to lowercase
    assert result['A'].tolist() == ['order', 'help']
    assert result['B'].tolist() == ['technical', 'support']

    # Check if the shape of the DataFrame is unchanged
    assert result.shape == (2, 2)
    
def test_remove_special_characters():
    # Create a sample DataFrame for testing
    data = pd.DataFrame({'A': ['Hello!', 'How can I reset my phone?\n'], 'B': ["go to 'Settings' > 'System' > 'Reset' > 'Factory data reset'",'Confirm the reset by following the on-screen instructions!']})

    # Call the remove_special_characters function
    result = remove_special_characters(data)

    # Check if special characters are removed from columns
    assert result['A'].tolist() == ['Hello', 'How can I reset my phone']
    assert result['B'].tolist() == ['go to Settings  System  Reset  Factory data reset', 'Confirm the reset by following the onscreen instructions']

    # Check if the shape of the DataFrame is unchanged
    assert result.shape == (2, 2)
    

