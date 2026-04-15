import unittest
from city_function import get_place
"""测试城市和国家的函数"""
class NamesTestCase(unittest.TestCase):
    """测试city_function.py"""
    def test_city_country(self):
         formatted_place=get_place('香港','中国','20000000')
         self.assertEqual(formatted_place,'香港, 中国人口20000000')
    def test_city_country(self):
         formatted_place=get_place('广州','中国','10000000')
         self.assertEqual(formatted_place,'广州, 中国人口10000000')

    
if __name__=='__main__':
    unittest.main()
    