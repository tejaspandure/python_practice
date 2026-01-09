iList = [11,21,51,[101,201]]

iLength = len(iList)

for iCnt in range(iLength):

    if type(iList(iCnt)) is list:

        if len(iList(iCnt))>1:
            m = len(iList[iCnt])

            for j in range(m):
                print(iCnt,j, iList[iCnt][j])

    else:
        print(iCnt,iList[iCnt])
