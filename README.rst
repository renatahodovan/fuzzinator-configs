=============================
Configurations for Fuzzinator
=============================

This repository collects various Fuzzinator_ configurations. Its primary
purpose is to ease the work of fuzzing enthusiasts with the initial framework
setup, which can be a time-consuming task. Here, fuzzing configurations of
various SUTs and fuzzers are collected, hence you only need to focus on
your awesome test generator.

The sut directory is intended to contain subdirectories named after the target
applications. Each subdirectory may contain Fuzzinator configurations, update
scripts, or report format templates. Format-specific resources,
e.g., ANTLR_ v4 grammars_ for the Picireny_ reducer are in the reduce
directory. Additionally, there is also a fuzzinator directory for target- and
format-independent configurations.

Almost all configuration and resource files should be general enough not to
need any manual editing. Preferably, only configuration files ending with
``-sample.ini`` should contain information that needs customization, e.g.,
local paths, fuzzing parameters, etc. These files should be duplicated, and
their copies edited and adapted to local needs.

Contributions are welcome. If you have created a new configuration for a new
target or found a problem in an existing one, don't hesitate to open a PR or
an issue on Github! :)

.. _Fuzzinator: https://github.com/renatahodovan/fuzzinator
.. _ANTLR: http://www.antlr.org
.. _grammars: https://github.com/antlr/grammars-v4
.. _Picireny: https://github.com/renatahodovan/picireny


Copyright and Licensing
=======================

Most files in the repository are licensed under the BSD 3-Clause License_ but
there is no single license for the repository as a whole. Each file has its
own license, so check inside the files for exact licensing terms.

.. _License: https://opensource.org/licenses/BSD-3-Clause
