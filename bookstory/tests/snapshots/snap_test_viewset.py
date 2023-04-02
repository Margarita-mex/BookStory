# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['BookTest::test_create_book 1'] = {
    'cost': '0.00',
    'id': 2,
    'language': 'en',
    'short_content': 'hello world',
    'title': 'test'
}
