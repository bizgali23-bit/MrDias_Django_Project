import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print('Tables:')
for row in cur.fetchall():
    print(row[0])

try:
    cur.execute('SELECT COUNT(*) FROM users_emailverification')
    print('EmailVerification rows:', cur.fetchone()[0])
except Exception as e:
    print('EmailVerification table check error:', e)

try:
    cur.execute('SELECT COUNT(*) FROM users_user')
    print('Users rows:', cur.fetchone()[0])
except Exception as e:
    print('Users table check error:', e)

conn.close()
