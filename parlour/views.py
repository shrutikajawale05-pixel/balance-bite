from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'parlour/home.html')

def menu_page(request):
    return render(request, 'parlour/menu.html')

def cart(request):
    return render(request, 'parlour/cart.html')

def payment(request):
    return render(request, "parlour/payment.html")

def order_success(request):
    customer_name = "Customer"
    customer_email = None
    
    if request.method == "POST":
        customer_name = request.POST.get('name', 'Customer')
        customer_email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        subject = f"Balance Bite - Order Confirmed! 🍨"
        message = f"""Hi {customer_name},

Thank you for ordering from Balance Bite!

Your payment was successful.
Name: {customer_name}
Phone: {phone}
Address: {address}

Your order will be delivered soon.

- Team Balance Bite
"""
        try:
            if customer_email:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [customer_email],
                    fail_silently=False,
                )
                print(f"Mail sent to {customer_email}")
        except Exception as e:
            print(f"Mail Error: {e}")

    return render(request, "parlour/order_success.html", {'name': customer_name})