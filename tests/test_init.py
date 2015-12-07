# PyXenon Xenon API wrapper
#
# Copyright 2015 Netherlands eScience Center
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import xenon
import os
from nose.tools import assert_equals, assert_not_equal

is_initiated = False


def make_init():
    global is_initiated
    if not is_initiated:
        assert_equals(None, xenon.jobs.JobDescription)
        xenon.init()
        assert_not_equal(None, xenon.jobs.JobDescription)
        is_initiated = True


def test_init():
    make_init()


def test_module_path():
    make_init()
    cd = os.path.join(os.getcwd(), 'tests', 'test_init.py')
    mpath = xenon._module_path(test_module_path)
    assert_equals(cd, mpath)