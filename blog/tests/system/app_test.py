from unittest import TestCase
from unittest.mock import patch
from app 


class AppTest(TestCase):
    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test Blog')


