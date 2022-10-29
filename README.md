# HerHackathon-BASF-Sonequitas
## Backend for bar code app
- Receives a product's barcode number (read via mobile barcode reader)
- Crosschecks the number with a list of product's barcodes using an API
  - https://api.barcodelookup.com/v3/products
- Fetches the list of ingredients of the scanned product
- Compares with BASF catalogue
- Returns list of ingredients found that BASF produces
