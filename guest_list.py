#3.4
guest_list = ['karlsson', 'vik', 'erik']
print(f"Dear {guest_list[0].title()}, you are invited to dinner.")
print(f"Dear {guest_list[1].title()}, you are invited to dinner.")
print(f"Dear {guest_list[2].title()}, you are invited to dinner.")
#3.5
print(guest_list)
print(f"{guest_list[1].title()} can't make it to dinner.")
guest_list[1] = 'lina'
print(guest_list)
print(f"Dear {guest_list[0].title()}, you are invited to dinner.")
print(f"Dear {guest_list[1].title()}, you are invited to dinner.")
print(f"Dear {guest_list[2].title()}, you are invited to dinner.")
#3.6
guest_list.insert(0, 'maria')
guest_list.insert(2, 'john')
guest_list.append('sara')
print(guest_list)
print(f"Dear {guest_list[0].title()}, you are invited to dinner.")
print(f"Dear {guest_list[1].title()}, you are invited to dinner.")
print(f"Dear {guest_list[2].title()}, you are invited to dinner.")
print(f"Dear {guest_list[3].title()}, you are invited to dinner.")
print(f"Dear {guest_list[4].title()}, you are invited to dinner.")
print(f"Dear {guest_list[5].title()}, you are invited to dinner.")
#3.7
print("I can only invite two people for dinner.")
removed_guest = guest_list.pop()
print(f"Sorry, {removed_guest.title()}, I can't invite you to dinner.")
removed_guest = guest_list.pop()
print(f"Sorry, {removed_guest.title()}, I can't invite you to dinner.")
removed_guest = guest_list.pop()
print(f"Sorry, {removed_guest.title()}, I can't invite you to dinner.")
removed_guest = guest_list.pop()
print(f"Sorry, {removed_guest.title()}, I can't invite you to dinner.")
print(f"Dear {guest_list[0].title()}, you are still invited to dinner.")
print(f"Dear {guest_list[1].title()}, you are still invited to dinner.")
del guest_list[0]
del guest_list[0]
print(guest_list)