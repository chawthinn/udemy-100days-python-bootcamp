dic = {
    "key1": "value1",
    "key2": "value2",
    3: "value3"
}

print(dic["key1"])
print(dic[3])

# Add new key-value pair to the dictionary
dic["4"] = "new value"
print(dic)

empty_dic = {}

# Wipe an existing dictionary
dic = {}
print(dic)

dic = {
    "key1": "value1",
    "key2": "value2",
    3: "value3"
}

# Loop through a dictionary
for key in dic:
    print(key)
    print(dic[key])