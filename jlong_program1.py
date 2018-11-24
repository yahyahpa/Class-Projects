Jlong 

#Enter desired batches
cookies = int(input('How many dozen cookies?\n'))
cakes = int(input('How many cakes?\n'))
donuts = int(input('How many dozen donuts?\n'))

#Finds total of each ingredient needed
butter = (cookies * 2.5) + (cakes * .5) + (donuts * .25)
sugar = (cookies * 2) + (cakes * 1) + (donuts * .5)
eggs = (cookies * 2) + (cakes * 2) + (donuts * 3)
flour = (cookies *8) + (cakes * 1.5) + (donuts * 5)
print('')
print('')

#Prints results and %.2f rounds to 2 digits after decimal
print('You will need to order:')
print('%.2f cups of butter' % butter)
print('%.2f cups of sugar' % sugar)
print('%d eggs' % eggs)
print('%.2f cups of flour' % flour)
