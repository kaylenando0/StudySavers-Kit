"""Landing page: hero with video, trust bar, and Why StudySavers."""

# The video file must sit in the same folder as index.html and logo.png.
HERO = """
<div style="max-width: 1360px; margin: 0 auto; padding: 64px 32px 56px; box-sizing: border-box; display: flex; align-items: center; gap: 40px; flex-wrap: wrap">
<div style="flex: 1 1 340px; min-width: 300px">
<div style="display: inline-block; background: #FFC93C; padding: 6px 14px; border-radius: 999px; font-weight: 700; font-size: 14px; letter-spacing: 0.5px; text-transform: uppercase">Emergency school supplies</div>
<h1 style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 48px; line-height: 1.05; letter-spacing: -1.5px; margin: 20px 0 0">Forgot your supplies? We've got you covered.</h1>
<p style="font-size: 19px; line-height: 1.5; margin: 20px 0 0; max-width: 480px">Ready-made emergency school supply bundles, packed and delivered fast, so a missing pen never costs you a grade.</p>
<div style="display: flex; gap: 14px; margin-top: 32px; flex-wrap: wrap">
<button type="button" style="background: #C8401B; color: #FFFFFF; border: 0; border-radius: 12px; padding: 16px 28px; font-size: 18px; font-weight: 700; min-height: 52px" data-action="nav" data-id="kits">Shop Kits</button>
<button type="button" style="background: #FFFFFF; color: #14213D; border: 2px solid #14213D; border-radius: 12px; padding: 14px 28px; font-size: 18px; font-weight: 700; min-height: 52px" data-action="nav" data-id="build">Build Your Own Kit</button>
</div>
</div>
<div style="flex: 2 1 560px; min-width: 300px; display: flex; justify-content: center">
<video src="intro.mp4" autoplay muted loop playsinline controls preload="auto" style="width: 100%; max-width: 880px; display: block; border: 2px solid #14213D; border-radius: 16px; background: #14213D"></video>
</div>
</div>

"""

TRUST = """
<div style="background: #14213D; color: #FFFFFF">
<div style="max-width: 1200px; margin: 0 auto; padding: 22px 32px; box-sizing: border-box; display: flex; justify-content: space-between; gap: 20px; flex-wrap: wrap; font-weight: 700; font-size: 17px">
<span>Fast delivery</span><span>Affordable</span><span>Student-approved</span><span>Pre-packed and ready</span>
</div>
</div>

"""

WHY = """
<div style="max-width: 1200px; margin: 0 auto; padding: 56px 32px 40px; box-sizing: border-box">
<h2 style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 44px; letter-spacing: -1px; margin: 0">Why StudySavers</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-top: 32px">
<div style="background: #FFFFFF; border: 2px solid #14213D; border-radius: 16px; padding: 24px"><div style="font-weight: 700; font-size: 20px">Saves time</div><p style="margin: 8px 0 0; font-size: 16px; line-height: 1.5">One tap instead of a store run during an emergency.</p></div>
<div style="background: #FFFFFF; border: 2px solid #14213D; border-radius: 16px; padding: 24px"><div style="font-weight: 700; font-size: 20px">Cheaper in a bundle</div><p style="margin: 8px 0 0; font-size: 16px; line-height: 1.5">Costs less than buying each item one by one.</p></div>
<div style="background: #FFFFFF; border: 2px solid #14213D; border-radius: 16px; padding: 24px"><div style="font-weight: 700; font-size: 20px">Made for your level</div><p style="margin: 8px 0 0; font-size: 16px; line-height: 1.5">Curated for Elementary, High School, and College.</p></div>
<div style="background: #FFFFFF; border: 2px solid #14213D; border-radius: 16px; padding: 24px"><div style="font-weight: 700; font-size: 20px">No guessing</div><p style="margin: 8px 0 0; font-size: 16px; line-height: 1.5">Pre-packed, so you already know what's inside.</p></div>
</div>
</div>
"""


def page():
    """Returns the HTML for the landing page."""
    return HERO + TRUST + WHY


def handle(action, item_id):
    """Nothing on this page needs its own button handling (the menu buttons are handled in main.py)."""
    return False