import os
from typing import Union


def is_empty(dir_path: Union[str, bytes, os.PathLike] = '.') -> bool:
    """
    ディレクトリが空であるかどうかを確認する

    Args:
        dir_path: ディレクトリのパス

    Returns:
        ディレクトリがからの場合、Trueを返す
        ディレクトリが空でない場合、Falseを返す

    Raises:
        NotADirectoryError: ディレクトリでないパスが渡された場合に発生する
        FileNotFoundError: 存在しないパスが渡された場合に発生する
    """
    return len(os.listdir(dir_path)) == 0
