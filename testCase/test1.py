from Myunittest import baseCase
import unittest
class test1(baseCase.baseCase):
    
    def test_add1(self):
        assert 1==1
        
    def test_add2(self):
        assert 1==2
        
if __name__=="__main__":
    
    unittest.main()