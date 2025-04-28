# Ingestion Health Monitor (for SDAP Collection Manager)

The **Ingestion Health Monitor** is a lightweight CLI tool designed to monitor the health of the ingestion pipeline for SDAP.  
It tracks both:

- New granule ingestions into **Solr**.
- Current queue depth inside **RabbitMQ**.

This helps detect ingestion stalls, backlogs, and repeated failures in real time, without needing to manually inspect systems.

GitHub repository:  
👉 [https://github.com/Jihnboii/sdap-ingester/tree/solr-monitor-tool](https://github.com/Jihnboii/sdap-ingester/tree/solr-monitor-tool)

---

## Prerequisites

- Python 3.7+
- Recommended: Create a virtual environment

```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
$ pip install -r requirements.txt  # Install dependencies
```

You must have access to a running instance of:

- Solr (port 8983 by default)
- RabbitMQ

You can easily set these up using SDAP Quickstart Docker images:  
🔗 [https://sdap-nexus.readthedocs.io/en/latest/build.html](https://sdap-nexus.readthedocs.io/en/latest/build.html)

---

## Running the Ingestion Health Monitor

From inside the `collection_manager/` directory, run:

```bash
$ python -m collection_manager.tools.solr_monitor --watch --interval 5
```

Available options:

| Option             | Description                                             |
| ------------------ | ------------------------------------------------------- |
| `--watch`          | Continuously poll Solr and RabbitMQ at intervals         |
| `--interval`       | Set polling interval in seconds (default: 10)            |
| `--granule`        | (Optional) Only monitor a specific granule               |
| `--rabbitmq-host`  | RabbitMQ host (default: `localhost`)                     |
| `--rabbitmq-user`  | RabbitMQ username (default: `user`)                      |
| `--rabbitmq-pass`  | RabbitMQ password (default: `bitnami`)                   |

Example with all options:

```bash
$ python -m collection_manager.tools.solr_monitor --watch --interval 5 --rabbitmq-host localhost --rabbitmq-user user --rabbitmq-pass bitnami
```

---

## Features

✅ Live Solr polling to detect new granule ingestion events  
✅ Live RabbitMQ queue depth monitoring  
✅ Alerts for repeated ingestion failures (zero tiles detected)  
✅ Lightweight CLI with animated updates (no terminal spamming)  
✅ Customizable polling intervals

---

## Windows Quickfix Notes

To enable local Windows development, we made minor fixes in the SDAP codebase:

- **GranuleLoader.py**  
  Forced NetCDF datasets to open using `engine="netcdf4"`.

- **CollectionProcessor.py**  
  Normalized granule file paths to `file:///` format for compatibility.

---

## Building SDAP Components

To run SDAP components locally:

```bash
$ cd common && python setup.py install
$ cd ../collection_manager && python setup.py install
```

Then run:

```bash
$ python collection_manager/collection_manager/main.py -h
```

Follow the README setup for SDAP Quickstart to launch Solr, RabbitMQ, and Nexus components.

---

# 📦 GitHub Repository

👉 [https://github.com/Jihnboii/sdap-ingester/tree/solr-monitor-tool](https://github.com/Jihnboii/sdap-ingester/tree/solr-monitor-tool)
