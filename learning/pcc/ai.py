alien_0 = {'color': "green", 'points': "5"}
print(alien_0['color'])
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
alien_0['x-position']= "56"
alien_0['y-position']= "90"
print(alien_0)
print(alien_0['x-position'])
del alien_0['points']
print(alien_0)
alien_0 = {"x_position": 0, "y_position": 25, "speed": 'fast' }
print(f"Original position: {alien_0['x_position']}")
#move the alien to the right.
#Determine how far to move the alien based on iys current speed."
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien. 
    x_increment = 3
#The new position is the old position plus the incremengt.
alien_0['x_position']= alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
fav_languages = {
    "pascal": 'python',
    "rain": 'c++',
    "jules": 'rust',
    "taylor": 'php',
    }
language = fav_languages['taylor'].title()
print(f"Sarah's favorite language is {language}")