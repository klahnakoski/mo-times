# encoding: utf-8
#
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Author: Kyle Lahnakoski (kyle@lahnakoski.com)
#

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from datetime import datetime

from mo_math import MAX
from mo_testing.fuzzytestcase import FuzzyTestCase

from mo_times.dates import Date
from mo_times.durations import MONTH, YEAR, WEEK, Duration, DAY


class TestDate(FuzzyTestCase):


    def test_mising_milli(self):
        date = Date("2015-10-04 13:53:11", '%Y-%m-%d %H:%M:%S.%f')
        expecting = Date(datetime(2015, 10, 4, 13, 53, 11))
        self.assertEqual(date, expecting)

    def test_max(self):
        date = Date("2015-10-04 13:53:11", '%Y-%m-%d %H:%M:%S.%f')
        self.assertEqual(MAX([None, date]), date)

    def test_floor_quarter(self):
        date = Date("2015-10-04 13:53:11", '%Y-%m-%d %H:%M:%S.%f')
        f = date.floor(3*MONTH)
        expected = Date("2015-10-01")
        self.assertEqual(f, expected)

    def test_floor_year(self):
        date = Date("2015-10-04 13:53:11", '%Y-%m-%d %H:%M:%S.%f')
        f = date.floor(YEAR)
        expected = Date("2015-01-01")
        self.assertEqual(f, expected)

    def test_floor_year2(self):
        date = Date("2015-10-04 13:53:11", '%Y-%m-%d %H:%M:%S.%f')
        f = date.floor(2*YEAR)
        expected = Date("2014-01-01")
        self.assertEqual(f, expected)

    def test_floor_week(self):
        date = Date('2016-09-30 15:51:50')
        f = date.floor(WEEK)
        expected = Date("2016-09-25")
        self.assertEqual(f, expected)

    def test_dow(self):
        date = Date('2018-10-01 12:42:00')
        self.assertEqual(date.dow, 0)   # MONDAY

    def test_ceiling_hours(self):
        date = Date('2018-10-01 12:42:00').ceiling(Duration("6hour"))
        expected = Date('2018-10-01 18:00:00')
        self.assertEqual(date, expected)

    def test_ceiling_hours_unchanged(self):
        date = Date('2018-10-01 18:00:00').ceiling(Duration("6hour"))
        expected = Date('2018-10-01 18:00:00')
        self.assertEqual(date, expected)

    def test_create_date(self):
        from datetime import timezone
        test = Date(datetime(2020, 3, 21, 0, 0, 0, 0, timezone.utc))
        self.assertEqual(float(test), 1584748800)

    def test_div(self):
        diff = Date.now()-(Date.now()-DAY)
        self.assertEqual(diff/DAY, 1)