# -*- coding:utf8 -*-
"""
"""
import os
from errbot import BotPlugin
from datetime import datetime
import pytz


if 'TIMEZONE' in os.environ:
    TZ = pytz.timezone(os.environ['TIMEZONE'])
else:
    TZ = pytz.UTC


class CrontabBase(BotPlugin):
    cronjob_list = []

    cronjob_config = []

    """Crontab polling plugin for Errbot
    """
    def activate(self):
        """Call poll_crontab every minutes.
        """
        super(Crontab, self).activate()
        self.register_jobs()
        self.start_poller(60, self.poll_crontab)

    def register_jobs(self):
        """Register configured jobs to Job instances
        """
        pass

    def poll_crontab(self):
        """Schedlued job runner.
        """
        self.log.debug('Run polling for crontab')
        polled_time = datetime.now(TZ)
