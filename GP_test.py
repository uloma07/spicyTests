lst_sem_gp = float(raw_input("What was your GP last semester? "))
lst_sem_unts = int(raw_input('How many units did you offer last semester? '))
target_CGPA = float(raw_input('What is your target CGPA at the end of the session? '))
this_sem_units = int(raw_input('How many units are you offering this semester? '))
cum_1 = lst_sem_gp * lst_sem_unts
cum_units = lst_sem_unts + this_sem_units
cum_2 = (target_CGPA * cum_units) - cum_1
if (target_CGPA > 5.0 or lst_sem_gp > 5.0):
    print 'That is unrealistic!'
else:
    this_sem_GP = cum_2 /this_sem_units
    if (this_sem_GP > 5.0):
        print 'That is unattainable'
    else:
        print '''
        Last semester you had a GP of %r while offering %r units \n
        Your target at the end of the session is %r \n
        This semester you have %r units and your cumulative units are %r  \n
        You need to get a GP of %r to attain your target.'''%(lst_sem_gp,lst_sem_unts,target_CGPA,this_sem_units,cum_units,this_sem_GP)
raw_input('Press any key to exit > ')