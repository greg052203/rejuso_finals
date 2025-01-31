from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm
from .models import Order, Payment
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Order
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'cafe/order_list.html', {'orders': orders})

def home(request):
    """Render the home page."""
    return render(request, 'cafe/home.html')


def menu(request):
    """Render the menu page."""
    return render(request, 'cafe/menu.html')


def about(request):
    """Render the about page."""
    return render(request, 'cafe/about.html')


def contact(request):
    """Render the contact page."""
    return render(request, 'cafe/contact.html')


def order_list(request):
    """Display a list of all orders."""
    orders = Order.objects.all()
    return render(request, 'cafe/order_list.html', {'orders': orders})


def order_create(request):
    """
    Create a new order. If an item is passed as a GET parameter,
    pre-fill the form with this data.
    """
    item = request.GET.get('item', '')  # Get the item from the query parameter

    # Initialize the form with the pre-filled data
    form = OrderForm(initial={'item': item})

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')

    return render(request, 'cafe/order_form.html', {'form': form})



def order_update(request, pk):
    """Update an existing order."""
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)

    return render(request, 'cafe/order_form.html', {'form': form})


def order_delete(request, pk):
    """Delete an existing order."""
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('order_list')

    return render(request, 'cafe/order_confirm_delete.html', {'order': order})


def pay_section(request):
    """
    Displays the total amount for all orders and handles payment.
    """
    orders = Order.objects.all()
    total_amount = sum(order.total for order in orders)

    if request.method == 'POST':
        # Process payment and move orders to the database
        Payment.objects.create(total_amount=total_amount)
        orders.delete()  # Clear orders after payment
        return redirect('order_list')  # Redirect to a fresh order list

    return render(request, 'cafe/pay_section.html', {'orders': orders, 'total_amount': total_amount})


def order_list(request):
    """
    Displays the list of current orders.
    """
    orders = Order.objects.all()
    return render(request, 'cafe/order_list.html', {'orders': orders})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data.get('is_superuser'):
                user.is_superuser = True
                user.is_staff = True
            user.save()
            return redirect('cafe/login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'cafe/signup.html', {'form': form})

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'cafe/signup.html'



