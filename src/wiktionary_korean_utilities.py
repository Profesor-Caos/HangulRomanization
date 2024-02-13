import re
import math

def decompose_jamo(syllable):
    if not re.match("[가-힣]", syllable):
        if re.match("[ᄀ-ᄒ]", syllable):
            return {"initial": syllable, "vowel": "Ø", "final": "Ø"}
        elif re.match("[ᅡ-ᅵ]", syllable):
            return {"initial": "Ø", "vowel": syllable, "final": "Ø"}
        elif re.match("[ᆨ-ᇂ]", syllable):
            return {"initial": "Ø", "vowel": "Ø", "final": syllable}
        elif re.match("[ㄱ-ㅎ]", syllable):
            return {"initial": "Ø", "vowel": "Ø", "final": syllable}
        elif re.match("[ㅏ-ㅣ]", syllable):
            return {"initial": "Ø", "vowel": syllable, "final": "Ø"}
        else:
            return {"initial": "Ø", "vowel": " ", "final": "X"}
    
    cp = ord(syllable)
    if not cp:
        return ["", "", ""]
    
    relative_cp = cp - 0xAC00
    jongseong = relative_cp % 28
    jungseong = math.floor((relative_cp % 588) / 28)
    choseong = math.floor(relative_cp / 588)
    
    return {
        "initial": chr(0x1100 + choseong),
        "vowel": chr(0x1161 + jungseong),
        "final": chr(0x11A7 + jongseong) if jongseong != 0 else ""
    }