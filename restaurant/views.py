from django.shortcuts import render
from models import Order, Table

def create_order(request):
    tables_list = Table.objects.all() \
            .order_by('name')
    
    print tables_list
    
    context = {'tables': tables_list,
               'page_title': 'Create new order'
               }
    
    return render(request, 'base/create_order.html', context)

def open_orders(request):
    order_list = Order.objects.filter(status = 'op') \
            .order_by('creation_date')
    
    context = {'orders': order_list,
               'page_title': 'Open orders'
               }
    
    return render(request, 'base/orders_list.html', context)
