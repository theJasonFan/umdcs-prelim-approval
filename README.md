# umdcs-prelim-approval

`list`, `search`, and `check` your prelim committee.

# Usage

List Field Committees:
```
./approveme.py list
```

Search for faculty:
```
./approveme.py search --name [Name ...]
```

Validate your Chair and Dept. Rep. committee
```
./approveme.py chach --chair CHAIR --dept-rep DEPT_REP
```

## Contributing
Please add your prelim comittee to the test cases!

Run: `python -m unittest`

## Field committees (last updated: nov 2022)
```
CMSC({
  "Algorithms and Theory of Computing": [
    "Childs",
    "Gasarch",
    "Gottesman",
    "Hajiaghayi",
    "Katz",
    "Kruskal",
    "Mount",
    "Srinivasan",
    "Wu"
  ],
  "Artificial Intelligence": [
    "Boyd-Graber",
    "Carpuat",
    "Daume",
    "Dickerson",
    "Feizi",
    "Huang",
    "Nau",
    "Perlis",
    "Reggia",
    "Regli",
    "Rudinger",
    "Tokekar"
  ],
  "Bioinformatics": [
    "Patro",
    "Pop",
    "Molloy"
  ],
  "Computer Systems": [
    "Agrawala",
    "Bhatele",
    "Bhattacharjee",
    "Hollingsworth",
    "Keleher",
    "Levin",
    "Mazurek",
    "Miers",
    "Roy",
    "Shankar",
    "Sussman"
  ],
  "Database Systems": [
    "Abadi",
    "Deshpande"
  ],
  "Scientific Computing": [
    "Duraiswami",
    "Elman",
    "Goldstein"
  ],
  "Software Engineering/Programming Languages/HCI": [
    "Cleaveland",
    "Hicks",
    "Lampropoulos",
    "Liu",
    "Peng",
    "Porter",
    "Purtilo",
    "Van Horn",
    "Paredes"
  ],
  "Visual and Geometric Computing": [
    "Aloimonos",
    "Davis",
    "Jacobs",
    "Lin",
    "Manocha",
    "Metzler",
    "Samet",
    "Shrivastava",
    "Varshney",
    "Zwicker"
  ]
})
```