test = (input("Enter your name:"))
name = ['Rudiger', 'Yoro', 'Maguire', 'Araujo', 'Courtois', 'Lemmens', 'Donnaruma','Bruno Fernandes', 'Mainoo', 'Bellingham', 'Pedri','Mbappe', 'Haaland', 'Mbeumo', 'Sesko']
if test.capitalize() in name:
   print(f"You are a great player {test.capitalize()}")
else:
   print(f"You are not a great according to our data{test.capitalize()}")