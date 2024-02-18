from collections import defaultdict
import unicodedata
from .wiktionary_romanization_data import RomanizationData
from .wiktionary_korean_utilities import decompose_jamo
import re
import math

class WiktionaryRomanization:
    title: str = ''
    input_string: str = ''

    def __init__(self, title, input_string):
        self.title = title
        self.input_string = input_string

    system_lookup = {
        'ph' : 0, # Phonetic Hangul
        'rr' : 1, # Revised Romanization
        'rrr' : 2, # Revised Romanization (translit.)
        'mr' : 3, # McCune-Reischauer
        'yr' :  4, # Yale Romanization
        'ipa' : 5, # IPA
    }

    question_mark = "<sup><small>[[Wiktionary:About Korean/Romanization|?]]</small></sup>"

    system_list = [
        {
            "abbreviation": "ph",
            "display": "Phonetic hangul: ",
            "separator": "/"
        },
        {
            "abbreviation": "rr",
            "display": "Revised Romanization" + question_mark,
            "separator": "/"
        },
        {
            "abbreviation": "rrr",
            "display": "Revised Romanization (translit.)" + question_mark,
            "separator": "/"
        },
        {
            "abbreviation": "mc",
            "display": "McCune–Reischauer" + question_mark,
            "separator": "/"
        },
        {
            "abbreviation": "yr",
            "display": "Yale Romanization" + question_mark,
            "separator": "/"
        },
        {
            "abbreviation": "ipa",
            "display": "(<i>[[w:South Korean standard language|SK Standard]]/[[w:Seoul dialect|Seoul]]</i>) [[Wiktionary:International Phonetic Alphabet|IPA]]<sup>([[Appendix:Korean pronunciation|key]])</sup>: ",
            "separator": " ~ "
        }
    ]

    # vowel_variation:
    #     rules for vowel transformation.
    #     key:
    #         the number of a syllable's vowel (vowel_id):
    #             math.floor(((codepoint('가') - 0xAC00) % 588) / 28) = 0
    #             math.floor(((codepoint('개') - 0xAC00) % 588) / 28) = 1
    #     value:
    #         an integer that is added to the decimal codepoint of the syllable
    #                 char(codepoint('개') + 112) = '게'

    # allowed_vowel_scheme:
    #     a list of which systems vowel transformation is reflected in.
    #     key:
    #         vowel_id .. "-" .. system_index
    #         system_index: see system_list above. IPA is #6
    #     value:
    #         1, representing true

    final_syllable_conversion = {"": "Ø", "X": ""}
    com_mc = {"g": "k", "d": "t", "b": "p", "j": "ch", "sy": "s", "s": "ss"}
    com_ph = {"ᄀ": "ᄁ", "ᄃ": "ᄄ", "ᄇ": "ᄈ", "ᄉ": "ᄊ", "ᄌ": "ᄍ"}
    vowel_variation = {
        1: 112,   # 개→게
        3: 112,   # 걔→계
        10: 140,  # 괘→궤
        7: -56,   # 계→게
        11: 112,  # 괴→궤
        16: 0,    # 귀→귀
    }
    allowed_vowel_scheme = {
        "1-0": 1,
        "1-5": 1,
        "3-0": 1,
        "3-5": 1,
        "10-0": 1,
        "10-5": 1,
        "7-0": 1,
        "7-5": 1,
        "11-0": 1,
        "11-5": 1,
        "16-5": 1,
    }
    ambiguous_intersyllabic_rr = {"oe": 1, "eo": 1, "eu": 1, "ae": 1, "ui": 1}
    ambiguous_intersyllabic_mr = {"oe": 1, "ae": 1}
    ambiguous_intersyllabic_yr = {
        "ay": 1,
        "ey": 1,
        "oy": 1,
        "uy": 1,
        "̄y": 1,
        "ya": 1,
        "ye": 1,
        "yo": 1,
        "yu": 1,
    }

    def decompose_syllable(word):
        decomposed_syllables = []
        for syllable in word:
            decomposed_syllables.append(decompose_jamo(syllable))
        return decomposed_syllables
    
    def tidy_phonetic(original, romanized):
        j, k, w = 0, 0, []
        for i in range(len(romanized)):
            if i == len(original):
                break
            romanized_syllable = romanized[k]
            original_syllable = original[j]
            if romanized_syllable != original_syllable:
                w.append('<b>' + romanized_syllable + '</b>')
                if re.match("[^; ]", original_syllable):
                    k += 1
                if re.match("[^; ]", romanized_syllable):
                    j += 1
            else:
                w.append('<span>' + romanized_syllable + '</span>')
                j += 1
                k += 1
        return ''.join(w)

    def tidy_ipa(ipa):
        ipa = re.sub("ʌ̹%(ː%)", "ɘ(ː)", ipa)  # TODO: [[멀다]] really should be [ˈmʌ̹ɭda̠] ~ [ˈmɘːɭda̠] instead of [ˈmɘ(ː)ɭda̠]
        ipa = re.sub("ɭɭi", "ʎʎi", ipa)
        ipa = re.sub("ɭɭj", "ʎʎ", ipa)
        ipa = re.sub("s([ʰ͈])ɥi", "ʃ\\1ɥi", ipa)
        ipa = re.sub("ss͈([ji])", "ɕɕ͈\\1", ipa)
        ipa = re.sub("s([ʰ͈])([ji])", "ɕ\\1\\2", ipa)
        ipa = re.sub("nj", "ɲ", ipa)
        ipa = re.sub("([ʑɕ])([ʰ͈]?)j", "\\1\\2", ipa)
        
        ipa = re.sub("kʰ[ijɯ]", lambda match: {
            "kʰi": "cçi",
            "kʰj": "cç",
            "kʰɯ": "kxɯ"
        }[match.group()], ipa)
        
        ipa = re.sub("[hɦ][ijɯouw]", lambda match: {
            "hi": "çi",
            "hj": "ç",
            "hɯ": "xɯ",
            "ho": "ɸʷo",
            "hu": "ɸʷu",
            "hw": "ɸw",
            "ɦi": "ʝi",
            "ɦj": "ʝ",
            "ɦɯ": "ɣɯ",
            "ɦo": "βo",
            "ɦu": "βu",
            "ɦw": "βw"
        }[match.group()], ipa)
        
        if re.search("ɥi", ipa):
            midpoint = math.floor(len(ipa) / 2)
            ipa = ipa[:midpoint] + re.sub("ɥi", "y", ipa[midpoint:])
        
        return ipa

    def romanize(system_index, args):
        text_param = args[1]

        p, optional_params = {}, ["nn", "l", "com", "cap", "ni"]
        for pm in optional_params:
            p[pm] = {}
            if args[pm]:
                for pp in args[pm].split(","):
                    p[pm][int(pp) if pp.isdigit() else pp] = 1

        categories = []

        vowel_ui_i, vowel_ui_e, no_batchim, batchim_reduce, s_variation, iotation = (
            args["ui"], args["uie"], args["nobc"], args["bcred"], args["svar"], args["iot"]
        )

        system_index = WiktionaryRomanization.system_lookup.get(system_index, system_index)
        text_param = re.sub(r'["](.)', r"\1", text_param)

        for primitive_word in re.findall(r"[\-ᄀ-하-ᅵᆨ-ᇂㄱ-ㅣ가-힣' 􀀀-􏿽]+", text_param):
            the_original = primitive_word
            primitive_word = primitive_word.replace("'''", "ß")
            formatting_position, formatting_count = {}, 0
            primitive_word = re.sub(r"()([ß􀀀-􏿽])", lambda m: formatting_position.setdefault(m.start(1) + formatting_count, "'''") if m.group(2) == "ß" else m.group(2), primitive_word)
            
            has_vowel = {}
            for ch in re.findall(".", primitive_word):
                jungseong = math.floor(((ord(ch) - 0xAC00) % 588) / 28)
                if ch not in ["예", "옛", "례", "롄"] and re.match(r"[가-힣]", ch):
                    has_vowel[jungseong] = True
            
            word_set = [primitive_word]

            def add_respelling(variable, modification, modification2=None):
                modification2 = modification2 or (lambda x: x)
                if variable and system_index in [0, 5]:
                    variable = int(variable) - 1 # Modification - this accounts for the original in Lua being a 1 indexed language
                    pre_length = len(word_set)
                    for i in range(pre_length):
                        item = list(word_set[i])
                        item[variable] = modification(item[variable])
                        if (variable + 1 < len(item)):
                            item[variable + 1] = modification2(item[variable + 1])
                        word_set.append("".join(item))
            
            add_respelling(vowel_ui_i, lambda x: "이")
            add_respelling(vowel_ui_e, lambda x: "에")

            def modify_no_batchim(x):
                return chr(ord(x) - ((ord(x) - 0xAC00) % 28))

            def modify_no_batchim2(y):
                return chr(ord(y) + 588)

            add_respelling(no_batchim, modify_no_batchim, modify_no_batchim2)
            
            add_respelling(s_variation, lambda x: chr(ord(x) - 12))
            add_respelling(iotation, lambda x: chr(ord(x) + 56))
            
            for vowel_id, vowel_variation_increment in WiktionaryRomanization.vowel_variation.items():
                if has_vowel.get(vowel_id) and WiktionaryRomanization.allowed_vowel_scheme.get(f"{vowel_id}-{system_index}"):
                    pre_length = len(word_set)
                    j = 0 # Modification - not sure how this worked in Lua, but if we're inserting in Python, our index 
                    # gets messed up, so we need to be able to modify the index we're grabbing and inserting into.
                    for i in range(pre_length):
                        item = list(word_set[j])
                        for num, it in enumerate(item):
                            if math.floor(((ord(it) - 0xAC00) % 588) / 28) == vowel_id:
                                item[num] = chr(ord(it) + vowel_variation_increment)
                        if vowel_id == 11:
                            word_set.insert(j, "".join(item))
                            j += 1
                        else:
                            word_set.append("".join(item))
                        j += 1

            word_set_romanizations = []
            for respelling in word_set:
                decomposed_syllables = WiktionaryRomanization.decompose_syllable(respelling)
                romanization = []
                formatting_insert_count = 0
                for index in range(-1, len(decomposed_syllables)):
                    this_syllable_text = respelling[index] if index != -1 else ""
                    if this_syllable_text != "-":
                        syllable = decomposed_syllables[index] if index != -1 else {"initial": "Ø", "vowel": "Ø", "final": "X"}
                        next_index = index
                        next_syllable_text = ""
                        saw_hyphen_after = False
                        while True:
                            next_index += 1
                            if next_index > len(decomposed_syllables):
                                break
                            next_syllable_text = respelling[next_index] if next_index < len(respelling) else ""
                            if next_syllable_text != "-":
                                break
                            saw_hyphen_after = True
                        next_syllable = decomposed_syllables[next_index] if next_index < len(decomposed_syllables) else {"initial": "Ø", "vowel": "Ø", "final": "Ø"}
                        syllable["final"] = WiktionaryRomanization.final_syllable_conversion.get(syllable["final"], syllable["final"])

                        if system_index == 4 and syllable["vowel"] == "ᅮ" and syllable["initial"] in "ᄆᄇᄈᄑ":
                            syllable["vowel"] = "ᅳ"

                        if system_index in [0, 1, 3, 5]:
                            if syllable["initial"] in "ᄌᄍᄎ":
                                if syllable["vowel"] == "ᅣ":
                                    syllable["vowel"] = "ᅡ"
                                elif syllable["vowel"] == "ᅤ":
                                    syllable["vowel"] = "ᅢ"
                                elif syllable["vowel"] == "ᅧ":
                                    syllable["vowel"] = "ᅥ"
                                elif syllable["vowel"] == "ᅨ":
                                    syllable["vowel"] = "ᅦ"
                                elif syllable["vowel"] == "ᅭ":
                                    syllable["vowel"] = "ᅩ"
                                elif syllable["vowel"] == "ᅲ":
                                    syllable["vowel"] = "ᅮ"

                        if system_index in [0, 5]:
                            if syllable["vowel"] == "ᅴ" and this_syllable_text != "의":
                                syllable["vowel"] = "ᅵ"

                        if system_index in [0, 1, 3, 5]:
                            if this_syllable_text == "넓":
                                if next_syllable["initial"] in "ᄌᄉ":
                                    syllable["final"] = "ᆸ"
                                elif next_syllable["initial"] == "ᄃ":
                                    if next_syllable["vowel"] not in "ᅡᅵ":
                                        syllable["final"] = "ᆸ"
                        
                        vowel = RomanizationData.vowels[syllable["vowel"]][system_index]

                        if len(p["nn"]) > 0 and p["nn"].get(next_index + 1, False) and system_index in [0, 1, 3, 5]:
                            next_syllable["initial"] = "ᄂ"
                        
                        if len(p["com"]) > 0 and p["com"].get(index + 1, False) and system_index in [0, 5]:
                            next_syllable["initial"] = WiktionaryRomanization.com_ph.get(next_syllable.get("initial", ""), next_syllable.get("initial", ""))

                        if len(p["ni"]) > 0 and p["ni"].get(next_index + 1, False) and system_index != 2:
                            next_syllable["initial"] = "ᄅ" if system_index == 4 and syllable.get("final", "") == "ᆯ" else "ᄂ"

                        if system_index in [0, 1, 3, 5]:
                            if batchim_reduce and int(batchim_reduce) == index + 1:
                                syllable["final"] = RomanizationData.boundary.get(syllable["final"] + "-Ø", [""])[0]

                            if index != -1 and this_syllable_text == "밟" and next_syllable["initial"] not in "ᄋᄒ":
                                syllable["final"] = "ᆸ"

                            if next_syllable_text == "없":
                                if syllable["final"] in "ᆩᆪᆰᆿ":
                                    syllable["final"] = "ᆨ"
                                elif syllable["final"] in "ᆬᆭ":
                                    syllable["final"] = "ᆫ"
                                elif syllable["final"] in "ᆺᆻᆽᆾᇀ":
                                    syllable["final"] = "ᆮ"
                                elif syllable["final"] in "ᆲᆳᆴᆶ":
                                    syllable["final"] = "ᆯ"
                                elif syllable["final"] == "ᆱ":
                                    syllable["final"] = "ᆷ"
                                elif syllable["final"] in "ᆵᆹᇁ":
                                    syllable["final"] = "ᆸ"

                            if not batchim_reduce or int(batchim_reduce) - 1 != index:
                                if syllable["final"] + next_syllable["initial"] in ["ᇀᄋ"]:
                                    if next_syllable["vowel"] == "ᅵ":
                                        syllable["final"] = "ᆾ"
                                    elif next_syllable["vowel"] == "ᅧ":
                                        syllable["final"] = "ᆾ"
                                        next_syllable["vowel"] = "ᅥ"
                                elif syllable["final"] + next_syllable["initial"] in ["ᆴᄋ"]:
                                    if next_syllable["vowel"] == "ᅵ":
                                        syllable["final"] = "ᆯ"
                                        next_syllable["initial"] = "ᄎ"
                                    elif next_syllable["vowel"] == "ᅧ":
                                        syllable["final"] = "ᆯ"
                                        next_syllable["initial"] = "ᄎ"
                                        next_syllable["vowel"] = "ᅥ"
                                elif syllable["final"] + next_syllable["initial"] in ["ᆮᄋ"] and (not s_variation or int(s_variation) - 1 != index):
                                    if next_syllable["vowel"] == "ᅵ":
                                        syllable["final"] = "ᆽ"
                                    elif next_syllable["vowel"] == "ᅧ":
                                        syllable["final"] = "ᆽ"
                                        next_syllable["vowel"] = "ᅥ"
                                elif syllable["final"] + next_syllable["initial"] in ["ᆮᄒ"]:
                                    if next_syllable["vowel"] == "ᅵ":
                                        syllable["final"] = "ᆾ"
                                        next_syllable["initial"] = "ᄋ"
                                    elif next_syllable["vowel"] == "ᅧ":
                                        syllable["final"] = "ᆾ"
                                        next_syllable["initial"] = "ᄋ"
                                        next_syllable["vowel"] = "ᅥ"
                                elif re.search(r"[ᆬᆽᆾ][ᄋᄒ]ᅧ", syllable["final"] + next_syllable["initial"] + next_syllable["vowel"]) :
                                    next_syllable["vowel"] = "ᅥ"
                            if syllable["final"] + next_syllable["initial"] == "ᆺᄋ" and next_syllable_text not in "아았어었에으은을음읍의이인일임입있":
                                syllable["final"] = "ᆮ"

                        bound = syllable["final"] + "-" + next_syllable["initial"]
                        if bound not in RomanizationData.boundary:
                            print(f"No boundary data for {bound}.")
                            return None
                        junction = RomanizationData.boundary[bound][system_index]

                        if system_index == 1:
                            pos_format_start = index + formatting_insert_count + 1
                            pos_format_end = pos_format_start
                            while pos_format_end in formatting_position:
                                pos_format_end += 1
                                formatting_insert_count += 1
                            if pos_format_end > pos_format_start:
                                a, b = re.match(r"^(ng%-?)(.?)$", junction) or re.match(r"^(.?%-?)(.*)$", junction)
                                junction = ("".join([formatting_position.get(pos, "") for pos in range(pos_format_start, pos_format_end)]) + (a or "") + (b or "")) if re.match(r"^Ø?[ᄀ-ᄒ]$", syllable["final"] + next_syllable["initial"]) else ((a or "") + "".join([formatting_position.get(pos, "") for pos in range(pos_format_start, pos_format_end)]) + (b or ""))

                        if len(p["l"]) > 0 and (p["l"].get(index, False) or (p["l"].get("y", False) and index == 0)):
                            # FIXME, verify this code still works with final/initial cons changes
                            if system_index == 0:
                                if len(junction) == 0:
                                    junction += "ː"
                                else:
                                    junction = re.sub(r"^(.)(.?)$", lambda m: (m.group(1) + "ː" + m.group(2)) if re.match(r"[ᆨ-ᇂ]", m.group(1)) else ("ː" + m.group(1) + m.group(2)), junction)
                            elif system_index == 4:
                                vowel = re.sub(r"([aeiou])", r"\1̄", vowel)

                            elif system_index == 5:
                                vowel += "ː"
                                if index == 0:
                                    categories.append("Korean terms with long vowels in the first syllable")

                        if len(p["l"]) > 0 and (p["l"].get("y", "") or p["l"].get("1", "")) and index == -1 and system_index == 5 and len(decomposed_syllables) > 1:
                            vowel += "ˈ"

                        if len(p["com"]) > 0 and p["com"].get(index + 1, False):
                            junction = re.sub(r"(.)$", lambda m: (("q" if system_index == 4 else "") + (WiktionaryRomanization.com_mc.get(m.group(1), m.group(1)) if system_index == 3 else m.group(1))), junction)

                        if len(p["ni"]) > 0 and p.get("ni", {}).get(next_index, False) and system_index == 4:
                            junction = re.sub(r"([nl])$", r"<sup>\1</sup>", junction)

                        final_cons, initial_cons = re.match(r"^(.*);(.*)$", junction).groups() if ";" in junction else (junction, "")
                        # if not final_cons:
                        #     if system_index == 1 and index != -1:
                        #         # Modification - this would always throw an exception because the initial boundary is always of the form ";x"
                        #         # where x is a letter
                        #         raise Exception("Need a semicolon in the boundary value for " + bound)     
                        #     final_cons = junction
                        #     initial_cons = ""
                        
                        if system_index == 1:
                            romanization.append(vowel + final_cons + ("-" if saw_hyphen_after else "") + initial_cons)
                        else:
                            romanization.append(vowel + junction)
                
                temp_romanization = "".join(romanization)
                if system_index == 0:
                    # Modification - Don't want to put html in the string
                    # temp_romanization = WiktionaryRomanization.tidy_phonetic(primitive_word, unicodedata.normalize('NFC', temp_romanization))
                    temp_romanization = unicodedata.normalize('NFC', temp_romanization)
                elif system_index in [1, 2]:
                    # Modification - I couldn't figure out why the semi-colon is removed for the wiki version but it remains
                    # in this version, so I strip it here
                    temp_romanization = temp_romanization.strip(";")
                    for _ in range(2):
                        temp_romanization = re.sub(r"(.)…(.)", lambda m: m.group(1) + ("'" if WiktionaryRomanization.ambiguous_intersyllabic_rr.get(m.group(1) + m.group(2)) else "") + m.group(2), temp_romanization)
                        temp_romanization = re.sub(r"wo'e", "woe", temp_romanization)
                        temp_romanization = re.sub(r"yo'e", "yoe", temp_romanization)
                        temp_romanization = re.sub(r"we'o", "weo", temp_romanization)
                        temp_romanization = re.sub(r"we'u", "weu", temp_romanization)
                        temp_romanization = re.sub(r"ye'u", "yeu", temp_romanization)
                        temp_romanization = re.sub(r"yu'i", "yui", temp_romanization)
                elif system_index == 3:
                    for _ in range(2):
                        temp_romanization = re.sub(r"(.)…(.)", lambda m: m.group(1) + ("'" if WiktionaryRomanization.ambiguous_intersyllabic_mr.get(m.group(1) + m.group(2)) else "") + m.group(2), temp_romanization)
                        temp_romanization = re.sub(r"yo'e", "yoe", temp_romanization)
                        temp_romanization = re.sub(r"a'e", "aë", temp_romanization)
                        temp_romanization = re.sub(r"o'e", "oë", temp_romanization)
                        temp_romanization = re.sub(r"n'k", "nk", temp_romanization)
                        temp_romanization = re.sub(r"swi", "shwi", temp_romanization)
                elif system_index == 4:
                    for _ in range(2):
                        temp_romanization = re.sub(r"(.)…(.)", lambda m: m.group(1) + ("." if WiktionaryRomanization.ambiguous_intersyllabic_yr.get(m.group(1) + m.group(2)) else "") + m.group(2), temp_romanization)
                        temp_romanization = re.sub(r"\.q", "q", temp_romanization)
                elif system_index == 5:
                    temp_romanization = "[" + temp_romanization + "]"

                if system_index in [0, 5]:
                    temp_romanization = re.sub(r"ː", "(ː)", temp_romanization)

                if p["cap"].get("y") and system_index in [1, 2, 3]:
                    temp_romanization = temp_romanization[0].upper() + temp_romanization[1:]

                temp_romanization = unicodedata.normalize('NFC', temp_romanization)
                word_set_romanizations.append(temp_romanization)

            text_param = re.sub(re.escape(the_original), WiktionaryRomanization.system_list[system_index]["separator"].join(word_set_romanizations), text_param, count=1)

        if system_index == 5:
            text_param = WiktionaryRomanization.tidy_ipa(text_param)

        # This part is definitely not needed for this use case of romanization
        # if categories:
        #     text_param += require("Module:utilities").format_categories(categories, m_ko_utilities.lang)

        return text_param

    def make(self):
        params = {
            1: {"default": self.title, "list": True},
            "a": {},
            "audio": {"alias_of": "a"},
            "nn": {},
            "l": {},
            "com": {},
            "cap": {},
            "ui": {},
            "uie": {},
            "nobc": {},
            "ni": {},
            "bcred": {},
            "svar": {},
            "iot": {},
        }

        args = self.process_params(self.input_string, params)

        current_word_dataset = []
        for system_index in WiktionaryRomanization.system_lookup.values():
            romanized = WiktionaryRomanization.romanize(system_index, args)
            current_word_dataset.append(romanized)

        return current_word_dataset

    def romanize_one(self, system_name):
        params = {
            1: self.title,
            "a": {},
            "audio": {"alias_of": "a"},
            "nn": {},
            "l": {},
            "com": {},
            "cap": {},
            "ui": {},
            "uie": {},
            "nobc": {},
            "ni": {},
            "bcred": {},
            "svar": {},
            "iot": {},
        }
        args = self.process_params(params)
        return WiktionaryRomanization.romanize(self.system_lookup[system_name], args)

    def process_params(self, params):
        pattern = r'\{\{\s*ko-ipa\s*(.*?)\s*\}\}'
        matches = re.findall(pattern, self.input_string, re.IGNORECASE)

        if matches:
            parameters_string = matches[0]
            parameters_list = parameters_string.split('|')

            for param in parameters_list:
                if '=' in param:
                    key, value = param.split('=')
                    params[key.strip()] = value.strip()
                elif param:
                    # parameter is the string to romanize
                    params[1] = param
                # TODO: make taking a different string to romanize as a parameter work
        
        return params