# CMM
This is a repository that runs a RESTful API on a nginx server. Transforming xml-based study metadata into DBPedia linked DDI-RDF data

myproject.py is the code that runs the server and calls all the other code

In main.py all the XML parsing is done and in and ddigen.py creates the DDI template and adds the enriched data to that template. Afterwards the API is served using Flask, this is done in the myproject.py file.

Project commissioned by ODISSEI, working with DANS-EASY data.

https://odissei-data.nl/nl/
https://dans.knaw.nl/nl
