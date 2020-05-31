#!/bin/bash

git reset --hard origin/master
git pull origin master
rm -rf prep/fuzz duk
mkdir -p prep/fuzz

python2 tools/configure.py --output-directory prep/fuzz --source-directory src-input --config-metadata config --option-file $(dirname $0)/duktape-fuzzinator-options.yaml

gcc -o duk \
    -std=c99 -D_POSIX_C_SOURCE=200809L -fstrict-aliasing \
    -O2 -g -ggdb \
    -Iprep/fuzz \
    -Iexamples/cmdline \
    -Iexamples/alloc-logging \
    -Iexamples/alloc-torture \
    -Iexamples/alloc-hybrid \
    -Iexamples/debug-trans-socket \
    -Iextras/print-alert \
    -Iextras/console \
    -Iextras/logging \
    -Iextras/module-duktape \
    -Iextras/cbor \
    -Ilinenoise \
    prep/fuzz/duktape.c \
    examples/cmdline/duk_cmdline.c \
    examples/alloc-logging/duk_alloc_logging.c \
    examples/alloc-torture/duk_alloc_torture.c \
    examples/alloc-hybrid/duk_alloc_hybrid.c \
    examples/debug-trans-socket/duk_trans_socket_unix.c \
    extras/print-alert/duk_print_alert.c \
    extras/console/duk_console.c \
    extras/logging/duk_logging.c \
    extras/module-duktape/duk_module_duktape.c \
    linenoise/linenoise.c \
    -lm
