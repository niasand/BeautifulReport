# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Author: Mocobk
# Data: 2019/03/18
# License: MIT
# Modified by ZhiWei Yang
# tencrance@gmail.com
# Modified At: 2020/11/15

import unittest
import os
from BeautifulReport import BeautifulReport
report_dir = os.path.expanduser("~/")

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('./tests', pattern='test_demo*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='Test Report', description='report', report_dir=report_dir, theme='theme_default')
