from unittest import TestCase
from unittest.mock import Mock

from massakai.snippets.decorator.retry import retry_on_failure


class RetryOnFailureTest(TestCase):
    def test_true(self):
        mock_func = Mock()
        mock_func.side_effect = [False] * 3 + [True]

        deco_func = retry_on_failure(retries=3, interval=0)(mock_func)

        response = deco_func()

        self.assertTrue(response)
        self.assertEqual(4, mock_func.call_count)

    def test_false(self):
        mock_func = Mock()
        mock_func.side_effect = [False] * 4 + [True]

        deco_func = retry_on_failure(retries=3, interval=0)(mock_func)

        response = deco_func()

        self.assertFalse(response)
        self.assertEqual(4, mock_func.call_count)
