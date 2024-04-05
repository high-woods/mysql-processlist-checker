#!/usr/bin/env python

import MySQLdb
import sqlparse


def main():
    db = MySQLdb.connect(
        host="127.0.0.1",
        # port=3306,
        user="root",
        passwd="password",
        db="testdb"
    )
    cur = db.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("select * from information_schema.PROCESSLIST where INFO IS NOT NULL and INFO NOT LIKE '%PROCESSLIST%'")
    rows = cur.fetchall()
    if len(rows) > 0:
        for row in rows:
            t = row["TIME_MS"]
            mem = row["MEMORY_USED"]
            max_mem = row["MAX_MEMORY_USED"]
            sql = row["INFO"]
            print("======================")
            print(f"time={t:,} msec")
            print(f"mem={mem:,}/{max_mem:,}")
            print(sqlparse.format(sql, reindent=True))
    else:
        print("No SQL process")

if __name__ == '__main__':
    main()

