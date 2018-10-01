import calendar
import datetime
import unittest


def get_total_day_from(start, end):
    days_in_period = end - start
    first_day_of_period = datetime.timedelta(days=1)
    return (days_in_period + first_day_of_period).days


def get_days_of_month(date):
    # recomment to __
    _, days_in_month = calendar.monthrange(date.year, date.month)
    return days_in_month


def get_budget_per_day(budget_in_month, days_in_month):
    return budget_in_month / days_in_month


def find_budget(start, end):
    budget = {
        9: 1000,
        10: 500, 
        11: 800,
        12: 1000,
    }

    total_day = get_total_day_from(start, end)

    total_days_in_start_month = get_days_of_month(start)
    total_days_in_end_month = get_days_of_month(end)

    average_start_budget = get_budget_per_day(budget[start.month], total_days_in_start_month)
    amount = 0

    if start.month == end.month:
        amount = average_start_budget * total_day
    else:
        days_in_start_month = total_days_in_start_month - start.day + 1
        first_month_budget = average_start_budget * days_in_start_month

        for month in range(start.month+1, end.month):
            amount += budget[month]
            total_day -= get_days_of_month(datetime.date(start.year, month, 1))
        
        average_end_month_budget = get_budget_per_day(budget[end.month], total_days_in_end_month)

        days_in_end_month = total_day - days_in_start_month
        end_month_budget =  average_end_month_budget * days_in_end_month

        amount += first_month_budget + end_month_budget

    return round(amount, 2)


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

    # @unittest.skip(reason='Still failed')
    def test_5_oct_to_10_dec_should_return_budget_734_dot_41(self):
        start = datetime.datetime(2018, 9, 5)
        end = datetime.datetime(2018, 12, 10)

        actual = find_budget(start, end)
        self.assertEqual(actual, 2489.25)


unittest.main()
