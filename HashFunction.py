my_dict = {'Cuong':'01','Anh':'02','Bao':'3'}
print("Dict_1 : ",my_dict)
print(type(my_dict))
# create dict by dict()
new_dict = dict(NhatCuong='001',VietAnh='002',NhatBao='003')
print("Dict_2: ",new_dict)
print("print Key: ",new_dict.keys())
print("print Values: ",new_dict.values())
print(my_dict.get('Bao'))