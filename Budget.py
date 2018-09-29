import calendar
import datetime
import unittest


def find_budget(start, end):
    budget = {9: 1000, 10: 500, 11: 800, 12: 1000}

    diff_date = end - start + datetime.timedelta(days=1)

    start_day_of_month = calendar.monthrange(start.year, start.month)
    end_day_of_month = calendar.monthrange(end.year, end.month) 

    if start.month == end.month:
        return round(budget[start.month] / start_day_of_month[1] * diff_date.days, 2)
    else:
        first_month_day = start_day_of_month[1] - start.day  + 1
        first_month_budget = first_month_day * (budget[start.month] / start_day_of_month[1])
        second_month_budget = (diff_date.days - first_month_day) * (budget[end.month] / end_day_of_month[1])
        
        return round(first_month_budget + second_month_budget, 2)


class TestBudget(unittest.TestCase):
    def test_1_sep_to_1_sep_should_return_budget_33_dot_33(self):
        start = datetime.datetime(2018, 9, 1)
        end = datetime.datetime(2018, 9, 1)

        actual = find_budget(start, end)
        self.assertEqual(actual, 33.33)

    def test_1_sep_to_5_sep_should_return_budget_166_dot_67(self):
        start = datetime.datetime(2018, 9, 1)
        end = datetime.datetime(2018, 9, 5)

        actual = find_budget(start, end)
        self.assertEqual(actual, 166.67)

    def test_1_sep_to_10_oct_should_return_budget_1161_dot_29(self):
        start = datetime.datetime(2018, 9, 1)
        end = datetime.datetime(2018, 10, 10)

        actual = find_budget(start, end)
        self.assertEqual(actual, 1161.29)

    def test_3_sep_to_10_oct_should_return_budget_1161_dot_29(self):
        start = datetime.datetime(2018, 10, 3)
        end = datetime.datetime(2018, 11, 10)

        actual = find_budget(start, end)
        self.assertEqual(actual, 734.41)

    def test_3_sep_to_10_oct_should_return_budget_1161_dot_29(self):
        start = datetime.datetime(2018, 10, 5)
        end = datetime.datetime(2018, 12, 10)

        actual = find_budget(start, end)
        self.assertEqual(actual, 734.41)


unittest.main()
