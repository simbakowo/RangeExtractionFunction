def solution(args):
    print(args)
    i = 0
    check_list = []
    sol = ''
    while i < (len(args) -1):
        if i == (len(args) -2): #if we're at the 2nd last element , also check if they're not in checklist
            if args[-2] not in check_list:
                sol = sol+str(args[-2])+','
                sol = sol+str(args[-1])+','
                break
            elif args[-1] not in check_list:
                sol = sol+str(args[-1])+','
                break
            else:
                break
        elif ((args[i+1] - args[i]) > 1):
            if args[i] not in check_list:
                sol = sol+str(args[i])+','
            i = i+1
        elif ((args[i+1] - args[i]) == 1):
            check_list = []
            while ((args[i+1] - args[i]) == 1):
                check_list.append(args[i])
                if args[i+1] not in check_list:
                    check_list.append(args[i+1])                
                if (i < (len(args)-2)):
                    i = i+1
                else:
                    break
            if (len(check_list) > 2):
                sol = sol+str(check_list[0])+'-'+str(check_list[-1])+','
            elif(len(check_list) == 2):
                sol = sol+str(check_list[0])+','
                sol = sol+str(check_list[1])+','
            else:        
                sol = sol+str(check_list[0])+',' 
    return sol[:-1]