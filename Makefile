
pp = poetry

install:
	pp install

run:
	$(pp) env activate | xclip -selection clipboard
	 && python3 -m maze.main

all:
	python3 -m maze.main


clean:
	@rm -rf */__pycache__
	@rm -rf .mypy_cache
