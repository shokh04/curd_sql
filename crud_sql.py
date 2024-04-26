import psycopg2

host = 'localhost'
user = 'postgres'
password = '1'
database = 'project'
port = 5432

conn = psycopg2.connect(host=host,
                        user=user,
                        password=password,
                        database=database,
                        port=port
                        )
cur = conn.cursor()


# CREATE

create_table = '''
    INSERT INTO cars (make ,model)
    VALUES ('Chevrolet', 'Jentra'),
           ('Chevrolet', 'Malibu'),
           ('Chevrolet', 'Equinox'),
           ('Chevrolet', 'Damas')
           ;
'''
cur.execute(create_table)
conn.commit()


# READ

select_car = '''
    SELECT * FROM cars ORDER BY id;
'''
cur.execute(select_car)
for i in cur.fetchall():
    print(i)


# UPDATE

update_car = '''
UPDATE cars SET make = 'BMW', model = 'M5' WHERE id = 4;
'''
cur.execute(update_table)
conn.commit()


# DELETE

delete_car = '''
    DELETE FROM cars WHERE id = 1;
'''
cur.execute(delete_car)
conn.commit()





# fibonacci
class Fibo:
    def __init__(self, stop):
        self.stop = stop
        self.prev = 0
        self.current = 1
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.stop:
            raise StopIteration
        else:
            result = self.prev
            self.prev, self.current = self.current, self.prev + self.current
            self.counter += 1
            return result


limit = int(input("Fibonacci sonini kiriting: "))
fib = Fibo(limit)
for i in fib:
    print(i)