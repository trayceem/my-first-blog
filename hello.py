volume	=	57 
if	volume	<	20:
	print("It's	kinda	quiet.") 
elif	20	<=	volume	<	40:
	print("It's	nice	for	background	music") 
elif	40	<=	volume	<	60:
	print("Perfect,	I	can	hear	all	the	details") 
elif	60	<=	volume	<	80:				
	print("Nice	for	parties") 
elif	80	<=	volume	<	100:				
	print("A	bit	loud!")
else:		
	print("My	ears	are	hurting!	:(")
#change the volume if its too loud
if volume < 20 or volume > 80:
	volume= 50
	print ('its better')
def hi():
	print('Hi there!')
	print ('How are you')
hi()
def hi(name):
	if name== ('Ola'):
		print ('Hi Ola')
	elif name== ('Sonja'):
		print ('Hi Sonja')
	else:
		print ('Hi Anonymus')
hi('Tracy')
def hi(name):
	print('Hi'+ name +'!')
hi ('Rachel')
