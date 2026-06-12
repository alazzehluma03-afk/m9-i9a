# Integration 9A — Query Suite Notes

Fill in one section per query (Q1–Q8) with:
- **Intent:** one sentence stating what the query answers in business terms.
- **Result:** the first 5 rows (or triple count for CONSTRUCT, boolean for ASK).

Use the template below.

---

## Q1 — Authors at NeurIPS

**Intent:** Find every author who has published at least one research paper at the NeurIPS conference venue.

**Result:** 14 unique authors matched. First 5 rows:

* `:author000` (Hinton)
* `:author001` (Dana goodfellow)
* `:author004` (Carlos king)
* `:author022` (Gita baker)
* `:author035` (Mira sharma)

---

## Q2 — Papers per topic

**Intent:** Calculate the total number of academic papers written across each research topic available in the graph.

**Result:** 25 topics found. First 5 rows:

* `?topic = :topic_question-answering`, `?n = 3`
* `?topic = :topic_language-models`, `?n = 5`
* `?topic = :topic_vision-transformers`, `?n = 7`
* `?topic = :topic_summarization`, `?n = 3`
* `?topic = :topic_reinforcement-learning`, `?n = 3`

---

## Q3 — Canonical coauthor pairs

**Intent:** Identify all unique collaborator pairings who have co-authored a paper together, filtering out duplicates and reversed-order rows.

**Result:** ~215 unique pairs. First 5 rows:

* `?a = :author000`, `?b = :author001`
* `?a = :author000`, `?b = :author004`
* `?a = :author000`, `?b = :author022`
* `?a = :author000`, `?b = :author035`
* `?a = :author000`, `?b = :author038`

---

## Q4 — Papers and DOIs

**Intent:** Provide a complete ledger of all registered papers alongside their Digital Object Identifier (DOI) strings if they have one, without omitting papers that lack a DOI.

**Result:** 80 rows total. First 5 rows:

* `?paper = :paper000`, `?doi = "10.1000/p000"`
* `?paper = :paper001`, `?doi = [unbound]` (paper lacks a DOI)
* `?paper = :paper002`, `?doi = [unbound]`
* `?paper = :paper003`, `?doi = "10.1000/p003"`
* `?paper = :paper004`, `?doi = [unbound]`

---

## Q5 — Prolific authors (ASK)

**Intent:** Check whether there is any highly active researcher in the system who has authored or co-authored more than 10 documents.

**Result:** `false` (No author in this dataset fixture crosses the threshold of having >10 papers).

---

## Q6 — 2023 papers with authors (CONSTRUCT)

**Intent:** Synthesize a freshly filtered, standalone RDF graph mapping ownership links exclusively for research papers published in the year 2023 back to their authors.

**Result:** Total triples emitted: 20 triples.

---

## Q7 — Top 5 most-cited

**Intent:** Isolate and rank the top 5 most highly cited scientific papers recorded in the dataset sorted strictly by their static citation counts.

**Result:** 5 rows:

* `?paper = :paper063`, `?cc = 485`
* `?paper = :paper043`, `?cc = 475`
* `?paper = :paper004`, `?cc = 473`
* `?paper = :paper007`, `?cc = 470`
* `?paper = :paper048`, `?cc = 470`

---

## Q8 — "Hinton" via SKOS

**Intent:** Track down all distinct author resource profiles whose names match the string "Hinton" using either their primary preferred name label or an alternative alias label.

**Result:** 2 unique author profiles found:

* `?author = :author000` (Matched via `skos:prefLabel "Hinton"`)
* `?author = :author007` (Matched via `skos:altLabel "Hinton"`)