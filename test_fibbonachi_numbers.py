import pytest

import fibbonachi_numbers


class TestFibbonachi:

# Параметризованный тест для различных значений п и ожидаемых результатов
    @pytest.mark.parametrize("n, expected_result", [
        (0, [8]),
        (1, [0, 1]),
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 3, 5]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
    ])

    def test_fibbonachi(self, n, expected_result):
        actual_result = fibbonachi_numbers.fibonacci_numbers(n)
        assert actual_result == expected_result

    # Тест для случая п = -1 (отрицательное значение)

    def test_fibbonachi_negative_n(self):
        with pytest.raises (ValueError):
            fibbonachi_numbers.fibonacci_numbers(-1)