
#given an array of string (command for bank request)
#given an array of accounts and balance
#perform the command and return result or error code

def bankRequests(accounts, requests):

    num_accs = len(accounts)
    num_reqs = len(requests)

    import re
    for index in range(num_reqs):
        if 'deposit' in requests[index]:
            acc, amount = map(int, re.findall('\d+', requests[index]))
            if acc > num_accs:
                return [-1 - index]
            else:
                accounts[acc - 1] += amount

        elif 'withdraw' in requests[index]:
            acc, amount = map(int, re.findall('\d+', requests[index]))
            if acc > num_accs:
                return [-1 - index]
            else:
                accounts[acc - 1] -= amount
                if accounts[acc - 1] < 0:
                    return [-1 - index]

        elif 'transfer' in requests[index]:
            acc1, acc2, amount = map(int, re.findall('\d+', requests[index]))
            if acc1 > num_accs or acc2 > num_accs:
                return [-1 - index]
            else:
                accounts[acc1 - 1] -= amount
                if accounts[acc1 - 1] < 0:
                    return [-1 - index]
                accounts[acc2 - 1] += amount
        else:
            return [-1 - index]

    return accounts