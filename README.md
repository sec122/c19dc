# Getting nineteenth century data from Library of Congress book records

This repository contains code and data supporting the essay "Moving the Capital of US Literature from Boston to New York: Evidence from 11 million Library of Congress records," a contribution to [the Nineteenth Century Data Collective](https://c19datacollective.com/).

The code can be modified to extract data from any [MARC record fields](https://www.loc.gov/marc/bibliographic/) from any [Library of Congress Classification Outline](https://www.loc.gov/aba/cataloging/classification/lcco/) range.

## Running locally

This code has been tested on macOS 14.5 (23F79) with Anaconda 2024.02.

### Requirements

- Download and extract [the most current version of the MDS Connect books all dataset](https://lccn.loc.gov/2020445551).
  - All figures referenced in the essay refer to the 2019 version, the most current as of this writing (2024-06-26).
- Reset local paths referenced in `get_lc_data.ipynb` (i.e., `/Users/erik...`) to paths on your machine.

### Original use

- As written, this identifies and extracts LC `"PS..."` records in the American literature range.
- It also extacts publication information, including first author, title, publication place, and year.
- It then normalizes place names and publication years to analyze the changing imprint geographies of US literature over a two-century nineteenth century (1745-1945).

### How to modify

- `get_lc_data.ipynb` contains all of the code used to extract and clean the records.
- There are values hard-coded in `process_record()` that can be modified to change the records to be pulled.
  - For instance, change the `str(classification).startswith("PS")` expression to subset for records in any value given in the [Library of Congress Classification Outline](https://www.loc.gov/aba/cataloging/classification/lcco/).
  - To change the subfield retrieved, either modify or expand the calls to `extract_subfields()` in `process_record()`

### Limitations

- The automated cleaning processes do not catch 100% of records. For some applications, it might be desirable to perform other steps to correct certain values.
  - For example, while almost all works have a four-digit year of publication, some are expressed by catalogers with uncertainty, e.g., `"18--?"` or `"187-?"`
  - The current model ignores such values (setting them to `0`, so that they are excluded from the analysis), but, in some circumstances, it might be desirable to include the information encoded at the level of the decade or century in such strings.

## AI Statement

I used GitHub Copilot completions in writing some of this code.
