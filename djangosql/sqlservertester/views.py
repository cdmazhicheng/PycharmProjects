from django.shortcuts import render
from sqlservertester.calltables import user_table, coupon_table, order_table
import time

#账号数据
def user(request):
    # 账号数据
    message_user = user_table.user_message(request) #pit_member_user表
    member_sms = user_table.member_user(request)#pit_member_sms表
    wechat_user = user_table.wechat_user(request)  # pit_wechat_user表
    member_finance = user_table.member_finance(request)  # pit_member_finance表

    # 格式化成2016-03-20 11:45:39形式
    mylocaltime = time.strftime("%Y-%m-%d", time.localtime())

    # 优惠券信息
    market_coupon_to_user = coupon_table.market_coupon_to_user(request)  # pit_market_coupon_to_user,pit_market_coupon表
    number_coupon = range(len(coupon_table.market_coupon_to_user(request)))#包含券的个数
    market_coupon_to_package = coupon_table.market_coupon_to_package(request) # pit_market_coupon,pit_market_coupon_to_package,pit_market_coupon_package表
    number_market_coupon_to_package = range(len(coupon_table.market_coupon_to_package(request)))#包含礼包的券的个数

    #订单信息
    oil_order_pay_sum = 0
    oil_order = order_table.oil_order(request)  # pit_oil_order表
    oil_order_pay = order_table.oil_order_pay(request)  # pit_oil_order_pay表
    oil_order_discount = order_table.oil_order_discount(request)  # pit_oil_order_discount表

    for i in range(len(oil_order_discount)):
        oil_order_pay_sum += int(order_table.oil_order_discount(request)[i][1])

    oil_order_discount_detail = order_table.oil_order_discount_detail(request)  # pit_oil_order_discount表

    order_list = zip(oil_order,oil_order_pay,oil_order_discount)

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
               'coupon': market_coupon_to_user,
                'number_coupon': number_coupon,
                'mylocaltime': mylocaltime,
                'market_coupon_to_package': market_coupon_to_package,
                'number_market_coupon_to_package': number_market_coupon_to_package,

                #订单信息
                'order_list': order_list,
                'oil_order_discount_detail': oil_order_discount_detail,
                'oil_order_pay_sum': oil_order_pay_sum,

               }

    return render(request, 'sqlservertester/home.html', context)
