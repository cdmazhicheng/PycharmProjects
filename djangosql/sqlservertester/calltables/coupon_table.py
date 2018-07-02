import pymssql

conn = pymssql.connect(host='192.168.5.32', user='test', password='85442791', database='Ytny')
cursor = conn.cursor()
mymobile = "13551002117"

# 查询用户的优惠券
def market_coupon_to_user(self):

    pit_sql_market_coupon_to_user = "select " \
                                    "pit_market_coupon_to_user.coupon_id, " \
                                    "pit_market_coupon_to_user.valid_end_time, " \
                                    "pit_market_coupon_to_user.is_used, " \
                                    "pit_market_coupon_to_user.use_order_id, " \
                                    "pit_market_coupon.name, " \
                                    "pit_market_coupon.send_method " \
                                    "from pit_market_coupon_to_user left join pit_market_coupon on pit_market_coupon_to_user.coupon_id = pit_market_coupon.id " \
                                    "where pit_market_coupon_to_user.user_id =(select id from pit_member_user where mobile={})".format(mymobile)
    cursor.execute(pit_sql_market_coupon_to_user)
    rs_pit_sql_market_coupon_to_user = cursor.fetchall()
    if rs_pit_sql_market_coupon_to_user == []:
        rs_pit_sql_market_coupon_to_user = [("--","--","--","--","--","--")]
    else:
        pass
    return rs_pit_sql_market_coupon_to_user

#优惠券所关联的礼包
def market_coupon_to_package(self):

    pit_sql_market_coupon_to_package = "select pit_market_coupon.id, pit_market_coupon_package.name from pit_market_coupon " \
                                       "inner join pit_market_coupon_to_package on pit_market_coupon.id = pit_market_coupon_to_package.coupon_id " \
                                       "inner join pit_market_coupon_package on pit_market_coupon_to_package.package_id = pit_market_coupon_package.id " \
                                       "where pit_market_coupon.id in (select coupon_id from pit_market_coupon_to_user " \
                                       "where user_id =(select id from pit_member_user where mobile={}))".format(mymobile)
    cursor.execute(pit_sql_market_coupon_to_package)
    rs_pit_sql_market_coupon_to_package = cursor.fetchall()

    b = []
    for j in range(len(rs_pit_sql_market_coupon_to_package)):
        a = [rs_pit_sql_market_coupon_to_package[j][0]]
        midderer = rs_pit_sql_market_coupon_to_package[j][0]
        for i in range(len(rs_pit_sql_market_coupon_to_package)):
            if midderer == rs_pit_sql_market_coupon_to_package[i][0]:
                a.append(rs_pit_sql_market_coupon_to_package[i][1])
            else:
                pass
        b.append(tuple(a))

    result_coupon = list(set(b))

    resulted_coupon = []
    for i in range(len(result_coupon)):
        c = [result_coupon[i][0]]
        s1 = "、"
        c.append(s1.join(result_coupon[i][1:]))
        resulted_coupon.append(c)

    if resulted_coupon == []:
        resulted_coupon = [("--","--")]
    else:
        pass

    return resulted_coupon
