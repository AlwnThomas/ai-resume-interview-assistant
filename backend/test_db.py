from database import engine

try:
    connection = engine.connect()
    print("succ")
    connection.close()

except Exception as e:
    print("Connection failed:")
    print(e)