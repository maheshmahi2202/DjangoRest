from __future__ import unicode_literals

from django.db import models


class TestResults(models.Model):
    project = models.CharField(max_length=10)
    suite = models.CharField(max_length=10)
    testcase_name = models.CharField(max_length=20)
    test_status = models.CharField(max_length=4)

    def __str__(self):
        return self.testcase_name

