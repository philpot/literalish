#!/usr/bin/env python
# -*- coding: utf-8 -*-

_phonemes = {
    "ae": ("ɑ", "U+0251"),
    "ey": ("A", None),
    "b": ("b", None),
    "ch": ("č", "U+010D"),
    "d": ("d", None),
    "eh": ("e", None),
    "iy": ("E", None),
    "er": ("Я", "U+042F"),
    "f": ("f", None),
    "g": ("g", None),
    "hh": ("h", None),
    "ih": ("i", None),
    "ay": ("I", None),
    "jh": ("j", None),
    "k": ("k", None),
    "l": ("l", None),
    "m": ("m", None),
    "n": ("ⓝ", "U+24DD"),
    "aa": ("o", None),
    "ao": ("o", None),
    "ow": ("O", None),
    "p": ("p", None),
    "r": ("r", None),
    "s": ("s", None),
    "sh": ("š", "U+0161"),
    "t": ("+", None),
    "ah": ("u", None),
    "uw": ("U", None),
    "uh": ("ü", "U+00FC"),
    "v": ("v", None),
    "w": ("w", None),
    "y": ("y", None),
    "z": ("z", None),
    # "th": ("þ", "U+00FE"),
    "th": ("Θ", "U+0398"),
    "dh": ("ð", "U+00F0"),
    "ng": ("ŋ", "U+014B"),
    "zh": ("ž", "U+017E"),
    "aw": ("¤", "U+00A4"),
    "oy": ("ø", "U+00F8")
    }

def _translate_payload(pair):
    try:
        c = unichr(int(pair[1][2:], 16))
    except:
        c = pair[0]
    return (pair[0], c)

phonemes = {k.upper(): _translate_payload(v) for (k, v) in _phonemes.iteritems()}
