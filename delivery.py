DELIVERY = """
<div id="delivery" style="max-width: 1200px; margin: 0 auto; padding: 56px 32px 40px; box-sizing: border-box">
<div style="background: #14213D; color: #FFFFFF; border-radius: 28px; padding: 48px; display: flex; gap: 40px; flex-wrap: wrap">
<div style="flex: 1 1 320px">
<h2 style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 44px; letter-spacing: -1px; margin: 0">Delivery and pickup</h2>
<p style="font-size: 18px; line-height: 1.5; margin: 14px 0 0">Choose what works when the bell is about to ring.</p>
</div>
<div style="flex: 2 1 480px; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px">
<div style="background: #22335C; border-radius: 16px; padding: 22px"><div style="font-weight: 700; font-size: 19px; color: #FFC93C">Rush delivery</div><p style="margin: 8px 0 0; font-size: 16px; line-height: 1.5">For real emergencies. It arrives within about 1 hour of ordering.</p></div>
<div style="background: #22335C; border-radius: 16px; padding: 22px"><div style="font-weight: 700; font-size: 19px; color: #FFC93C">Same-day delivery</div><p style="margin: 8px 0 0; font-size: 16px; line-height: 1.5">It arrives later the same day, for example within 3 to 4 hours or before dismissal.</p></div>
<div style="background: #22335C; border-radius: 16px; padding: 22px"><div style="font-weight: 700; font-size: 19px; color: #FFC93C">Campus pickup</div><p style="margin: 8px 0 0; font-size: 16px; line-height: 1.5">The student picks the kit up at a campus point.</p></div>
</div>
</div>
</div>

"""


def page():
    """Returns the HTML for the Delivery page."""
    return DELIVERY