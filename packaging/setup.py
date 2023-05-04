# encoding: utf-8
# THIS FILE IS AUTOGENERATED!
from setuptools import setup
setup(
    author='Kyle Lahnakoski',
    author_email='kyle@lahnakoski.com',
    classifiers=["Development Status :: 4 - Beta","Programming Language :: Python :: 3.7","Programming Language :: Python :: 3.9","Topic :: Software Development :: Libraries","Topic :: Software Development :: Libraries :: Python Modules","License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)","Programming Language :: Python :: 3.10","Programming Language :: Python :: 3.8"],
    description='More Time! Time as a vector space, the way it was meant to be.',
    extras_require={"tests":["mo-testing>3"]},
    include_package_data=True,
    install_requires=["mo-dots==9.376.23121","mo-future==7.340.23006","mo-logs==7.378.23124","mo-math==7.378.23124"],
    license='MPL 2.0',
    long_description='# More Times!\n\nAssume time forms an algebraic field over GMT. Finally! \n\n[![PyPI Latest Release](https://img.shields.io/pypi/v/mo-times.svg)](https://pypi.org/project/mo-times/)\n[![Build Status](https://app.travis-ci.com/klahnakoski/mo-times.svg?branch=master)](https://travis-ci.com/github/klahnakoski/mo-times)\n [![Coverage Status](https://coveralls.io/repos/github/klahnakoski/mo-times/badge.svg?branch=dev)](https://coveralls.io/github/klahnakoski/mo-times?branch=dev)\n[![Downloads](https://pepy.tech/badge/mo-times)](https://pepy.tech/project/mo-times)\n\n\n## Details \n\n`Date` is a simplified class for time manipulation. This library is intended for personal and business applications where assuming every solar day has 24 * 60 * 60 seconds is considered accurate. [See *GMT vs UTC* below](//#GMT%20vs%20UTC).\n\n\n### Assumptions\n\n* **All time is in GMT** - Timezone math is left to be resolved at the human endpoints: Machines should only be dealing with one type of time; without holes, without overlap, and with minimal context.\n* **Single time type** - There is no distinction between dates, datetime and times; all measurements in the time dimension are handled by one type called `Date`. This is important for treating time as a vector space.\n* **Standard range comparision** - All time range comparisons have been standardized to `min <= value < max`. The minimum is inclusive (`<=`), and the maximum is exclusive (`<`). \n\n\n## `Date` class \n\nThe `Date()` method will convert unix timestamps, millisecond timestamps, various string formats and simple time formulas to create a GMT time\n\n### `Date.now()`\n\nReturn `Date` instance with millisecond resolution (in GMT).\n\n### `Date.eod()` \n\nReturn end-of-day: Smallest `Date` which is greater than all time points in today. Think of it as tomorrow. Same as `now().ceiling(DAY)`\n\n### `Date.today()`\n\nThe beginning of today. Same as `now().floor(DAY)`\n\n### Date.range(min, max, interval)\n\nReturn an explicit list of `Dates` starting with `min`, each `interval` more than the last, but now including `max`.   Used in defining partitions in time domains.\n\n### `floor(duration=None)`\n\nThis method is usually used to perform date comparisons at the given resolution (aka `duration`). Round down to the nearest whole duration. `duration` as assumed to be `DAY` if not provided.\n\n### `format(format="%Y-%m-%d %H:%M:%S")`\n\nJust like `strftime`\n\n### `milli`\n\nNumber of milliseconds since epoch\n\n### `unix`\n\nNumber of seconds since epoch\n\n\n### `add(duration)`\n\nAdd a `duration` to the time to get a new `Date` instance. The `self` is not modified.\n\n### `addDay()`\n\nConvenience method for `self.add(DAY)`\n\n\n## `Duration` class\n\nRepresents the difference between two `Dates`. There are two scales:\n\n*  **`DAY` scale** - includes seconds, minutes, hours, days and weeks.\n*  **`YEAR` scale** - includes months, quarters, years, and centuries.\n\n### `floor(interval=None)`\n\nRound down to nearest `interval` size.\n\n### `seconds` \n\nreturn total number of seconds (including partial) in this duration (estimate given for `YEAR` scale)\n\n### `total_seconds()`\n\nSame as the `seconds` property\n\n### `round(interval, decimal=0)`\n\nReturn number of given `interval` rounded to given `decimal` places\n\n### `format(interval, decimal=0)`\n\nReturn a string representing `self` using given `interval` and `decimal` rounding\n\n\n# Time as an algebraic field\n\nThe `Date` and `Duration` objects are the point and vectors in a one dimensional vector space. As such, the `+` and `-` operators are allowed. Comparisons with (`>`, `>=`, `<=`, `<`) are also supported.\n\n\n## GMT vs UTC\n\nThe solar day is he most popular timekeeping unit. This library chose GMT (UT1) for its base clock because of its consistent seconds in a solar day. UTC suffers from inconsistent leap seconds and makes time-math difficult, even while forcing us to make pedantic conclusions like some minutes do not have 60 seconds. Lucky for us Python\'s implementation of UTC (`datetime.utcnow()`) is wrong, and implements GMT: Which is what we use.\n\n## Error Analysis\n\nAssuming we need a generous leap second each 6 months (the past decade saw only 4 leap seconds), then GMT deviates from UTC by up to 1 seconds over 181 days (December to June, 15,638,400 seconds) which is an error rate `error = 1/15,638,400 = 0.000006395%`. If we want to call the error "noise", we have a 70dB signal/noise ratio. All applications that can tolerate this level of error should use GMT as their time basis.\n\n\n',
    long_description_content_type='text/markdown',
    name='mo-times',
    packages=["mo_times/vendor/dateutil/zoneinfo","mo_times/vendor/dateutil","mo_times/vendor","mo_times"],
    url='https://github.com/klahnakoski/mo-times',
    version='5.378.23124'
)