"""Cart: add/remove items, totals, delivery fee and checkout."""
import json
from pyscript import window

from data import DELIVERY_FEES, el, escape, peso, toast

STORAGE_KEY = "studysavers_cart"
SMALL_STYLE = 'width:30px;height:30px;border:2px solid #14213D;background:#fff;color:#14213D;border-radius:8px;font-weight:700;cursor:pointer;padding:0'

cart = {}  # id -> {"name", "price", "qty", "detail"}


def save_cart():
    window.localStorage.setItem(STORAGE_KEY, json.dumps(cart))


def load_cart():
    raw = window.localStorage.getItem(STORAGE_KEY)
    if raw:
        try:
            cart.clear()
            cart.update(json.loads(raw))
        except Exception:
            cart.clear()


def subtotal():
    return sum(i["price"] * i["qty"] for i in cart.values())


def delivery_fee():
    if not cart:
        return 0
    return DELIVERY_FEES[el("delivery-option").value]


def add_to_cart(item_id, name, price, detail=""):
    if item_id in cart:
        cart[item_id]["qty"] += 1
    else:
        cart[item_id] = {"name": name, "price": price, "qty": 1, "detail": detail}
    save_cart()
    render_cart()
    toast("Added to cart: " + name)


def change_qty(item_id, delta):
    if item_id not in cart:
        return
    cart[item_id]["qty"] += delta
    if cart[item_id]["qty"] <= 0:
        del cart[item_id]
    save_cart()
    render_cart()


def remove_item(item_id):
    cart.pop(item_id, None)
    save_cart()
    render_cart()


def render_cart():
    count = sum(i["qty"] for i in cart.values())
    el("cart-btn").innerText = f"Cart ({count})"

    if not cart:
        el("cart-items").innerHTML = '<p style="margin:0;color:#4a5675">Your cart is empty.</p>'
        el("summary").innerHTML = ""
        return

    rows = ""
    for cid, i in cart.items():
        detail = ""
        if i.get("detail"):
            detail = f'<div style="color:#4a5675;font-size:14px;line-height:1.4">{escape(i["detail"])}</div>'
        rows += f'''
        <div style="display:flex;justify-content:space-between;align-items:center;gap:10px;padding:10px 0;border-bottom:2px dashed #14213D">
          <div><b>{escape(i["name"])}</b>{detail}<div>{peso(i["price"])}</div></div>
          <span style="display:flex;align-items:center;gap:6px">
            <button type="button" data-action="cart-dec" data-id="{cid}" style="{SMALL_STYLE}" aria-label="Less">-</button>
            <b style="min-width:18px;text-align:center">{i["qty"]}</b>
            <button type="button" data-action="cart-inc" data-id="{cid}" style="{SMALL_STYLE}" aria-label="More">+</button>
            <button type="button" data-action="cart-remove" data-id="{cid}" style="{SMALL_STYLE};background:#C8401B;color:#fff;border-color:#C8401B" aria-label="Remove">x</button>
          </span>
        </div>'''
    el("cart-items").innerHTML = rows
    render_summary()


def render_summary():
    if not cart:
        el("summary").innerHTML = ""
        return
    sub = subtotal()
    fee = delivery_fee()
    el("summary").innerHTML = f'''
      <div style="display:flex;justify-content:space-between"><span>Subtotal</span><span>{peso(sub)}</span></div>
      <div style="display:flex;justify-content:space-between"><span>Delivery</span><span>{peso(fee)}</span></div>
      <div style="display:flex;justify-content:space-between;font-size:20px;font-weight:700;margin-top:6px"><span>Total</span><span>{peso(sub + fee)}</span></div>'''


def update_delivery_ui():
    campus = el("delivery-option").value == "campus"
    el("address-label").innerText = "Campus pickup point" if campus else "Delivery address"
    render_summary()


def order_message(text, error=False):
    box = el("order-msg")
    box.innerHTML = text
    box.style.background = "#FFD3C2" if error else "#CDEFD9"
    box.style.display = "block"


def checkout():
    if not cart:
        order_message("Your cart is empty.", error=True)
        return

    name = el("name").value.strip()
    phone = el("phone").value.strip()
    address = el("address").value.strip()
    payment = el("payment").value

    digits = "".join(ch for ch in phone if ch.isdigit())
    if not name:
        order_message("Please enter your name.", error=True); return
    if len(digits) < 10:
        order_message("Please enter a valid phone number.", error=True); return
    if not address:
        order_message("Please enter your address or pickup point.", error=True); return

    total = subtotal() + delivery_fee()
    order_id = "SSK-" + str(int(window.Date.now()))[-6:]
    lines = "".join(f'<li>{i["qty"]} x {escape(i["name"])}</li>' for i in cart.values())

    order_message(f'''
        <b>Order {order_id} placed!</b><br>
        Thank you for ordering {escape(name)}, we'll contact you at {escape(phone)}.
        <ul style="margin:8px 0;padding-left:20px">{lines}</ul>
        Total: <b>{peso(total)}</b> via {escape(payment)}.''')

    cart.clear()
    save_cart()
    render_cart()


def handle(action, item_id):
    if action == "cart-inc":
        change_qty(item_id, 1)
    elif action == "cart-dec":
        change_qty(item_id, -1)
    elif action == "cart-remove":
        remove_item(item_id)
    elif action == "checkout":
        checkout()
    else:
        return False
    return True