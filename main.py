import unittest
import random

class CodeCoverageSimulator:
    def __init__(self):
        self.code_coverage = {}

    def execute_code(self, code):
        self.code_coverage = {}
        for line in code.split('\n'):
            if line.strip():
                self.code_coverage[line.strip()] = True
        return self.code_coverage

    def get_code_coverage(self):
        return self.code_coverage

class TestCodeCoverageSimulator(unittest.TestCase):
    def setUp(self):
        self.simulator = CodeCoverageSimulator()

    def test_execute_code(self):
        code = """
        def add(a, b):
            return a + b

        def subtract(a, b):
            return a - b

        add(2, 3)
        subtract(5, 2)
        """
        self.simulator.execute_code(code)
        self.assertEqual(self.simulator.get_code_coverage(), {
            'def add(a, b):', 'return a + b', 'def subtract(a, b):', 'return a - b', 'add(2, 3)', 'subtract(5, 2)'
        })

    def test_execute_empty_code(self):
        code = ''
        self.simulator.execute_code(code)
        self.assertEqual(self.simulator.get_code_coverage(), {})

    def test_execute_code_with_comments(self):
        code = """
        # This is a comment
        def add(a, b):
            return a + b

        # This is another comment
        def subtract(a, b):
            return a - b

        add(2, 3)
        subtract(5, 2)
        """
        self.simulator.execute_code(code)
        self.assertEqual(self.simulator.get_code_coverage(), {
            'def add(a, b):', 'return a + b', 'def subtract(a, b):', 'return a - b', 'add(2, 3)', 'subtract(5, 2)'
        })

    def test_execute_code_with_empty_lines(self):
        code = """
        def add(a, b):

        return a + b

        def subtract(a, b):
            return a - b

        add(2, 3)
        subtract(5, 2)
        """
        self.simulator.execute_code(code)
        self.assertEqual(self.simulator.get_code_coverage(), {
            'def add(a, b):', 'return a + b', 'def subtract(a, b):', 'return a - b', 'add(2, 3)', 'subtract(5, 2)'
        })

if __name__ == '__main__':
    unittest.main()
```

Bu kodda, `CodeCoverageSimulator` klassi yaratilib, uda `execute_code` va `get_code_coverage` metodlari yaratilib. `execute_code` metodida, kodi qayta ishlab, har bir satrni qayta ishlab, agar satrda kod bor bo'lsa, u satrni `code_coverage` slovoriga qo'shib, keyin qayta ishlab chiqarib qaytadi. `get_code_coverage` metodida, `code_coverage` slovoriga qaytarib beradi.

`TestCodeCoverageSimulator` klassida, `setUp` metodida, har bir testni boshlash uchun `CodeCoverageSimulator` obyekti yaratib, `test_execute_code`, `test_execute_empty_code`, `test_execute_code_with_comments` va `test_execute_code_with_empty_lines` metodlari yaratilib. Bu metodlarda, turli holatlarda `execute_code` metodining ishlashini tekshirib, natijalarni tekshirib, testlarni yakunlaydi.

`if __name__ == '__main__':` qismida, `unittest.main()` funksiyasi chaqirib, testlarni boshlaydi.
