import numpy as np
SIZE = 50

dateList = ['0614', '0615', '0616', '0617', '0628', '0629']

for date in dateList:
    cntName = './dataInput/' + date + '_count.txt'
    pntName = './dataInput/' + date + '_percent.txt'
    outName = './dataOutput/' + date

    cntFile = open(cntName, 'r')
    pntFile = open(pntName, 'r')
    perZone = []
    for cnt in cntFile:
        cnt = int(cnt)

        pnt = pntFile.readline()
        pnt = pnt.strip().split(' ')
        for z in pnt:
            s = np.random.binomial(cnt, float(z), SIZE)
            perZone.append(s)

    for i in range(0,50):
        outputName = outName + '_' + str(i+1) + 'sim.txt'
        output = open(outputName, 'w')
        for j in range(0,37):
            for k in range(0,12):
                #print(perZone[k + 12 * j][i])
                sim = perZone[k + 12 * j][i]
                res = str(sim) + ' '
                output.write(res)
            output.write('\n')
        output.close()