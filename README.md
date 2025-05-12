# pfblocker_geomap

**pfblocker_geomap** is a Python-based tool designed to visualize IP ranges blocked by pfBlockerNG on pfSense. By leveraging GeoIP data, it generates interactive maps that help administrators understand the geographical distribution of blocked IP addresses.

---

## 🧭 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Output](#-output)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Contact](#-contact)
- [Show Your Support](#️-show-your-support)

---

## 🚀 Features

- Extracts blocked IP ranges from pfBlockerNG configuration or logs.
- Maps IP ranges to geographical locations using GeoIP.
- Generates interactive, zoomable HTML maps.
- Customizable map styles and output formats.
- Lightweight and easy to integrate into existing pfSense environments.

---

## 📸 Screenshots

![Sample Map](images/sample_map.png)

*Example: Interactive map showing blocked IP ranges by country.*

---

## 📋 Prerequisites

- Python 3.6+
- Access to pfBlockerNG IP block data (via config or export)
- MaxMind GeoLite2 or GeoIP2 database (requires free registration)
- `pip` package manager

---

## ⚙️ Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/guelzimtr/pfblocker_geomap.git
   cd pfblocker_geomap

## 🗺️ Download GeoIP Database

To enable IP geolocation, follow these steps:

1. Create a free account at [MaxMind](https://www.maxmind.com).
2. Download the **GeoLite2-City.mmdb** database.
3. Place the `.mmdb` file in the project directory **or** specify its full path in the `config.yaml` file.


