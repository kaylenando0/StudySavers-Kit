from data import KITS, escape, peso, find
import cart

KITS_HEAD = """
<div id="kits" style="max-width: 1200px; margin: 0 auto; padding: 56px 32px 40px; box-sizing: border-box">
<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 16px; flex-wrap: wrap">
<h2 style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 44px; letter-spacing: -1px; margin: 0">Pick your kit</h2>
<span style="font-size: 17px">Pre-packed bundles for every school emergency</span>
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 24px; margin-top: 36px">"""


def kit_card(k):
    return f'''<div style="background: #FFFFFF; border: 2px solid #14213D; border-radius: 20px; overflow: hidden; display: flex; flex-direction: column">
<div style="background: {k["color"]}; height: 150px; display: flex; align-items: center; justify-content: center">{k["icon"]}</div>
<div style="padding: 24px; display: flex; flex-direction: column; gap: 10px; flex: 1">
<h3 style="font-family: 'Bricolage Grotesque', sans-serif; font-size: 26px; margin: 0">{escape(k["name"])}</h3>
<p style="margin: 0; font-size: 16px; line-height: 1.5; flex: 1">{escape(k["items"])}</p>
<div style="display: flex; align-items: center; justify-content: space-between; margin-top: 8px">
<span style="font-weight: 700; font-size: 22px">{peso(k["price"])}</span>
<button type="button" data-action="add-kit" data-id="{k["id"]}" style="background: #14213D; color: #FFFFFF; border: 0; border-radius: 10px; padding: 12px 20px; font-size: 16px; font-weight: 700; min-height: 44px">Add to cart</button>
</div>
</div>
</div>'''


def page():
    cards = "".join(kit_card(k) for k in KITS)
    return KITS_HEAD + cards + "</div></div>"


def handle(action, item_id):
    if action == "add-kit":
        k = find(KITS, item_id)
        cart.add_to_cart(k["id"], k["name"], k["price"], k["items"])
        return True
    return False