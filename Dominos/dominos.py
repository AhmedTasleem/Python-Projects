import sqlite3
conn=sqlite3.connect('my.db')
b=conn.cursor()
#b.execute('create table user(name char,phno number,email char)')
#b.execute('create table domuser(name char,phno number, email char)')
#b.execute('create table cart(phno number,cartval char)')
d={
    'veg':{'Margerita':129,'cheese_and_corn':169,'peppi_paneer':260,'veg_loaded':210,'tomato_tangi':170},
    'non_veg':{'pepper_barbeque':199,'non_veg_loaded':269,'chicken_sausage':200},
    'snacks':{'garlic_bread':120,'zinger_chicken':59,'chicken_cheese_balls':170},
    'desserts':{'Rasmalai':69,'choco_lava':100,'mousse_cake':169},
    'drinks':{'coke':90,'pepsi':80,'thumbs_up':55}
}

login_status=False
cart={}
phnum=''
mode=0

def valid_phno(phno):
    s=str(phno)
    return len(s)==10 and '6'<=s[0]<='9' and s.isnumeric()

def chk_phno(phno):
    l=list(b.execute('select phno from domuser'))
    return (phno,) in l

def valid_email(e):
    s=e[-10:]
    return s in ['@gmail.com','@yahoo.com'] and 'a'<=e[0]<='z' and e[0:-10].isalnum()

def chk_email(e):
    l=list(b.execute('select email from domuser'))
    return (e,) in l

def Dominos():
    print('Enter 1 for Sign up')
    print('Enter 2 for Login')
    ch=int(input('Enter your choice : '))
    if ch==1:
        while True:
            print('please fill details ')
            name=input('enter your name : ')
            while True:
                phno=int(input('Enter Phone : '))
                if valid_phno(phno):
                    break
                else:
                    print('Invalid Phone number')
            while True:
                email=(input('Enter email : '))
                if valid_email(email):
                    break
                else:
                    print('Invalid email')
            m,n=chk_email(email),chk_phno(phno)
            if m==False and n == False:
                b.execute(f'insert into domuser values("{name}","{phno}","{email}")')
                conn.commit()
                print('Sign up successfull.....')
                break
            elif m==True:
                print('Email already exists')
            else:
                print('Phone already exists')
    else:
        login()

def get_otp(a):
    global login_status
    import random
    while True:
        otp=random.randint(100000,999999)
        print('your otp is : ',otp)
        print('An Otp has sent to your ',a)
        tp=int(input('Enter OTP : '))
        if tp==otp:
            print('login successfull...')
            login_status=True
            break
        else:
            print('Incorrect OTP''\n''Enter Correct OTP')

def login():
    global phnum,login_status
    if login_status==True:
        return 'Already logged in'
    print('Enter 1 to login with phone number')
    print('Enter 2 to login with email ')
    c=int(input('enter your choice : '))
    if c==1:
        phnum=int(input('Enter Phno : '))
        if chk_phno(phnum):
            get_otp(phnum)
        else:
            print("phno number doesn't exist")
    else:
        email=input('Enter your email : ')
        phnum=list(b.execute(f'select phno from dom user where email="{email}"'))[0][0]
        if chk_email(email):
            get_otp(email)
        else:
            print("Email doesn't exist")

def log_out():
    global login_status
    login_status=False
    print('Logged out successfully')

def order(new=0):
    global mode
    if login_status==True:
        print('Enter 1 : Dine in')
        print('Enter 2 : Take Away')
        print('Enter 3 : Home Delivery')
        ch=int(input('enter a choice : '))
        mode=ch
        out={}
        di=list(d)
        while True:
            print('Enter 1 : Veg')
            print('Enter 2 : non_veg')
            print('Enter 3 : Snacks')
            print('Enter 4 : Deserts')
            print('Enter 5 : Drinks')
            print('Enter 6 : End')
            c=int(input('Enter your Item : '))
            if 1<=c<=6:
                if c==6:
                    break
                m=list(d)[c-1]
                m=list(d[m])
                for i in range(1,len(m)+1):
                    print(f'Enter {i} : {m[i-1]}')
                    ch=int(input('Enter your choice : '))
                    q=int(input('Enter Quantity : '))
                    if 1<=ch<=len(m):
                        out[m[ch-1]]=[q,q*d[di[c-1]][m[ch-1]]]
                        print('Item added')
                    else:
                        print('Invalid choice')
            else:
                print('Invalid choice')
        cart.update(out)
        if cart!={} and new==0:
            b.execute(f'insert into cart values("{phnum}","{cart}")')
            conn.commit()
    else:
        print('Please login first')

def disp_bill():
    if login_status==True:
        if mode==1:
            total_amt=0
        elif mode==2:
            print('parcel charges of 25 Rs. will be included')
            total_amt=25
        elif mode==3:
            print('delivery charges of 50 Rs. and parcel charges of 25 Rs. will be included')
            total_amt=75
        print('Item',' '*16,'Quantity',' '*7,'Price')
        for i in cart:
            print(i,'.'*(25-len(i)),cart[i][0],' '*10,cart[i][1])
            total_amt+=cart[i][1]
        print('Total Bill:',' '*27,total_amt)
    else:
        print('Please login first')