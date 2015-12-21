import os
import sys
import unittest
import subprocess
from subprocess import PIPE, STDOUT

#
# FIXME: make this work on Windows,
# FIXME: launch tinypy as a binary, not as a script, and check exit codes
#

in_directory = os.getcwd() + '/tinypy/tests'
proper_tests_dir = in_directory
failing_tests_dir = in_directory + '/fail'

python_binary = sys.executable
tinypy_binary = "tinypy"


class FileTestCase(unittest.TestCase):

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def __str__(self):
        return self.__class__.__name__ + ":" + os.path.basename(self.file_path)


class ProperParserTest(FileTestCase):

    def runTest(self):
        result = subprocess.run(
            tinypy_binary + " --parse " + self.file_path, stdout=PIPE, stderr=STDOUT,
            shell=True, universal_newlines=True
        )

        #self.assertEqual(result.returncode, 0)
        self.assertTrue(not result.stdout)
        self.assertTrue(not result.stderr)


class FailingParserTest(FileTestCase):

    def runTest(self):
        result = subprocess.run(
            tinypy_binary + " --parse " + self.file_path, stdout=PIPE, stderr=STDOUT,
            shell=True, universal_newlines=True
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(result.stdout != '')


class SemanticTest(FileTestCase):

    def runTest(self):
        tinypy_result = subprocess.run(
            tinypy_binary + ' ' + self.file_path, stdout=PIPE, stderr=STDOUT,
            shell=True, universal_newlines=True
        )
        python_result = subprocess.run(
            python_binary + ' ' + self.file_path, stdout=PIPE, stderr=STDOUT,
            shell=True, universal_newlines=True
        )

        self.assertEqual(tinypy_result.returncode, python_result.returncode)
        self.assertEqual(tinypy_result.stdout, python_result.stdout)


def get_suite():
    suite = unittest.TestSuite()

    for file in os.listdir(proper_tests_dir):

        if file.endswith(".txt"):
            file_path = proper_tests_dir + '/' + file
            suite.addTest(ProperParserTest(file_path))

        elif file.endswith(".py"):
            file_path = proper_tests_dir + '/' + file
            suite.addTest(SemanticTest(file_path))

    for file in os.listdir(failing_tests_dir):
        if file.endswith(".txt"):
            file_path = failing_tests_dir + '/' + file
            suite.addTest(FailingParserTest(file_path))

    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(get_suite())
