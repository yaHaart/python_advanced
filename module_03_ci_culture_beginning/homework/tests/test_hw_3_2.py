import unittest

import module_02_linux.homework.hw_3_2 as hw_3_2


class TestFinaceApp(unittest.TestCase):
    def setUp(self):
        hw_3_2.app.config['TESTING'] = True
        hw_3_2.app.config['DEBUG'] = False
        self.app = hw_3_2.app.test_client()
        self.storage = hw_3_2.storage

    def test_can_add_sum_in_date(self):
        summ = '100'
        date = '20200101'
        # print('??', self.storage)
        response = self.app.get("/add" + '/' + date + '/' + summ)
        response_text = response.data.decode()
        # print('!', response_text)
        # print('!!!', self.storage[date])
        self.assertTrue(self.storage[date] == int(summ))

    def test_can_calculate_year(self):
        hw_3_2.storage = {
            '19001225': 666,
            '19001226': 334,
            '19001125': 666,
            '19001025': 666,
        }
        response = self.app.get("/calculate/1900").data.decode().split()
        # print(response)
        self.assertTrue(response[0] == '2332')

    def test_can_calculate_month(self):
        hw_3_2.storage = {
            '19001225': 666,
            '19001226': 334,
            '19001125': 666,
            '19001025': 666,
        }
        response = self.app.get("/calculate/1900/12").data.decode().split()
        # print(response)
        self.assertTrue(response[0] == '1000')

    def test_date_formate(self):
        dates_to_check = [
            '10001212',
            '2002',
            '1212',
            'qqqqqqqq',
            ''

        ]


