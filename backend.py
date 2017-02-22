import sqlite3
import folium
import os
import webbrowser
from geopy.geocoders import Nominatim


class DataAccess:

    def __init__(self):
        self.conn = sqlite3.connect("coffee_shops.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS coffee_shop (shop_id INTEGER PRIMARY KEY, name text, address text, city text,\
                    state text, zip_code integer, latitude text, longitude text)")
        self.conn.commit()

        self.geolocator = Nominatim()

    def __del__(self):
        self.conn.close()

    def insert(self, name, address, city, state, zip_code):
        full_address = address + ", " + city + ", " + state + " " + zip_code
        geo_address = self.geolocator.geocode(full_address)
        if geo_address is None:
            print "Not a recognized location"
            return -1
        latitude = str(geo_address.latitude)
        longitude = str(geo_address.longitude)

        self.cur.execute("INSERT INTO coffee_shop VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", (name, address, city, state, zip_code,
                                                                                   latitude, longitude))
        self.conn.commit()

    def view_address(self):
        self.cur.execute("SELECT shop_id, name, address, city, state, zip_code FROM coffee_shop")
        rows = self.cur.fetchall()
        return rows

    def view_all(self):
        self.cur.execute("SELECT * FROM coffee_shop")
        rows = self.cur.fetchall()
        return rows

    def search(self, name, address, city, state, zip_code):
        self.cur.execute("SELECT shop_id, name, address, state, zip_code FROM coffee_shop WHERE name=? OR address=? OR city=? \
                     OR state=? OR zip_code=?",
                    (name, address, city, state, zip_code))
        rows = self.cur.fetchall()
        return rows

    def delete(self, shop_id):
        self.cur.execute("DELETE FROM coffee_shop WHERE shop_id=?", (shop_id,))
        self.conn.commit()

    def update(self, shop_id, name, address, city, state, zip_code):
        full_address = address + ", " + city + ", " + state + " " + zip_code
        geo_address = self.geolocator.geocode(full_address)
        if geo_address is None:
            print "Not a recognized location"
            return -1
        latitude = str(geo_address.latitude)
        longitude = str(geo_address.longitude)

        self.cur.execute("UPDATE coffee_shop SET name=?, address=?, city=?, state=?, zip_code=?, latitude=?, longitude=? \
          WHERE shop_id=?",
                    (name, address, city, state, zip_code, latitude, longitude, shop_id))
        self.conn.commit()

    def show_map(self):
        home = self.geolocator.geocode("4604 West Ox Rd, Fairfax, VA 22030")
        map = folium.Map(location=[home.latitude, home.longitude], zoom_start=12)
        map.simple_marker(location=[home.latitude, home.longitude], popup="Elik", marker_color="red")
        for shop in self.view_all():
            data = list(shop)
            map.simple_marker(location=[data[6], data[7]], popup=data[1], marker_color="green")
        filename = 'coffee_shops_around_me.html'
        map.create_map(path=filename)
        webbrowser.open('file://' + os.path.realpath(filename))

