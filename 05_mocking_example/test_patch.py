import pandas as pd
from unittest.mock import patch
from codebase import pipeline

@patch('codebase.pd.read_csv')
def test_aggregate_mean_feature_1(read_csv):   
    read_csv.return_value = pd.DataFrame([[0, 2, 7, 4, 8],
                                          [1, 7, 6, 3, 7],
                                          [1, 1, "None", 8, 9],
                                          [0, 2, 3, "None", 6],
                                          [0, 5, 1, 4, 9]], 
                                          columns = [f'feature_{i}' if i!=0 
                                                     else 'class' for i in range(5)])
    result = pipeline("feature_1")
    assert result == {0: 3, 1: 4}

# When we run pytest -v, the large .csv will not be loaded and instead replaced with our small dataset. 
# The test runs quickly and we can easily test new cases!
# run cmd: pytest -v

