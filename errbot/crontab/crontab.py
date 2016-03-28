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

    """Crontab polling plugin for Errbot
    """
    def activate(self):
        """Call poll_crontab every minutes.
        """
        super(CrontabBase, self).activate()
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
        self.run_jobs(polled_time)

    def run_jobs(self, polled_time):
        for cronjob in self.cronjob_list:
            if cronjob['trigger'](polled_time):
                user = self.build_identifier(cronjob['to'])
                self.send(user, cronjob['message'])
