import pymssql

conn = pymssql.connect(host='192.168.5.32', user='test', password='85442791', database='Ytny')
cursor = conn.cursor()

# 查询用户的优惠券
pit_sql_market_coupon_to_user = "select * from pit_market_coupon_to_user " \
                                "where user_id =(select id from pit_member_user where mobile='13551002117')"
cursor.execute(pit_sql_market_coupon_to_user)
rs_pit_sql_market_coupon_to_user = cursor.fetchall()

for i in range(len(rs_pit_sql_market_coupon_to_user)):
    print(rs_pit_sql_market_coupon_to_user[i])

