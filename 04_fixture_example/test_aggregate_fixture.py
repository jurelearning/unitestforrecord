import pandas as pd
import pytest 

@pytest.fixture(scope='module')
def data():
    df = pd.DataFrame([[0, 2, 7, 4, 8],
                         [1, 7, 6, 3, 7],
                         [1, 1, "None", 8, 9],
                         [0, 2, 3, "None", 6],
                         [0, 5, 1, 4, 9]], 
                        columns = [f'feature_{i}' if i!=0 
                                  else 'class' for i in range(5)])
    return df


def aggregate_mean(df, column):
    return df.groupby("class")[column].mean().to_dict()


@pytest.mark.parametrize("column, expected", [("feature_1", {0: 3, 1: 4}), ("feature_3", {0: 3, 1: 4})])
def test_aggregate_mean_feature_1(data, column, expected): 
    # data doesn't need to be a variables because it appear above by pytest.fixture  
    assert expected == aggregate_mean(data, column)

# Prevent repeating code in your unit tests with Fixtures
# Fixtures are a great way to increase readability and reduce the chance of any errors in the test functions.

# run cmd: pytest -v