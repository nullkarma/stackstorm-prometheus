#!/usr/bin/env python

from st2actions.runners.pythonrunner import Action
from collections import defaultdict

class AlertAggregateCheck(object):
    def run(self, alerts, node_label, check_label):
        a = defaultdict(list)
        for alert in alerts:
            a[alert['labels'][node_label]].append(alert['labels'][check_label])

        return a
