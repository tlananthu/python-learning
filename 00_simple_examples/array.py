
accountBalances=[10,2000,5000,1,1,1,1,3,34,34,3,43,4,34,3,43,4,2,23,23,23,2,3,23]
idx=0

for acct in accountBalances:
    accountBalances[idx]=accountBalances[idx]+500
    idx=idx+1

print(accountBalances)