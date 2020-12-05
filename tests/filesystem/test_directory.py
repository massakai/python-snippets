from pathlib import Path
from tempfile import TemporaryDirectory, NamedTemporaryFile
from unittest import TestCase

from massakai.snippets.filesystem.directory import is_empty


class IsEmptyTest(TestCase):

    def test_return_true_if_empty_directory_str(self):
        with TemporaryDirectory() as tmp_dir:
            self.assertTrue(is_empty(tmp_dir))

    def test_return_true_if_empty_directory_bytes(self):
        with TemporaryDirectory() as tmp_dir:
            self.assertTrue(is_empty(tmp_dir.encode('utf-8')))

    def test_return_true_if_empty_directory_path_like(self):
        with TemporaryDirectory() as tmp_dir:
            self.assertTrue(is_empty(Path(tmp_dir)))

    def test_return_false_if_not_empty_directory_str(self):
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / 'file'
            file_path.touch()

            self.assertFalse(is_empty(tmp_dir))

    def test_return_false_if_not_empty_directory_bytes(self):
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / 'file'
            file_path.touch()

            self.assertFalse(is_empty(tmp_dir.encode('utf-8')))

    def test_return_false_if_not_empty_directory_path_like(self):
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / 'file'
            file_path.touch()

            self.assertFalse(is_empty(Path(tmp_dir)))

    def test_raise_exception_if_file_str(self):
        with NamedTemporaryFile() as tmp_file:
            with self.assertRaises(NotADirectoryError):
                is_empty(tmp_file.name)

    def test_raise_exception_if_file_bytes(self):
        with NamedTemporaryFile() as tmp_file:
            with self.assertRaises(NotADirectoryError):
                is_empty(tmp_file.name.encode('utf-8'))

    def test_raise_exception_if_file_path_like(self):
        with NamedTemporaryFile() as tmp_file:
            with self.assertRaises(NotADirectoryError):
                is_empty(Path(tmp_file.name))

    def test_raise_exception_if_not_exist_str(self):
        with self.assertRaises(FileNotFoundError):
            is_empty('/tmp/not_exist')

    def test_raise_exception_if_not_exist_bytes(self):
        with self.assertRaises(FileNotFoundError):
            is_empty('/tmp/not_exist'.encode('utf-8'))

    def test_raise_exception_if_not_exist_path_like(self):
        with self.assertRaises(FileNotFoundError):
            is_empty(Path('/tmp/not_exist'))
