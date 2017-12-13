def calculateNetIncome(gross, state):
    net = gross -(gross *.10)
    
    state_tax = {'CA':10,'NY':9,'TX':10,'NJ':6}
    if state in state_tax:
        net = net - (gross* state_tax[state]/100)
        print("Your net income after all the heacy taxes is: "+ str(net))
        return net
    else:
        print("State not in the list")
        return None


print(calculateNetIncome(10000, 'CA'))
