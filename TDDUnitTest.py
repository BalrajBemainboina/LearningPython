from TDDExample import Employee
from unittest.mock import  patch
import unittest


class TestingEmployee(unittest.TestCase):

    def setUp(self):
        print ('Setup')
        self.emp_1 = Employee('balraj','yadav',50000)
        self.emp_2 = Employee('banu','prakash',45000)

    def tearDown(self):
        print('Tearing down the setup')

    def test_email(self):
        print('Testing Email func')
        self.assertEqual(self.emp_1.email,'balraj.yadav@email.com')
        self.assertEqual(self.emp_2.email,'banu.prakash@email.com')

        self.emp_1.first = 'Janu'
        self.emp_2.first = 'kumar'

        self.assertEqual(self.emp_1.email, 'Janu.yadav@email.com')
        self.assertEqual(self.emp_2.email, 'kumar.prakash@email.com')

    def test_fullname(self):
        print('Testing Fullname Func')
        self.assertEqual(self.emp_1.fullname, 'balraj yadav')
        self.assertEqual(self.emp_2.fullname, 'banu prakash')

        self.emp_1.first = 'Janu'
        self.emp_2.first = 'kumar'

        self.assertEqual(self.emp_1.fullname, 'Janu yadav')
        self.assertEqual(self.emp_2.fullname, 'kumar prakash')

    def test_apply_raise(self):
        print('Testing apply_raise Func')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 250000)
        self.assertEqual(self.emp_2.pay, 225000)

''' def test_checkWebpage(self):
        with patch('Employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.emp_1.checkWebpage()
            mocked_get.assert_called_with('https://www.google.com/')
            self.assertEqual(schedule, 'Success')
'''

if __name__ == '__main__':
    main()
