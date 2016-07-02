import unittest

class testCase(unittest.TestCase):
    
    
    
    
    def setUp(self):
        err=len(self._resultForDoCleanups.errors)+len(self._resultForDoCleanups.failures)
        print err
        print "set  up"
        
    def tearDown(self):
        err1=len(self._resultForDoCleanups.errors)+len(self._resultForDoCleanups.failures)
        print self._testMethodName
        
        print err1
        print "tear down"
        
    def testAdd(self):
        print "case 1"
        assert 3==4
        
if __name__=="__main__":
    try:
        
        unittest.main()
    except:
        pass
    exec "print \" hellp\""