import calendar
import datetime
import unittest


def get_total_days_from(first, last):
    days_in_period = last - first
    first_day_of_period = datetime.timedelta(days=1)
    return (days_in_period + first_day_of_period).days


def get_days_of_month(date):
    # recomment to __
    _, days_in_month = calendar.monthrange(date.year, date.month)
    return days_in_month


def get_budget_per_day(budget_in_month, days_in_month):
    return budget_in_month / days_in_month


def get_first_month_budget(budget, first, total_days_in_first_month):
    average_first_budget = get_budget_per_day(
        budget[first.month],
        total_days_in_first_month
    )
    days_in_first_month = total_days_in_first_month - first.day + 1
    first_month_budget = average_first_budget * days_in_first_month

    return first_month_budget


def get_last_month_budget(
    budget,
    first,
    last,
    total_days_in_first_month,
    total_days_in_last_month,
    total_days,
):
    average_last_month_budget = get_budget_per_day(
        budget[last.month],
        total_days_in_last_month
    )
    days_in_last_month = total_days - (total_days_in_first_month - first.day + 1)
    last_month_budget = average_last_month_budget * days_in_last_month

    return last_month_budget

# def get_range_month_budget():
    
def find_budget(first, last):
    budget = {
        9: 1000,
        10: 500,
        11: 800,
        12: 1000,
    }

    total_days = get_total_days_from(first, last)

    total_days_in_first_month = get_days_of_month(first)
    total_days_in_last_month = get_days_of_month(last)
    
    amount = get_first_month_budget(budget, first, total_days_in_first_month)

    for month in range(first.month + 1, last.month):
        amount += budget[month]
        total_days -= get_days_of_month(datetime.date(first.year, month, 1))
    
    amount += get_last_month_budget(
        budget,
        first,
        last,
        total_days_in_first_month,
        total_days_in_last_month,
        total_days,
    )

    return round(amount, 2)


class TestBudget(unittest.TestCase):
    def test_1_sep_to_1_sep_should_return_budget_33_dot_33(self):
        first = datetime.datetime(2018, 9, 1)
        last = datetime.datetime(2018, 9, 1)

        actual = find_budget(first, last)
        self.assertEqual(actual, 33.33)

    def test_1_sep_to_5_sep_should_return_budget_166_dot_67(self):
        first = datetime.datetime(2018, 9, 1)
        last = datetime.datetime(2018, 9, 5)

        actual = find_budget(first, last)
        self.assertEqual(actual, 166.67)

    def test_1_sep_to_10_oct_should_return_budget_1161_dot_29(self):
        first = datetime.datetime(2018, 9, 1)
        last = datetime.datetime(2018, 10, 10)

        actual = find_budget(first, last)
        self.assertEqual(actual, 1161.29)

    def test_3_sep_to_10_oct_should_return_budget_1161_dot_29(self):
        first = datetime.datetime(2018, 10, 3)
        last = datetime.datetime(2018, 11, 10)

        actual = find_budget(first, last)
        self.assertEqual(actual, 734.41)

    # @unittest.skip(reason='Still failed')
    def test_5_oct_to_10_dec_should_return_budget_734_dot_41(self):
        first = datetime.datetime(2018, 9, 5)
        last = datetime.datetime(2018, 12, 10)

        actual = find_budget(first, last)
        self.assertEqual(actual, 2489.25)


unittest.main()
