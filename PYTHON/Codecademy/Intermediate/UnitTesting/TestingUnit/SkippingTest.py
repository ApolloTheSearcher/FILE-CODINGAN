# SkippingTest
'''
Terkadang kami memiliki pengujian yang seharusnya hanya berjalan dalam konteks tertentu. Misalnya,
kami mungkin memiliki sekelompok pengujian yang hanya berjalan di sistem operasi Windows tetapi tidak di
Linux atau macOS. Untuk situasi ini, akan sangat membantu jika Anda dapat melewati tes.
Jadi pada unittest terdapat 2 perbedaan alur untuk SkippingTest:
1. @unittest skip decorator
2. skipTest() method
Nah jika kita menggunakan skip decorator ada 2 hal yang harus diperhatikan:
@unittest.skipIf(condition, reason) => untuk melewati test jika kondisi tersebut bernilai True
@unitest.skipUnless(condition, reason) => untuk melewati test jika kondisi tersebut bernilai False
'''
import unittest
from Entertainment import entertainment

class EntertainmentSystemTests(unittest.TestCase):

    @unittest.skipIf(entertainment.regional_jet(), 'Not available on regional jets')
    def test_movie_license(self):
        daily_movie = entertainment.get_daily_movie()
        licensed_movies = entertainment.get_licensed_movies()
        self.assertIn(daily_movie, licensed_movies)

    @unittest.skipUnless(entertainment.regional_jet() is False, 'Not available on regional jets')
    def test_wifi_status(self):
        wifi_enabled = entertainment.get_wifi_status()
        self.assertTrue(wifi_enabled)

    def test_device_temperature(self):

        device_temp = entertainment.get_device_temp()
        self.assertLess(device_temp, 35)
        if entertainment.regional_jet() is True:
            self.skipTest('Not available on regional jets')

    def test_maximum_display_brightness(self):
        if entertainment.regional_jet() is True:
            self.skipTest('Not available on regional jets')
        brightness = entertainment.get_maximum_display_brightness()
        self.assertAlmostEqual(brightness, 400)
# Run the tests
unittest.main()