# avengersList = ["Ironman","Captain America","Thor"]
# print(avengersList,type(avengersList))

# print(avengersList[1])

# avengersList = ["Ironman","Captain America","Thor"]
# ratingList = [10,9,8]

# resultList=[]

# for i in range(len(avengersList)):
#     resultList.append(avengersList[i])
#     resultList.append(ratingList[i])

# print(resultList)    


#Extract the superhero Ironman and its score

# print(resultList[-2:]) 


# avengersTuple = ("Ironman","Captain America","Thor")
# avengersList = ["Ironman","Captain America","Thor"]
# avengersList[0]="Batman"
# print(avengersList)

# avengersTuple[0] = "Batman"
# print(avengersTuple)

# print(avengersTuple[0])

# ral = [["Spiderman",8],["Groot",7],["Black Widow",8]]

# for i in ral:
#     print(ral[i][j])

# print(ral[-1][-1])



# for i in range(len(ral)):
#     for j in range(len(ral[i])):
#         print(ral[i][j])


# for i in ral:
#     for j in i:
#         print(j)        

# avangerDict = {"Ironman":8,
#         "Captain America":9,
#         "Thor":8}
# print("Ironman Score:",avangerDict["Ironman"])

empList = [

{
    "name":"Tony Stark",
    "emp_id": 3,
    "address": [
        {
            "l1":"a",
            "l2":"b",
            "state":"WB",
            "pin":"733121"
        },
        {
            "l1":"c",
            "l2":"d",
            "state":"WB",
            "pin":"733121"
        }
    ]
}
]

# # print("Employee name:",emp["name"])
# # print("Employee address:",emp["address"])

# # for address in emp["address"]:
# #     print(address)

# # for emp in empList:
# #     print("name:",emp["name"])
# #     print("id:",emp["emp_id"])
# #     for address in emp["address"]:
# #         print("Pincode:",address["pin"])

# emp_pin_list =[]
# for emp in empList:
#     emp_pin_list.append({"name":emp["name"]})
#     print(emp_pin_list)
#     emp_pin_list[empList.index(emp)]["pin"] = []
#     print(emp_pin_list)
#     for address in emp["address"]:
#         print(empList.index(emp))
#         emp_pin_list[empList.index(emp)]["pin"].append(address["pin"])


# print(emp_pin_list)

# emp_pin = {}
# emp_pin["emp-pin"] = "Tony"
# print(emp_pin)

def get_emp_address(empList,key):
    emp_address_list =[]
    for emp in empList:
        emp_address_list.append({"name":emp["name"]})
        emp_address_list[empList.index(emp)][key] = []
        for address in emp["address"]:
            emp_address_list[empList.index(emp)][key].append(address[key])

    return emp_address_list


# print(get_emp_address(empList,"pin"))
# get_emp_address(empList,"state")