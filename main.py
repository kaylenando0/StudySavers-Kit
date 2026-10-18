"""StudySavers Kit - starts the app, builds the page frame (nav, footer, cart panel) and switches pages."""
from pyscript import document, window
from pyscript.ffi import create_proxy

import cart, build, landing, kits, how, delivery
from data import el, toast

# ------------------------------------------------------------------
# DESIGN  (styles and the frame shown on every page)
# ------------------------------------------------------------------
CSS = """html{scroll-behavior:smooth}body{margin:0;font-family:'DM Sans',sans-serif;color:#14213D;background:#F6F8FC}
a{color:#14213D;text-decoration:none}
a:hover{color:#C8401B}
button{font-family:'DM Sans',sans-serif;cursor:pointer}
.navlink{padding:6px 0;border-bottom:3px solid transparent}
.navlink.active{border-bottom-color:#FFC93C}"""

FONT_URL = 'https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800&family=DM+Sans:wght@400;500;700&display=swap'

PAGE_OPEN = """<div style="background: #F6F8FC; color: #14213D; font-family: 'DM Sans', sans-serif; min-height: 100vh; display: flex; flex-direction: column">

"""

NAV = """
<div style="background: #FFFFFF; border-bottom: 2px solid #14213D">
<div style="max-width: 1200px; margin: 0 auto; padding: 16px 32px; display: flex; align-items: center; justify-content: space-between; gap: 24px; flex-wrap: wrap; box-sizing: border-box">
<a href="#/" style="display: flex; align-items: center; gap: 10px; color: #14213D">
<img src="./logo.png" alt="StudySavers Kit logo" height="60" style="display: block; height: 60px; width: auto">
<span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 24px; letter-spacing: -0.5px">StudySavers Kit</span>
</a>
<div style="display: flex; gap: 28px; font-weight: 500; font-size: 16px; flex-wrap: wrap">
<a class="navlink" data-route="kits" href="#/kits">Kits</a>
<a class="navlink" data-route="build" href="#/build">Build Your Own</a>
<a class="navlink" data-route="how" href="#/how">How It Works</a>
<a class="navlink" data-route="delivery" href="#/delivery">Delivery</a>
</div>
<button type="button" style="background: #14213D; color: #FFFFFF; border: 0; border-radius: 999px; padding: 12px 22px; font-size: 16px; font-weight: 700; min-height: 44px" id="cart-btn" data-action="open-cart">Cart (0)</button>
</div>
</div>

"""

FOOTER = """
<div style="background: #14213D; color: #FFFFFF">
<div style="max-width: 1200px; margin: 0 auto; padding: 56px 32px 40px; box-sizing: border-box; display: flex; gap: 48px; flex-wrap: wrap; justify-content: space-between">
<div style="flex: 1 1 280px">
<div style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 26px">StudySavers Kit</div>
<p style="margin: 10px 0 0; font-size: 16px; line-height: 1.5; max-width: 320px">Born from a student's last-minute scramble, so no one misses a deadline because of a missing pen.</p>
</div>
<div style="flex: 1 1 200px; font-size: 16px; line-height: 2">
<div style="font-weight: 700; color: #FFC93C">Contact</div>
<div>StudySaversKit2026@gmail.com</div>
<div>09671834505</div>
<div>StudySavers Kit</div>
</div>
<div style="flex: 1 1 200px; font-size: 16px; line-height: 2">
<div style="font-weight: 700; color: #FFC93C">Delivery hours</div>
<div>Mon to Fri</div>
<div>7 AM to 9 PM</div>
<div>Feel free to order anytime! Just keep in mind that orders placed outside our working hours will be processed on the next business day.</div>
</div>
</div>
<div style="max-width: 1200px; margin: 0 auto; padding: 0 32px 32px; box-sizing: border-box; font-size: 14px; display: flex; gap: 24px; flex-wrap: wrap">
</div>
</div>

</div>"""

