'''
Read From File 
Exercise 22 
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

Extra:
Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.
'''

def extra(path,sep,main):
    tfile=open(path,'r')
    tcount={}
    for line in tfile:
        category=line.split(sep)[main]
        if category not in tcount:
            tcount[category]=1
        else:
            tcount[category]+=1
    print(tcount,file=open('pe22_output.txt','a'))

if __name__=='__main__':
    txt1='pe22txt1.txt'
    txt2='pe22txt2.txt'
    extra(txt1,'\n',0)
    extra(txt2,'/',2)
    
'''
    tfile=open(txt1,'r')
    category=[]
    tcount={}
    n=0
    for lines in tfile:
        n+=1
        name=lines.split('\n')[0]
        if name not in category:
            category.append(name)
            tcount[name]=1
            print(name,tcount[name])
            print(tcount)
        else:
            tcount[name]+=1
            print(lines,tcount[name])
            print(tcount)
    print(tcount)
    print(n)
'''