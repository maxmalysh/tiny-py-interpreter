import os
import sys
import unittest
import subprocess
from subprocess import PIPE, STDOUT

#
# FIXME: make this work on Windows,
# FIXME: launch tinypy as a binary, not as a script, and check exit codes
#

in_directory = os.getcwd() + '/tests'
proper_tests_dir = in_directory
failing_tests_dir = in_directory + '/fail'

tinypy_binary = "python3 " + os.getcwd() + "/tinypy.py"
python_binary = sys.executable


class ParserTests(unittest.TestCase):

    def test_proper_syntax(self):
        for file in os.listdir(proper_tests_dir):
            if not file.endswith(".txt"):
                continue

            with self.subTest(msg=file):
                file_path = proper_tests_dir + '/' + file

                result = subprocess.run(
                    tinypy_binary + " --parse " + file_path, stdout=PIPE, stderr=STDOUT,
                    shell=True, universal_newlines=True
                )

                # self.assertEqual(result.returncode, 0)
                self.assertTrue(not result.stdout)
                self.assertTrue(not result.stderr)

    def test_fails(self):
        for file in os.listdir(failing_tests_dir):
            if not file.endswith(".txt"):
                continue

            with self.subTest(msg="fail/" + file):
                file_path = failing_tests_dir + '/' + file

                result = subprocess.run(
                    tinypy_binary + " --parse " + file_path, stdout=PIPE, stderr=STDOUT,
                    shell=True, universal_newlines=True
                )

                # self.assertNotEqual(result.returncode, 0)
                self.assertTrue(result.stdout != '')


class SemanticTests(unittest.TestCase):

    def test_semantics(self):
        for file in os.listdir(proper_tests_dir):
            if not file.endswith(".py"):
                continue

            with self.subTest(msg=file):
                file_path = proper_tests_dir + '/' + file

                tinypy_result = subprocess.run(
                    tinypy_binary + ' ' + file_path, stdout=PIPE, stderr=STDOUT,
                    shell=True, universal_newlines=True
                )
                python_result = subprocess.run(
                    python_binary + ' ' + file_path, stdout=PIPE, stderr=STDOUT,
                    shell=True, universal_newlines=True
                )

                # self.assertEqual(result.returncode, 0)
                self.assertEqual(tinypy_result.stdout, python_result.stdout)


if __name__ == '__main__':
    unittest.main()
