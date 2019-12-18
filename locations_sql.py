from mysql.connector import connect


def delete_locations():
    cursor = conn.cursor()
    cursor.execute("delete from location_tags")
    cursor.execute("delete from locations")
    cursor.close()


def count_locations():
    cursor = conn.cursor()
    cursor.execute("select count(*) from locations")
    count = ""
    for row in cursor:
        count = row[0]
    cursor.close()
    return count


def print_locations():
    cursor = conn.cursor()
    cursor.execute("select name, lat, lon from locations")
    for (name, lat, lon) in cursor:
        print(f"{name} ({lat}, {lon})")
    cursor.close()


def insert_location(name, coords):
    coords = coords.split(",")
    lat = coords[0]
    lon = coords[1]
    cursor = conn.cursor()
    cursor.execute(f"insert into locations (NAME, lat, lon) VALUES (%s, %s, %s)", (name, lat, lon))
    cursor.close()


def assert_location_exists(name, coords):
    coords = coords.split(",")
    lat = coords[0]
    lon = coords[1]
    cursor = conn.cursor()
    cursor.execute("select count(*) from locations where name = %s and lat = %s and lon = %s", (name, lat, lon)
                   )
    for (count,) in cursor:
        assert not count == 0
    cursor.close()


def assert_location_exists_alt(name, coords):
    loc_found = find_location_by_name(name)
    assert loc_found is not None
    coords = coords.split(",")
    lat = float(coords[0])
    lon = float(coords[1])
    assert lat == loc_found[1]
    assert lon == loc_found[2]


def find_location_by_name(name):
    location_found = None
    cursor = conn.cursor()
    cursor.execute("select name, lat, lon from locations where name = %s", (name,))
    for (name, lat, lon) in cursor:
        location_found = (name, lat, lon)
    return location_found
    cursor.close()


conn = connect(
    host="localhost",
    user="locations",
    passwd="locations",
    database="locations"
)

#cursor = conn.cursor()
#letter = input("Add meg az első betűt")
#cursor.execute(f"select name, lat, lon from locations where name like '{letter}%'")
#for (name, lat, lon) in cursor:
#    print(f"{name} ({lat}, {lon})")
#cursor.close()

#insert_location("Beregszász", "44.00,88.22")

assert_location_exists("Beregszász", "44.00,88.22")

print(find_location_by_name("Beregszász"))

print_locations()

cursor = conn.cursor()
cursor.execute("update locations set name = concat(name, 'yyy'), lat = lat + 3 where name like 'Budapest'")
conn.commit()