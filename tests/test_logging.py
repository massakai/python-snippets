from logging import CRITICAL, DEBUG, ERROR, INFO, LogRecord, WARNING
from unittest import TestCase

from massakai.snippets.logging import LogLevelFilter


class LogLevelFilterTest(TestCase):
    def test_default(self):
        log_filter = LogLevelFilter()

        self.assertTrue(log_filter.filter(create_log_record(CRITICAL)))
        self.assertTrue(log_filter.filter(create_log_record(ERROR)))
        self.assertTrue(log_filter.filter(create_log_record(WARNING)))
        self.assertFalse(log_filter.filter(create_log_record(INFO)))
        self.assertFalse(log_filter.filter(create_log_record(DEBUG)))

    def test(self):
        log_filter = LogLevelFilter(include_levels={INFO, DEBUG})

        self.assertFalse(log_filter.filter(create_log_record(CRITICAL)))
        self.assertFalse(log_filter.filter(create_log_record(ERROR)))
        self.assertFalse(log_filter.filter(create_log_record(WARNING)))
        self.assertTrue(log_filter.filter(create_log_record(INFO)))
        self.assertTrue(log_filter.filter(create_log_record(DEBUG)))


def create_log_record(level: int) -> LogRecord:
    """
    テスト用のLogRecordを生成する

    Args:
        level: ログレベル

    Returns:
        LogRecord: ログレコード
    """
    return LogRecord(name='name', level=level, pathname='pathname',
                     lineno=1, msg='message', args=(), exc_info=None)
