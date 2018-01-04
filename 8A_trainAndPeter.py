station_flags = raw_input()
first_period = raw_input()
second_period = raw_input()

r_station_flags = station_flags[::-1]
forward_flag = False
backward_flag = False

if station_flags.find(first_period) >= 0:
    f_index = station_flags.find(first_period)
    if station_flags[f_index+len(first_period):].find(second_period) >= 0:
        forward_flag = True

if r_station_flags.find(first_period) >= 0:
    rf_index = r_station_flags.find(first_period)
    if r_station_flags[rf_index+len(first_period):].find(second_period) >= 0:
        backward_flag = True

if forward_flag == True and backward_flag == True:
    print "both"
elif forward_flag == True and backward_flag == False:
    print "forward"
elif forward_flag == False and backward_flag == True:
    print "backward"
else:
    print "fantasy"

    
