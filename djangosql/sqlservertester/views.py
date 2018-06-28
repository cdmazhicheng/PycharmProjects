from django.shortcuts import render
from sqlservertester.calltables import user_table, coupon_table

#账号数据
def user(request):
    # 账号数据
    message_user = user_table.user_message(request) #pit_member_user表
    member_sms = user_table.member_user(request)#pit_member_sms表
    wechat_user = user_table.wechat_user(request)  # pit_wechat_user表
    member_finance = user_table.member_finance(request)  # pit_member_finance表

    # 优惠券信息
    market_coupon_to_user = coupon_table.market_coupon_to_user(request)  # pit_market_coupon_to_user表

    context = {
               # 账号数据
               'user_id': message_user[0][0],
               'suggest_user_id': message_user[0][1],
               'nickname': message_user[0][2],
               'mobile': message_user[0][3],
               'member_sms': member_sms[0][0],
               'wechat_user': wechat_user[0][0],
               'member_finance': member_finance[0][0],
               'oil_order_count': member_finance[0][1],
               'weixin_union_id': message_user[0][4],
               # 优惠券信息
               'test': market_coupon_to_user,
               }

    return render(request, 'sqlservertester/home.html', context)
