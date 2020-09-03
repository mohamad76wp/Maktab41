print('gi')
# product_list = [
#        {
#            "type": "1",
#            "name": "shirt",
#            "price": 30,
#            "unit": "Dollar",
#            "commission_groups": ["A", "B"]
#        },
#        {
#            "type": "2",
#            "name": "pants",
#            "price": 50,
#            "unit": "Dollar",
#            "commission_groups": ["A", "C"]
#        },
#        {
#            "type": "3",
#            "name": "shoes",
#            "price": 80,
#            "unit": "Dollar",
#            "commission_groups": ["B"]
#        },
#        {
#            "type": "4",
#            "name": "hat",
#            "price": 20,
#            "unit": "Dollar",
#            "commission_groups": []
#        }
# ]
#
# markup_list = [
#     {
#         "product_type": "1",
#         "lower_cost": 10,
#         "upper_cost": 20,
#         "unit": "percent",
#         "lower_count": 10
#     },
#     {
#         "product_type": "2",
#         "lower_cost": 15,
#         "upper_cost": 20,
#         "unit": "percent",
#         "lower_count": 10
#     },
#     {
#         "product_type": "3",
#         "lower_cost": 10,
#         "upper_cost": 15,
#         "unit": "percent",
#         "lower_count": 5
#     },
#     {
#         "product_type": "4",
#         "lower_cost": 10,
#         "upper_cost": 30,
#         "unit": "percent",
#         "lower_count": 20
#     }
# ]
#
# commission_list = [
#     {
#         "group_name": "A",
#         "cost": 5,
#         "unit": "percent",
#         "users": [1001, 1002, 1003, 1005]
#     },
#     {
#         "group_name": "B",
#         "cost": 3,
#         "unit": "Dollar",
#         "users": [1001, 1003, 1006]
#     },
#     {
#         "group_name": "C",
#         "cost": 7,
#         "unit": "percent",
#         "users": [1001, 1002, 1004]
#     }
# ]
#
# user_list = [
#     {
#         "userid": 1001,
#         "first_name": "Mohsen",
#         "last_name": "Bayat",
#     },
#     {
#         "userid": 1002,
#         "first_name": "Sobhan",
#         "last_name": "Taghadosi",
#     },
#     {
#         "userid": 1003,
#         "first_name": "Javad",
#         "last_name": "Jafari",
#     },
#     {
#         "userid": 1004,
#         "first_name": "Masoud",
#         "last_name": "Hosseini",
#     },
#     {
#         "userid": 1005,
#         "first_name": "Hassan",
#         "last_name": "Zand",
#     },
#     {
#         "userid": 1006,
#         "first_name": "Ali",
#         "last_name": "Ebadi",
#     }
# ]
#
#
#
# def markup_calc(product_type,product_count):
#
#     for i in markup_list:
#         product_type_trigger = i['product_type']
#
#         if product_type == int(product_type_trigger):
#             selected_product = i
#             break
#
#     lower_count = int(selected_product['lower_count'])
#
#     if product_count == 1:
#         return selected_product['upper_cost']
#
#     elif product_count >= lower_count:
#         return selected_product['lower_cost']
#
#     elif 1 < product_count < lower_count:
#         slope = (selected_product['upper_cost'] - selected_product['lower_cost']) / (1 - selected_product['lower_count'])
#         slope_abs = abs(round(slope,3))
#         B = slope_abs + selected_product['upper_cost']
#         linear_cost = round(slope,3) * product_count + B
#
#         return round(linear_cost,3)
#
#
# def commission_calc(product_type,product_count,uID = 0):
#     markup_precent = markup_calc(product_type,product_count)
#     print(f'\nmarkup_precent {markup_precent}\n')
#
#
#     for i in product_list:
#         product_type_trigger = int(i['type'])
#
#         if product_type == product_type_trigger:
#             bought_product = i
#
#     product_price = bought_product['price']
#     product_name = bought_product['name']
#     product_groups = bought_product['commission_groups']
#     user_subscribe_group = []
#     for group in product_groups:
#         for group_name in commission_list:
#             group_name_trigger = group_name['group_name']
#             if group_name_trigger == group:
#                 user_subscribe_group.append(group_name)
#
#     first_name = ''
#     last_name = ''
#     user_subscribe_group_status = ''
#     for user in user_list:
#         if user['userid'] == uID:
#             first_name = user['first_name']
#             last_name = user['last_name']
#             user_subscribe_group_status = user_subscribe_group
#             break
#
#
#     markup_value = round(product_price * markup_precent / 100,3)
#     total_price = (product_price + markup_value) * product_count
#
#     for j in user_subscribe_group:
#         if uID in j['users']:
#             print(f'user is in group {j["group_name"]}')
#         else:
#             user_subscribe_group.remove(j)
#
#     if len(user_subscribe_group_status) != 0:
#
#         compare_commition_list = []
#         for t in user_subscribe_group:
#             commission_cost_temp = t['cost']
#             commission_unit_temp = t['unit']
#
#             if commission_unit_temp == 'percent':
#                 commission_precent = total_price * commission_cost_temp / 100
#                 total_with_commition = total_price - commission_precent
#
#             elif commission_unit_temp == 'Dollar':
#                 total_with_commition = total_price - commission_cost_temp
#
#             compare_commition_list.append(total_with_commition)
#
#         minimum = compare_commition_list[0]
#         for w in compare_commition_list:
#             if w < minimum:
#                 minimum = w
#         total_with_commition = minimum
#
#         result = {"product_name": product_name,"total_price": total_price,"total_with_commission": round(total_with_commition,3),"discount": commission_precent,"username": {"first_name": first_name,"last_name": last_name}}
#         return result
#     else:
#         result = {"product_name": product_name,"total_price": total_price,"total_with_commission": total_price, "discount": 0,"username": {"first_name": first_name,"last_name": last_name}}
#         return result
#
#
# print(commission_calc(1,10,1002))
# print(commission_calc(1,15,1003))
# print(commission_calc(4,20,1005))
# print(commission_calc(2,1))
#
