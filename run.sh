#!/usr/bin/env sh
docker build --tag spacemaps-challenge .
docker run --rm spacemaps-challenge https://amp-spacemaps-technical-challenge.s3-ap-northeast-1.amazonaws.com/spacemaps_technical_challenge.txt 30
