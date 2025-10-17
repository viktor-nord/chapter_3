
guest_list = ['karlsson', 'vik', 'erik']

print(guest_list)
print(len(guest_list))

guest_list.insert(0, 'maria')
print(len(guest_list))
guest_list.insert(2, 'john')
print(len(guest_list))
guest_list.append('sara')
print(len(guest_list))
print(guest_list)

removed_guest = guest_list.pop()
print(len(guest_list))
removed_guest = guest_list.pop()
print(len(guest_list))
removed_guest = guest_list.pop()
print(len(guest_list))
removed_guest = guest_list.pop()

del guest_list[0]
print(len(guest_list))
del guest_list[0]
print(len(guest_list))
print(guest_list)