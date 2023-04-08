# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['AuthorTest::test_get_author_list 1'] = [
    {
        'bio': 'пишет часто по осени',
        'id': 1,
        'language': 'русский',
        'title': 'Тестовый Августин'
    }
]

snapshots['AuthorTest::test_patch_author_partial_update_id 1'] = {
    'bio': 'пишет часто по осени',
    'id': 1,
    'language': 'русский',
    'title': 'Тестовый Августин'
}

snapshots['AuthorTest::test_post_author_create 1'] = {
    'bio': 'пишет часто по осени',
    'id': 2,
    'language': 'русский',
    'title': 'Тестовый Августин'
}

snapshots['AuthorTest::test_put_author_update_id 1'] = {
    'bio': 'пишет часто по осени',
    'id': 1,
    'language': 'русский',
    'title': 'Тестовый Августин'
}

snapshots['BookTest::test_create_book 1'] = {
    'cost': '0.00',
    'id': 2,
    'language': 'en',
    'short_content': 'hello world',
    'title': 'test'
}
