from email.utils import collapse_rfc2231_value
from symtable import Symbol
import unittest
from xmlrpc.client import DateTime
import datetime
from ast import Lambda
import chart
import time


#Test symbol Charctrized 1-7
class TestSymbol(unittest.TestCase):
    def test_Symbol(self):
        fetch_symbol = symbol("alpha charcters")
        self.assertEqual (fetch_symbol.captilized 1-7,"Enter the stock symbol you are looking for")

#Test Chart type
class Testchart(unittest):
    def test_chart(self):
        chart_1 = ("datesObeject 1")
        chart_2 = ("datesObject 2")

        self.assertEqual(chart_1.object, "datesObject1")
        self.assertEqual(chart_2.object, "datesObject2")

#Chart Type Error

def one_two(self):

    self.assertRaises(ValueError, one_two)

       if __name__ == '__main__':
            unittest.main(one_two, "Please only enter 1 or 2")



#Test time series
class Testtime(unittest):
    def test_time(self):
        case_interval = time("intervalChoice")
        self.assertEqual(case_1.interval,"1")
        self.assertEqual(case_2.interval,"5")
        self.assertEqual(case_3.interval,"15")
        self.assertEqual(case_4.interval,"30")
        case_1 = "1"
        case_2 = "5"
        case_3 = "15"
        case_4 = "30"
        
#time series error
def unexpected_value(self):

     self.assertRaises(ValueError, unexpected_value)

        if __name__ == '__main__':
            unittest.main(unexpected_value, "This is an unacceptable response, enter a valid value")


#end date test
class Testdate(unittest.TestCase):
   
    def test_date(self):
       end_date = Date('YYYY-MM-DD')
       self.assertEqual(end_date, "2021-05-16")
#Start date test
    def start_date(self):
        start_Date = startDate('YYYY-MM-DD')
        self.assertEqual(start_Date, "2021-03-15")


#before begening error
def test_beforebeg(self):

    self.assertRaises(ValueError, test_beforebeg)

       if __name__ == '__main__':
            unittest.main(test_beforebeg, "The ending date must not be before the beginning date")