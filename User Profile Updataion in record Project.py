#!/usr/bin/env python
# coding: utf-8

# In[4]:


mylogin={1:{'name':'ravi','email':'ravi@gmail.com','password':'abc@123'},
         2:{'name':'Lavina','email':'lavi@gmail.com','password':'lav@123'},
         3:{'name':'cm','email':'cm@gmail.com','password':'cm@123'}}
username=int(input("enter your roll no"))
if username in mylogin:
    print(mylogin[username])
    change=(input('press Y to update existing info: '))
    if change =='Y' or 'y':
        b=int(input('press 1 to update name, press 2 to update emailid, press3 to update password: '))
        if b==1:
            c=input('enter your new name: ')
            mylogin[username]['name']=c
            print('your name updated detail',mylogin[username])
        if b==2:
            d=input('enter your new mail id: ')
            mylogin[username]['email']=d
            print('Your mail id updated detail',mylogin[username])
        if b==3:
            s=input('enter your new password: ')
            mylogin[username]['password']=s
            print('Your password updated successfully',mylogin[username]) 
    else:
        print("Thank you for the visit")
else:
    print('your roll no does not exist')
    enter=int(input('press 0 if you want to add your detail: '))
    if enter==0:
        name=input('enter your name: ')
        email=input('enter your mail: ')
        pas=input('enter your password: ')
        b="name: {} ,email: {} ,password: {}".format(name, email, pas)
        mylogin[4]={b}
        print(mylogin)
        print("your profile successfully added")
    else:
        print('Thank you')


# In[ ]:




