.PHONY: build
build:
	docker build --tag spacemaps-challenge .

.PHONY: run
run:
	docker run --rm spacemaps-challenge https://amp-spacemaps-technical-challenge.s3-ap-northeast-1.amazonaws.com/spacemaps_technical_challenge.txt 30
