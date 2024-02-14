import re

def parse_korean_text(input_text):
    # Regular expressions to extract information
    title_pattern = r"^(.*?)\s*(?:\([^)]*\))?\s*\n"
    ko_ipa_pattern = r"({{ko-ipa.*?}})\s*\n"
    phonetic_hangul_pattern  = r"Phonetic hangul:\s*\[([^]]+)\]"
    rom_pattern = r"Romanizations\s*Revised Romanization\?([^\n]+)\n\s*Revised Romanization \(translit\.\)\?([^\n]+)\n\s*McCune–Reischauer\?([^\n]+)\n\s*Yale Romanization\?([^\n]+)"
    ipa_pattern = r"IPA\(key\):\s*(\[.*\]\n)"

    # Extracting information using regular expressions
    title_match = re.search(title_pattern, input_text)
    ko_ipa_match = re.search(ko_ipa_pattern, input_text, re.IGNORECASE)
    phonetic_hangul_match  = re.search(phonetic_hangul_pattern, input_text)
    rom_match = re.search(rom_pattern, input_text)
    ipa_match = re.search(ipa_pattern, input_text)

    if not (title_match and ko_ipa_match and phonetic_hangul_match and rom_match and ipa_match):
        return None  # Return None if any required information is missing

    # Extracted information
    title = title_match.group(1).strip()
    ko_ipa = ko_ipa_match.group(1).strip()
    phonetic_hangul = phonetic_hangul_match.group(1).strip()
    revised_rom = rom_match.group(1).strip()
    revised_rom_translit = rom_match.group(2).strip()
    mccune_reischauer = rom_match.group(3).strip()
    yale_rom = rom_match.group(4).strip()
    ipa_key = ipa_match.group(1).strip()

    result_string = ""
    for name, expected in zip(["ph", "rr", "rrr", "mr", "yr", "ipa"], [phonetic_hangul, revised_rom, revised_rom_translit, mccune_reischauer, yale_rom, ipa_key]):
        result_string += f'''def test_{revised_rom.replace(' ', '_').replace("'", "").replace("/", "_")}_{name}(self):\n\tself.run_test("{title}", "{ko_ipa}", "{expected}", "{name}")\n'''
    return result_string

print(parse_korean_text('''법률학 (法律學, beomnyulhak)

{{ko-IPA}}

    (SK Standard/Seoul) IPA(key): [pʌ̹mɲuɾɦa̠k̚]
    Phonetic hangul: [범뉼학]

Romanizations
Revised Romanization?	beomnyulhak
Revised Romanization (translit.)?	beoblyulhag
McCune–Reischauer?	pŏmnyurhak
Yale Romanization?	peplyul.hak'''))

print(parse_korean_text('''편찮다 (pyeonchanta)

{{ko-IPA}}

    (SK Standard/Seoul) IPA(key): [pʰjʌ̹ɲt͡ɕʰa̠ntʰa̠]
    Phonetic hangul: [편찬타]

Romanizations
Revised Romanization?	pyeonchanta
Revised Romanization (translit.)?	pyeonchanhda
McCune–Reischauer?	p'yŏnch'ant'a
Yale Romanization?	phyen.chanhta'''))

print(parse_korean_text('''음식값 (飮食—, eumsikgap)

{{ko-IPA|l=y}}

    (SK Standard/Seoul) IPA(key): [ˈɯ(ː)mɕʰik̚k͈a̠p̚]
    Phonetic hangul: [음(ː)식깝]
        Though still prescribed in Standard Korean, most speakers in both Koreas no longer distinguish vowel length.

Romanizations
Revised Romanization?	eumsikgap
Revised Romanization (translit.)?	eumsiggabs
McCune–Reischauer?	ŭmsikkap
Yale Romanization?	ūmsik.kaps'''))

