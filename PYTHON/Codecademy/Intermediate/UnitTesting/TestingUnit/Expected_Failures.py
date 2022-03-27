# Hampir sama kerja nya seperti Skipping Test menggunakan decorator unittest
# unittest.expectedFailure() => untuk menangani error yang tidak diinginkan
# diselingi dengan raise atau assert method lainnya
# Contoh program:
import unittest
from Feedback import feedback

class CustomerFeedbackTests(unittest.TestCase):

    # Write your code below:
    @unittest.expectedFailure # untuk menangani error yang tidak diinginkan
    def test_survey_form(self):
        self.assertEqual(feedback.issue_survey(), 'Success')

    def test_complaint_form(self):
        self.assertEqual(feedback.log_customer_complaint(), 'Success')

unittest.main()