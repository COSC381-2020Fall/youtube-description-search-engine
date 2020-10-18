# YouTube Description Search Engine
## Set up
1. run `python3 -m pip install -r requirements.txt`
## Retrieves Google Search results
1. modify config.py to add your api key and cse key
2. run: `python3 cse.py`
## Retrieves Video Ids from search results
1. run `python3 parse_search_results.py google_search.json videoids.txt`