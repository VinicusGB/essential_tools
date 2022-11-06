import functools

def decorator(func):
    @functools.wraps(func)
    def wrappert_decorator(*args,**kwargs):
        # Do something before
        value = func(*args,**kwargs)
        # Do something after
        return value
    return wrappert_decorator