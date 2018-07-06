import pymssql

conn = pymssql.connect(host='192.168.5.32', user='test', password='85442791', database='Ytny')
cursor = conn.cursor()
begin_time = '2018-04-04'
end_time = '2018-04-05'

#######注册用户模块##########

# 时间区间中的注册人员
def pit_member_user_register(self):

    sql_pit_member_user_register = "select COUNT(*) from pit_member_user " \
                          "where register_time > = '{} 00:00:00.000' and register_time < = '{} 00:00:00.000'".format(begin_time, end_time)
    cursor.execute(sql_pit_member_user_register)
    rs_sql_pit_member_user_register= cursor.fetchall()
    return rs_sql_pit_member_user_register

# 当日注册人员
def pit_member_user_register_today(self):

    sql_pit_member_user_register_today = "select COUNT(*) from pit_member_user where DateDiff(dd,register_time,getdate())=0"
    cursor.execute(sql_pit_member_user_register_today)
    rs_sql_pit_member_user_register_today= cursor.fetchall()
    return rs_sql_pit_member_user_register_today

# 昨日注册人员
def pit_member_user_register_yesterday(self):

    sql_pit_member_user_register_yesterday = "select COUNT(*) from pit_member_user where DateDiff(dd,register_time,getdate())=1"
    cursor.execute(sql_pit_member_user_register_yesterday)
    rs_sql_pit_member_user_register_yesterday= cursor.fetchall()
    return rs_sql_pit_member_user_register_yesterday



#######新增会员模块##########

#新增会员数量
def pit_member_user_vip(self):
    sql_pit_member_user_vip = "select COUNT(*) from pit_member_finance " \
                              "inner join pit_member_user " \
                              "on pit_member_user.id = pit_member_finance.id " \
                              "where pit_member_user.register_time > = '{} 00:00:00.000' " \
                              "and pit_member_user.register_time < = '{} 00:00:00.000' " \
                              "and pit_member_finance.growth_level>0".format(begin_time, end_time)
    cursor.execute(sql_pit_member_user_vip)
    rs_sql_pit_member_user_vip= cursor.fetchall()
    return rs_sql_pit_member_user_vip

# 当日新增会员
def pit_member_user_vip_today(self):
    sql_pit_member_user_vip_today = "select COUNT(*) from pit_member_finance " \
                                    "inner join pit_member_user " \
                                    "on pit_member_user.id = pit_member_finance.id " \
                                    "where DateDiff(dd,pit_member_user.register_time,getdate())=0 " \
                                    "and pit_member_finance.growth_level>0"
    cursor.execute(sql_pit_member_user_vip_today)
    rs_sql_pit_member_user_vip_today= cursor.fetchall()
    return rs_sql_pit_member_user_vip_today

#  昨日新增会员
def pit_member_user_vip_yesterday(self):
    sql_pit_member_user_vip_yesterday = "select COUNT(*) from pit_member_finance " \
                                    "inner join pit_member_user " \
                                    "on pit_member_user.id = pit_member_finance.id " \
                                    "where DateDiff(dd,pit_member_user.register_time,getdate())=0 " \
                                    "and pit_member_finance.growth_level=1"
    cursor.execute(sql_pit_member_user_vip_yesterday)
    rs_sql_pit_member_user_vip_yesterday= cursor.fetchall()
    return rs_sql_pit_member_user_vip_yesterday


#######支付人数##########

#  选取时间段的支付人数
def pit_member_user_pay_number(self):
    sql_pit_member_user_pay_number = "select pit_oil_order.user_id,COUNT(*) from pit_member_finance " \
                                 "inner join pit_member_user " \
                                 "on pit_member_user.id = pit_member_finance.id " \
                                 "inner join pit_oil_order " \
                                 "on pit_member_user.id = pit_oil_order.user_id " \
                                 "where pit_oil_order.pay_time > = '{} 00:00:00.000' " \
                                 "and pit_oil_order.pay_time < = '{} 00:00:00.000' " \
                                 "and pit_member_finance.growth_level>0 group by user_id ".format(begin_time, end_time)
    cursor.execute(sql_pit_member_user_pay_number)
    rs_sql_pit_member_user_user_pay_number= cursor.fetchall()
    return rs_sql_pit_member_user_user_pay_number

