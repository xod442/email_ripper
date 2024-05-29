counter = 0
employee = []
partner =  []
cr = '\n'
with open('data.csv') as file:
    for line in file:
        mylist = line.split(',')
        if 'Attendee' in mylist:
            for item in mylist:
                if '@' in item:
                    name,company = item.split('@')
                    if company == 'hpe.com':
                        if item.lower() not in employee:
                            employee.append(item.lower())
                    if company != 'hpe.com':
                        if item.lower() not in partner:
                            partner.append(item.lower())
    for i in employee:
        print(i)
    print(f"{len(employee)} employees attended the call")
    print('-----------------------------------------------')
    for i in partner:
        print(i)
    print(f"{len(partner)} partners attended the call")
