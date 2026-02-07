from pprint import pprint
import json
with open("C:/Users/user/Downloads/menu_items (11).json") as f:
    data = json.load(f)

pprint(data)

# for value in data:
#     print(value.get("name"))

# for category in data:
#      menu_items = category.get("menuItems")
#      if menu_items:      
#          for item in menu_items:
#              print(item.get("name"))

# total_price = 0
# count = 0
 
# for category in data:
#      if category.get("name") == "Beverages":
#          for sub in category.get("subCategories", []):
#             if sub.get("name") == "Non Alcoholic Beverages":
#                 for item in sub.get("menuItems", []):
#                     for cfg in item.get("customConfigs", []):
#                          total_price += cfg.get("itemPrice", 0)
#                          count += 1

# average_price = total_price / count if count else 0
# print("Average Beverage Price:", round(average_price, 2))

# 4
# # for category in data:
#     for item in category.get("menuItems") or []:
#         if len(item.get("customConfigs", [])) > 1:
#             print(item.get("name"))

# 6
# # for category in data:
#     for item in category.get("menuItems") or []:
#         if item.get("name") == "Chicken Wings":
#             for cfg in item.get("customConfigs", []):
#                 for modifier in cfg.get("mandatoryModifiers", []):
#                     if modifier.get("name") == "Wing Flavor":
#                         for flavor in modifier.get("modifiers", []):
#                             print(flavor.get("name"))

# 7
# # for category in data:
#     for item in category.get("menuItems") or []:
#         for cfg in item.get("customConfigs", []):
#              if cfg.get("mandatoryModifiers"):
#                  print(item.get("name"))
#                  break

# 8
# # _max = 0
# final = 0
# for category in data:
#     for item  in category.get("menuItems") or []:
#         for cfg in item.get("customConfigs",[]):
#             value = cfg.get("itemPrice",0)
#             if value > _max:
#                 _max = value
#                 final = item.get("name")
# print(final)      
# 

# 9
# # for category in data:
#     for item in  category.get("menuItems") or []:
#         max_price = 0
#         for cfg in item.get("customConfigs",[]):
#             value = cfg.get("itemPrice",0) 
#             if value > max_price:
#                 max_price = value

#         if max_price < 800 :
#            print(item.get("name"),"cheap")
#         elif max_price <= 1200 :          
#            print(item.get("name"),"Moderte")
#         elif max_price > 1200:
#            print(item.get("name"),"Expensive") 

# 10
# # d = {}

# for category in data:
#     d[category.get("name")] = [
#         item.get("name")
#         for item in (category.get("menuItems") or [])
#     ]

# print(d)




   

        



            
        
            

 