# Unit Testing Framework:
# Sebelumnya jika kita menggunakan assert statement, kita harus mengimplementasikan fungsi yang akan ditesting. jadinya cape kan.
# Nah di python sudah tersedia framework yang bisa kita gunakan untuk mengimplementasikan unit testing.
# Framework ini kerjanya pada modul unittest sehingga kita harus mengimportnya terlebih dahulu
# Contoh penggunaan:
# your code below:
# Importing unittest framework
import unittest
from Entertainment import entertainment, entertainment2
from Alerts import alerts
from KIOSK import kiosk
# TEST 1
# Fungsi yang digunakan untuk testnya
def get_nearest_exit(row_number):
    if row_number < 15:
        location = 'front'
    elif row_number < 30:
        location = 'middle'
    else:
        location = 'back'
    return location

# Write your code below:
# Test Classnya:
class NearestExitTests(unittest.TestCase):
    def test_row_1(self):
        self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')

    def test_row_20(self):
        self.assertEqual(get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')

    def test_row_40(self):
        self.assertEqual(get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')
# Run the tests
unittest.main()

'''
Cara penulisan Unit Testing: ketika menggunakan modul unittest pada function di class
self.PerintahAssertion(value1, value2, message)
untuk PerintahAssertion bisa pakai yang assertEqual atau yang lainnya
'''
# Perintah Assertion (Assertion Method):
'''
Equality and Membership Assert Method:
- self.assertEqual(a, b, msg=None) ekuivalen dengan assert a == b
- self.assertNotEqual(a, b, msg=None) ekuivalen dengan assert a != b
- self.assertIn(a, b, msg=None) ekuivalen dengan assert a in b contoh assertIn(5, [1, 2, 3, 4]) ekuivalen dengan assert 5 in [1, 2, 3, 4]
- self.asserTrue(x, msg=None) ekuivalen dengan assert bool(x) is True
Quantity Assert Method:
- self.assertLess(a, b, msg=None) ekuivalen dengan assert a < b
- self.assertAlmostEqual(value1, value2) ekuivalen dengan assert round(value1, value2) == 0 (dipakai untuk menghitung desimal)
Exception and Warning Assert Method:
- self.assertRaise(specificException, function, functionArguments...)
-self.assertWarns(specificWarningException, function, functionArguments...)
'''
# Contoh penggunaan: kita import folder entertainment yang ada di folder ini

# Write your code below: 
# Ini untuk test menggunakan Equality and Membership Assert Method
# TEST 2
class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self, daily_movie, licensed_movies):
        daily_movie = entertainment.get_daily_movie()
        self.assertIn(daily_movie, licensed_movies)
        licensed_movies = entertainment.get_licensed_movies()



    def test_wifi_status(self):
        wifi_enabled = entertainment.get_wifi_status()
        self.assertTrue(wifi_enabled)
# Run the tests
unittest.main()
# ===============================================================
# Contoh penggunaan Quantity Assert Method:
# TEST 3
class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        daily_movie = entertainment.get_daily_movie()
        licensed_movies = entertainment.get_licensed_movies()
        self.assertIn(daily_movie, licensed_movies)

    def test_wifi_status(self):
        wifi_enabled = entertainment.get_wifi_status()
        self.assertTrue(wifi_enabled)

    # Write your code below:
    def test_maximum_display_brightness(self):
        brightness = entertainment.get_maximum_display_brightness()
        self.assertAlmostEqual(brightness, 400)
    def test_device_temperature(self):
        device_temp = entertainment.get_device_temp()
        self.assertLess(device_temp, 35)
# Run the tests
unittest.main()
# ===============================================================
# Contoh penggunaan Exception and Warning Assert Method:
# TEST 4
class SystemAlertTests(unittest.TestCase):
    pass
    def test_power_outage_alert(self):
        self.assertRaises(alerts.PowerError, alerts.power_outage_detected, True)
    def test_water_levels_warning(self):
        self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, 150)
# Run the tests
unittest.main()
# ===============================================================
# Nah kan kita pernah membuat suatu program add dengan menggunakan expection hanya saja itu kurang efisien
# dimana dia berkerja untuk fungsi berbagai input
# Namun, logika sebenarnya dari pengujian kami benar-benar tidak berubah, untuk menghindari perulangan
# Python memberikan perangkat khusus ntuk pengujian dengan hanya sedikit perbedaan. Ini dikenal sebagai
# Test Parameterization 
# Namanya itu subTest / bisa digunakan dengan with subTest(parameter)
# Contoh
import unittest

class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        daily_movies = entertainment2.get_daily_movies()
        licensed_movies = entertainment2.get_licensed_movies()
    # Write your code below:
        for movie in daily_movies:
            print(movie)
            with self.subTest(movie):
                self.assertIn(movie, licensed_movies)
# Run the tests
unittest.main()
# ===============================================================
# Text Fixtures
# Jadi kita disini itu menggunakan text fixture jadi kita bisa membetulkan suatu error dengan menggunakan @classmethod (decorator)
# Contoh:
class CheckInKioskTests(unittest.TestCase):

    def test_check_in_with_flight_number(self):
        print('Testing the check-in process based on flight number')

    def test_check_in_with_passport(self):
        print('Testing the check-in process based on passport')
    # Checkpoint 2
    @classmethod
    def tearDownClass(cls):
        kiosk.power_off_kiosk()
    @classmethod
    def setUpClass(cls):
        kiosk.power_on_kiosk()

    def setUp(self):
        kiosk.return_to_welcome_page()
# Run the tests
unittest.main()
# ===============================================================


# Ini perubahan contoh cara update GIT TESTING