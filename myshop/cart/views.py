
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from products.models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    cart[str(product.id)] = cart.get(str(product.id), 0) + 1
    request.session['cart'] = cart
    request.session.modified = True

    messages.success(request, f"Added {product.name} to cart.")
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id_str, quantity in cart.items():
        try:
            product = get_object_or_404(Product, id=int(product_id_str))
            item_total = product.price * quantity
            total_price += item_total
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total,
            })
        except:
            continue

    return render(request, 'cart/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart
        request.session.modified = True
        messages.success(request, "Item removed from cart.")

    return redirect('cart_detail')