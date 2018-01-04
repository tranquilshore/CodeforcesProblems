chat_history = list()
try:
	while True:
		s = raw_input()
		if s != "":
			chat_history.append(s)
		else:
			break
except EOFError:
	pass

chat_area = list()
bytes_send = 0

for i in chat_history:
    if i[0] == "+":
        chat_area.append(i[1:])
    elif i[0] == "-":
        chat_area.remove(i[1:])
    else:
        t_list = i.split(":")
        msg_len = len(t_list[1])
        bytes_send += msg_len*len(chat_area)
        
print bytes_send
        