from userbot import LOGS


def __list_all_modules():
    import glob
    from os.path import basename, dirname, isfile

    mod_paths = glob.glob(f"{dirname(__file__)}/*.py")
    return [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]


ALL_MODULES = sorted(__list_all_modules())
LOGS.info("Loading modules please wait.......")
__all__ = ALL_MODULES + ["ALL_MODULES"]
