# API Consumer

A Python script that fetches product data from the DummyJSON API and processes it into clean datasets.

## Features

The data is normalized into the following fields:

- id
- name
- category
- price
- rating
- inStock

## Supported Operations

- Sort by price.
- Sort by rating.
- Filter in-stock products.
- Retrieve top N most expensive products.

## Output Formats

The processed data is exported as:

- JSON
- CSV
- TXT

You can apply one operation or export the normalized data without processing.

#

## Error handling

The program stops execution if the API returns an error or invalid input is provided.
