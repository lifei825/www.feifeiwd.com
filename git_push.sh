#!/bin/bash

git pull && \
git add . && \
read -p "input git commit -m :" a && \
git commit -m "$a" && \
git push && \
echo OK 

