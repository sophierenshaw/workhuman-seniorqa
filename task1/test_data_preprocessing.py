import pandas as pd

from data_preprocessing import drop_columns

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