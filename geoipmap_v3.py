import socket
import folium
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl, IPvAnyAddress
from fastapi.responses import HTMLResponse, FileResponse
import geoip2.database

# === Configuration ===
MAP_PATH = "ip_map.html"
GEO_DB_PATH = "./maxmind/GeoLite2-City_20250509/GeoLite2-City.mmdb"

# Define data model
class IPAddressInput(BaseModel):
    ip: IPvAnyAddress

# === Input Model ===
class URLInput(BaseModel):
    url: HttpUrl

# === App and State ===
app = FastAPI()
ip_data = []  # List of {"ip": ..., "hostname": ...}
#fmap = folium.Map(location=[0, 0], zoom_start=3)
# === Load GeoIP2 database ===
try:
    reader = geoip2.database.Reader(GEO_DB_PATH)
except FileNotFoundError:
    raise RuntimeError(f"GeoLite2 database not found at: {GEO_DB_PATH}")

# === Function to update map file ===
def update_map(col="blue"):
    fmap = folium.Map(location=[0, 0], zoom_start=3)
    for entry in ip_data:
        ip = entry["ip"]
        hostname = entry["hostname"]
        try:
            geo = reader.city(ip)
            lat, lon = geo.location.latitude, geo.location.longitude
            if lat and lon:
                folium.Marker(
                    location=[lat, lon],
                    popup=f"{hostname} ({ip})",
                    icon=folium.Icon(color=entry["marker_color"], icon="globe")
                ).add_to(fmap)
            else:
                print(f"IP not found in Geo List: {ip}")
        except Exception:
            continue
    fmap.save(MAP_PATH)


@app.post("/add_ip/")
def add_ip(ip_input: IPAddressInput):
    ip = str(ip_input.ip)

    # Add IP to memory
    if not any(entry["ip"] == ip for entry in ip_data):
        ip_data.append({"ip": ip, "hostname": "", "marker_color": "red"})
        update_map()

    return {"message": "IP added"}


# === API: Add URL and update map ===
@app.post("/add_url/")
def add_url(data: URLInput):
    try:
        hostname = data.url.host
        ip = socket.gethostbyname(hostname)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"DNS resolution failed: {e}")

    if not any(entry["ip"] == ip for entry in ip_data):
        ip_data.append({"ip": ip, "hostname": hostname, "marker_color":"blue"})
        update_map()

    return {"message": "IP resolved and added", "ip": ip, "hostname": hostname}

# === API: Serve iframe map page with auto-refresh ===
@app.get("/map", response_class=HTMLResponse)
def get_map_wrapper():
    if not os.path.exists(MAP_PATH):
        raise HTTPException(status_code=404, detail="Map not yet generated")

    html_wrapper = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>IP Map</title>
        <meta http-equiv="refresh" content="3">
        <style>
            body, html { margin: 0; padding: 0; height: 100%; }
            iframe { border: none; width: 100%; height: 100%; }
        </style>
    </head>
    <body>
        <iframe src="/ip_map"></iframe>
    </body>
    </html>
    """
    return html_wrapper

# === API: Serve the static ip_map.html file itself ===
@app.get("/ip_map", response_class=HTMLResponse)
def serve_map_file():
    if os.path.exists(MAP_PATH):
        with open(MAP_PATH, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise HTTPException(status_code=404, detail="Map file not found")

# === Run with: uvicorn script_name:app ===
