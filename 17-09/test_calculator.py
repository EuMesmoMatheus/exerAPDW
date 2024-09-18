import unittest
from calculator import WorkHourCalculator

class TestWorkHourCalculator(unittest.TestCase):

    def test_valid_work_hours(self):
        calculator = WorkHourCalculator()
        start_time = "08:00"
        end_time = "17:00"
        worked_hours = calculator.calculate_hours(start_time, end_time)
        self.assertEqual(worked_hours, 9)

    def test_invalid_format(self):
        calculator = WorkHourCalculator()
        with self.assertRaises(ValueError):
            calculator.calculate_hours("8am", "5pm")

    def test_lunch_break(self):
        calculator = WorkHourCalculator()
        start_time = "08:00"
        end_time = "17:00"
        lunch_break = "01:00"  # 1 hora de almoço
        worked_hours = calculator.calculate_hours(start_time, end_time, lunch_break)
        self.assertEqual(worked_hours, 8)  # 9 - 1 = 8 horas

    def test_reverse_time(self):
        calculator = WorkHourCalculator()
        start_time = "17:00"
        end_time = "08:00"
        worked_hours = calculator.calculate_hours(start_time, end_time)
        self.assertEqual(worked_hours, 15)  # Corrigido para refletir 15 horas de trabalho

    def test_no_colon(self):
        calculator = WorkHourCalculator()
        start_time = "0800"
        end_time = "1700"
        worked_hours = calculator.calculate_hours(start_time, end_time)
        self.assertEqual(worked_hours, 9)

    def test_midnight_shift(self):
        calculator = WorkHourCalculator()
        start_time = "23:00"
        end_time = "00:00"
        worked_hours = calculator.calculate_hours(start_time, end_time)
        self.assertEqual(worked_hours, 1)

    def test_lunch_break_format(self):
        calculator = WorkHourCalculator()
        start_time = "08:00"
        end_time = "17:00"
        lunch_breaks = ["00:30", "1:00", "01:00"]
        for lunch_break in lunch_breaks:
            worked_hours = calculator.calculate_hours(start_time, end_time, lunch_break)
            if lunch_break == "00:30":
                self.assertEqual(worked_hours, 8.5)
            elif lunch_break == "01:00":
                self.assertEqual(worked_hours, 8)
    
    def test_24_hour_format(self):
        calculator = WorkHourCalculator()
        start_time = "0000"
        end_time = "1200"
        worked_hours = calculator.calculate_hours(start_time, end_time)
        self.assertEqual(worked_hours, 12)

        start_time = "00:00"
        end_time = "12:00"
        worked_hours = calculator.calculate_hours(start_time, end_time)
        self.assertEqual(worked_hours, 12)

    def test_lunch_break_no_colon(self):
        calculator = WorkHourCalculator()
        start_time = "09:00"
        end_time = "18:00"
        lunch_break = "0015"  # 15 minutos de almoço
        worked_hours = calculator.calculate_hours(start_time, end_time, lunch_break)
        self.assertEqual(worked_hours, 8.75)  # 9 - 0.25 = 8.75 horas

if __name__ == '__main__':
    unittest.main()
