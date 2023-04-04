#!/usr/bin/env python
import sentry_sdk
from os import getenv



def main():
    import gist
    import giststared
    import repoForked
    import repoSource
    import repoStared


if __name__ == "__main__":
    with open("/cache/cache.json", "w") as f:
        f.write("{}")
    if sentry_dsn := getenv("SENTRY_DSN"):
        sentry_sdk.init(sentry_dsn)
    main()
