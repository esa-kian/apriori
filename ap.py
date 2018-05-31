from itertools import combinations
import random
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def confCount(x):
        c=0
        for ii in range(len(randTransactions)):
                try:
                        if randTransactions[ii].index(x):
                                c=c+1
                except:
                        continue
        c=float(c)/countOfTrans
        return c

def makeAssociation(nexTrans2):
        print ("Making Association Priori!!!")
        for i in range(len(nexTrans2)):
                x=nexTrans2[i]
                confCount(x)
                
        
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#محاسبه ساپورت 8تايي ها
def counter7(x,y,z,p,q,r,s,t):
        c=0
        for i in range(len(randTransactions)):
                try:
                        if randTransactions[i].index(x) and randTransactions[i].index(y) and randTransactions[i].index(z) and randTransactions[i].index(p) and randTransactions[i].index(q)and randTransactions[i].index(r) and randTransactions[i].index(s) and randTransactions[i].index(t):
                                c=c+1
                except:
                        continue
        c=float(c)/countOfTrans#support 8taie ha
        return c
#محاسبه ساپورت هاي 7 تايي
def counter6(x,y,z,p,q,r,s):
        c=0
        for i in range(len(randTransactions)):
                try:
                        if randTransactions[i].index(x) and randTransactions[i].index(y) and randTransactions[i].index(z) and randTransactions[i].index(p) and randTransactions[i].index(q)and randTransactions[i].index(r) and randTransactions[i].index(s):
                                c=c+1
                except:
                        continue
        c=float(c)/countOfTrans#support 7taie ha
        return c
#محاسبه ساپورت هاي 6تايي
def counter5(x,y,z,p,q,r):
        c=0
        for i in range(len(randTransactions)):
                try:
                        if randTransactions[i].index(x) and randTransactions[i].index(y) and randTransactions[i].index(z) and randTransactions[i].index(p) and randTransactions[i].index(q) and randTransactions[i].index(r):
                                c=c+1
                except:
                        continue
        c=float(c)/countOfTrans#support 6taie ha
        return c
#محاسبه ساپورت هاي 5 تايي
def counter4(x,y,z,p,q):
        c=0
        for i in range(len(randTransactions)):
                try:
                        if randTransactions[i].index(x) and randTransactions[i].index(y) and randTransactions[i].index(z) and randTransactions[i].index(p) and randTransactions[i].index(q):
                                c=c+1
                except:
                        continue
        c=float(c)/countOfTrans#support 5taie ha
        return c
#محاسبه ساپورت هاي 4تايي
def counter3(x,y,z,p):
        c=0
        for i in range(len(randTransactions)):
                try:
                        if randTransactions[i].index(x) and randTransactions[i].index(y)and randTransactions[i].index(z) and randTransactions[i].index(p):
                                c=c+1
                except:
                        continue
        c=float(c)/countOfTrans#support 4taie ha
        return c
#محاسبه ساپورت هاي 3تايي
def counter2(x,y,z):
        c=0
        for i in range(len(randTransactions)):
                try:
                        if randTransactions[i].index(x) and randTransactions[i].index(y) and randTransactions[i].index(z):
                                c=c+1
                except:
                        continue
        c=float(c)/countOfTrans#support 3taie ha
        return c
#محاسبه ساپورت هاي 2تايي
def counter(x,y):
        c=0
        for i in range(len(randTransactions)):
                try:
                        if randTransactions[i].index(x) and randTransactions[i].index(y):
                                c=c+1
                except:
                        continue
        c=float(c)/countOfTrans#support 2taie ha
        return c
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def makeStep8(supported2):
        for pair in combinations(supported2,8):
                x=pair[0]
                y=pair[1]
                z=pair[2]
                p=pair[3]
                q=pair[4]
                r=pair[5]
                s=pair[6]
                t=pair[7]
                if counter7(x,y,z,p,q,r,s,t)>=minSup:
                        nexTrans.append([x,y,z,p,q,r,s,t])
def makeStep7(supported2):
        for pair in combinations(supported2,7):
                x=pair[0]
                y=pair[1]
                z=pair[2]
                p=pair[3]
                q=pair[4]
                r=pair[5]
                s=pair[6]
                if counter6(x,y,z,p,q,r,s)>=minSup:
                        nexTrans.append([x,y,z,p,q,r,s])
def makeStep6 (supported2):
        for pair in combinations(supported2,6):
                x=pair[0]
                y=pair[1]
                z=pair[2]
                p=pair[3]
                q=pair[4]
                r=pair[5]
                if counter5(x,y,z,p,q,r)>=minSup:
                        nexTrans.append([x,y,z,p,q,r])
