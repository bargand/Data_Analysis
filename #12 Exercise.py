import datetime

now = datetime.datetime.now()

a = now.strftime("%H:%M:%S")
hour = int(now.strftime("%H"))
# minu = now.strftime("%M")
# sec = now.strftime("%S")

# print(a, hour, minu, sec)
# print(type(a))

if(0<=hour<=4):
    print("Time is ",a,"AM, good night")
elif(5<=hour<12):
    print("Time is ",a,"AM, good morning")
elif(hour==12):
    print("Time is ",a,"PM, good noon")
elif(13<=hour<=16):
    print("Time is ",a,"PM, good afternoon")
elif(17<=hour<=23):
    print("Time is ",a,"PM, good evening")
else:
    print("do not understand")