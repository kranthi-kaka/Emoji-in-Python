#----------------------------------------------
#--- Author         : Kranthi Kumar D
#--- GitHub         : kranthi-kaka
#----------------------------------------------

#Add Emoji to your code.

#pip3 install emoji

from emoji import emojize

print(emojize(':car: :poop:'))

#In some cases you need to add the "Use_aliases=True" parameter to allow the name. 
#user example, "telephone:" is accessible by default, while ":phone:" is not. 

print(emojize(':phone:', use_aliases=True))

#End code print(emojize(':peace:'))
