# More Times!

Assume time forms an algebraic field over GMT. Finally! 


## Details 

`Date` is a simplified class for time manipulation. This library is intended for personal and business applications where assuming every solar day has 24 * 60 * 60 seconds is considered accurate. [See *GMT vs UTC* below](//#GMT%20vs%20UTC).


### Assumptions

* **All time is in GMT** - Timezone math is left to be resolved at the human endpoints: Machines should only be dealing with one type of time; without holes, without overlap, and with minimal context.
* **Single time type** - There is no distinction between dates, datetime and times; all measurements in the time dimension are handled by one type called `Date`. This is important for treating time as a vector space.
* **Standard range comparision** - All time range comparisons have been standardized to `min <= value < max`. The minimum is inclusive (`<=`), and the maximum is exclusive (`<`). 


## `Date` class 

The `Date()` method will convert unix timestamps, millisecond timestamps, various string formats and simple time formulas to create a GMT time

### `Date.now()`

Return `Date` instance with millisecond resolution (in GMT).

### `Date.eod()` 

Return end-of-day: Smallest `Date` which is greater than all time points in today. Think of it as tomorrow. Same as `now().ceiling(DAY)`

### `Date.today()`

The beginning of today. Same as `now().floor(DAY)`

### Date.range(min, max, interval)

Return an explicit list of `Dates` starting with `min`, each `interval` more than the last, but now including `max`.   Used in defining partitions in time domains.

### `floor(duration=None)`

This method is usually used to perform date comparisons at the given resolution (aka `duration`). Round down to the nearest whole duration. `duration` as assumed to be `DAY` if not provided.

### `format(format="%Y-%m-%d %H:%M:%S")`

Just like `strftime`

### `milli`

Number of milliseconds since epoch

### `unix`

Number of seconds since epoch


### `add(duration)`

Add a `duration` to the time to get a new `Date` instance. The `self` is not modified.

### `addDay()`

Convenience method for `self.add(DAY)`


## `Duration` class

Represents the difference between two `Dates`. There are two scales:

*  **`DAY` scale** - includes seconds, minutes, hours, days and weeks.
*  **`YEAR` scale** - includes months, quarters, years, and centuries.

### `floor(interval=None)`

Round down to nearest `interval` size.

### `seconds` 

return total number of seconds (including partial) in this duration (estimate given for `YEAR` scale)

### `total_seconds()`

Same as the `seconds` property

### `round(interval, decimal=0)`

Return number of given `interval` rounded to given `decimal` places

### `format(interval, decimal=0)`

Return a string representing `self` using given `interval` and `decimal` rounding


# Time as an algebraic field

The `Date` and `Duration` objects are the point and vectors in a one dimensional vector space. As such, the `+` and `-` operators are allowed. Comparisons with (`>`, `>=`, `<=`, `<`) are also supported.


## GMT vs UTC

The solar day is he most popular timekeeping unit. This library chose GMT (UT1) for its base clock because of its consistent seconds in a solar day. UTC suffers from inconsistent leap seconds and makes time-math difficult, even while forcing us to make pedantic conclusions like some minutes do not have 60 seconds. Lucky for us Python's implementation of UTC (`datetime.utcnow()`) is wrong, and implements GMT: Which is what we use.

## Error Analysis

Assuming we need a generous leap second each 6 months (the past decade saw only 4 leap seconds), then GMT deviates from UTC by up to 1 seconds over 181 days (December to June, 15,638,400 seconds) which is an error rate `error = 1/15,638,400 = 0.000006395%`. If we want to call the error "noise", we have a 70dB signal/noise ratio. All applications that can tolerate this level of error should use GMT as their time basis.


