import unittest
from parameterized import parameterized
from functions import *


class FunctionTest(unittest.TestCase):

    @parameterized.expand([
        [1, 1, 8, 8.0, 1.0],
        [4.4493, 4.9012, 500, 453.9, 0.9077980902636089],
        [1.1209, 4.936, 200, 45.42, 0.2270867098865478],
        [4, 2, 50, 100, 2.0],
        [2, 4, 50, 25.0, 0.5],
        ["", 1, 10, "ERROR3"],
        [1, "", 10, "ERROR3"],
        ["xyz", 1, 10, "ERROR3"],
        [1, "xyz", 10, "ERROR3"],
        [6, 3, "10,5", "ERROR3"],
        [6, 3, "xyz", "ERROR3"],
        [2, 0, 10, "ERROR4"],
    ])
    def test_1(self, ex_rate_1, ex_rate_2, value, final_result, currency_ratio=None):

        if currency_ratio is not None:
            self.assertEqual(calculate_result(
                ex_rate_1, ex_rate_2, value), (final_result, currency_ratio))
        else:
            self.assertEqual(calculate_result(
                ex_rate_1, ex_rate_2, value), final_result)

    test_nbp_list = {'table': 'A', 'no': '248/A/NBP/2020', 'effectiveDate': '2020-12-21', 'rates':
                     [{'currency': 'Polish Zloty', 'code': 'PLN', 'mid': 1.0},
                      {'currency': 'bat (Tajlandia)',
                       'code': 'THB', 'mid': 0.1233},
                         {'currency': 'dolar amerykański',
                             'code': 'USD', 'mid': 3.7082},
                         {'currency': 'dolar australijski',
                             'code': 'AUD', 'mid': 2.7802},
                      ]}
    test_nbp_list_corrupted = {'table': 'A', 'no': '248/A/NBP/2020', 'EEEeffectiveDate': '2020-12-21', 'rates':
                               [{'currency': 'Polish Zloty', 'code': 'PLN', 'mid': 1.0},
                                ]}
    test_nbp_list_corrupted1 = {'table': 'A', 'no': '248/A/NBP/2020', 'effectiveDate': '2020-12-21', 'RRRrates':
                                [{'currency': 'Polish Zloty', 'code': 'PLN', 'mid': 1.0},
                                 ]}
    test_nbp_list_corrupted2 = {'table': 'A', 'no': '248/A/NBP/2020', 'effectiveDate': '2020-12-21', 'rates':
                                [{'currency': 'Polish Zloty', 'code': 'PLN', 'midDDD': 1.0},
                                 ]}
    test_nbp_list_corrupted3 = {}

    @parameterized.expand([
        [test_nbp_list, 'effectiveDate', '2020-12-21'],
        [test_nbp_list, 'THB', 0.1233],
        [test_nbp_list, 'AUD', 2.7802],
        [test_nbp_list, '', 'ERROR2'],
        [test_nbp_list, 'USDD', 'ERROR2'],
        [test_nbp_list, 'effectiveDateEEE', 'ERROR2'],
        [test_nbp_list_corrupted, 'effectiveDate', 'ERROR2.2'],
        [test_nbp_list_corrupted1, 'PLN', 'ERROR2.2'],
        [test_nbp_list_corrupted2, 'PLN', 'ERROR2.2'],
        [test_nbp_list_corrupted3, 'PLN', 'ERROR2.2'],
    ])
    def test_2(self, test_nbp_list, request, reply):

        self.assertEqual(extracting_data_nbp_reply(
            test_nbp_list, request), reply)


if __name__ == '__main__':
    unittest.main()
