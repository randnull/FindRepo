SEARCH_TYPE_LOCAL=local
SEARCH_TYPE_GLOBAL=global

start_serp:
	docker-compose up -d

global_search: start_serp
	python3 FindRepo/finder.py -type $(SEARCH_TYPE_GLOBAL) -file $(file) $(args)

global: global_search
	docker-compose down

local:
	python3 FindRepo/finder.py -type $(SEARCH_TYPE_LOCAL) -file $(file) $(args)
