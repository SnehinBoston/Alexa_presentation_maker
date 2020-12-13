import requests,json

# # url = 'http://127.0.0.1:5000/'
# # myobj = {"req": "create_chart",
# #         "details": {
# #             "create_pie_chart": True,
# #             "pie_data": {
# #                 "categories": ["Russia", "India", "Bangladesh"],
# #                 "percentages": [30.0, 30.0, 40.0]
# #             },
# #             "create_bar_chart": True,
# #             "bar_data": {
# #                 "categories": ["Russia", "Russia", "Russia"],
# #                 "values": [20, 20]
# #             },
# #             "create_line_chart": True,
# #             "line_data": {
# #                 "Label": ["India", "Bangladesh"],
# #                 "Value": [20, 30]
# #             }
# #         }
# #     }

# # data = json.dumps(myobj)

# # # print(type(data))
# # x = requests.post(url, data = data)

# # print(x.text)
# import requests

# requ = requests.Request('POST','http://127.0.0.1:5000',headers={'X-Custom':'Test'},
# data={"req": "create_chart",
#         "details": {
#             "create_pie_chart": True,
#             "pie_data": {
#                 "categories": ["Russia", "India", "Bangladesh"],
#                 "percentages": [30.0, 30.0, 40.0]
#             },
#             "create_bar_chart": True,
#             "bar_data": {
#                 "categories": ["Russia", "Russia", "Russia"],
#                 "values": [20, 20]
#             },
#             "create_line_chart": True,
#             "line_data": {
#                 "Label": ["India", "Bangladesh"],
#                 "Value": [20, 30]
#             }}}
#         )
# prepared = requ.prepare()

# def pretty_print_POST(requ):
#     """
#     At this point it is completely built and ready
#     to be fired; it is "prepared".

#     However pay attention at the formatting used in 
#     this function because it is programmed to be pretty 
#     printed and may differ from the actual request.
#     """
#     print('{}\n{}\r\n{}\r\n\r\n{}'.format(
#         '-----------START-----------',
#         requ.method + ' ' + requ.url,
#         '\r\n'.join('{}: {}'.format(k, v) for k, v in requ.headers.items()),
#         requ.body,
#     ))

# pretty_print_POST(prepared)

# s = requests.Session()
# s.send(prepared)
# print(prepared.text)
import requests

# data = {
#     "req":'create_chart',
#     "details":{
#         "create_pie_chart": True,
#         "pie_data": {
#             "categories": ["Russia", "India", "Bangladesh"],
#             "percentages": [30.0, 30.0, 40.0]
#         }
#     }
# }
data = {
    "req": "create_ppt_count",
    "title": "India",
    "count": "10",
    "source": "nytimes"
    }

#     "req": "create_ppt_count",
#     "title": "India",
#     "count": "10",
#     "source": "nytimes"
#     }
# {
#     "req": "create_ppt",
#     "title": "India",
#     "source": "wikipedia"
#     }
    
#     "create_bar_chart": True,
#     "bar_data": {
#       "categories": ["Russia", "Russia", "Russia"],
#       "values": [20, 20]
#     },
#     "create_line_chart": True,
#     "line_data": {
#       "Label": ["India", "Bangladesh"],
#       "Value": [20, 30]
#     }
# }
# }



r = requests.post("http://127.0.0.1:5000", json=data)
# print(r.url)
# print(r.text)