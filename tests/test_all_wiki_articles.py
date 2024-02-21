import inspect
import unittest
from src.wiktionary_romanization import WiktionaryRomanization

class TestAllWikiArticles(unittest.TestCase):
	file = ''

	def set_file(self, file):
		self.file = file

	def test_wikibaekgwa_ipa(self):
		return self.run_test("위키백과", "{{ko-IPA|a=Ko-위키백과.oga}}", "[ɥicçibɛk̚k͈wa̠] ~ [ɥicçibe̞k̚k͈wa̠] ~ [ycçibɛk̚k͈wa̠] ~ [ycçibe̞k̚k͈wa̠]", "ipa")
	def test_daeryukbatjwi_ipa(self):
		return self.run_test("대륙밭쥐", "{{ko-IPA|l=y}}", "[ˈtɛ(ː)ɾjuk̚p͈a̠t̚t͡ɕ͈ɥi] ~ [ˈte̞(ː)ɾjuk̚p͈a̠t̚t͡ɕ͈ɥi] ~ [ˈtɛ(ː)ɾjuk̚p͈a̠t̚t͡ɕ͈y] ~ [ˈte̞(ː)ɾjuk̚p͈a̠t̚t͡ɕ͈y]", "ipa")
	def test_saengjwi_ipa(self):
		return self.run_test("생쥐", "{{ko-IPA|l=y}}", "[ˈsʰɛ(ː)ŋd͡ʑɥi] ~ [ˈsʰe̞(ː)ŋd͡ʑɥi] ~ [ˈsʰɛ(ː)ŋd͡ʑy] ~ [ˈsʰe̞(ː)ŋd͡ʑy]", "ipa")
	def test_soegalbatjwi_ipa(self):
		return self.run_test("쇠갈밭쥐", "{{ko-IPA}}", "[sʰwe̞ɡa̠ɭba̠t̚t͡ɕ͈ɥi] ~ [sʰø̞ɡa̠ɭba̠t̚t͡ɕ͈ɥi] ~ [sʰwe̞ɡa̠ɭba̠t̚t͡ɕ͈y] ~ [sʰø̞ɡa̠ɭba̠t̚t͡ɕ͈y]", "ipa")
	def test_anjuaegibakjwi_ipa(self):
		return self.run_test("안주애기박쥐", "{{ko-IPA}}", "[a̠ɲd͡ʑuɛɡiba̠k̚t͡ɕ͈ɥi] ~ [a̠ɲd͡ʑue̞ɡiba̠k̚t͡ɕ͈ɥi] ~ [a̠ɲd͡ʑuɛɡiba̠k̚t͡ɕ͈y] ~ [a̠ɲd͡ʑue̞ɡiba̠k̚t͡ɕ͈y]", "ipa")
	def test_aegibakjwi_ipa(self):
		return self.run_test("애기박쥐", "{{ko-IPA}}", "[ɛɡiba̠k̚t͡ɕ͈ɥi] ~ [e̞ɡiba̠k̚t͡ɕ͈ɥi] ~ [ɛɡiba̠k̚t͡ɕ͈y] ~ [e̞ɡiba̠k̚t͡ɕ͈y]", "ipa")
	def test_bukbangaegibakjwi_ipa(self):
		return self.run_test("북방애기박쥐", "{{ko-IPA}}", "[puk̚p͈a̠ŋɛɡiba̠k̚t͡ɕ͈ɥi] ~ [puk̚p͈a̠ŋe̞ɡiba̠k̚t͡ɕ͈ɥi] ~ [puk̚p͈a̠ŋɛɡiba̠k̚t͡ɕ͈y] ~ [puk̚p͈a̠ŋe̞ɡiba̠k̚t͡ɕ͈y]", "ipa")
	def test_huinbaewitsuyeombakjwi_ipa(self):
		return self.run_test("흰배윗수염박쥐", "{{ko-IPA}}", "[çinbɛɥiss͈ujʌ̹mba̠k̚t͡ɕ͈ɥi] ~ [çinbe̞ɥiss͈ujʌ̹mba̠k̚t͡ɕ͈ɥi] ~ [çinbɛyss͈ujʌ̹mba̠k̚t͡ɕ͈y] ~ [çinbe̞yss͈ujʌ̹mba̠k̚t͡ɕ͈y]", "ipa")
	def test_saengbakjwi_ipa(self):
		return self.run_test("생박쥐", "{{ko-IPA}}", "[sʰɛŋba̠k̚t͡ɕ͈ɥi] ~ [sʰe̞ŋba̠k̚t͡ɕ͈ɥi] ~ [sʰɛŋba̠k̚t͡ɕ͈y] ~ [sʰe̞ŋba̠k̚t͡ɕ͈y]", "ipa")
	def test_ginnalgaebakjwi_ipa(self):
		return self.run_test("긴날개박쥐", "{{ko-IPA}}", "[kinna̠ɭɡɛba̠k̚t͡ɕ͈ɥi] ~ [kinna̠ɭɡe̞ba̠k̚t͡ɕ͈ɥi] ~ [kinna̠ɭɡɛba̠k̚t͡ɕ͈y] ~ [kinna̠ɭɡe̞ba̠k̚t͡ɕ͈y]", "ipa")
	def test_soedwijwi_ipa(self):
		return self.run_test("쇠뒤쥐", "{{ko-IPA}}", "[sʰwe̞dɥid͡ʑɥi] ~ [sʰø̞dɥid͡ʑɥi] ~ [sʰwe̞dyd͡ʑy] ~ [sʰø̞dyd͡ʑy]", "ipa")
	def test_baekdusandwijwi_ipa(self):
		return self.run_test("백두산뒤쥐", "{{ko-IPA}}", "[pɛk̚t͈usʰa̠ndɥid͡ʑɥi] ~ [pe̞k̚t͈usʰa̠ndɥid͡ʑɥi] ~ [pɛk̚t͈usʰa̠ndyd͡ʑy] ~ [pe̞k̚t͈usʰa̠ndyd͡ʑy]", "ipa")
	def test_wiwonhoe_ipa(self):
		return self.run_test("위원회", "{{ko-IPA}}", "[ɥiwʌ̹nβwe̞] ~ [ɥiwʌ̹nɦø̞] ~ [ywʌ̹nβwe̞] ~ [ywʌ̹nɦø̞]", "ipa")
	def test_waemaechi_ph(self):
		return self.run_test("왜매치", "{{ko-IPA}}", "왜매치/왜메치/웨매치/웨메치", "ph")
	def test_waemaechi_ipa(self):
		return self.run_test("왜매치", "{{ko-IPA}}", "[wɛmɛt͡ɕʰi] ~ [wɛme̞t͡ɕʰi] ~ [we̞mɛt͡ɕʰi] ~ [we̞me̞t͡ɕʰi]", "ipa")
	def test_waemolgae_ph(self):
		return self.run_test("왜몰개", "{{ko-IPA}}", "왜몰개/왜몰게/웨몰개/웨몰게", "ph")
	def test_waemolgae_ipa(self):
		return self.run_test("왜몰개", "{{ko-IPA}}", "[wɛmo̞ɭɡɛ] ~ [wɛmo̞ɭɡe̞] ~ [we̞mo̞ɭɡɛ] ~ [we̞mo̞ɭɡe̞]", "ipa")
	def test_haengwi_ipa(self):
		return self.run_test("행위", "{{ko-IPA}}", "[hɛŋɥi] ~ [he̞ŋɥi] ~ [hɛŋy] ~ [he̞ŋy]", "ipa")
	def test_gwichaeksayu_ipa(self):
		return self.run_test("귀책사유", "{{ko-IPA|l=y}}", "[ˈkɥi(ː)t͡ɕʰɛks͈a̠ju] ~ [ˈkɥi(ː)t͡ɕʰe̞ks͈a̠ju] ~ [ˈky(ː)t͡ɕʰɛks͈a̠ju] ~ [ˈky(ː)t͡ɕʰe̞ks͈a̠ju]", "ipa")
	def test_widaehada_ipa(self):
		return self.run_test("위대하다", "{{ko-IPA}}", "[ɥidɛɦa̠da̠] ~ [ɥide̞ɦa̠da̠] ~ [ydɛɦa̠da̠] ~ [yde̞ɦa̠da̠]", "ipa")
	def test_gwittaegi_ipa(self):
		return self.run_test("귀때기", "{{ko-IPA}}", "[kɥit͈ɛɡi] ~ [kɥit͈e̞ɡi] ~ [kyt͈ɛɡi] ~ [kyt͈e̞ɡi]", "ipa")
	def test_gwissadaegi_ipa(self):
		return self.run_test("귀싸대기", "{{ko-IPA}}", "[kɥis͈a̠dɛɡi] ~ [kɥis͈a̠de̞ɡi] ~ [kys͈a̠dɛɡi] ~ [kys͈a̠de̞ɡi]", "ipa")
	def test_soe_ipa(self):
		return self.run_test("쇠-", "{{ko-IPA|l=y}}", "[sʰwe̞(ː)] ~ [sʰø̞(ː)]", "ipa")
	def test_saendeuwichi_ipa(self):
		return self.run_test("샌드위치", "{{ko-IPA}}", "[sʰɛndɯɥit͡ɕʰi] ~ [sʰe̞ndɯɥit͡ɕʰi] ~ [sʰɛndɯyt͡ɕʰi] ~ [sʰe̞ndɯyt͡ɕʰi]", "ipa")
	def test_bammareun_jwiga_deutgo_nanmareun_saega_deunneunda_ipa(self):
		return self.run_test("밤말은 쥐가 듣고 낮말은 새가 듣는다", "{{ko-IPA}}", "[pa̠mma̠ɾɯn t͡ɕɥiɡa̠ tɯt̚k͈o̞ na̠nma̠ɾɯn sʰɛɡa̠ tɯnnɯnda̠] ~ [pa̠mma̠ɾɯn t͡ɕɥiɡa̠ tɯt̚k͈o̞ na̠nma̠ɾɯn sʰe̞ɡa̠ tɯnnɯnda̠] ~ [pa̠mma̠ɾɯn t͡ɕyɡa̠ tɯt̚k͈o̞ na̠nma̠ɾɯn sʰɛɡa̠ tɯnnɯnda̠] ~ [pa̠mma̠ɾɯn t͡ɕyɡa̠ tɯt̚k͈o̞ na̠nma̠ɾɯn sʰe̞ɡa̠ tɯnnɯnda̠]", "ipa")
	def test_seonghaengwi_ipa(self):
		return self.run_test("성행위", "{{ko-IPA|l=y}}", "[ˈsʰɘ(ː)ŋɦɛŋɥi] ~ [ˈsʰɘ(ː)ŋɦe̞ŋɥi] ~ [ˈsʰɘ(ː)ŋɦɛŋy] ~ [ˈsʰɘ(ː)ŋɦe̞ŋy]", "ipa")
	def test_wisaeng_ipa(self):
		return self.run_test("위생", "{{ko-IPA}}", "[ɥisʰɛŋ] ~ [ɥisʰe̞ŋ] ~ [ysʰɛŋ] ~ [ysʰe̞ŋ]", "ipa")
	def test_lge_ph(self):
		return self.run_test("-ㄹ게", "{{ko-IPA|com=1}}", "ㄹ께", "ph")
	def test_lge_mr(self):
		return self.run_test("-ㄹ게", "{{ko-IPA|com=1}}", "lke", "mr")
	def test_lge_yr(self):
		return self.run_test("-ㄹ게", "{{ko-IPA|com=1}}", "lqkey", "yr")
	def test_lge_ipa(self):
		return self.run_test("-ㄹ게", "{{ko-IPA|com=1}}", "[ɭk͈e̞]", "ipa")
	def test_eulge_ph(self):
		return self.run_test("-을게", "{{ko-IPA|com=1}}", "을께", "ph")
	def test_eulge_mr(self):
		return self.run_test("-을게", "{{ko-IPA|com=1}}", "ŭlke", "mr")
	def test_eulge_yr(self):
		return self.run_test("-을게", "{{ko-IPA|com=1}}", "ulqkey", "yr")
	def test_eulge_ipa(self):
		return self.run_test("-을게", "{{ko-IPA|com=1}}", "[ɯɭk͈e̞]", "ipa")
	def test_eulji_ph(self):
		return self.run_test("-을지", "{{ko-IPA|com=1}}", "을찌", "ph")
	def test_eulji_mr(self):
		return self.run_test("-을지", "{{ko-IPA|com=1}}", "ŭlchi", "mr")
	def test_eulji_yr(self):
		return self.run_test("-을지", "{{ko-IPA|com=1}}", "ulqci", "yr")
	def test_eulji_ipa(self):
		return self.run_test("-을지", "{{ko-IPA|com=1}}", "[ɯʎt͡ɕ͈i]", "ipa")
	def test_keukeukeu_kâkâkâ_ph(self):
		return self.run_test("ㅋㅋㅋ", "{{ko-IPA|크크크 (kıkıkı)}}", "크크크 (kâkâkâ)", "ph")
	def test_keukeukeu_kâkâkâ_rr(self):
		return self.run_test("ㅋㅋㅋ", "{{ko-IPA|크크크 (kıkıkı)}}", "keukeukeu (kâkâkâ)", "rr")
	def test_keukeukeu_kâkâkâ_rrr(self):
		return self.run_test("ㅋㅋㅋ", "{{ko-IPA|크크크 (kıkıkı)}}", "keukeukeu (kâkâkâ)", "rrr")
	def test_keukeukeu_kâkâkâ_mr(self):
		return self.run_test("ㅋㅋㅋ", "{{ko-IPA|크크크 (kıkıkı)}}", "k'ŭk'ŭk'ŭ (kâkâkâ)", "mr")
	def test_keukeukeu_kâkâkâ_yr(self):
		return self.run_test("ㅋㅋㅋ", "{{ko-IPA|크크크 (kıkıkı)}}", "khu.khu.khu (kâkâkâ)", "yr")
	def test_keukeukeu_kâkâkâ_ipa(self):
		return self.run_test("ㅋㅋㅋ", "{{ko-IPA|크크크 (kıkıkı)}}", "[kxɯkxɯkxɯ ](kâkâkâ)", "ipa")
	def test_hubaewi_ipa(self):
		return self.run_test("후배위", "{{ko-IPA|l=y}}", "[ˈɸʷu(ː)bɛɥi] ~ [ˈɸʷu(ː)be̞ɥi] ~ [ˈɸʷu(ː)bɛy] ~ [ˈɸʷu(ː)be̞y]", "ipa")
	def test_wisaengsil_ipa(self):
		return self.run_test("위생실", "{{ko-IPA}}", "[ɥisʰɛŋɕʰiɭ] ~ [ɥisʰe̞ŋɕʰiɭ] ~ [ysʰɛŋɕʰiɭ] ~ [ysʰe̞ŋɕʰiɭ]", "ipa")
	def test_daewi_ipa(self):
		return self.run_test("대위", "{{ko-IPA|l=y}}", "[ˈtɛ(ː)ɥi] ~ [ˈte̞(ː)ɥi] ~ [ˈtɛ(ː)y] ~ [ˈte̞(ː)y]", "ipa")
	def test_widae_ipa(self):
		return self.run_test("위대", "{{ko-IPA}}", "[ɥidɛ] ~ [ɥide̞] ~ [ydɛ] ~ [yde̞]", "ipa")
	def test_hoegwi_ipa(self):
		return self.run_test("회귀", "{{ko-IPA}}", "[ɸwe̞ɡɥi] ~ [hø̞ɡɥi] ~ [ɸwe̞ɡy] ~ [hø̞ɡy]", "ipa")
	def test_gugeubwisaengcha_ipa(self):
		return self.run_test("구급위생차", "{{ko-ipa|l=y}}", "[ˈku(ː)ɡɯbɥisʰɛŋt͡ɕʰa̠] ~ [ˈku(ː)ɡɯbɥisʰe̞ŋt͡ɕʰa̠] ~ [ˈku(ː)ɡɯbysʰɛŋt͡ɕʰa̠] ~ [ˈku(ː)ɡɯbysʰe̞ŋt͡ɕʰa̠]", "ipa")
	def test_toewi_ipa(self):
		return self.run_test("퇴위", "{{ko-IPA}}", "[tʰwe̞ɥi] ~ [tʰø̞ɥi] ~ [tʰwe̞y] ~ [tʰø̞y]", "ipa")
	def test_aegeupjwi_ipa(self):
		return self.run_test("애급쥐", "{{ko-IPA}}", "[ɛɡɯp̚t͡ɕ͈ɥi] ~ [e̞ɡɯp̚t͡ɕ͈ɥi] ~ [ɛɡɯp̚t͡ɕ͈y] ~ [e̞ɡɯp̚t͡ɕ͈y]", "ipa")
	def test_gwaengechaeita_ph(self):
		return self.run_test("괜게채잏다", "{{ko-IPA}}", "괜게채이타/괜게체이타/궨게채이타/궨게체이타", "ph")
	def test_gwaengechaeita_ipa(self):
		return self.run_test("괜게채잏다", "{{ko-IPA}}", "[kwɛnɡe̞t͡ɕʰɛitʰa̠] ~ [kwɛnɡe̞t͡ɕʰe̞itʰa̠] ~ [kwe̞nɡe̞t͡ɕʰɛitʰa̠] ~ [kwe̞nɡe̞t͡ɕʰe̞itʰa̠]", "ipa")
	def test_eul_geot_gatda_ph(self):
		return self.run_test("-을 것 같다", "{{ko-IPA|com=3}}", "을 걷 갇따", "ph")
	def test_eul_geot_gatda_yr(self):
		return self.run_test("-을 것 같다", "{{ko-IPA|com=3}}", "ul keqs kathta", "yr")
	def test_eul_geot_gatda_ipa(self):
		return self.run_test("-을 것 같다", "{{ko-IPA|com=3}}", "[ɯɭ kʌ̹t̚ ka̠t̚t͈a̠]", "ipa")
	def test_naeswida_ipa(self):
		return self.run_test("내쉬다", "{{ko-IPA|l=y}}", "[ˈnɛ(ː)ʃʰɥida̠] ~ [ˈne̞(ː)ʃʰɥida̠] ~ [ˈnɛ(ː)ʃʰyda̠] ~ [ˈne̞(ː)ʃʰyda̠]", "ipa")
	def test_gwimagae_ipa(self):
		return self.run_test("귀마개", "{{ko-IPA}}", "[kɥima̠ɡɛ] ~ [kɥima̠ɡe̞] ~ [kyma̠ɡɛ] ~ [kyma̠ɡe̞]", "ipa")
	def test_oekwi_ipa(self):
		return self.run_test("외퀴", "{{ko-IPA|l=y}}", "[ˈwe̞(ː)kʰɥi] ~ [ˈø̞(ː)kʰɥi] ~ [ˈwe̞(ː)kʰy] ~ [ˈø̞(ː)kʰy]", "ipa")
	def test_yeot_ipa(self):
		return self.run_test("엿-", "{{ko-IPA|l=y}}", "[jɘ(ː)t̚]", "ipa")
	def test_daeryukgeomeunjippagwi_ipa(self):
		return self.run_test("대륙검은지빠귀", "{{ko-ipa}}", "[tɛɾjuk̚k͈ʌ̹mɯɲd͡ʑip͈a̠ɡɥi] ~ [te̞ɾjuk̚k͈ʌ̹mɯɲd͡ʑip͈a̠ɡɥi] ~ [tɛɾjuk̚k͈ʌ̹mɯɲd͡ʑip͈a̠ɡy] ~ [te̞ɾjuk̚k͈ʌ̹mɯɲd͡ʑip͈a̠ɡy]", "ipa")
	def test_doejippagwi_ipa(self):
		return self.run_test("되지빠귀", "{{ko-ipa|l=y}}", "[ˈtwe̞(ː)d͡ʑip͈a̠ɡɥi] ~ [ˈtø̞(ː)d͡ʑip͈a̠ɡɥi] ~ [ˈtwe̞(ː)d͡ʑip͈a̠ɡy] ~ [ˈtø̞(ː)d͡ʑip͈a̠ɡy]", "ipa")
	def test_hwiparamsolgae_ipa(self):
		return self.run_test("휘파람솔개", "{{ko-ipa}}", "[hɥipʰa̠ɾa̠msʰo̞ɭɡɛ] ~ [hɥipʰa̠ɾa̠msʰo̞ɭɡe̞] ~ [hypʰa̠ɾa̠msʰo̞ɭɡɛ] ~ [hypʰa̠ɾa̠msʰo̞ɭɡe̞]", "ipa")
	def test_hwiparamsae_ipa(self):
		return self.run_test("휘파람새", "{{ko-ipa}}", "[hɥipʰa̠ɾa̠msʰɛ] ~ [hɥipʰa̠ɾa̠msʰe̞] ~ [hypʰa̠ɾa̠msʰɛ] ~ [hypʰa̠ɾa̠msʰe̞]", "ipa")
	def test_seomhwiparamsae_ipa(self):
		return self.run_test("섬휘파람새", "{{ko-ipa}}", "[sʰʌ̹mɦɥipʰa̠ɾa̠msʰɛ] ~ [sʰʌ̹mɦɥipʰa̠ɾa̠msʰe̞] ~ [sʰʌ̹mɦypʰa̠ɾa̠msʰɛ] ~ [sʰʌ̹mɦypʰa̠ɾa̠msʰe̞]", "ipa")
	def test_gaedwaeji_ph(self):
		return self.run_test("개돼지", "{{ko-IPA|l=y}}", "개(ː)돼지/게(ː)돼지/개(ː)뒈지/게(ː)뒈지", "ph")
	def test_gaedwaeji_ipa(self):
		return self.run_test("개돼지", "{{ko-IPA|l=y}}", "[ˈkɛ(ː)dwɛd͡ʑi] ~ [ˈke̞(ː)dwɛd͡ʑi] ~ [ˈkɛ(ː)dwe̞d͡ʑi] ~ [ˈke̞(ː)dwe̞d͡ʑi]", "ipa")
	def test_daechwita_ipa(self):
		return self.run_test("대취타", "{{ko-IPA|l=y}}", "[ˈtɛ(ː)t͡ɕʰɥitʰa̠] ~ [ˈte̞(ː)t͡ɕʰɥitʰa̠] ~ [ˈtɛ(ː)t͡ɕʰytʰa̠] ~ [ˈte̞(ː)t͡ɕʰytʰa̠]", "ipa")
	def test_Pampangga_rr(self):
		return self.run_test("팜팡가", "{{ko-IPA}}", "Pampangga", "rr")
	def test_Pampangga_rrr(self):
		return self.run_test("팜팡가", "{{ko-IPA}}", "Pampangga", "rrr")
	def test_Pampangga_mr(self):
		return self.run_test("팜팡가", "{{ko-IPA}}", "P'amp'angga", "mr")
	def test_haetgwi_ipa(self):
		return self.run_test("햇귀", "{{ko-IPA}}", "[hɛt̚k͈ɥi] ~ [he̞t̚k͈ɥi] ~ [hɛt̚k͈y] ~ [he̞t̚k͈y]", "ipa")
	def test_gwihwanbihaeng_ipa(self):
		return self.run_test("귀환비행", "{{ko-IPA|l=y}}", "[ˈkɥi(ː)βwa̠nbiɦɛŋ] ~ [ˈkɥi(ː)βwa̠nbiɦe̞ŋ] ~ [ˈky(ː)βwa̠nbiɦɛŋ] ~ [ˈky(ː)βwa̠nbiɦe̞ŋ]", "ipa")
	def test_siwidae_ipa(self):
		return self.run_test("시위대", "{{ko-IPA|l=y}}", "[ˈɕʰi(ː)ɥidɛ] ~ [ˈɕʰi(ː)ɥide̞] ~ [ˈɕʰi(ː)ydɛ] ~ [ˈɕʰi(ː)yde̞]", "ipa")
	def test_araewi_ipa(self):
		return self.run_test("아래위", "{{ko-IPA}}", "[a̠ɾɛɥi] ~ [a̠ɾe̞ɥi] ~ [a̠ɾɛy] ~ [a̠ɾe̞y]", "ipa")
	def test_wiarae_ipa(self):
		return self.run_test("위아래", "{{ko-IPA}}", "[ɥia̠ɾɛ] ~ [ɥia̠ɾe̞] ~ [ya̠ɾɛ] ~ [ya̠ɾe̞]", "ipa")
	def test_wipaldongmaek_ipa(self):
		return self.run_test("위팔동맥", "{{ko-IPA}}", "[ɥipʰa̠ɭdo̞ŋmɛk̚] ~ [ɥipʰa̠ɭdo̞ŋme̞k̚] ~ [ypʰa̠ɭdo̞ŋmɛk̚] ~ [ypʰa̠ɭdo̞ŋme̞k̚]", "ipa")
	def test_wipaljeongmaek_ipa(self):
		return self.run_test("위팔정맥", "{{ko-IPA}}", "[ɥipʰa̠ʎd͡ʑʌ̹ŋmɛk̚] ~ [ɥipʰa̠ʎd͡ʑʌ̹ŋme̞k̚] ~ [ypʰa̠ʎd͡ʑʌ̹ŋmɛk̚] ~ [ypʰa̠ʎd͡ʑʌ̹ŋme̞k̚]", "ipa")
	def test_chinwidae_ipa(self):
		return self.run_test("친위대", "{{ko-IPA}}", "[t͡ɕʰinɥidɛ] ~ [t͡ɕʰinɥide̞] ~ [t͡ɕʰinydɛ] ~ [t͡ɕʰinyde̞]", "ipa")
	def test_Chinwidae_ipa_1(self):
		return self.run_test("친위대", "{{ko-IPA|cap=y}}", "[t͡ɕʰinɥidɛ] ~ [t͡ɕʰinɥide̞] ~ [t͡ɕʰinydɛ] ~ [t͡ɕʰinyde̞]", "ipa")
	def test_wijojipye_ipa(self):
		return self.run_test("위조지폐", "{{ko-IPA}}", "[ɥid͡ʑo̞d͡ʑipʰje̞] ~ [ɥid͡ʑo̞d͡ʑipʰe̞] ~ [yd͡ʑo̞d͡ʑipʰje̞] ~ [yd͡ʑo̞d͡ʑipʰe̞]", "ipa")
	def test_baekkwida_ipa(self):
		return self.run_test("배뀌다", "{{ko-IPA}}", "[pɛk͈ɥida̠] ~ [pe̞k͈ɥida̠] ~ [pɛk͈yda̠] ~ [pe̞k͈yda̠]", "ipa")
	def test_gyojojuui_ph(self):
		return self.run_test("교조주의", "{{ko-IPA|l=y|ui=5}}", "교(ː)조주의/교(ː)조주의이", "ph")
	def test_gyojojuui_ipa(self):
		return self.run_test("교조주의", "{{ko-IPA|l=y|ui=5}}", "[ˈkjo(ː)d͡ʑo̞d͡ʑuɰi] ~ [ˈkjo(ː)d͡ʑo̞d͡ʑuɰii]", "ipa")
	def test_maenwi_ipa(self):
		return self.run_test("맨위", "{{ko-IPA}}", "[mɛnɥi] ~ [me̞nɥi] ~ [mɛny] ~ [me̞ny]", "ipa")
	def test_chaechwi_ipa(self):
		return self.run_test("채취", "{{ko-IPA}}", "[t͡ɕʰɛt͡ɕʰɥi] ~ [t͡ɕʰe̞t͡ɕʰɥi] ~ [t͡ɕʰɛt͡ɕʰy] ~ [t͡ɕʰe̞t͡ɕʰy]", "ipa")
	def test_banggwijaengi_ipa(self):
		return self.run_test("방귀쟁이", "{{ko-IPA|l=y}}", "[ˈpa̠(ː)ŋɡɥid͡ʑɛŋi] ~ [ˈpa̠(ː)ŋɡɥid͡ʑe̞ŋi] ~ [ˈpa̠(ː)ŋɡyd͡ʑɛŋi] ~ [ˈpa̠(ː)ŋɡyd͡ʑe̞ŋi]", "ipa")
	def test_chwijae_ipa(self):
		return self.run_test("취재", "{{ko-IPA}}", "[t͡ɕʰɥid͡ʑɛ] ~ [t͡ɕʰɥid͡ʑe̞] ~ [t͡ɕʰyd͡ʑɛ] ~ [t͡ɕʰyd͡ʑe̞]", "ipa")
	def test_dae_ipa(self):
		return self.run_test("대-", "{{ko-IPA|l=1}}", "[tɛ(ː)] ~ [te̞(ː)]", "ipa")

	def run_test(self, hangul, param_string, expected, system_name):
		wr = WiktionaryRomanization(hangul, param_string)
		if (self.file):
			try:
				value = wr.romanize_one(system_name)
				print(f"{inspect.stack()[1].frame.f_code.co_name}: { 'success' if value == expected else f'fail expected {expected} but received {value}'}", file=self.file)
				return value == expected
			except Exception as e:
				print(f"{inspect.stack()[1].frame.f_code.co_name}: fail {e}", file=self.file)
				return False
		else:
			value = wr.romanize_one(system_name)
			self.assertEqual(value, expected)
