import data
import unittest
import final_project

class TestCases(unittest.TestCase):
    # Test county_consumption
    def test_county_consumption(self):
        expected = 2724953
        result = final_project.county_consumption(data.counties, "Placer County")
        assert expected == result

    #Test daily_average
    def test_daily_average(self):
        expected = 5.7 #kilowatts per person
        result = final_project.county_res_average(data.counties, "Los Angeles County")
        assert expected == result

    #Test Commercial_usage
    def test_commercial_usage(self):
        expected = 3099.2
        result = final_project.commercial_usage(data.counties, "Placer County")
        assert expected == result

    # Test Commercial_usage
    def test_industrial_usage(self):
        expected = 27754.0
        result = final_project.industrial_usage(data.counties, "Los Angeles County")
        assert expected == result








if __name__ == '__main__':
    unittest.main()