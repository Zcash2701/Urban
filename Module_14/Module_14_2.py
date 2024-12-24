import sqlite3

connect = sqlite3.connect('not_telegram.db')
cursor = connect.cursor()

# 1) delete user #6
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

# 2)  users count
cursor.execute('SELECT COUNT(*) FROM Users')
user_count = cursor.fetchone()[0]

# 3) balance summ
cursor.execute('SELECT SUM(balance) FROM Users')
balance_sum = cursor.fetchone()[0]

# 4) avg balance  v1
cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]
print(avg_balance)
# v2
print(balance_sum/user_count)


connect.commit()
connect.close()