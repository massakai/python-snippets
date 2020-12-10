from logging import CRITICAL, ERROR, Filter, LogRecord, WARNING
from typing import Optional, AbstractSet


class LogLevelFilter(Filter):
    """
    ログに記録するかどうかをログレベルで指定するフィルタ
    """

    def __init__(self, name: str = '',
                 include_levels: Optional[AbstractSet[int]] = None) -> None:
        """
        フィルタを初期化する

        Args:
            name (str): フィルタ名
            include_levels (set[int]): ログに記録するログレベルの集合 (デフォルト: WARNING以上)
        """
        super().__init__(name)

        if include_levels is None:
            include_levels = {CRITICAL, ERROR, WARNING}
        self.include_levels: AbstractSet[int] = include_levels

    def filter(self, record: LogRecord) -> bool:
        """
        ログを記録すべきかどうかを判定する

        Args:
            record (LogRecord): ログレコード

        Returns:
            bool: 記録する場合はTrueを返す。記録しない場合はFalseを返す。

        """
        return record.levelno in self.include_levels
