import contextlib
import warnings


def _bit_length_26(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return len(bin(x)) - 2


class ResettableCache(dict):
    """
    Dictionary whose elements mey depend one from another.
    If entry `B` depends on entry `A`, changing the values of entry `A` will
    reset the value of entry `B` to a default (None); deleteing entry `A` will
    delete entry `B`.  The connections between entries are stored in a
    `_resetdict` private attribute.
    Parameters
    ----------
    reset : dictionary, optional
        An optional dictionary, associated a sequence of entries to any key
        of the object.
    items : var, optional
        An optional dictionary used to initialize the dictionary
    """

    def __init__(self, reset=None, **items):
        self._resetdict = reset or {}
        dict.__init__(self, **items)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        # if hasattr needed for unpickling with protocol=2
        if hasattr(self, "_resetdict"):
            for mustreset in self._resetdict.get(key, []):
                self[mustreset] = None

    def __delitem__(self, key):
        dict.__delitem__(self, key)
        for mustreset in self._resetdict.get(key, []):
            del self[mustreset]


resettable_cache = ResettableCache


def _next_regular(target):
    """
    Find the next regular number greater than or equal to target.
    Regular numbers are composites of the prime factors 2, 3, and 5.
    Also known as 5-smooth numbers or Hamming numbers, these are the optimal
    size for inputs to FFTPACK.
    Target must be a positive integer.
    """
    if target <= 6:
        return target

    # Quickly check if it's already a power of 2
    if not (target & (target - 1)):
        return target

    match = float("inf")  # Anything found will be smaller
    p5 = 1
    while p5 < target:
        p35 = p5
        while p35 < target:
            # Ceiling integer division, avoiding conversion to float
            # (quotient = ceil(target / p35))
            quotient = -(-target // p35)
            # Quickly find next power of 2 >= quotient
            try:
                p2 = 2 ** ((quotient - 1).bit_length())
            except AttributeError:
                # Fallback for Python <2.7
                p2 = 2 ** _bit_length_26(quotient - 1)

            N = p2 * p35
            if target == N:
                return N
            elif match > N:
                match = N
            p35 *= 3
            if p35 == target:
                return p35
        if p35 < match:
            match = p35
        p5 *= 5
        if p5 == target:
            return p5
    if p5 < match:
        match = p5
    return match


class CacheWriteWarning(UserWarning):
    pass


class CachedAttribute:
    def __init__(self, func, cachename=None, resetlist=None):
        self.fget = func
        self.name = func.__name__
        self.cachename = cachename or "_cache"
        self.resetlist = resetlist or ()

    def __get__(self, obj, type_=None):
        if obj is None:
            return self.fget
        # Get the cache or set a default one if needed
        _cachename = self.cachename
        _cache = getattr(obj, _cachename, None)
        if _cache is None:
            setattr(obj, _cachename, resettable_cache())
            _cache = getattr(obj, _cachename)
        # Get the name of the attribute to set and cache
        name = self.name
        _cachedval = _cache.get(name, None)
        # print("[_cachedval=%s]" % _cachedval)
        if _cachedval is None:
            # Call the "fget" function
            _cachedval = self.fget(obj)
            # Set the attribute in obj
            # print("Setting %s in cache to %s" % (name, _cachedval))
            try:
                _cache[name] = _cachedval
            except KeyError:
                setattr(_cache, name, _cachedval)
            # Update the reset list if needed (and possible)
            resetlist = self.resetlist
            if resetlist != ():
                with contextlib.suppress(AttributeError):
                    _cache._resetdict[name] = self.resetlist
        # else:
        # print("Reading %s from cache (%s)" % (name, _cachedval))
        return _cachedval

    def __set__(self, obj, value):
        errmsg = f"The attribute '{self.name}' cannot be overwritten"
        warnings.warn(errmsg, CacheWriteWarning, stacklevel=2)


class _cache_readonly:
    """
    Decorator for CachedAttribute
    """

    def __init__(self, cachename=None, resetlist=None):
        self.func = None
        self.cachename = cachename
        self.resetlist = resetlist or None

    def __call__(self, func):
        return CachedAttribute(func, cachename=self.cachename, resetlist=self.resetlist)


cache_readonly = _cache_readonly()
