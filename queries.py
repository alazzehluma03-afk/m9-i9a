"""Eight SPARQL queries against the publications ontology.

Each function returns a SPARQL query string. See learner_notes.md for the
intent and result snapshot per query.
"""


def q1():
    """Q1 — List all authors who have published at venue :NeurIPS.
    Variables in the SELECT: ?author.
    """
    #  SELECT distinct authors of papers where ?paper :publishedIn :NeurIPS.
    return """
    PREFIX : <http://aispire.example.org/publications/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    
    SELECT DISTINCT ?author
    WHERE {
        ?paper :publishedIn :NeurIPS ;
               :authoredBy ?author .
    }
    """


def q2():
    """Q2 — For each topic, count the number of papers on that topic.

    Variables in the SELECT: ?topic ?n.
    Use GROUP BY ?topic and COUNT(?paper) AS ?n.
    """
    # SELECT with GROUP BY topic.
    return """
    PREFIX : <http://aispire.example.org/publications/>
    
    SELECT ?topic (COUNT(?paper) AS ?n)
    WHERE {
        ?paper :topic ?topic .
    }
    GROUP BY ?topic
    """


def q3():
    """Q3 — All author-coauthor pairs in canonical form.

    Variables in the SELECT: ?a ?b.

    Two requirements (omit either and the row count is wrong):
    1. `SELECT DISTINCT ?a ?b` — coauthors who share multiple papers
       otherwise produce one row per shared paper (~230 rows on this
       fixture); DISTINCT collapses them to one row per pair (~215).
    2. `FILTER (str(?a) < str(?b))` — without it, each unordered pair
       appears twice (a,b) and (b,a).
    """
    #  SELECT DISTINCT ?a ?b WHERE { ?p :authoredBy ?a, ?b . FILTER ... }
    return """
    PREFIX : <http://aispire.example.org/publications/>
    
    SELECT DISTINCT ?a ?b
    WHERE {
        ?p :authoredBy ?a , ?b .
        FILTER (STR(?a) < STR(?b))
    }
    """


def q4():
    """Q4 — Every paper and its DOI, DOI OPTIONAL.

    Variables in the SELECT: ?paper ?doi.
    The :doi triple must live inside OPTIONAL { ... } — putting it in the
    main WHERE drops papers without a DOI.
    """
    # ?paper a :Paper . OPTIONAL { ?paper :doi ?doi } .
    return """
    PREFIX : <http://aispire.example.org/publications/>
    
    SELECT ?paper ?doi
    WHERE {
        ?paper a :Paper .
        OPTIONAL { ?paper :doi ?doi } .
    }
    """


def q5():
    """Q5 — ASK whether any author has more than 10 papers.

    Returns a boolean.
    """
    # ASK against a sub-SELECT that COUNTs papers per author with HAVING.
    return """
    PREFIX : <http://aispire.example.org/publications/>
    
    ASK {
        SELECT ?author
        WHERE {
            ?paper :authoredBy ?author .
        }
        GROUP BY ?author
        HAVING (COUNT(?paper) > 10)
    }
    """


def q6():
    """Q6 — CONSTRUCT a graph of 2023 papers and their authors.

    Returns triples ?paper :authoredBy ?author for papers with :year 2023.
    """
    #  CONSTRUCT { ... } WHERE { ?paper :year 2023 ; :authoredBy ?author }
    return """
    PREFIX : <http://aispire.example.org/publications/>
    
    CONSTRUCT {
        ?paper :authoredBy ?author .
    }
    WHERE {
        ?paper :year 2023 ;
               :authoredBy ?author .
    }
    """


def q7():
    """Q7 — Top 5 most-cited papers by literal :citationCount, DESC.

    Variables in the SELECT: ?paper ?cc.
    """
    #  ORDER BY DESC(?cc) LIMIT 5 against ?paper :citationCount ?cc.
    return """
    PREFIX : <http://aispire.example.org/publications/>
    
    SELECT ?paper ?cc
    WHERE {
        ?paper :citationCount ?cc .
    }
    ORDER BY DESC(?cc)
    LIMIT 5
    """


def q8():
    """Q8 — Authors whose name matches "Hinton" via skos:prefLabel OR skos:altLabel.

    Variables in the SELECT: ?author.
    """
    #  union of prefLabel / altLabel matches on "Hinton".
    return """
    PREFIX : <http://aispire.example.org/publications/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    
    SELECT DISTINCT ?author
    WHERE {
        ?author ?label "Hinton" .
        FILTER (?label = skos:prefLabel || ?label = skos:altLabel)
    }
    """
