import pymssql
from sqlserveruser import models

conn = pymssql.connect(host='192.168.5.32', user='test', password='85442791', database='Ytny')
cursor = conn.cursor()
mymobile = models.Persion.objects.values('mobile')[0]['mobile']

# 查询订单表数据
def oil_order(self):

    pit_sql_oil_order = "select id,org_amt,product_type_id,org_price,org_oil_litre " \
                        "from pit_oil_order " \
                        "where user_id=(select id from pit_member_user where mobile={})"\
                        "order by id".format(mymobile)
    cursor.execute(pit_sql_oil_order)
    rs_pit_sql_oil_order = cursor.fetchall()
    if rs_pit_sql_oil_order == []:
        rs_pit_sql_oil_order = [("--","--","--","--","--")]
    else:
        pass
    return rs_pit_sql_oil_order

# 查询订单支付记录表数据
def oil_order_pay(self):

    pit_sql_oil_order_pay = "select pay_amt,pay_remark " \
                            "from pit_oil_order_pay where order_id " \
                            "in(select id from pit_oil_order where user_id=(select id from pit_member_user where mobile={}))" \
                            "order by order_id".format(mymobile)
    cursor.execute(pit_sql_oil_order_pay)
    rs_pit_sql_oil_order_pay = cursor.fetchall()
    if rs_pit_sql_oil_order_pay == []:
        rs_pit_sql_oil_order_pay = [("--","--","--","--","--")]
    else:
        pass
    return rs_pit_sql_oil_order_pay

# 查询订单节省金额数据
def oil_order_discount(self):

    pit_sql_oil_order_discount = "select order_id, SUM(discount_amt) as discount_all " \
                                 "from pit_oil_order_discount where order_id " \
                                 "in(select id from pit_oil_order where user_id=(select id from pit_member_user where mobile={})) " \
                                 "group by order_id order by order_id;".format(mymobile)
    cursor.execute(pit_sql_oil_order_discount)
    rs_pit_sql_oil_order_discount = cursor.fetchall()
    if rs_pit_sql_oil_order_discount == []:
        rs_pit_sql_oil_order_discount = [(0,0,0,0,0)]
    else:
        pass
    return rs_pit_sql_oil_order_discount

# 查询订单优惠数据
def oil_order_discount_detail(self):

    pit_sql_oil_order_discount_detail = "select order_id, discount_type,discount_by,discount_amt " \
                                        "from pit_oil_order_discount " \
                                        "where order_id " \
                                        "in(select id from pit_oil_order " \
                                        "where user_id=(select id from pit_member_user " \
                                        "where mobile={})) order by order_id;".format(mymobile)
    cursor.execute(pit_sql_oil_order_discount_detail)
    rs_pit_sql_oil_order_discount_detail = cursor.fetchall()
    if rs_pit_sql_oil_order_discount_detail == []:
        rs_pit_sql_oil_order_discount_detail = [("--","--","--","--")]
    else:
        pass
    return rs_pit_sql_oil_order_discount_detail

