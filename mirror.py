#!/usr/bin/env python
import sentry_sdk
from os import getenv
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import requests



def main():
    requests.post(getenv("HEALTH_CHECK"))
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

    scheduler = BlockingScheduler()
    scheduler.add_job(
        main,
        CronTrigger.from_crontab(getenv("CRON")),
    )
    scheduler.start()
