def printTicket(uid='123',meal='Lunch'):
	from escpos import printer

	p=printer.Usb(0x1fc9,0x0064,4,0x81,0x03)#NGX printer

	#chineese printer  p=printer.Usb(0x0456,0x0808,4,0x81,0x03)

	p.set(align=u'center',font=u'b',width=4,height=4)

	p.text("     RSD MESS\n")
	p.set()
	p.text("******************************************\n")
	
	p.text(meal)
	p.text('\n')
	p.set()
	p.text('UID :'+uid+'\n******************************************\n\n')


