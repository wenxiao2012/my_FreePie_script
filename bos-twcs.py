import time


def update_check_joys():
	stick_state = 'stick : nk'
	rudder_state = 'rudder : nk'
	throttle_state = 'throttle : nk'
	try:
		if joystick['T.16000M']:stick_state = 'stick : ok'
	except:pass
	
	try:
		if joystick['VKB Tiny BOX ']:rudder_state = 'rudder : ok'
	except:pass
	
	try:
		if joystick['TWCS Throttle']:throttle_state = 'throttle : ok'
	except:pass
	return [stick_state,rudder_state,throttle_state]

def update_watch_joys(opt):
	diagnostics.watch(opt[0])
	diagnostics.watch(opt[1])
	diagnostics.watch(opt[2])

def butt_0_op(idt_lst):
	if idt_lst[0] == False:
		pass
	elif idt_lst[1]:
		keyboard.setKeyDown(Key.LeftAlt)
	elif idt_lst[2]:
		keyboard.setKeyDown(Key.RightAlt)
def butt_0_ep(idt_lst):
	keyboard.setKeyUp(Key.LeftAlt)
	keyboard.setKeyUp(Key.RightAlt)


def butt_1_op(idt_lst):
	if idt_lst[0] == False:
		keyboard.setKeyDown(Key.Comma)
	elif idt_lst[1]:
		keyboard.setKeyDown(Key.LeftShift)
	elif idt_lst[2]:
		keyboard.setKeyDown(Key.RightShift)
def butt_1_ep(idt_lst):
	keyboard.setKeyUp(Key.Comma)
	keyboard.setKeyUp(Key.LeftShift)
	keyboard.setKeyUp(Key.RightShift)

def butt_2_op(idt_lst):
	if idt_lst[0] == False:
		keyboard.setKeyDown(Key.Period)
	elif idt_lst[1]:
		keyboard.setKeyDown(Key.LeftControl)
	elif idt_lst[2]:
		keyboard.setKeyDown(Key.RightControl)
def butt_2_ep(idt_lst):
	keyboard.setKeyUp(Key.Period)
	keyboard.setKeyUp(Key.LeftControl)
	keyboard.setKeyUp(Key.RightControl)
	
	
def dc_inc(dc_ind):
	system.threadExecutionInterval = 5
	return dc_ind + 1

##########################################################################
if starting:
	try:
		if joystick['TWCS Throttle']:my_tr = joystick['TWCS Throttle']
	except:my_tr = None
	
	global_state = False
	left_mode = False
	right_mode = False
	
	idt_lst = [global_state,left_mode,right_mode]
	dc_ind = 80
	opt = update_check_joys()
	update_watch_joys(opt)
pass

if dc_ind < 80:dc_ind = dc_inc(dc_ind)

inc_str = ''
if my_tr.getPressed(0):
	if dc_ind < 50 :
		if not my_tr.getDown(1) and not my_tr.getDown(2):
			inc_str = '0 1 2 press'
			idt_lst = [False,False,False]
			speech.say('shift off')
		elif my_tr.getDown(1):
			inc_str = '0 1 press'
			idt_lst = [True,True,False]
			speech.say('left shift on')
		elif my_tr.getDown(2):
			inc_str = '0 2 press'
			idt_lst = [True,False,True]
			speech.say('right shift on')
		dc_ind = 80
	else:dc_ind = 0

	

if my_tr.getDown(0):butt_0_op(idt_lst)
if my_tr.getDown(1):butt_1_op(idt_lst)
if my_tr.getDown(2):butt_2_op(idt_lst)

if not my_tr.getDown(0):butt_0_ep(idt_lst)
if not my_tr.getDown(1):butt_1_ep(idt_lst)
if not my_tr.getDown(2):butt_2_ep(idt_lst)

diagnostics.watch(inc_str)
diagnostics.watch(dc_ind)

