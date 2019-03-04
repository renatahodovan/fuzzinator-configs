#!/bin/bash

# Copyright (c) 2019 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE-BSD-3-Clause.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except according to
# those terms.

git reset --hard origin/master
git pull origin master
rm -rf build

# $1 is the build command to execute.
eval $1
