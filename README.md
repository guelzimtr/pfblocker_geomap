
# pfblocker_geomap

**pfblocker_geomap** is a Python-based tool designed to visualize IP ranges blocked by pfBlockerNG on pfSense. By leveraging GeoIP data, it generates interactive maps that help administrators understand the geographical distribution of blocked IP addresses.

---

## 🧭 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Download GeoIP Database](#-download-geoip-database)
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

### Create a Virtual Environment and Install Requirements

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🗺️ Download GeoIP Database

To enable IP geolocation, you must download the GeoLite2 database from MaxMind.

1. Create a free account at [MaxMind](https://www.maxmind.com).
2. Download the `GeoLite2-City.mmdb` database file.
3. Place the `.mmdb` file in your project directory, or specify its full path in the `config.yaml` file.

---

## 🧪 Usage

Run the script from your terminal:

```bash
python pfblocker_geomap.py
```

The script will:
- Parse the pfBlockerNG input data.
- Perform GeoIP lookups.
- Generate an interactive map in HTML format in the `output` directory.

---

## ⚙️ Configuration

Edit the `config.yaml` file to fit your setup:

```yaml
geoip_db_path: "/path/to/GeoLite2-City.mmdb"
input_file: "data/pfblockerng.log"
output_dir: "output"
map_title: "Blocked IP Regions"
default_zoom: 2
color_scheme: "red"
```

- `geoip_db_path`: Path to the GeoIP database.
- `input_file`: pfBlockerNG log or configuration output.
- `output_dir`: Where the map HTML and assets will be saved.
- `map_title`: Title displayed on the map.
- `default_zoom`: Default zoom level for the map.
- `color_scheme`: Color used for blocked regions.

---

## 📤 Output

- `output/map.html`: Interactive HTML map of blocked IP ranges.
- (Planned) Export to CSV and JSON for integration with other tools.

---

## 📈 Roadmap

- [x] Initial IP parsing and geolocation
- [x] Interactive map output
- [ ] CLI argument support
- [ ] Export in CSV/JSON
- [ ] Support for pfBlockerNG aliases
- [ ] Docker container for deployment

---

## 🤝 Contributing

We welcome contributions of all kinds!

### How to contribute

1. Fork the repository
2. Create your feature branch:

   ```bash
   git checkout -b feature/my-feature
   ```

3. Commit your changes:

   ```bash
   git commit -am 'Add my feature'
   ```

4. Push to your fork:

   ```bash
   git push origin feature/my-feature
   ```

5. Open a pull request describing your changes

---

## 📝 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [pfBlockerNG](https://docs.netgate.com/pfsense/en/latest/packages/pfblocker.html)
- [MaxMind GeoLite2](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data)
- [Folium](https://python-visualization.github.io/folium/) for map rendering

---

## 📬 Contact

**Maintainer**: [Guelzim T.](https://github.com/guelzimtr)  
**Repository**: [https://github.com/guelzimtr/pfblocker_geomap](https://github.com/guelzimtr/pfblocker_geomap)

---

## ⭐️ Show Your Support

If you found this tool helpful:

- Give us a ⭐️ on GitHub
- Share it with colleagues and the community
