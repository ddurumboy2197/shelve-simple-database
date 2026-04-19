import shelve

# Shelve bilan oddiy database yaratish
def create_database(filename):
    try:
        db = shelve.open(filename)
        return db
    except Exception as e:
        print(f"Error: {e}")

# Kalit-qiymat qo'shish
def add_item(db, key, value):
    db[key] = value

# Kalit-qiymat o'zgartirish
def update_item(db, key, value):
    if key in db:
        db[key] = value
    else:
        print("Kalit mavjud emas.")

# Kalit-qiymat o'chirish
def delete_item(db, key):
    if key in db:
        del db[key]
    else:
        print("Kalit mavjud emas.")

# Kalit-qiymat ko'rish
def read_item(db, key):
    if key in db:
        return db[key]
    else:
        print("Kalit mavjud emas.")

# Shelve bilan database yopish
def close_database(db):
    db.close()

# Test qismi
if __name__ == "__main__":
    filename = "example.db"
    db = create_database(filename)

    add_item(db, "name", "John Doe")
    add_item(db, "age", 30)

    print(read_item(db, "name"))  # John Doe
    print(read_item(db, "age"))   # 30

    update_item(db, "age", 31)
    print(read_item(db, "age"))   # 31

    delete_item(db, "name")
    print(read_item(db, "name"))  # Kalit mavjud emas.

    close_database(db)
