# eduview2 toolchain
These are the modified set generators for the data.

### Set IDs for fetch.py
1. uaij-e68c (Graduates list)
2. id7n-c5cq (Schools directory)

### Directory
1. schools.py: structures schools.json (id7n-c5cq)
2. graduates.py: structures graduates.json (uaij-e68c)
3. matcher2.py: matches schools to graduates using the only links we could find
4. fetch.py: scrapes full datasets from Socrata

### Uses
1. schools.py [output.json, optional=debug]
2. graduates.py [output.json, optional=debug]
3. matcher2.py [output.json, optional=debug]
4. fetch.pyoptional
