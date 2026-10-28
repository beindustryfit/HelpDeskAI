.PHONY: test train
test:
	pytest -q
train:
	python -m ml.train
