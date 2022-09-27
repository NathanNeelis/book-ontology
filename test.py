from pylode import OntDoc

# initialise
print("Creating HTML ontology file")
od = OntDoc(ontology="Nathan_books_ontology.ttl")

# or save HTML to a file
od.make_html(destination="test.html")