DRAWER = """
<div id="overlay" data-action="close-cart" style="display: none; position: fixed; top: 0; right: 0; bottom: 0; left: 0; background: rgba(20,33,61,0.55); z-index: 50"></div>
<div id="drawer" style="display: none; position: fixed; top: 0; right: 0; bottom: 0; width: 440px; max-width: 100%; background: #FFFFFF; border-left: 2px solid #14213D; z-index: 51; overflow-y: auto; padding: 24px; box-sizing: border-box; font-family: 'DM Sans', sans-serif; color: #14213D">
<div style="display: flex; justify-content: space-between; align-items: center">
<h2 style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 32px; letter-spacing: -1px; margin: 0">Your cart</h2>
<button type="button" data-action="close-cart" style="background: #14213D; color: #FFFFFF; border: 0; border-radius: 10px; padding: 10px 16px; font-size: 16px; font-weight: 700; min-height: 44px">Close</button>
</div>
<div id="cart-items" style="margin-top: 16px"></div>
<label for="delivery-option" style="display: block; font-weight: 700; font-size: 14px; margin: 14px 0 6px">Delivery option</label>
<select id="delivery-option" style="width: 100%; min-height: 44px; border: 2px solid #14213D; border-radius: 10px; padding: 0 12px; font-size: 16px; font-family: 'DM Sans', sans-serif; box-sizing: border-box; background: #FFFFFF; color: #14213D"><option value="rush">Rush delivery</option><option value="standard">Same-day delivery</option><option value="campus">Campus pickup</option></select>
<label for="payment" style="display: block; font-weight: 700; font-size: 14px; margin: 14px 0 6px">Payment</label>
<select id="payment" style="width: 100%; min-height: 44px; border: 2px solid #14213D; border-radius: 10px; padding: 0 12px; font-size: 16px; font-family: 'DM Sans', sans-serif; box-sizing: border-box; background: #FFFFFF; color: #14213D"><option>GCash</option><option>Cash on delivery</option></select>
<label for="name" style="display: block; font-weight: 700; font-size: 14px; margin: 14px 0 6px">Name</label>
<input id="name" placeholder="Full name" style="width: 100%; min-height: 44px; border: 2px solid #14213D; border-radius: 10px; padding: 0 12px; font-size: 16px; font-family: 'DM Sans', sans-serif; box-sizing: border-box; background: #FFFFFF; color: #14213D">
<label for="phone" style="display: block; font-weight: 700; font-size: 14px; margin: 14px 0 6px">Phone</label>
<input id="phone" placeholder="09XX XXX XXXX" style="width: 100%; min-height: 44px; border: 2px solid #14213D; border-radius: 10px; padding: 0 12px; font-size: 16px; font-family: 'DM Sans', sans-serif; box-sizing: border-box; background: #FFFFFF; color: #14213D">
<label for="address" id="address-label" style="display: block; font-weight: 700; font-size: 14px; margin: 14px 0 6px">Delivery address</label>
<input id="address" placeholder="Building, room, street" style="width: 100%; min-height: 44px; border: 2px solid #14213D; border-radius: 10px; padding: 0 12px; font-size: 16px; font-family: 'DM Sans', sans-serif; box-sizing: border-box; background: #FFFFFF; color: #14213D">
<div id="summary" style="margin-top: 16px; font-size: 17px; display: flex; flex-direction: column; gap: 4px"></div>
<button type="button" data-action="checkout" style="width: 100%; margin-top: 16px; background: #C8401B; color: #FFFFFF; border: 0; border-radius: 12px; padding: 16px 28px; font-size: 18px; font-weight: 700; min-height: 52px">Place order</button>
<div id="order-msg" style="display: none; margin-top: 14px; padding: 14px; border-radius: 12px; font-size: 16px; line-height: 1.5"></div>
</div>
<div id="toast" style="display: none; position: fixed; left: 50%; bottom: 28px; transform: translateX(-50%); background: #14213D; color: #FFFFFF; padding: 14px 22px; border-radius: 999px; font-weight: 700; font-size: 16px; z-index: 60; font-family: 'DM Sans', sans-serif"></div>
"""

# ------------------------------------------------------------------
# PAGES
# ------------------------------------------------------------------
PAGES = {
    "home": landing.page,
    "kits": kits.page,
    "build": build.page,
    "how": how.page,
    "delivery": delivery.page,
}

TITLES = {
    "home": "StudySavers Kit",
    "kits": "Kits | StudySavers Kit",
    "build": "Build Your Own | StudySavers Kit",
    "how": "How It Works | StudySavers Kit",
    "delivery": "Delivery | StudySavers Kit",
}


# ------------------------------------------------------------------
# FRAME  (nav, footer, cart panel)
# ------------------------------------------------------------------
def build_shell():
    """Builds the frame once. Only the #view area changes between pages."""
    link = document.createElement("link")
    link.rel = "stylesheet"
    link.href = FONT_URL
    document.head.appendChild(link)

    style = document.createElement("style")
    style.textContent = CSS
    document.head.appendChild(style)

    el("app").innerHTML = (
        PAGE_OPEN + NAV
        + '<div id="view" style="flex: 1 1 auto"></div>'
        + FOOTER + DRAWER
    )


def set_active(route):
    """Underline the current page in the menu."""
    links = document.querySelectorAll(".navlink")
    for i in range(links.length):
        a = links.item(i)
        if a.getAttribute("data-route") == route:
            a.classList.add("active")
        else:
            a.classList.remove("active")


def open_cart():
    el("overlay").style.display = "block"
    el("drawer").style.display = "block"


def close_cart():
    el("overlay").style.display = "none"
    el("drawer").style.display = "none"


def goto(target_id):
    target = el(target_id)
    if target:
        target.scrollIntoView()


def frame_handle(action, item_id):
    """Buttons that belong to the frame: menu and cart open/close."""
    if action == "goto":
        goto(item_id)
    elif action == "nav":
        window.location.hash = "#/" + item_id
    elif action == "open-cart":
        open_cart()
    elif action == "close-cart":
        close_cart()
    else:
        return False
    return True


# every module that reacts to button clicks (each has handle(action, item_id))
HANDLERS = (frame_handle, cart.handle, build.handle, landing.handle, kits.handle)


# ------------------------------------------------------------------
# ROUTER
# ------------------------------------------------------------------
def current_route():
    route = window.location.hash.replace("#/", "").replace("#", "")
    return route if route in PAGES else "home"


def show_page():
    route = current_route()
    el("view").innerHTML = PAGES[route]()
    set_active(route)
    if route == "build":
        build.render()
    window.document.title = TITLES[route]
    window.scrollTo(0, 0)


def on_click(event):
    target = event.target.closest("[data-action]")
    if not target:
        return
    action = target.getAttribute("data-action")
    item_id = target.getAttribute("data-id")
    for handler in HANDLERS:
        if handler(action, item_id):
            return


# ------------------------------------------------------------------
# START
# ------------------------------------------------------------------
build_shell()
window.document.addEventListener("click", create_proxy(on_click))
window.addEventListener("hashchange", create_proxy(lambda e: show_page()))
el("delivery-option").addEventListener("change", create_proxy(lambda e: cart.update_delivery_ui()))

cart.load_cart()
show_page()
cart.render_cart()
cart.update_delivery_ui()