# encoding: utf-8
#
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Author: Kyle Lahnakoski (kyle@lahnakoski.com)
#

from datetime import datetime

from mo_math import MAX
from mo_testing.fuzzytestcase import FuzzyTestCase, add_error_reporting
from mo_threads import join_all_threads, Thread

from mo_times.dates import Date
from mo_times.durations import MONTH, YEAR, WEEK, Duration, DAY, HOUR


@add_error_reporting
class TestDate(FuzzyTestCase):
    def test_mising_milli(self):
        date = Date("2015-10-04 13:53:11", "%Y-%m-%d %H:%M:%S.%f")
        expecting = Date(datetime(2015, 10, 4, 13, 53, 11))
        self.assertEqual(date, expecting)

    def test_max(self):
        date = Date("2015-10-04 13:53:11", "%Y-%m-%d %H:%M:%S.%f")
        self.assertEqual(MAX([None, date]), date)

    def test_floor_quarter(self):
        date = Date("2015-10-04 13:53:11", "%Y-%m-%d %H:%M:%S.%f")
        f = date.floor(3 * MONTH)
        expected = Date("2015-10-01")
        self.assertEqual(f, expected)

    def test_floor_year(self):
        date = Date("2015-10-04 13:53:11", "%Y-%m-%d %H:%M:%S.%f")
        f = date.floor(YEAR)
        expected = Date("2015-01-01")
        self.assertEqual(f, expected)

    def test_floor_year2(self):
        date = Date("2015-10-04 13:53:11", "%Y-%m-%d %H:%M:%S.%f")
        f = date.floor(2 * YEAR)
        expected = Date("2014-01-01")
        self.assertEqual(f, expected)

    def test_floor_week(self):
        date = Date("2016-09-30 15:51:50")
        f = date.floor(WEEK)
        expected = Date("2016-09-25")
        self.assertEqual(f, expected)

    def test_dow(self):
        date = Date("2018-10-01 12:42:00")
        self.assertEqual(date.dow, 0)  # MONDAY

    def test_ceiling_hours(self):
        date = Date("2018-10-01 12:42:00").ceiling(Duration("6hour"))
        expected = Date("2018-10-01 18:00:00")
        self.assertEqual(date, expected)

    def test_ceiling_hours_unchanged(self):
        date = Date("2018-10-01 18:00:00").ceiling(Duration("6hour"))
        expected = Date("2018-10-01 18:00:00")
        self.assertEqual(date, expected)

    def test_create_date(self):
        from datetime import timezone

        test = Date(datetime(2020, 3, 21, 0, 0, 0, 0, timezone.utc))
        self.assertEqual(float(test), 1584748800)

    def test_div(self):
        now = Date.now()
        diff = now - (now - DAY)
        self.assertEqual(diff / DAY, 1)

    def test_date_range(self):
        result = list(Date.range(Date("2011-01-01"), Date("2021-01-01"), YEAR))
        expected = [
            1293840000,
            1325376000,
            1356998400,
            1388534400,
            1420070400,
            1451606400,
            1483228800,
            1514764800,
            1546300800,
            1577836800,
        ]
        self.assertAlmostEqual(result, expected)
        self.assertAlmostEqual(expected, result)

    def test_hour_equals_hour(self):
        self.assertEqual(Date("hour"), HOUR)

    def test_parse_w_timezone(self):
        test = Date("2022-02-04T06:05:55.038+0000")
        expect = Date("2022-02-04T06:05:55.038000")
        self.assertEqual(test, expect)

    def test_duration_hashable(self):
        a = {Duration("hour"): "hour"}
        self.assertEqual(a[Duration("60minute")], "hour")

    def test_int(self):
        now = Date.now()
        self.assertEqual(int(now), int(now.unix))

        dur = Duration(12.45)
        self.assertEqual(int(dur), 12)

        dur = Duration(seconds=12.45)
        self.assertEqual(int(dur), 12)

    def test_date(self):
        example = "2023-03-25 17:04:01"
        result = Date(example)
        self.assertEqual(result.format(), example)

    def test_date2(self):
        example = "2023-11-10 20:17:35.821719"
        result = Date(example)
        self.assertEqual(result.format("%Y-%m-%d %H:%M:%S.%f"), example)

    def test_date3(self):
        example = "February 3, 2023"
        result = Date(example).format("%Y-%m-%d")
        self.assertEqual(result, "2023-02-03")

    def test_date4(self):
        example = "Feb. 3"
        result = Date(example).format("%Y-%m-%d")

        today = Date.today()
        if today < Date(f"{today.year}-02-03"):
            expected = f"{today.year-1}-02-03"
        else:
            expected = f"{today.year}-02-03"
        self.assertEqual(result, expected)

    def test_subtraction(self):
        now = Date.now().datetime
        self.assertIsInstance(now - MONTH, Date)
        self.assertEqual(Date(now - MONTH), Date(now) - MONTH)

    def test_month_feb(self):
        self.assertEqual(Date("2024-02-27") - YEAR, Date("2023-02-27"))
        self.assertEqual(Date("2024-02-28") - YEAR, Date("2023-02-28"))
        self.assertEqual(Date("2024-02-29") - YEAR, Date("2023-02-28"))
        self.assertEqual(Date("2024-03-01") - YEAR, Date("2023-03-01"))

        self.assertEqual(Date("2023-02-27") + YEAR, Date("2024-02-27"))
        self.assertEqual(Date("2023-02-28") + YEAR, Date("2024-02-29"))
        self.assertEqual(Date("2024-02-29") + YEAR - YEAR, Date("2024-02-29"))

        self.assertEqual(Date("2024-03-01") - YEAR, Date("2023-03-01"))
        self.assertEqual(Date("2023-01-28") + MONTH, Date("2023-02-28"))
        self.assertEqual(Date("2023-01-29") + MONTH, Date("2023-02-28"))
        self.assertEqual(Date("2023-01-30") + MONTH, Date("2023-02-28"))
        self.assertEqual(Date("2023-01-31") + MONTH, Date("2023-02-28"))
        self.assertEqual(Date("2023-01-31") + MONTH + MONTH, Date("2023-03-31"))

    def test_year_is_year(self):
        now = Date.now()
        self.assertEqual(now + YEAR, now + Duration(YEAR))

    def test_single_digits(self):
        self.assertEqual(Date("2023-01-01"), Date("2023-1-1"))

    def test_single_digits2(self):
        self.assertEqual(Date("2023-01-01"), Date("2023-1-01"))

    def test_single_time_digits(self):
        self.assertEqual(Date("2023-01-01 01:01:01"), Date("2023-01-01 1:1:1"))

    def test_div(self):
        self.assertEqual("day"/HOUR, 24)
        self.assertEqual(DAY/"hour", 24)


    def test_many_decoders(self):

        def parser(please_stop):
            for i in range(50):
                Date("3 jan 2024")
                Date("20-01-2023")
                Date("2024-02-16")

        join_all_threads([Thread.run(str(i), parser) for i in range(100)])


