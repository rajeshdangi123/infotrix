from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.modals.customer import Customer
from django.contrib.auth.hashers import check_password,make_password
from django.contrib import messages #import messages
# Create your views here.
def home(request):
    return render(request,"app1/base.html")

def singup1(request):
    if request.method =="GET":
        return render(request,'app1/singup.html')
    else:
        try:
            messages.success(request,"welcome to contact")
            postdata=request.POST
            user_name=postdata.get("user_name")
            first_name=postdata.get("first_name")
            last_name=postdata.get('last_name')
            email_field=postdata.get('email_field')
            phone_number=postdata.get('phone_number')
            password=postdata.get('password')
            #password=make_password(password1)
            print(user_name,first_name,last_name,email_field,password)
            my_user=Customer(user_name=user_name,first_name=first_name,last_name=last_name,
                            phone_number=phone_number, email_field=email_field,password=password)
            if len(first_name)<4:
                return render(request,'app1/singup.html')
            elif (not first_name):
                return render(request,'app1/singup.html')
            elif my_user.isExists():
                return HttpResponse("email alredy register ")
            else:
            
                my_user.password=make_password(my_user.password)
                my_user.register()
                return render(request,'app1/login.html')
        except  Exception as e:
            print(e)
def login1(request):
    if request.method =="GET":

        return render(request,'app1/login.html')
    else:
        
        postdata=request.POST
        email_field=postdata.get('email_field')
        password=postdata.get('password')
       
        print("hello1",email_field,password)  
        customer=Customer.get_customer_by_email(email_field)
        print("hello2",customer)
        
        if customer:
            flag=check_password(password,customer.password)
            print("hello3",flag)
            if flag:
                request.session['customer']=customer.id
                #request.session['email_field']=customer.email_field
                print("hello4")

                return redirect('home')
                print("hello")
            else:
                return  HttpResponse("Email or Password invalid !!")
     
        print(email_field,password)  
        return render(request,'app1/login.html')
        # user=Customer.objects.get(email_field=email_field)
        # print(user)
#         # if customer is None:
            
#         #     #flag=check_password(password,customer.password1)
#         #     print("all ok")


def log_out(request):

    request.session.clear()
    return redirect('login1')


def read(request):
    #i =Customer.objects.all()
    if request.method =="GET":
        print("chalo")
        #return render(request,'app1/login.html')
    else:
        
        postdata=request.POST
        email_field=postdata.get('email_field')
        #password=postdata.get('password')
        my_user=Customer(email_field=email_field)
        # print("hello1",email_field,password)  
        #customer=Customer.get_customer_by_email(email_field)
        if my_user.isExists():
            print("hello1")
            customer=Customer.objects.get(email_field=email_field)
            print("hello2",customer.user_name,customer.first_name,customer.last_name)
            #pi=Customer.objects.get()
            #request.session['customer']=customer.id
        
            
            return render(request,"app1/read1.html",{'customer':customer})
    return render(request,"app1/read.html" )


# def update1(request ):
#     if request.method =="GET":
#         return render(request,'app1/singup.html')
#     else:
#         messages.success(request,"welcome to contact")
#         postdata=request.POST
#         user_name=postdata.get("user_name")
#         first_name=postdata.get("first_name")
#         last_name=postdata.get('last_name')
#         email_field=postdata.get('email_field')
#         phone_number=postdata.get('phone_number')
#         password=postdata.get('password')
#         #password=make_password(password1)
#         print(user_name,first_name,last_name,email_field,password)
#         my_user=Customer(user_name=user_name,first_name=first_name,last_name=last_name,
#                         phone_number=phone_number, email_field=email_field,password=password)
#         if len(first_name)<4:
#             return render(request,'app1/singup.html')
#         elif (not first_name):
#             return render(request,'app1/singup.html')
#         elif my_user.isExists():
#             return HttpResponse("email alredy register ")
#         else: 
#             my_user.password=make_password(my_user.password)
#             my_user.register()
#             #return render(request,'app1/login.html')
    
#     return render(request,"app1/update.html")


def update(request ):
    if request.method =="GET":
        print("chalo")
        #return render(request,'app1/login.html')
    else:
        
        postdata=request.POST
        email_field=postdata.get('email_field')
        #password=postdata.get('password')
        my_user=Customer(email_field=email_field)
        print("hello1",email_field)  
        customer=Customer.objects.get(email_field=email_field)
        return render(request,"app1/update.html",{'customer':customer})
        
        # if my_user.isExists():
        #     print("hello1")
        #     customer=Customer.objects.get(email_field=email_field)
        #     #return render(request,"app1/update.html",{'customer':customer})
                
        #         #pi=Customer.objects.get()
        #         #request.session['customer']=customer.id
        #     if request.method =="GET":
        #         print("lalilijnjjh")
        #     else:
        #             user_name=postdata.get("user_name")
        #             first_name=postdata.get("first_name")
        #             last_name=postdata.get('last_name')
        #             email_field=postdata.get('email_field')
        #             phone_number=postdata.get('phone_number')
        #             password=postdata.get('password')
        #             #password=make_password(password1)
        #             print(user_name,first_name,last_name,email_field,password)
        #             my_user=Customer(user_name=user_name,first_name=first_name,last_name=last_name,
        #                             phone_number=phone_number, email_field=email_field,password=password)
        #             # if len(first_name)<4:
        #             #     return render(request,'app1/singup.html')
        #             if (not first_name):
        #                 return render(request,'app1/singup.html')
        #             elif my_user.isExists():
        #                 return HttpResponse("email alredy register ")
        #             else: 
        #                 my_user.password=make_password(my_user.password)
        #                 my_user.register()
        #         ####
        #                 get_user=Customer.objects.get(email_field=email_field)
        #                 get_user.user_name=user_name
        #                 get_user.first_name=first_name
        #                 get_user.last_name=last_name
        #                 get_user.phone_number=phone_number
        #                 get_user.password=password
        #                 get_user.save()
        #                 print("than")
        #                 return redirect('read')
                
           
       
            
            #return render(request,"app1/read1.html",{'customer':customer})
    return render(request,"app1/read.html")
    