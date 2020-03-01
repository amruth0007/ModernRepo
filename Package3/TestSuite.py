import unittest
from Package1.TC_Login import TC_login
from Package1.TC_SignUp import TC_SignUp
from Package2.TC_Payment import TC_Payment

TC1=unittest.TestLoader().loadTestsFromTestCase(TC_login)
TC2=unittest.TestLoader().loadTestsFromTestCase(TC_SignUp)
TC3=unittest.TestLoader().loadTestsFromTestCase(TC_Payment)

FunctionalTestSuite=unittest.TestSuite([TC1,TC2])
SanityTestSuite=unittest.TestSuite([TC3])
MasterTestSuite=unittest.TestSuite([TC1,TC2,TC3])

unittest.TextTestRunner().run(MasterTestSuite)

