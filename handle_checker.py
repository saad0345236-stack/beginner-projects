# Handle Checker:
handle = input("Handle: ")

if handle.startswith('creator_'):
    print("CREATOR")

elif handle.startswith('biz_'):
    print("BUSINESS")

elif handle.startswith('gg_'):
    print("GAMING")

else:
    print("INVALID HANDLE")