def makeStep5 (supported2):
        for pair in combinations(supported2,5):
                x=pair[0]
                y=pair[1]
                z=pair[2]
                p=pair[3]
                q=pair[4]
                if counter4(x,y,z,p,q)>=minSup:
                        nexTrans.append([x,y,z,p,q])
def makeStep4 (supported2):
        for pair in combinations(supported2,4):
                x=pair[0]
                y=pair[1]
                z=pair[2]
                p=pair[3]
                if counter3(x,y,z,p)>=minSup:
                        nexTrans.append([x,y,z,p])
                        
def makeStep3 (supported2):
        for pair in combinations(supported2,3):
                x=pair[0]
                y=pair[1]
                z=pair[2]
                if counter2(x,y,z)>=minSup:
                        nexTrans.append([x,y,z])

def makeStep2(supported2):
        for pair in combinations(supported2,2):
                x=pair[0]
                y=pair[1]
                if counter(x,y)>=minSup:
                        nexTrans.append([x,y])

def makeStep1(randTransactions):
	temp=[]
	for t in range(len(randTransactions)):
		for tt in range(len(randTransactions[t])):	
			temp.append(randTransactions[t][tt])
	#محاسبه ساپورت هاي 1تايي
	for c in range(1,21):
		sup=temp.count(c)
		sup=float(sup)/countOfTrans
		sup=round(sup,2)
		sup=int(sup*100)
		print ("support of %d="%c)
		print ("%s"%sup)
		if sup>=minSup:
			supported.append(c)
#$$$$$$$$$$$$$$$$______Main_____$$$$$$$$$$$$$$$$$$$$$$
transaction=[]
randTransactions=[]
supported=[]
supported2=[]
nexTrans=[]
nexTrans2=[]
minSup = input("Please enter Minsup:")
minSup = float(minSup)/100
countOfTrans=random.randint(10,30)
#ايجاد تراکنش هاي تصادفي
for l in range(countOfTrans):
	countOfGoods=random.randint(1,10)
	i=0
	goods=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	while i<countOfGoods:
		x=random.choice(goods)
		transaction.insert(i,x)
		goods.remove(x)
		i=i+1
	randTransactions.append(transaction[0:countOfGoods])
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#نمايش تراکنش ها
print ("Transactions:")
for pr in range(len(randTransactions)):
        print (randTransactions[pr])
#پيدا کردن الگو هاي مکرر يک تايي
makeStep1(randTransactions)
supported2=supported.copy()
print ("step1 completed!:")
print (supported2)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#پيدا کردن الگوهاي مکرر دوتايي
makeStep2(supported2)
print("step2 completed:")
if len(nexTrans)==0:
        makeAssociation(nexTrans2)
else:
        print(nexTrans)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#پيداکردن الگوهاي مکرر سه تايي
if len(nexTrans)>0:
        nexTrans2=nexTrans.copy()
        nexTrans.clear()
        makeStep3(supported2)
        print("step3 completed:")
        if len(nexTrans)==0:
                makeAssociation(nexTrans2)
        else:
                print(nexTrans)
                nexTrans2.clear()
        
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#پيدا کردن الگو هاي مکرر 4تايي
if len(nexTrans)>0:
        nexTrans2=nexTrans.copy()
        nexTrans.clear()
        makeStep4(supported2)
        print("step4 completed!")
        if len(nexTrans)==0:
                makeAssociation(nexTrans2)
        else:
                print(nexTrans)
                nexTrans2.clear()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#پيدا کردن الگوهاي مکرر 5تايي
if len(nexTrans)>0:
        nexTrans2=nexTrans.copy()
        nexTrans.clear()
        makeStep5(supported2)
        print("step5 completed!")
        if len(nexTrans)==0:
                makeAssociation(nexTrans2)
        else:
                print(nexTrans)
                nexTrans2.clear()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#پيدا کردن الگو هاي مکرر 6تايي
if len(nexTrans)>0:
        nexTrans2=nexTrans.copy()
        nexTrans.clear()
        makeStep6(supported2)
        print("step6 completed!")
        if len(nexTrans)==0:
                makeAssociation(nexTrans2)
        else:
                print(nexTrans)
                nexTrans2.clear()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#پيدا کردن الگو هاي مکرر 7تايي
if len(nexTrans)>0:
        nexTrans2=nexTrans.copy()
        nexTrans.clear()
        makeStep7(supported2)
        print("step7 completed!")
        if len(nexTrans)==0:
                makeAssociation(nexTrans2)
        else:
                print(nexTrans)
                nexTrans2.clear()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#پيدا کردن الگو هاي مکرر 8تايي
if len(nexTrans)>0:
        nexTrans2=nexTrans.copy()
        nexTrans.clear()
        makeStep8(supported2)
        print("step8 completed!")
        if len(nexTrans)==0:
                makeAssociation(nexTrans2)
        else:
                print(nexTrans)
                nexTrans2.clear()

print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
