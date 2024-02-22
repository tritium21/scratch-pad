#!/bin/bash
ls -R "$@" | cut -f2 | sed '/\//! s/^/    /'
