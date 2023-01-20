waiting_list = ['sen','ben','john']
# waiting_list.sort()
waiting_list.sort(reverse=True)

for k,v in enumerate(waiting_list):
    print(f"{k+1}.{v.capitalize()}")