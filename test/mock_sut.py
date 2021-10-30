# Copyright (c) 2020-2021 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.

import fuzzinator


class MockSubprocessCall(fuzzinator.call.Call):

    def __call__(self, test, field='stderr', **kwargs):
        with open(test, 'r') as f:
            return {field: f.read()}
