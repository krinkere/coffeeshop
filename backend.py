import sqlite3


def connect():
    conn = sqlite3.connect("coffee_shops.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS coffee_shop (shop_id INTEGER PRIMARY KEY, name text, address text, city text,\
                state text, zip_code integer)")
    conn.commit()
    conn.close()


def insert(name, address, city, state, zip_code):
    conn = sqlite3.connect("coffee_shops.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO coffee_shop VALUES (NULL, ?, ?, ?, ?, ?)", (name, address, city, state, zip_code))
    conn.commit()
    conn.close()


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
    cur.execute("SELECT * FROM coffee_shop WHERE name=? OR address=? OR city=? OR state=? OR zip_code=?",
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
    conn = sqlite3.connect("coffee_shops.db")
    cur = conn.cursor()
    cur.execute("UPDATE coffee_shop SET name=?, address=?, city=?, state=?, zip_code=? WHERE shop_id=?",
                (name, address, city, state, zip_code, shop_id))
    conn.commit()
    conn.close()

connect()