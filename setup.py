# encoding: utf-8
# THIS FILE IS AUTOGENERATED!
from __future__ import unicode_literals
from setuptools import setup
setup(
    author='Kyle Lahnakoski',
    author_email='kyle@lahnakoski.com',
    classifiers=["Development Status :: 4 - Beta","Topic :: Software Development :: Libraries","Topic :: Software Development :: Libraries :: Python Modules","License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)"],
    description='More Time! Time as a vector space, the way it was meant to be.',
    include_package_data=True,
    install_requires=["mo-dots>=3.46.20032","mo-future>=3.45.20031","mo-logs>=3.46.20032","mo-math>=3.41.20031"],
    license='MPL 2.0',
    long_description='\n\n# `Date` class\n\nA simplified date and time class for time manipulation. This library is intended for personal and business applications where assuming every solar day has 24 * 60 * 60 seconds is considered accurate. [See *GMT vs UTC* below](//#GMT%20vs%20UTC).\n\n\n## Assumptions\n\n* **All time is in GMT** - Timezone math is left to be resolved at the human endpoints: Machines should only be dealing with one type of time; without holes, without overlap, and with minimal context.\n* **Single time type** - There is no distinction between dates, datetime and times; all measurements in the time dimension are handled by one type called `Date`. This is important for treating time as a vector space.\n* **Standard range comparision** - All time range comparisons have been standardized to `min <= value < max`. The minimum is inclusive (`<=`), and the maximum is exclusive (`<`). \n\n\n# `Date` properties\n\n### `Date()` constructor\n\nThe `Date()` method will convert unix timestamps, millisecond timestamps, various string formats and simple time formulas to create a GMT time\n\n\n### `now()` staticmethod ###\n\nReturn `Date` instance with millisecond resolution (in GMT).\n\n### `eod()` staticmethod ###\n\nReturn end-of-day: Smallest `Date` which is greater than all time points in today. Think of it as tomorrow. Same as `now().ceiling(DAY)`\n\n### `today()` staticmethod ###\n\nThe beginning of today. Same as `now().floor(DAY)`\n\n\n### range(min, max, interval) staticmethod ###\n\nReturn an explicit list of `Dates` starting with `min`, each `interval` more than the last, but now including `max`.   Used in defining partitions in time domains.\n\n\n### `floor(duration=None)` method\n\nThis method is usually used to perform date comparisons at the given resolution (aka `duration`). Round down to the nearest whole duration. `duration` as assumed to be `DAY` if not provided.\n\n### `format(format="%Y-%m-%d %H:%M:%S")` method\n\nJust like `strftime`\n\n### `milli` property\n\nNumber of milliseconds since epoch\n\n### `unix` property\n\nNumber of seconds since epoch\n\n\n### `add(duration)` method\n\nAdd a `duration` to the time to get a new `Date` instance. The `self` is not modified.\n\n### `addDay()` method\n\nConvenience method for `self.add(DAY)`\n\n\n# `Duration` class\n\nRepresents the difference between two `Dates`. There are two scales:\n\n*  **`DAY` scale** - includes seconds, minutes, hours, days and weeks.\n*  **`YEAR` scale** - includes months, quarters, years, and centuries.\n\n### `Duration()` constructor\n\nCreate a new `Duration` by name, by formula, by `timespan`, or (more rarely) number of milliseconds.\n\n### `floor(interval=None)` method\n\nRound down to nearest `interval` size.\n\n### `seconds` property\n\nreturn total number of seconds (including partial) in this duration (estimate given for `YEAR` scale)\n\n### `total_seconds()` method ###\n\nSame as the `seconds` property\n\n### `round(interval, decimal=0)` method ###\n\nReturn number of given `interval` rounded to given `decimal` places\n\n### `format(interval, decimal=0)` method ###\n\nReturn a string representing `self` using given `interval` and `decimal` rounding\n\n\n# Time Vector Space\n\nThe `Date` and `Duration` objects are the point and vectors in a one dimensional vector space. As such, the `+` and `-` operators are allowed. Comparisons with (`>`, `>=`, `<=`, `<`) are also supported.\n\n\n## GMT vs UTC\n\nThe solar day is he most popular timekeeping unit. This library chose GMT (UT1) for its base clock because of its consistent seconds in a solar day. UTC suffers from inconsistent leap seconds and makes time-math difficult, even while forcing us to make pedantic conclusions like some minutes do not have 60 seconds. Lucky for us Python\'s implementation of UTC (`datetime.utcnow()`) is wrong, and implements GMT: Which is what we use.\n\n## Error Analysis\n\nAssuming we need a generous leap second each 6 months (the past decade saw only 4 leap seconds), then GMT deviates from UTC by up to 1 seconds over 181 days (December to June, 15,638,400 seconds) which is an error rate `error = 1/15,638,400 = 0.000006395%`. If we want to call the error "noise", we have a 70dB signal/noise ratio. All applications that can tolerate this level of error should use GMT as their time basis.\n\n\n',
    long_description_content_type='text/markdown',
    name='mo-times',
    packages=["mo_times/vendor/dateutil/zoneinfo","mo_times/vendor/dateutil","mo_times/vendor","mo_times"],
    url='https://github.com/klahnakoski/mo-times',
    version='3.46.20032'
)