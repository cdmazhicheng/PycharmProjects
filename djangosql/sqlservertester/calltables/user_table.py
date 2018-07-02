import pymssql

conn = pymssql.connect(host='192.168.5.32', user='test', password='85442791', database='Ytny')
cursor = conn.cursor()
mymobile = "13551002117"

# 查询用户表数据
def user_message(self):

    pit_sql_user_message = "select id,suggest_user_id,nickname,mobile,weixin_union_id " \
                           "from pit_member_user " \
                           "where mobile={}".format(mymobile)
    cursor.execute(pit_sql_user_message)
    rs_pit_sql_user_message = cursor.fetchall()
    if rs_pit_sql_user_message == []:
        rs_pit_sql_user_message = [("还没有建立账号！","--","--","--","--")]
    else:
        pass
    return rs_pit_sql_user_message

# 查看用户短信验证码
def member_user(self):

    pit_sql_member_user = "select code " \
                          "from pit_member_sms " \
                          "where send_time=(select MAX(send_time) from pit_member_sms where mobile={})".format(mymobile)
    cursor.execute(pit_sql_member_user)
    rs_pit_sql_member_user = cursor.fetchall()
    if rs_pit_sql_member_user == []:
        rs_pit_sql_member_user = [("--",)]
    else:
        pass
    return rs_pit_sql_member_user

# 查看用户微信信息
def wechat_user(self):

    pit_sql_wechat_user = "select follow_status " \
                          "from pit_wechat_user " \
                          "where member_user_id=(select id from pit_member_user where mobile={})".format(mymobile)
    cursor.execute(pit_sql_wechat_user)
    rs_pit_sql_wechat_user = cursor.fetchall()
    if rs_pit_sql_wechat_user == []:
        rs_pit_sql_wechat_user = [("亲，微信还未与手机绑定！",)]
    else:
        pass
    return rs_pit_sql_wechat_user

# 查看用户金额信息
def member_finance(self):

    pit_sql_member_finance = "select coin_balance, oil_order_count " \
                             "from pit_member_finance " \
                             "where id =(select id from pit_member_user where mobile={})".format(mymobile)
    cursor.execute(pit_sql_member_finance)
    rs_pit_sql_member_finance = cursor.fetchall()
    if rs_pit_sql_member_finance == []:
        rs_pit_sql_member_finance = [("--","--")]
    else:
        pass
    return rs_pit_sql_member_finance