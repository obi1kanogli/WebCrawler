import unittest
from crawler import main
from click.testing import CliRunner


class TestCrawler(unittest.TestCase):
    """
    Test if running with more threads executes faster
    """
    def test_multiprocessing(self):
        runner = CliRunner()
        elapsed_with = runner.invoke(main,
                                     '--base_url="https://www.pdx.edu" '
                                     '--limit=30 '
                                     '--threads=20').output
        elapsed_without = runner.invoke(main,
                                        '--base_url="https://www.pdx.edu" '
                                        '--limit=30 '
                                        '--threads=1').output
        self.assertFalse(elapsed_with < elapsed_without)


if __name__ == '__main__':
    unittest.main()
