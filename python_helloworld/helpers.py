"""HELPERS
"""

__all__ = ("get_greet",)


def get_greet_dict():
    try:
        import addict
        data = addict.Dict()
        data.greet = "Hello World!"
    except ImportError:
        data = dict()
        data["greet"] = "Hello (without addict) World!"
    return data


def get_greet():
    return get_greet_dict()["greet"]
