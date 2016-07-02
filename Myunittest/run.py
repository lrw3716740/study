import unittest
import sys
sys.path.append("../testCase/")
from unittest.suite import TestSuite
from test1 import  *

from Myunittest.baseCase import baseCase


def getSuite():
    
    suite=unittest.TestSuite()
    
    suite.addTest(unittest.makeSuite(test1))
    return suite
    
if __name__=="__main__":

    suite=getSuite()
    runner=unittest.TextTestRunner()
    runner.run(suite)
    