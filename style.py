import manim
from manim import *

cyan = "#99FFFF"

style = {
    "color": cyan,
    "tex_template": TexFontTemplates.helvetica_fourier_it
}

text_style = {
    "color": cyan,
    "font": "Helvetica"
}

w = config["frame_width"]
h = config["frame_height"]

def c2p(x, y):
    return (-w / 2 + w * (x / 1920), h / 2 - h * (y / 1080), 0)


def from_screen_width(width):
    return (width / 1920) * w


def from_screen_height(height):
    return (height / 1080) * h

def CreateArrow(arrow):
    return Create(arrow, lag_ratio=0.4)

def UncreateArrow(arrow):
    return Uncreate(arrow, lag_ratio=0.4)

def Arrow(*args, **kwargs):
    arrow = manim.Arrow(*args, **kwargs)
    arrow[1].shift(-0.1*arrow[1].length*arrow[1].vector)
    # arrow[2].shift(-0.1*arrow[2].length*arrow[2].vector)
    return arrow

def CurvedArrow(*args, **kwargs):
    arrow = manim.CurvedArrow(*args, **kwargs)
    arrow[1].shift(-0.1*arrow[1].length*arrow[1].vector)
    # arrow[2].shift(-0.1*arrow[2].length*arrow[2].vector)
    return arrow

def DoubleArrow(*args, **kwargs):
    arrow = manim.DoubleArrow(*args, **kwargs)
    arrow[1].shift(-0.1*arrow[1].length*arrow[1].vector)
    arrow[2].shift(-0.1*arrow[2].length*arrow[2].vector)
    return arrow

def CurvedDoubleArrow(*args, **kwargs):
    arrow = manim.CurvedDoubleArrow(*args, **kwargs)
    arrow[1].shift(-0.1*arrow[1].length*arrow[1].vector)
    arrow[2].shift(-0.1*arrow[2].length*arrow[2].vector)
    return arrow