# Copyright (c) 2020 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.

import configparser
import json
import pytest

from os.path import abspath, dirname, join

from fuzzinator.config import config_get_callable

root_dir = dirname(dirname(abspath(__file__)))
resources_dir = join(root_dir, 'test', 'resources')


@pytest.mark.parametrize('sut, field, test, exp', [
    ('duktape', 'backtrace', 'gdb.txt', 'gdb_exp.txt'),
    ('duktape', 'stderr', 'duktape_assert.txt', 'duktape_assert_exp.txt'),
    ('escargot', 'backtrace', 'gdb.txt', 'gdb_exp.txt'),
    ('escargot', 'stderr', 'escargot_assert.txt', 'escargot_assert_exp.txt'),
    ('espruino', 'stderr', 'espruino_assert.txt', 'espruino_assert_exp.txt'),
    ('iotjs', 'backtrace', 'gdb.txt', 'gdb_exp.txt'),
    ('iotjs', 'stderr', 'iotjs_assert.txt', 'iotjs_assert_exp.txt'),
    ('iotjs', 'stderr', 'iotjs_not_implemented.txt', 'iotjs_not_implemented_exp.txt'),
    ('jerryscript', 'stderr', 'asan_dyn_bof.txt', 'asan_dyn_bof_exp.txt'),
    ('jerryscript', 'stderr', 'asan_hbo.txt', 'asan_hbo_exp.txt'),
    ('jerryscript', 'stderr', 'asan_segv.txt', 'asan_segv_exp.txt'),
    ('jerryscript', 'stderr', 'asan_uaf.txt', 'asan_uaf_exp.txt'),
    ('jerryscript', 'stderr', 'jerry_assert.txt', 'jerry_assert_exp.txt'),
    ('jsc', 'stderr', 'asan_segv.txt', 'asan_segv_exp.txt'),
    ('jsc', 'stderr', 'jsc_argument_bad.txt', 'jsc_argument_bad_exp.txt'),
    ('jsc', 'stderr', 'jsc_assert.txt', 'jsc_assert_exp.txt'),
    ('jsc', 'stderr', 'jsc_should_not_reached.txt', 'jsc_should_not_reached_exp.txt'),
    ('v8', 'stderr', 'v8_dcheck.txt', 'v8_dcheck_exp.txt'),
])
def test_regex(sut, field, test, exp):
    config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation(),
                                       strict=False,
                                       allow_no_value=True)
    config.read([
        join(root_dir, 'sut', sut, sut + '.ini'),
        join(root_dir, 'sut', sut, sut + '_sample.ini'),
        join(root_dir, 'test', 'sut.ini')
    ])

    sut_call, sut_call_kwargs = config_get_callable(config, 'sut.mock_' + sut, 'call')
    assert sut_call, sut
    issue = sut_call(test=join(resources_dir, sut, test), field=field, **sut_call_kwargs)
    del issue[field]
    issue = dict((k, v.decode() if isinstance(v, bytes) else v) for k, v in issue.items())
    with open(join(resources_dir, sut, exp), 'r') as f:
        assert f.read() == json.dumps(issue, indent=2, sort_keys=True)
