from xgoogle.search import GoogleSearch, SearchError

try:
  gs = GoogleSearch("yugoiuygiuygiuyg")
  gs.results_per_page = 50
  results = gs.get_results()
  print results
  print 'results', gs.num_results  # number of results
  for res in results:
    print res.title.encode("utf8")
    print res.desc.encode("utf8")
    print res.url.encode("utf8")
    print
except SearchError, e:
  print "Search failed: %s" % e