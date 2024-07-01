'''this class in unittest.mock offers additional functionality hence the pref
choice of mockin in python.
it is a subclass of Mock and inherits all its capabilities
however it adds some extra magic to make mocking even easier and more flexible
'''
#with mock u need to def methods explicitly on the mock obj
#magicmock sutomatically creates methods on the fly
from unittest.mock import MagicMock
weather_api = MagicMock()
weather_api.get_temperature()  # This works even if not defined earlier!


'''using MagicMock in ur weather API test'''
from unittest.mock import MagicMock

def test_get_clothing_recommendation(self):
  weather_api = MagicMock()
  weather_api.get_temperature.return_value = 25
  with patch('your_program.weather_api', weather_api):
      recommended_clothing = get_clothing_recommendation()
      self.assertEqual(recommended_clothing, "T-shirt")
