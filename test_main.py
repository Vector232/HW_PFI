import pytest
import main


class Tester:
    def test_is_balance(self):
        exprs = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
        anss = ['Сбалансированно', 'Сбалансированно', 'Сбалансированно', 'Несбалансированно', 'Несбалансированно', 'Несбалансированно']

        for exp, ans in zip (exprs, anss):
            assert main.is_balance(exp) == ans

if __name__ == '__main__':
    pytest.main(["-vv"])