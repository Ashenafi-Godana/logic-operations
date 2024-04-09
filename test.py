# test_main.py
import pytest
from main import generate_truth_table


@pytest.mark.parametrize("expression, expected_output", [
    ("~p & q | r", """p | q | r | ~p & q | r
--------------------
0 | 0 | 0 | 1
0 | 0 | 1 | 1
0 | 1 | 0 | 0
0 | 1 | 1 | 1
1 | 0 | 0 | 0
1 | 0 | 1 | 1
1 | 1 | 0 | 0
1 | 1 | 1 | 1
"""),
    ("(p -> q) & r", """p | q | r | (p -> q) & r
--------------------
0 | 0 | 0 | 0
0 | 0 | 1 | 0
0 | 1 | 0 | 0
0 | 1 | 1 | 1
1 | 0 | 0 | 0
1 | 0 | 1 | 0
1 | 1 | 0 | 1
1 | 1 | 1 | 1
"""),
    # Add more test cases as needed
])
def test_generate_truth_table(expression, expected_output, capsys):
    generate_truth_table(expression)
    captured = capsys.readouterr()
    assert captured.out == expected_output


if __name__ == '__main__':
    pytest.main()
