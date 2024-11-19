# Getting nineteenth century data from Library of Congress book records

This repository contains code and data supporting the essay "Moving the Capital of US Literature from Boston to New York: Evidence from 11 million Library of Congress records," which will be published by [the Nineteenth Century Data Collective](https://c19datacollective.com/).

The code can be modified to extract data from any [MARC record fields](https://www.loc.gov/marc/bibliographic/) from any [Library of Congress Classification Outline](https://www.loc.gov/aba/cataloging/classification/lcco/) range available in the [MDSConnect "Books All"](https://lccn.loc.gov/2020445551) dataset.

## Basic information about the dataset

- Normalized places of publication for C19 US literature books
- Original data source: <https://lccn.loc.gov/2020445551>
- Data analysis: Erik Fredner
- Dataset languages: Primarily English, though some titles in other languages

## Data structure

See the `data` folder in this repository for the dataset (`data.csv`) and a data dictionary (`data_dictionary.csv`) describing its columns. All transformatons to the MDSConnect Books All dataset are recorded in this repository.

## Ethics

MDSConnect is the LC's open access MARC records dataset.

## Format

The essay and dataset are both available in plain text formats (`.qmd` and `.csv` respectively). The essay is also available as [Quarto](https://quarto.org)-rendered `.html` or `.pdf` documents.

## About this repo

This repository follows the conventions [outlined here](https://goodresearch.dev).

## Local reproduction and customization

This code has been tested on macOS 15.1 (24B83) with the `conda` environment indicated in `environment.yml`

### Requirements

- Download and extract [the most current version of the MDS Connect books all dataset](https://lccn.loc.gov/2020445551).
  - All figures referenced in the essay refer to the 2019 version, the most current as of this writing.
- Reset any local paths referenced in the Jupyter notebooks to paths on your machine.

### Original use

- As written, this identifies and extracts LC `"PS..."` records in the American literature range from the complete books dataset.
- It also extacts publication information, including first author, title, publication place, and year, as visibile in `data/data.csv`
- It then normalizes place names and publication years to measure the changing imprint geographies of US literature.

### How to modify

- Assuming that another user of this code might want to select a different set of records or extract different fields from them, they will need to modify  `src/data_collection.py`.
- There are values hard-coded in `process_record()` that can be modified to change the records to be pulled.
  - For instance, change the `str(classification).startswith("PS")` expression to subset for records in any value given in the [Library of Congress Classification Outline](https://www.loc.gov/aba/cataloging/classification/lcco/).
  - To change the subfield retrieved, either modify or expand the calls to `extract_subfields()` in `process_record()` to a subfield as defined in the [MARC format](https://www.loc.gov/marc/bibliographic/).

For example, if you wanted to extract information about the extent of each book, you could do so by referencing [MARC field 300 (Physical Description)](https://www.loc.gov/marc/bibliographic/bd300.html) and adding a call to `process_record()` like so:

```python
extent = extract_subfields(record=record, tag="300", subfield_code="a", ns=ns)
```

## Known Limitations

The automated cleaning processes do not catch 100% of records by design. For some applications, it might be desirable to perform other steps to correct certain values.

For example, while almost all works have a four-digit year of publication, some are expressed by catalogers with uncertainty, e.g., `"18--?"` or `"187-?"` The current model ignores such values (setting them to `0`, so that they are excluded from the analysis in preference to assuming that `"187?"` should be treated as `1870` or `1875`. Other researchers might prefer  the information encoded at the level of the decade or century in such strings. Less than 1% of records have uncertain or ambiguous dates.

## AI Statement

I used GitHub Copilot completions in writing some of this code.