print(parse_korean_text('''어떻게 (eotteoke)

{{ko-IPA}}

    (SK Standard/Seoul) IPA(key): [ʌ̹t͈ʌ̹kʰe̞]
    Phonetic hangul: [어떠케]

Romanizations
Revised Romanization?	eotteoke
Revised Romanization (translit.)?	eo'tteohge
McCune–Reischauer?	ŏttŏk'e
Yale Romanization?	e.ttehkey'''))
print(parse_korean_text('''몇몇 (myeonmyeot)

{{ko-IPA}}

    (SK Standard/Seoul) IPA(key): [mjʌ̹nmjʌ̹t̚]
    Phonetic hangul: [면멷]

Romanizations
Revised Romanization?	myeonmyeot
Revised Romanization (translit.)?	myeochmyeoch
McCune–Reischauer?	myŏnmyŏt
Yale Romanization?	myechmyech'''))
print(parse_korean_text('''뜻밖에 (tteutbakke)

{{ko-IPA}}

    (SK Standard/Seoul) IPA(key): [t͈ɯt̚p͈a̠k͈e̞]
    Phonetic hangul: [뜯빠께]

Romanizations
Revised Romanization?	tteutbakke
Revised Romanization (translit.)?	tteusbakk'e
McCune–Reischauer?	ttŭtpakke
Yale Romanization?	ttuspakk.ey'''))
print(parse_korean_text('''끊임없다 (kkeunimeopda)

{{ko-IPA}}

    (SK Standard/Seoul) IPA(key): [k͈ɯnimʌ̹p̚t͈a̠]
    Phonetic hangul: [끄니멉따]

Romanizations
Revised Romanization?	kkeunimeopda
Revised Romanization (translit.)?	kkeunh'im'eobsda
McCune–Reischauer?	kkŭnimŏpta
Yale Romanization?	kkunh.im.epsta'''))
print(parse_korean_text('''낯설다 (natseolda)

{{ko-IPA}}

    (SK Standard/Seoul) IPA(key): [na̠ss͈ʌ̹ɭda̠]
    Phonetic hangul: [낟썰다]

Romanizations
Revised Romanization?	natseolda
Revised Romanization (translit.)?	nachseolda
McCune–Reischauer?	nassŏlda
Yale Romanization?	nachselta'''))
print(parse_korean_text('''공산주의 (共産主義, gongsanjuui)

{{ko-IPA|l=y|ui=4}}

    (SK Standard/Seoul) IPA(key): [ˈko̞(ː)ŋsʰa̠ɲd͡ʑuɰi] ~ [ˈko̞(ː)ŋsʰa̠ɲd͡ʑui]
    Phonetic hangul: [공(ː)산주의/공(ː)산주이]
        Though still prescribed in Standard Korean, most speakers in both Koreas no longer distinguish vowel length.

Romanizations
Revised Romanization?	gongsanjuui
Revised Romanization (translit.)?	gongsanjuui
McCune–Reischauer?	kongsanjuŭi
Yale Romanization?	kōngsan.cwuuy'''))
print(parse_korean_text('''고춧가루 (gochutgaru)

{{ko-IPA|nobc=2}}

    (SK Standard/Seoul) IPA(key): [ko̞t͡ɕʰut̚k͈a̠ɾu] ~ [ko̞t͡ɕʰuk͈a̠ɾu]
    Phonetic hangul: [고춛까루/고추까루]

Romanizations
Revised Romanization?	gochutgaru
Revised Romanization (translit.)?	gochusgalu
McCune–Reischauer?	koch'utkaru
Yale Romanization?	ko.chwuskalwu'''))
print(parse_korean_text('''합법화되다 (合法化—, hapbeophwadoeda)

{{ko-IPA}}

    (SK Standard/Seoul) IPA(key): [ha̠p̚p͈ʌ̹pʰwa̠dwe̞da̠] ~ [ha̠p̚p͈ʌ̹pʰwa̠dø̞da̠]
    Phonetic hangul: [합뻐퐈뒈다/합뻐퐈되다]

Romanizations
Revised Romanization?	hapbeophwadoeda
Revised Romanization (translit.)?	habbeobhwadoeda
McCune–Reischauer?	happŏphwadoeda
Yale Romanization?	hap.pep.hwatoyta'''))
print(parse_korean_text('''몫몫이 (mongmoksi)

{{ko-IPA}}

    (SK Standard/Seoul) IPA(key): [mo̞ŋmo̞kɕ͈i]
    Phonetic hangul: [몽목씨]

Romanizations
Revised Romanization?	mongmoksi
Revised Romanization (translit.)?	mogsmogs'i
McCune–Reischauer?	mongmoksi
Yale Romanization?	moksmoks.i'''))
print(parse_korean_text('''굵다랗다 (gukdarata)

{{ko-IPA|l=y}}

    (SK Standard/Seoul) IPA(key): [ˈku(ː)k̚t͈a̠ɾa̠tʰa̠]
    Phonetic hangul: [국(ː)따라타]
        Though still prescribed in Standard Korean, most speakers in both Koreas no longer distinguish vowel length.

Romanizations
Revised Romanization?	gukdarata
Revised Romanization (translit.)?	gulgdalahda
McCune–Reischauer?	kuktarat'a
Yale Romanization?	kwūlktalahta'''))
print(parse_korean_text('''새해 복 많이 받으세요 (saehae bok mani badeuseyo)

{{ko-IPA|새해 복많이 받으세요|새해 복 많이 받으세요}}

    (SK Standard/Seoul) IPA(key): [sʰɛɦɛ po̞ŋma̠ni pa̠dɯsʰe̞jo] ~ [sʰe̞ɦe̞ po̞ŋma̠ni pa̠dɯsʰe̞jo] ~ [sʰɛɦɛ po̞k̚ ma̠ni pa̠dɯsʰe̞jo] ~ [sʰe̞ɦe̞ po̞k̚ ma̠ni pa̠dɯsʰe̞jo]
    Phonetic hangul: [새해 봉마니 바드세요/세헤 봉마니 바드세요/새해 복 마니 바드세요/세헤 복 마니 바드세요]

Romanizations
Revised Romanization?	saehae bongmani badeuseyo/saehae bok mani badeuseyo
Revised Romanization (translit.)?	saehae bogmanh'i bad'euseyo/saehae bog manh'i bad'euseyo
McCune–Reischauer?	saehae pongmani padŭseyo/saehae pok mani padŭseyo
Yale Romanization?	sayhay pokmanh.i pat.useyyo/sayhay pok manh.i pat.useyyo'''))
print(parse_korean_text('''한국 (韓國, han'guk)

{{ko-IPA|l=y|cap=y}}

    (SK Standard/Seoul) IPA(key): [ˈha̠(ː)nɡuk̚]
    Phonetic hangul: [한(ː)국]
        Though still prescribed in Standard Korean, most speakers in both Koreas no longer distinguish vowel length.

Romanizations
Revised Romanization?	Han'guk
Revised Romanization (translit.)?	Hangug
McCune–Reischauer?	Han'guk
Yale Romanization?	hānkwuk'''))
print(parse_korean_text('''상사병 (相思病, sangsabyeong)

{{ko-IPA|com=2}}

    (SK Standard/Seoul) IPA(key): [sʰa̠ŋsʰa̠p͈jʌ̹ŋ]
    Phonetic hangul: [상사뼝]

Romanizations
Revised Romanization?	sangsabyeong
Revised Romanization (translit.)?	sangsabyeong
McCune–Reischauer?	sangsapyŏng
Yale Romanization?	sangsaqpyeng'''))
print(parse_korean_text('''서클 (seokeul)

{{ko-IPA|com=0}}

    (SK Standard/Seoul) IPA(key): [s͈ʌ̹kxɯɭ]
    Phonetic hangul: [써클]

Romanizations
Revised Romanization?	seokeul
Revised Romanization (translit.)?	seokeul
McCune–Reischauer?	ssŏk'ŭl
Yale Romanization?	qse.khul'''))
print(parse_korean_text('''의견란 (意見欄, uigyeollan)

{{ko-IPA|nn=3|l=y}}

    (SK Standard/Seoul) IPA(key): [ˈɰi(ː)ɡjʌ̹nna̠n]
    Phonetic hangul: [의(ː)견난]
        Though still prescribed in Standard Korean, most speakers in both Koreas no longer distinguish vowel length.

Romanizations
Revised Romanization?	uigyeonnan
Revised Romanization (translit.)?	uigyeonlan
McCune–Reischauer?	ŭigyŏnnan
Yale Romanization?	ūykyenlan'''))
print(parse_korean_text('''의 (ui)

{{ko-IPA|uie=1}}

    (SK Standard/Seoul) IPA(key): [ɰi] ~ [e̞]
    Phonetic hangul: [의/에]

Romanizations
Revised Romanization?	ui
Revised Romanization (translit.)?	ui
McCune–Reischauer?	ŭi
Yale Romanization?	uy'''))
print(parse_korean_text('''깻잎 (kkaedip)

{{ko-IPA|ni=2}}

    (SK Standard/Seoul) IPA(key): [k͈ɛnnip̚] ~ [k͈e̞nnip̚]
    Phonetic hangul: [깬닙/껜닙]

Romanizations
Revised Romanization?	kkaennip
Revised Romanization (translit.)?	kkaes'ip
McCune–Reischauer?	kkaennip
Yale Romanization?	kkaysniph'''))
print(parse_korean_text('''값어치 (gapseochi)

{{ko-IPA|bcred=1}}

    (SK Standard/Seoul) IPA(key): [ka̠bʌ̹t͡ɕʰi]
    Phonetic hangul: [가버치]

Romanizations
Revised Romanization?	gabeochi
Revised Romanization (translit.)?	gabs'eochi
McCune–Reischauer?	kabŏch'i
Yale Romanization?	kaps.e.chi'''))
print(parse_korean_text('''맞흥정 (macheungjeong)

{{ko-IPA|bcred=1}}

    (SK Standard/Seoul) IPA(key): [ma̠tʰɯŋd͡ʑʌ̹ŋ]
    Phonetic hangul: [마틍정]

Romanizations
Revised Romanization?	matheungjeong
Revised Romanization (translit.)?	majheungjeong
McCune–Reischauer?	mathŭngjŏng
Yale Romanization?	mac.hungceng'''))
print(parse_korean_text('''곧이어 (gojieo)

{{ko-IPA|bcred=1}}

    (SK Standard/Seoul) IPA(key): [ko̞diʌ̹]
    Phonetic hangul: [고디어]

Romanizations
Revised Romanization?	godieo
Revised Romanization (translit.)?	god'ieo
McCune–Reischauer?	kodiŏ
Yale Romanization?	kot.ie'''))
print(parse_korean_text('''멋있다 (meositda)

{{ko-IPA|svar=1}}

    (SK Standard/Seoul) IPA(key): [mʌ̹ɕʰit̚t͈a̠] ~ [mʌ̹dit̚t͈a̠]
    Phonetic hangul: [머싣따/머딛따]

Romanizations
Revised Romanization?	meositda
Revised Romanization (translit.)?	meos'issda
McCune–Reischauer?	mŏsitta
Yale Romanization?	mes.issta'''))
print(parse_korean_text('''뛰어들다 (ttwieodeulda)

{{ko-IPA|iot=2}}

    (SK Standard/Seoul) IPA(key): [t͈ɥiʌ̹dɯɭda̠] ~ [t͈ɥijʌ̹dɯɭda̠] ~ [t͈yʌ̹dɯɭda̠] ~ [t͈yjʌ̹dɯɭda̠]
    Phonetic hangul: [뛰어들다/뛰여들다]

Romanizations
Revised Romanization?	ttwieodeulda
Revised Romanization (translit.)?	ttwieodeulda
McCune–Reischauer?	ttwiŏdŭlda
Yale Romanization?	ttwietulta'''))
print(parse_korean_text('''계속 (繼續, gyesok)

{{ko-IPA|l=y}}

    (SK Standard/Seoul) IPA(key): [ˈkje̞(ː)sʰo̞k̚] ~ [ˈke̞(ː)sʰo̞k̚]
    Phonetic hangul: [계(ː)속/게(ː)속]
        Though still prescribed in Standard Korean, most speakers in both Koreas no longer distinguish vowel length.

Romanizations
Revised Romanization?	gyesok
Revised Romanization (translit.)?	gyesog
McCune–Reischauer?	kyesok
Yale Romanization?	kyēysok'''))
print(parse_korean_text('''계속되다 (繼續—, gyesokdoeda)

{{ko-IPA|l=y}}

    (SK Standard/Seoul) IPA(key): [ˈkje̞(ː)sʰo̞k̚t͈we̞da̠] ~ [ˈkje̞(ː)sʰo̞k̚t͈ø̞da̠] ~ [ˈke̞(ː)sʰo̞k̚t͈we̞da̠] ~ [ˈke̞(ː)sʰo̞k̚t͈ø̞da̠]
    Phonetic hangul: [계(ː)속뛔다/계(ː)속뙤다/게(ː)속뛔다/게(ː)속뙤다]
        Though still prescribed in Standard Korean, most speakers in both Koreas no longer distinguish vowel length.

Romanizations
Revised Romanization?	gyesokdoeda
Revised Romanization (translit.)?	gyesogdoeda
McCune–Reischauer?	kyesoktoeda
Yale Romanization?	kyēysoktoyta'''))
print(parse_korean_text('''세 명 (se myeong)

{{ko-IPA|l=y}}

    (SK Standard/Seoul) IPA(key): [ˈsʰe̞(ː) mjʌ̹ŋ]
    Phonetic hangul: [세(ː)(ː)(ː)]
        Though still prescribed in Standard Korean, most speakers in both Koreas no longer distinguish vowel length.

Romanizations
Revised Romanization?	se myeong
Revised Romanization (translit.)?	se myeong
McCune–Reischauer?	se myŏng
Yale Romanization?	sēy myeng'''))
