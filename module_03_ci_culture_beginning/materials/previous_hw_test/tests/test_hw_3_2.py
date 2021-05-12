import unittest

from module_02_linux.homework.hw_3_2 import app, storage


class TestFinaceApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        # self.storage = storage
        # print('setup', self.storage)
        storage = {
            '12121900': 666,
            '11111900': 334
        }
        self.storage = storage

    def test_can_add_sum_in_date(self):
        summ = '100'
        date = '20200101'
        print('??', self.storage)
        response = self.app.get("/add" + '/' + date + '/' + summ)
        response_text = response.data.decode()
        print('!', response_text)
        print('!!!', self.storage)
        self.assertTrue(date in storage)


