from time import sleep
from unittest import TestCase

from mo_logs import logger

from mo_times import Timer
from tests import StructuredLogger_usingList


class TestTimer(TestCase):
    def test_timer(self):
        logger.main_log, temp = StructuredLogger_usingList(), logger.main_log
        with Timer("test {i}", param=dict(i=10), verbose=True) as timer:
            pass

        self.assertLogs(timer.duration, 0.001)
        self.assertEqual(logger.main_log.lines[0], "Timer start: test 10")
        self.assertTrue(logger.main_log.lines[1].startswith("Timer end  : test 10 (took 0"))
        logger.main_log = temp

    def test_timer_too_long(self):
        logger.main_log, temp = StructuredLogger_usingList(), logger.main_log
        with Timer("test {i}", param=dict(i=10), verbose=True, too_long=0.1) as timer:
            sleep(0.15)

        self.assertLogs(timer.duration, 0.15)
        self.assertEqual(logger.main_log.lines[0], "Timer start: test 10")
        self.assertTrue(logger.main_log.lines[1].startswith("Time too long: test 10 "))
        logger.main_log = temp

    def test_timer_too_long_quiet(self):
        logger.main_log, temp = StructuredLogger_usingList(), logger.main_log
        with Timer("test {i}", param=dict(i=10), too_long=0.1) as timer:
            sleep(0.05)

        self.assertEqual(len(logger.main_log.lines), 0)
        logger.main_log = temp
