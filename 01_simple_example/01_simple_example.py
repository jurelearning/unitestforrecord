
def new_sum(iterable):
    result = 0
    for val in iterable:
        result += val
    return result

def test_new_sum_list():
    assert new_sum([1, 2, 3]) == 6
    
def test_new_sum_tuple():
    assert new_sum((-1, 2, 3)) == 6

if __name__ == "__main__":
    test_new_sum_list()
    test_new_sum_tuple()
    # run cmd: python 01_simple_example.py
    # Unit tests are not perfect and it is near impossible to achieve 100% code coverage