import csv
import sqlite3


def main():
    csv_path = "./tests/init_db_data.csv"
    db_path = "./tests/data.db"

    with open(csv_path) as csvfile:
        reader = csv.reader(csvfile)
        with sqlite3.connect(db_path) as db:
            cur = db.cursor()
            for row in reader:
                try:
                    to_insert = [ cell.lower() for cell in row ]
                    cur.execute("INSERT INTO inventory VALUES (?, ?, ?, ?)", to_insert)
                except sqlite3.IntegrityError:
                    pass
            db.commit()


if __name__ == '__main__':
    main()