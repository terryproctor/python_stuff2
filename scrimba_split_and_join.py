csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
# print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise
# print(','.join(csv.split(';')))
# print(','.join(csv.split(';')).split(':'))

#solution1
# friends_list = (','.join(','.join(csv.split(';')).split(':')).split(','))

#solution2
friends_list = csv.replace(';',':').replace(':',',').split(',')

print(friends_list)

#regular expressions is a better solution than these two