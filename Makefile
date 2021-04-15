tag = spacemaps-challenge
source = https://amp-spacemaps-technical-challenge.s3-ap-northeast-1.amazonaws.com/spacemaps_technical_challenge.txt
results = 30

.PHONY: build
build:
	docker build --tag $(tag) .

.PHONY: run
run:
	docker run --rm $(tag) $(source) $(results)

.PHONY: test
test:
	python3 -B -m unittest tests/*
