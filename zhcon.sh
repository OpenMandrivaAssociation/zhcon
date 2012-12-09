#!/bin/sh

if [ "`locale charmap`" = "UTF-8" ]; then
	alias zhcon='zhcon --utf8'
fi
