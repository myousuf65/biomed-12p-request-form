yy = '24'
mm = '07'
tt = '1'
sn = 100

quantity = 3
counter = 0  

for test_kit_number in range(sn, sn+int(quantity)):
    sum_val = int(sn)+counter
    s = "{:03d}".format(sum_val)
    print(yy+mm+tt+str(s))
    counter += 1
