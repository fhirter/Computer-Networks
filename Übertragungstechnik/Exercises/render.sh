#!/usr/bin/env bash

for i in *.md ; do
  [[ -f "$i" ]] || continue
  pandoc "$i" -o "${i%.md}.pdf"
done
