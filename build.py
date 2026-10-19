from data import CATALOG, el, escape, peso, find, toast
import cart

STEP_STYLE = 'width:34px;height:34px;border:2px solid #14213D;background:#fff;color:#14213D;border-radius:8px;font-weight:700;font-size:18px;cursor:pointer;padding:0'

BUILD_HEAD = """
<div id="build" style="max-width: 1200px; margin: 0 auto; padding: 56px 32px 40px; box-sizing: border-box">
<div style="background: #FFC93C; border: 2px solid #14213D; border-radius: 28px; padding: 48px; display: flex; gap: 40px; flex-wrap: wrap; align-items: center">
<div style="flex: 1 1 380px">
<h2 style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 44px; letter-spacing: -1px; margin: 0">Build your own kit</h2>
<p style="font-size: 19px; line-height: 1.5; margin: 14px 0 0">Need something specific? Pick items one by one from pens, paper, art supplies, and tech accessories. Your running total updates as you go.</p>
<button type="button" style="margin-top: 24px; background: #14213D; color: #FFFFFF; border: 0; border-radius: 12px; padding: 16px 28px; font-size: 18px; font-weight: 700; min-height: 52px" data-action="goto" data-id="build-card">Start building</button>
</div>
"""

BUILD_CARD = """<div id="build-card" style="flex: 1 1 340px; background: #FFFFFF; border: 2px solid #14213D; border-radius: 20px; padding: 24px; display: flex; flex-direction: column; gap: 12px">
<div id="build-list" style="display: flex; flex-direction: column; gap: 12px"></div>
<div style="border-top: 2px dashed #14213D; padding-top: 14px; display: flex; justify-content: space-between; font-size: 20px; font-weight: 700"><span>Running total</span><span id="build-total">₱0</span></div>
<div style="display: flex; gap: 10px; justify-content: flex-end; flex-wrap: wrap">
<button type="button" data-action="build-clear" style="background: #FFFFFF; color: #14213D; border: 2px solid #14213D; border-radius: 10px; padding: 10px 18px; font-size: 16px; font-weight: 700; min-height: 44px">Clear</button>
<button type="button" data-action="build-add" style="background: #14213D; color: #FFFFFF; border: 0; border-radius: 10px; padding: 12px 20px; font-size: 16px; font-weight: 700; min-height: 44px">Add to cart</button>
</div>
</div>"""

build = {}  
custom_counter = 0


def build_total():
    total = 0
    for cid, qty in build.items():
        total += find(CATALOG, cid)["price"] * qty
    return total


def page():
    """Returns the HTML for the Build Your Own page."""
    return BUILD_HEAD + BUILD_CARD + "</div></div>"


def render():
    """Fills in the item list. Call after the page is on screen."""
    if not el("build-list"):
        return
    rows = ""
    for c in CATALOG:
        qty = build.get(c["id"], 0)
        rows += f'''
        <div style="display:flex;justify-content:space-between;align-items:center;gap:10px;font-size:17px">
          <span>{escape(c["name"])} <span style="color:#4a5675;font-size:14px">{peso(c["price"])}</span></span>
          <span style="display:flex;align-items:center;gap:8px">
            <button type="button" data-action="build-dec" data-id="{c["id"]}" style="{STEP_STYLE}" aria-label="Less">-</button>
            <b style="min-width:18px;text-align:center">{qty}</b>
            <button type="button" data-action="build-inc" data-id="{c["id"]}" style="{STEP_STYLE}" aria-label="More">+</button>
          </span>
        </div>'''
    el("build-list").innerHTML = rows
    el("build-total").innerText = peso(build_total())


def change(item_id, delta):
    new_qty = max(0, build.get(item_id, 0) + delta)
    if new_qty == 0:
        build.pop(item_id, None)
    else:
        build[item_id] = new_qty
    render()


def add_custom_kit():
    global custom_counter
    if not build:
        toast("Pick at least one item for your kit.")
        return
    custom_counter += 1
    parts = [f'{qty} x {find(CATALOG, cid)["name"]}' for cid, qty in build.items()]
    cart.add_to_cart(f"custom-{custom_counter}", "Custom Kit", build_total(), ", ".join(parts))
    build.clear()
    render()


def handle(action, item_id):
    if action == "build-inc":
        change(item_id, 1)
    elif action == "build-dec":
        change(item_id, -1)
    elif action == "build-clear":
        build.clear()
        render()
    elif action == "build-add":
        add_custom_kit()
    else:
        return False
    return True