#  今日支付人数
def pit_member_user_pay_number_today(self):
    sql_pit_member_user_pay_number_today = "select pit_oil_order.user_id,COUNT(*) from pit_member_finance " \
                                           "inner join pit_member_user " \
                                           "on pit_member_user.id = pit_member_finance.id " \
                                           "inner join pit_oil_order " \
                                           "on pit_member_user.id = pit_oil_order.user_id " \
                                           "where DateDiff(dd,pit_oil_order.pay_time,getdate())=0 " \
                                           "and pit_member_finance.growth_level>0 group by user_id".format(begin_time, end_time)
    cursor.execute(sql_pit_member_user_pay_number_today)
    rs_sql_pit_member_user_user_pay_number_today= cursor.fetchall()
    return rs_sql_pit_member_user_user_pay_number_today

#  昨日支付人数
def pit_member_user_pay_number_yesterday(self):
    sql_pit_member_user_pay_number_yesterday = "select pit_oil_order.user_id,COUNT(*) from pit_member_finance " \
                                           "inner join pit_member_user " \
                                           "on pit_member_user.id = pit_member_finance.id " \
                                           "inner join pit_oil_order " \
                                           "on pit_member_user.id = pit_oil_order.user_id " \
                                           "where DateDiff(dd,pit_oil_order.pay_time,getdate())=1 " \
                                           "and pit_member_finance.growth_level>0 group by user_id".format(begin_time, end_time)
    cursor.execute(sql_pit_member_user_pay_number_yesterday)
    rs_sql_pit_member_user_user_pay_number_yesterday = cursor.fetchall()
    return rs_sql_pit_member_user_user_pay_number_yesterday


#######支付金额##########

#  选取时间段的支付金额
def pit_member_user_pay_amt(self):
    sql_pit_member_user_pay_amt = "select sum(pit_oil_order.pay_amt) from pit_member_finance " \
                                  "inner join pit_member_user on pit_member_user.id = pit_member_finance.id " \
                                  "inner join pit_oil_order on pit_member_user.id = pit_oil_order.user_id " \
                                  "where pit_oil_order.pay_time > = '{} 00:00:00.000' " \
                                  "and pit_oil_order.pay_time < = '{} 00:00:00.000' " \
                                  "and pit_member_finance.growth_level>0".format(begin_time, end_time)
    cursor.execute(sql_pit_member_user_pay_amt)
    rs_sql_pit_member_user_user_pay_amt= cursor.fetchall()
    return rs_sql_pit_member_user_user_pay_amt

#  当日的支付金额
def pit_member_user_pay_amt_today(self):
    sql_pit_member_user_pay_amt_today = "select sum(pit_oil_order.pay_amt) from pit_member_finance " \
                                        "inner join pit_member_user on pit_member_user.id = pit_member_finance.id " \
                                        "inner join pit_oil_order on pit_member_user.id = pit_oil_order.user_id " \
                                        "where DateDiff(dd,pit_oil_order.pay_time,getdate())=0  " \
                                        "and pit_member_finance.growth_level>0"
    cursor.execute(sql_pit_member_user_pay_amt_today)
    rs_sql_pit_member_user_user_pay_amt_today= cursor.fetchall()
    return rs_sql_pit_member_user_user_pay_amt_today

#  昨日的支付金额
def pit_member_user_pay_amt_yesterday(self):
    sql_pit_member_user_pay_amt_yesterday = "select sum(pit_oil_order.pay_amt) from pit_member_finance " \
                                        "inner join pit_member_user on pit_member_user.id = pit_member_finance.id " \
                                        "inner join pit_oil_order on pit_member_user.id = pit_oil_order.user_id " \
                                        "where DateDiff(dd,pit_oil_order.pay_time,getdate())=1  " \
                                        "and pit_member_finance.growth_level>0"
    cursor.execute(sql_pit_member_user_pay_amt_yesterday)
    rs_sql_pit_member_user_user_pay_amt_yesterday= cursor.fetchall()
    return rs_sql_pit_member_user_user_pay_amt_yesterday