import pandas as pd
import pytest

def load_data():
    data = pd.DataFrame([[0, 2, 7, 4, 8],
                         [1, 7, 6, 3, 7],
                         [1, 1, "None", 8, 9],
                         [0, 2, 3, "None", 6],
                         [0, 5, 1, 4, 9]], 
                        columns = [f"feature_{i}" if i!=0 
                                  else "class" for i in range(5)])
    return data

def aggregate_mean(df, column):
    return df.groupby("class")[column].mean().to_dict()

# Run multiple test cases with Parametrize
@pytest.mark.parametrize("column, expected", [("feature_1", {0: 3, 1: 4}), ("feature_3", {0: 4, 1: 5.5})])
def test_aggregate_mean_feature_1(column, expected):   
    data = load_data()
    result = aggregate_mean(data, column)
    assert expected == result

# run cmd: pytest -v