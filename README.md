# GList

**(WIP)** GList is a simple, ultra-fast list management system that stores all data in JSON files. It is designed for small commerce and inventory workflows where data needs to be managed quickly without the complexity of a database.

> **Note:** The default table column names are in French. Feel free to modify them to match your language or workflow.

## Features

* Fast JSON-based data storage.
* Organize data into categories (typically suppliers).
* Each category contains its own list of items.
* Dedicated page for special orders (implemented as a category with a reserved name "commandes").
* Final summary page listing all suppliers, allowing you to record:

  * Paid amounts.
  * Merchandise pickup status.
* Automatically generate a clean, professional PDF report from the stored JSON data.

## Logo

To include a custom logo in the generated PDF, place a JPG image named:

```text
image/top_logo.jpg
```

inside the `image` folder.

**Recommended dimensions:** **21 cm × 5 cm**.
