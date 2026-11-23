# Data analytics portfolio

[View the published case studies](https://cbratto2-dev.github.io/data-portfolio/)

| Case study | Python source | What it covers |
| --- | --- | --- |
| ASOS revenue | [asos.py](code/asos.py) | Clean mixed-format values and compare monthly totals with weekly averages. |
| Olympic athletes | [olympics.py](code/olympics.py) | Summarize athlete measurements by season and count country records. |
| Mars weather | [mars.py](code/mars.py) | Calculate monthly weather averages and order Martian months numerically. |

Run `python3 code/asos.py` to reproduce the revenue table without extra packages. The Olympics and Mars functions accept Pandas DataFrames. Olympics expects `Season`, `Games`, `Height`, `Weight`, and `Country`. Mars expects `month`, `min_temp`, and `pressure`. The course datasets and complete notebooks are kept separately from this public repository. The site charts display saved coursework results.
