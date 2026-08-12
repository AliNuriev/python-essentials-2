![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![Course](https://img.shields.io/badge/Cisco%20NetAcad-Python%20Essentials%202-049fd9?logo=cisco&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20progress-yellow)

# Python Essentials 2

Practice code, lab solutions, and personal experiments from Cisco Networking Academy's **Python Essentials 2 (PCAP)** course — the sequel to Python Essentials 1. This module moves past the language basics into modules & packages, strings, object-oriented programming, and generators/iterators, on the way toward file handling and the standard library (`os`, `datetime`, `calendar`, …).

Every script is self-contained, runnable, and — where the course itself doesn't provide one — written from scratch to explore the concept being studied. Some files also carry inline notes (occasionally in Russian) written while working through trickier ideas such as generator frames and lazy evaluation.

## Table of Contents

- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Module 1 — Modules](#module-1--modules)
- [Module 2 — Strings, Exceptions & Mini-Programs](#module-2--strings-exceptions--mini-programs)
- [Module 3 — Object-Oriented Programming](#module-3--object-oriented-programming)
- [Module 4 — Generators, Iterators, Closures & the Standard Library](#module-4--generators-iterators-closures--the-standard-library)
- [The `extra` Package (Modules & Packages Demo)](#the-extra-package-modules--packages-demo)
- [Extra / Bonus Scripts](#extra--bonus-scripts)
- [Running the Scripts](#running-the-scripts)
- [About](#about)

## Requirements

- Python 3.10+ (developed and tested with **Python 3.14**)
- No third-party packages are required for the course scripts themselves.
  `misc_bson to json.py` additionally needs [`pymongo`](https://pypi.org/project/pymongo/) (for the `bson` module) — install with `pip install pymongo` if you want to run that one file.

## Project Structure

```
CISCO Python Essentials 2/
├── 1.1 Section 1 – Introduction to modules in Python.py
├── 1.2 Section 2 – Selected Python modules (math, random, platform).py
├── 1.3 Section 3 – Modules and Packages.py
├── 2.2 Section 2 – The nature of strings in Python.py
├── 2.3 Section 3 – String Methods.py
├── 2.4 Section 4 – String in action.py
├── 2.5 Section 5 – Four simple programs.py
├── 2.8 Section 8 – Useful exceptions.py
├── 3.2 Section 2 – A short journey from procedural to object approach.py
├── 3.2.8 - LABs on classes and objects.py
├── 3.2.9 - LAB, Queue aka FIFO.py
├── 3.2.10 - LAB, Queue aka FIFO, part 2.py
├── 3.3 Section 3 – OOP Properties.py
├── 3.6 Section 6 – Exceptions once again.py
├── 4.1 Section 1 – Generators, iterators, and closures.py
├── module.py                              # helper module imported by 1.3
├── extra/                                 # package used by 1.3 (Modules & Packages)
│   ├── __init__.py
│   ├── iota.py
│   ├── good/
│   │   ├── alpha.py
│   │   ├── beta.py
│   │   └── best/
│   │       ├── sigma.py
│   │       └── tau.py
│   └── ugly/
│       ├── omega.py
│       └── psi.py
├── misc_Encapsulation in Python.py
├── misc_Python Object Oriented Programming Full Course.py
└── misc_bson to json.py
```

## Module 1 — Modules

| File | Key concepts |
|---|---|
| `1.1 Section 1 – Introduction to modules in Python.py` | What a module is, `import`, name shadowing (writing your own `sin()` next to `math.sin()`), the `math` module |
| `1.2 Section 2 – Selected Python modules (math, random, platform).py` | Exploring a module with `dir()`, `math` constants/functions, `random` (seeding & reproducibility), `platform` for system info |
| `1.3 Section 3 – Modules and Packages.py` | Importing your own module (`module.py`), `from module import ...`, building a package (`extra/`), `__init__.py`, nested packages, dotted imports |

## Module 2 — Strings, Exceptions & Mini-Programs

| File | Key concepts |
|---|---|
| `2.2 Section 2 – The nature of strings in Python.py` | Strings as immutable sequences, multiline strings, `ord()`, indexing, iterating, slicing, `min()`/`max()` on characters |
| `2.3 Section 3 – String Methods.py` | `.endswith()`, `.find()`/`.rfind()`, `.isalnum()`, `.isalpha()`, `.isdigit()`, `.islower()`/`.isupper()`, `.isspace()`, `.join()`, `.lower()`/`.upper()`, `.lstrip()`/`.rstrip()`/`.strip()`, `.replace()`, `.split()`, `.startswith()`, `.swapcase()`, `.title()` |
| `2.4 Section 4 – String in action.py` | Lexicographic vs. numeric comparison of strings, `str()`/numeric conversions |
| `2.5 Section 5 – Four simple programs.py` | Small applied programs (e.g. a Caesar-cipher-style text scrambler) combining string tools learned so far |
| `2.8 Section 8 – Useful exceptions.py` | `assert`, catching built-in exceptions, writing a small "safe input" LAB routine |

## Module 3 — Object-Oriented Programming

| File | Key concepts |
|---|---|
| `3.2 Section 2 – A short journey from procedural to object approach.py` | Turning a procedural stack (functions + global list) into a class; name mangling (`__attr`) and encapsulation |
| `3.2.8 - LABs on classes and objects.py` | LAB: implementing a `Stack` class from scratch |
| `3.2.9 - LAB, Queue aka FIFO.py` | LAB: implementing a `Queue` (FIFO) class, custom `QueueError` exception |
| `3.2.10 - LAB, Queue aka FIFO, part 2.py` | Extending the Queue LAB further |
| `3.3 Section 3 – OOP Properties.py` | Instance vs. class attributes, `hasattr()`, introspecting object state |
| `3.6 Section 6 – Exceptions once again.py` | Exceptions as classes, the exception hierarchy, defining custom exceptions, a LAB example |

## Module 4 — Generators, Iterators, Closures & the Standard Library

This module is **in progress**. It opens with iterators/generators/closures and, per the course syllabus, continues into file handling and useful standard-library modules (`os`, `datetime`, `calendar`, and others) — those sections will be added here as they're completed.

| File | Key concepts |
|---|---|
| `4.1 Section 1 – Generators, iterators, and closures.py` | The iterator protocol (`__iter__`/`__next__`, `StopIteration`), building a custom `Fib` iterator class, `yield` and generator functions, `return` vs. `yield` (frame suspension vs. destruction), generator expressions vs. list comprehensions (laziness, memory, no `len()`), conditional expressions (`x if cond else y`) inside comprehensions |

**Coming up in Module 4:**

| Planned topic | What it covers |
|---|---|
| File handling | Opening/closing files, read/write modes, text vs. binary streams, context managers (`with open(...)`) |
| `os` module | Filesystem navigation, path manipulation, environment info, process/OS interaction |
| `datetime` module | Working with dates and times, formatting/parsing, timedeltas |
| `calendar` module | Calendar generation, weekday/leap-year calculations |

## The `extra` Package (Modules & Packages Demo)

Supports `1.3 Section 3 – Modules and Packages.py`. A minimal, purpose-built package tree used to demonstrate package structure, `__init__.py`, and dotted (`extra.good.best.tau`) imports:

| Path | Module | Exposes |
|---|---|---|
| `extra/iota.py` | `extra.iota` | `FunI()` → `"Iota"` |
| `extra/good/alpha.py` | `extra.good.alpha` | `FunA()` → `"Alpha"` |
| `extra/good/beta.py` | `extra.good.beta` | `FunB()` → `"Beta"` |
| `extra/good/best/sigma.py` | `extra.good.best.sigma` | Sigma-level nested module |
| `extra/good/best/tau.py` | `extra.good.best.tau` | Tau-level nested module |
| `extra/ugly/omega.py` | `extra.ugly.omega` | `FunO()` → `"Omega"` |
| `extra/ugly/psi.py` | `extra.ugly.psi` | `FunP()` → `"Psi"` |

`module.py` (project root) is a standalone helper module — `sum1()`/`prod1()` over a list, plus a private `__counter` — imported directly by `1.3`.

## Extra / Bonus Scripts

Self-directed practice beyond the official course material:

| File | Description |
|---|---|
| `misc_Encapsulation in Python.py` | Deep dive into encapsulation: private/protected naming conventions, `@property` getters/setters, worked examples (`BankAccount`, a secure vault, a game-character state manager) |
| `misc_Python Object Oriented Programming Full Course.py` | A broad OOP walkthrough: inheritance (single/multiple/multilevel), abstract classes, `super()`, polymorphism, duck typing, aggregation vs. composition, nested classes, instance/static/class methods, magic methods, `@property` |
| `misc_bson to json.py` | Converting MongoDB `bson`/`ObjectId` data to JSON using `bson`, `json`, `os`, and `datetime` |

## Running the Scripts

Each file is a standalone script — run any of them directly with Python 3:

```bash
python "4.1 Section 1 – Generators, iterators, and closures.py"
```

Some scripts (e.g. `2.8`, `2.5`) prompt for input via `input()`, so run them from an interactive terminal.

## About

Written while working through the [Python Essentials 2](https://www.netacad.com) course on Cisco Networking Academy — the companion project to [Python Essentials 1](../CISCO%20Python%20Essentials%201).