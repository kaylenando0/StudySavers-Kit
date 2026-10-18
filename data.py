"""Shop data (edit kit names, contents and prices here) plus small helpers used by every page."""
from pyscript import document, window
from pyscript.ffi import create_proxy

KITS = [
    {
        "id": 'emergency-pen',
        "name": 'Emergency Pen Kit',
        "items": '2 ballpens, 1 Pencil, 1 Eraser',
        "price": 35,
        "color": '#FFC93C',
        "icon": '<svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="#14213D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20l1-4L16 5l3 3L8 19z"/><path d="M14 7l3 3"/></svg>',
    },
    {
        "id": 'quiz-exam',
        "name": 'Quiz Exam Kit',
        "items": '2 ballpens, 2 Pencils, 1 Yellow Pad',
        "price": 85,
        "color": '#BFD9FF',
        "icon": '<svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="#14213D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="3.5" width="14" height="17" rx="2"/><path d="M9 9.5l2 2 4-4M9 15.5h6"/></svg>',
    },
    {
        "id": 'submission',
        "name": 'Submission Kit',
        "items": 'Folder, Envelope, Bondpaper, Ballpen',
        "price": 77,
        "color": '#DAD3FF',
        "icon": '<svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="#14213D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8.500a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>',
    },
    {
        "id": 'note-taking',
        "name": 'Note-Taking Kit',
        "items": 'Notebook, 2 Ballpens, Highlighter',
        "price": 90,
        "color": '#CDEFD9',
        "icon": '<svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="#14213D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 3v18M11 8h6M11 12h6M11 16h4"/></svg>',
    },
    {
        "id": 'project',
        "name": 'Project Kit',
        "items": 'Colored paper, glue, scissors, markers, tape, ruler, Bondpaper',
        "price": 122,
        "color": '#FFD3C2',
        "icon": '<svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="#14213D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="6" cy="18" r="2.5"/><circle cx="6" cy="6" r="2.5"/><path d="M8 7.5l12 9M8 16.5l12-9"/></svg>',
    },
    {
        "id": 'group',
        "name": 'Group Project Kit',
        "items": 'Manila Paper, Marker, Tape, Scissors, Glue',
        "price": 70,
        "color": '#FFD1E3',
        "icon": '<svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="#14213D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="7" width="14" height="10" rx="1.500"/><path d="M7 7V5h14v10h-4"/><path d="M6 11h6M6 14h4"/></svg>',
    },
]

CATALOG = [
    {"id": 'pen', "name": 'Ballpen (black)', "price": 12},
    {"id": 'pencil', "name": 'Pencil', "price": 8},
    {"id": 'paper', "name": 'Yellow pad paper', "price": 45},
    {"id": 'notebook', "name": 'Notebook', "price": 35},
    {"id": 'highlighter', "name": 'Highlighter set', "price": 60},
    {"id": 'calc', "name": 'Scientific calculator', "price": 350},
    {"id": 'glue', "name": 'Glue', "price": 25},
    {"id": 'scissors', "name": 'Scissors', "price": 40},
]



DELIVERY_FEES = {'rush': 50, 'standard': 30, 'campus': 0}



def el(element_id):
    return document.getElementById(element_id)


def escape(text):
    """Make text safe to put inside HTML."""
    text = str(text)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return text.replace('"', "&quot;").replace("'", "&#x27;")


def peso(n):
    """1234 -> \u20b11,234"""
    s = str(int(round(n)))
    tail = ""
    while len(s) > 3:
        tail = "," + s[-3:] + tail
        s = s[:-3]
    return "\u20b1" + s + tail


def find(items, item_id):
    for it in items:
        if it["id"] == item_id:
            return it
    return None


def hide_toast():
    el("toast").style.display = "none"


def toast(text):
    box = el("toast")
    box.innerText = text
    box.style.display = "block"
    window.setTimeout(create_proxy(hide_toast), 2600)