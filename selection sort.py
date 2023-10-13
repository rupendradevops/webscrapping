def selectionsort(inputlist):
    for idx in range(len(inputlist)):

        for j in range(idx +1, len(inputlist)):

         if inputlist[idx] > inputlist[j]:
            minidx = j

            inputlist[idx], inputlist[minidx] = inputlist[minidx],inputlist[idx]

l = [19,2,31,45,30,11,121,27]
selectionsort(l)
print(l)