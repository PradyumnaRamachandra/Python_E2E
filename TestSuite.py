import HtmlTestRunner
import os
import unittest


loader = unittest.TestLoader()
suite = loader.discover("C:\\PythonProjects\\Python_E2E\\Testcases")
runner=HtmlTestRunner.HTMLTestRunner(output="C:/PythonProjects/Python_E2E/reports")
if suite:
    runner.run(suite)