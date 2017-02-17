import sqlite3
import folium
import os
import webbrowser
from geopy.geocoders import Nominatim


def connect():
    conn = sqlite3.connect("coffee_shops.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS coffee_shop (shop_id INTEGER PRIMARY KEY, name text, address text, city text,\
                state text, zip_code integer, latitude text, longitude text)")
    conn.commit()
    conn.close()


def insert(name, address, city, state, zip_code):
    full_address = address + ", " + city + ", " + state + " " + zip_code
    geo_address = geolocator.geocode(full_address)
    if geo_address is None:
        print "Not a recognized location"
        return -1
    latitude = str(geo_address.latitude)
    longitude = str(geo_address.longitude)

    conn = sqlite3.connect("coffee_shops.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO coffee_shop VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", (name, address, city, state, zip_code,
                                                                               latitude, longitude))
    conn.commit()
    conn.close()


def view_address():
    conn = sqlite3.connect("coffee_shops.db")
    cur = conn.cursor()
    cur.execute("SELECT shop_id, name, address, state, zip_code FROM coffee_shop")
    rows = cur.fetchall()
    conn.close()
    return rows


def view_all():
    conn = sqlite3.connect("coffee_shops.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM coffee_shop")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name, address, city, state, zip_code):
    conn = sqlite3.connect("coffee_shops.db")
    cur = conn.cursor()
    cur.execute("SELECT shop_id, name, address, state, zip_code FROM coffee_shop WHERE name=? OR address=? OR city=? \
                 OR state=? OR zip_code=?",
                (name, address, city, state, zip_code))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(shop_id):
    conn = sqlite3.connect("coffee_shops.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM coffee_shop WHERE shop_id=?", (shop_id,))
    conn.commit()
    conn.close()


def update(shop_id, name, address, city, state, zip_code):
    full_address = address + ", " + city + ", " + state + " " + zip_code
    geo_address = geolocator.geocode(full_address)
    if geo_address is None:
        print "Not a recognized location"
        return -1
    latitude = str(geo_address.latitude)
    longitude = str(geo_address.longitude)

    conn = sqlite3.connect("coffee_shops.db")
    cur = conn.cursor()
    cur.execute("UPDATE coffee_shop SET name=?, address=?, city=?, state=?, zip_code=?, latitude=?, longitude=? \
                 WHERE shop_id=?",
                (name, address, city, state, zip_code, shop_id, latitude, longitude))
    conn.commit()
    conn.close()


def show_map():
    home = geolocator.geocode("4604 West Ox Rd, Fairfax, VA 22030")
    map = folium.Map(location=[home.latitude, home.longitude], zoom_start=12)
    map.simple_marker(location=[home.latitude, home.longitude], popup="Elik", marker_color="red")
    for shop in view_all():
        print shop
        data = list(shop)
        print data
        print data[6]
        print data[7]
        map.simple_marker(location=[data[6], data[7]], popup=data[1], marker_color="green")
    filename = 'coffee_shops_around_me.html'
    map.create_map(path=filename)
    webbrowser.open('file://' + os.path.realpath(filename))

connect()
geolocator = Nominatim()