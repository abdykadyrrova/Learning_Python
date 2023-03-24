#!/bin/bash

## get latest
git pull

## adding files to push
git add .

## use $1 as our message
git commit -m $1

## push files to github
git push -u origin main

## testing new lines
