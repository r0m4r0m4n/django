from django.shortcuts import redirect


def redirect_shop(request):
    return redirect('orders_list_url', permanent=True)
