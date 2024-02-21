import inspect
import unittest
from src.wiktionary_romanization import WiktionaryRomanization

class TestAllWikiArticles(unittest.TestCase):
	file = ''

	def set_file(self, file):
		self.file = file

	def test_reul_rr(self):
		return self.run_test("-를", "{{ko-IPA}}", "reul", "rr")
	def test_cheoreom_rr(self):
		return self.run_test("-처럼", "{{ko-IPA}}", "cheoreom", "rr")
	def test_wikibaekgwa_ipa(self):
		return self.run_test("위키백과", "{{ko-IPA|a=Ko-위키백과.oga}}", "[ɥicçibɛk̚k͈wa̠] ~ [ɥicçibe̞k̚k͈wa̠] ~ [ycçibɛk̚k͈wa̠] ~ [ycçibe̞k̚k͈wa̠]", "ipa")
	def test_ida_rr(self):
		return self.run_test("-이다", "{{ko-IPA}}", "ida", "rr")
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
	def test_eseo_rr(self):
		return self.run_test("-에서", "{{ko-ipa}}", "eseo", "rr")
	def test_hago_rr(self):
		return self.run_test("-하고", "{{ko-IPA}}", "hago", "rr")
	def test_ut_rr(self):
		return self.run_test("웃-", "{{ko-IPA}}", "ut", "rr")
	def test_imyeo_rr(self):
		return self.run_test("-이며", "{{ko-IPA}}", "imyeo", "rr")
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
	def test_aji_rr(self):
		return self.run_test("-아지", "{{ko-IPA}}", "aji", "rr")
	def test_nya_rr(self):
		return self.run_test("-냐", "{{ko-ipa}}", "nya", "rr")
	def test_ege_rr(self):
		return self.run_test("-에게", "{{ko-IPA}}", "ege", "rr")
	def test_wit_rr(self):
		return self.run_test("윗-", "{{ko-IPA}}", "wit", "rr")
	def test_hante_rr(self):
		return self.run_test("-한테", "{{ko-IPA}}", "hante", "rr")
	def test_mankeum_rr(self):
		return self.run_test("-만큼", "{{ko-IPA}}", "mankeum", "rr")
	def test_jjeum_rr(self):
		return self.run_test("-쯤", "{{ko-IPA}}", "jjeum", "rr")
	def test_haengwi_ipa(self):
		return self.run_test("행위", "{{ko-IPA}}", "[hɛŋɥi] ~ [he̞ŋɥi] ~ [hɛŋy] ~ [he̞ŋy]", "ipa")
	def test_gwichaeksayu_ipa(self):
		return self.run_test("귀책사유", "{{ko-IPA|l=y}}", "[ˈkɥi(ː)t͡ɕʰɛks͈a̠ju] ~ [ˈkɥi(ː)t͡ɕʰe̞ks͈a̠ju] ~ [ˈky(ː)t͡ɕʰɛks͈a̠ju] ~ [ˈky(ː)t͡ɕʰe̞ks͈a̠ju]", "ipa")
	def test_euro_rr(self):
		return self.run_test("-으로", "{{ko-IPA}}", "euro", "rr")
	def test_kke_rr(self):
		return self.run_test("-께", "{{ko-IPA}}", "kke", "rr")
	def test_kkeseo_rr(self):
		return self.run_test("-께서", "{{ko-IPA}}", "kkeseo", "rr")
	def test_kkaji_rr(self):
		return self.run_test("-까지", "{{ko-IPA}}", "kkaji", "rr")
	def test_dul_rr(self):
		return self.run_test("둘-", "{{ko-IPA}}", "dul", "rr")
	def test_widaehada_ipa(self):
		return self.run_test("위대하다", "{{ko-IPA}}", "[ɥidɛɦa̠da̠] ~ [ɥide̞ɦa̠da̠] ~ [ydɛɦa̠da̠] ~ [yde̞ɦa̠da̠]", "ipa")
	def test_hi_rr(self):
		return self.run_test("-히", "{{ko-IPA}}", "hi", "rr")
	def test_gwittaegi_ipa(self):
		return self.run_test("귀때기", "{{ko-IPA}}", "[kɥit͈ɛɡi] ~ [kɥit͈e̞ɡi] ~ [kyt͈ɛɡi] ~ [kyt͈e̞ɡi]", "ipa")
	def test_gwissadaegi_ipa(self):
		return self.run_test("귀싸대기", "{{ko-IPA}}", "[kɥis͈a̠dɛɡi] ~ [kɥis͈a̠de̞ɡi] ~ [kys͈a̠dɛɡi] ~ [kys͈a̠de̞ɡi]", "ipa")
	def test_ke_rr(self):
		return self.run_test("-케", "{{ko-IPA}}", "ke", "rr")
	def test_mae_rr(self):
		return self.run_test("-매", "{{ko-IPA}}", "mae", "rr")
	def test_myeo_rr(self):
		return self.run_test("-며", "{{ko-IPA}}", "myeo", "rr")
	def test_seo_rr(self):
		return self.run_test("-서", "{{ko-IPA}}", "seo", "rr")
	def test_soe_rr(self):
		return self.run_test("쇠-", "{{ko-IPA|l=y}}", "soe", "rr")
	def test_soe_ipa(self):
		return self.run_test("쇠-", "{{ko-IPA|l=y}}", "[sʰwe̞(ː)] ~ [sʰø̞(ː)]", "ipa")
	def test_saendeuwichi_ipa(self):
		return self.run_test("샌드위치", "{{ko-IPA}}", "[sʰɛndɯɥit͡ɕʰi] ~ [sʰe̞ndɯɥit͡ɕʰi] ~ [sʰɛndɯyt͡ɕʰi] ~ [sʰe̞ndɯyt͡ɕʰi]", "ipa")
	def test_deot_rr(self):
		return self.run_test("덧-", "{{ko-IPA}}", "deot", "rr")
	def test_bammareun_jwiga_deutgo_nanmareun_saega_deunneunda_ipa(self):
		return self.run_test("밤말은 쥐가 듣고 낮말은 새가 듣는다", "{{ko-IPA}}", "[pa̠mma̠ɾɯn t͡ɕɥiɡa̠ tɯt̚k͈o̞ na̠nma̠ɾɯn sʰɛɡa̠ tɯnnɯnda̠] ~ [pa̠mma̠ɾɯn t͡ɕɥiɡa̠ tɯt̚k͈o̞ na̠nma̠ɾɯn sʰe̞ɡa̠ tɯnnɯnda̠] ~ [pa̠mma̠ɾɯn t͡ɕyɡa̠ tɯt̚k͈o̞ na̠nma̠ɾɯn sʰɛɡa̠ tɯnnɯnda̠] ~ [pa̠mma̠ɾɯn t͡ɕyɡa̠ tɯt̚k͈o̞ na̠nma̠ɾɯn sʰe̞ɡa̠ tɯnnɯnda̠]", "ipa")
	def test_mnikka_rr(self):
		return self.run_test("-ㅂ니까", "{{ko-IPA}}", "mnikka", "rr")
	def test_ropda_rr(self):
		return self.run_test("-롭다", "{{ko-IPA}}", "ropda", "rr")
	def test_jjeokda_rr(self):
		return self.run_test("-쩍다", "{{ko-IPA}}", "jjeokda", "rr")
	def test_seyo_rr(self):
		return self.run_test("-세요", "{{ko-IPA}}", "seyo", "rr")
	def test_tteurida_rr(self):
		return self.run_test("-뜨리다", "{{ko-IPA}}", "tteurida", "rr")
	def test_seonghaengwi_ipa(self):
		return self.run_test("성행위", "{{ko-IPA|l=y}}", "[ˈsʰɘ(ː)ŋɦɛŋɥi] ~ [ˈsʰɘ(ː)ŋɦe̞ŋɥi] ~ [ˈsʰɘ(ː)ŋɦɛŋy] ~ [ˈsʰɘ(ː)ŋɦe̞ŋy]", "ipa")
	def test_ira_rr(self):
		return self.run_test("-이라", "{{ko-IPA}}", "ira", "rr")
	def test_rani_rr(self):
		return self.run_test("-라니", "{{ko-ipa}}", "rani", "rr")
	def test_eupsida_rr(self):
		return self.run_test("-읍시다", "{{ko-IPA}}", "eupsida", "rr")
	def test_seumnida_rr(self):
		return self.run_test("-습니다", "{{ko-IPA|com=0}}", "seumnida", "rr")
	def test_mnida_rr(self):
		return self.run_test("-ㅂ니다", "{{ko-IPA}}", "mnida", "rr")
	def test_seumnikka_rr(self):
		return self.run_test("-습니까", "{{ko-IPA|com=0}}", "seumnikka", "rr")
	def test_wisaeng_ipa(self):
		return self.run_test("위생", "{{ko-IPA}}", "[ɥisʰɛŋ] ~ [ɥisʰe̞ŋ] ~ [ysʰɛŋ] ~ [ysʰe̞ŋ]", "ipa")
	def test_neunda_rr(self):
		return self.run_test("-는다", "{{ko-ipa}}", "neunda", "rr")
	def test_rago_rr(self):
		return self.run_test("-라고", "{{ko-IPA}}", "rago", "rr")
	def test_raseo_rr(self):
		return self.run_test("-라서", "{{ko-IPA}}", "raseo", "rr")
	def test_eunji_rr(self):
		return self.run_test("-은지", "{{ko-IPA}}", "eunji", "rr")
	def test_neunde_rr(self):
		return self.run_test("-는데", "{{ko-IPA}}", "neunde", "rr")
	def test_eunde_rr(self):
		return self.run_test("-은데", "{{ko-IPA}}", "eunde", "rr")
	def test_neunji_rr(self):
		return self.run_test("-는지", "{{ko-IPA}}", "neunji", "rr")
	def test_ramyeo_rr(self):
		return self.run_test("-라며", "{{ko-IPA}}", "ramyeo", "rr")
	def test_ayo_rr(self):
		return self.run_test("-아요", "{{ko-IPA}}", "ayo", "rr")
	def test_eoyo_rr(self):
		return self.run_test("-어요", "{{ko-IPA}}", "eoyo", "rr")
	def test_jiman_rr(self):
		return self.run_test("-지만", "{{ko-IPA}}", "jiman", "rr")
	def test_lge_ph(self):
		return self.run_test("-ㄹ게", "{{ko-IPA|com=1}}", "ㄹ께", "ph")
	def test_lge_rr(self):
		return self.run_test("-ㄹ게", "{{ko-IPA|com=1}}", "lge", "rr")
	def test_lge_mr(self):
		return self.run_test("-ㄹ게", "{{ko-IPA|com=1}}", "lke", "mr")
	def test_lge_yr(self):
		return self.run_test("-ㄹ게", "{{ko-IPA|com=1}}", "lqkey", "yr")
	def test_lge_ipa(self):
		return self.run_test("-ㄹ게", "{{ko-IPA|com=1}}", "[ɭk͈e̞]", "ipa")
	def test_eulge_ph(self):
		return self.run_test("-을게", "{{ko-IPA|com=1}}", "을께", "ph")
	def test_eulge_rr(self):
		return self.run_test("-을게", "{{ko-IPA|com=1}}", "eulge", "rr")
	def test_eulge_mr(self):
		return self.run_test("-을게", "{{ko-IPA|com=1}}", "ŭlke", "mr")
	def test_eulge_yr(self):
		return self.run_test("-을게", "{{ko-IPA|com=1}}", "ulqkey", "yr")
	def test_eulge_ipa(self):
		return self.run_test("-을게", "{{ko-IPA|com=1}}", "[ɯɭk͈e̞]", "ipa")
	def test_eullae_rr(self):
		return self.run_test("-을래", "{{ko-IPA}}", "eullae", "rr")
	def test_eulji_ph(self):
		return self.run_test("-을지", "{{ko-IPA|com=1}}", "을찌", "ph")
	def test_eulji_rr(self):
		return self.run_test("-을지", "{{ko-IPA|com=1}}", "eulji", "rr")
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
	def test_seureopda_rr(self):
		return self.run_test("-스럽다", "{{ko-IPA}}", "seureopda", "rr")
	def test_ina_rr(self):
		return self.run_test("-이나", "{{ko-ipa}}", "ina", "rr")
	def test_jocha_rr(self):
		return self.run_test("-조차", "{{ko-IPA}}", "jocha", "rr")
	def test_heot_rr(self):
		return self.run_test("헛-", "{{ko-IPA}}", "heot", "rr")
	def test_georida_rr(self):
		return self.run_test("-거리다", "{{ko-IPA}}", "georida", "rr")
	def test_lkka_rr(self):
		return self.run_test("-ㄹ까", "{{ko-IPA}}", "lkka", "rr")
	def test_eulkka_rr(self):
		return self.run_test("-을까", "{{ko-IPA}}", "eulkka", "rr")
	def test_put_rr(self):
		return self.run_test("풋-", "{{ko-IPA}}", "put", "rr")
	def test_dapda_rr(self):
		return self.run_test("-답다", "{{ko-IPA}}", "dapda", "rr")
	def test_jaengi_rr(self):
		return self.run_test("-쟁이", "{{ko-IPA}}", "jaeng'i", "rr")
	def test_hubaewi_ipa(self):
		return self.run_test("후배위", "{{ko-IPA|l=y}}", "[ˈɸʷu(ː)bɛɥi] ~ [ˈɸʷu(ː)be̞ɥi] ~ [ˈɸʷu(ː)bɛy] ~ [ˈɸʷu(ː)be̞y]", "ipa")
	def test_kkal_rr(self):
		return self.run_test("-깔", "{{ko-IPA}}", "kkal", "rr")
	def test_bakke_rr(self):
		return self.run_test("-밖에", "{{ko-IPA}}", "bakke", "rr")
	def test_rado_rr(self):
		return self.run_test("-라도", "{{ko-IPA}}", "rado", "rr")
	def test_eoya_hada_rr(self):
		return self.run_test("-어야 하다", "{{ko-ipa}}", "eoya hada", "rr")
	def test_wisaengsil_ipa(self):
		return self.run_test("위생실", "{{ko-IPA}}", "[ɥisʰɛŋɕʰiɭ] ~ [ɥisʰe̞ŋɕʰiɭ] ~ [ysʰɛŋɕʰiɭ] ~ [ysʰe̞ŋɕʰiɭ]", "ipa")
	def test_daewi_ipa(self):
		return self.run_test("대위", "{{ko-IPA|l=y}}", "[ˈtɛ(ː)ɥi] ~ [ˈte̞(ː)ɥi] ~ [ˈtɛ(ː)y] ~ [ˈte̞(ː)y]", "ipa")
	def test_si_rr(self):
		return self.run_test("-시-", "{{ko-IPA}}", "si", "rr")
	def test_widae_ipa(self):
		return self.run_test("위대", "{{ko-IPA}}", "[ɥidɛ] ~ [ɥide̞] ~ [ydɛ] ~ [yde̞]", "ipa")
	def test_bodado_rr(self):
		return self.run_test("-보다도", "{{ko-IPA}}", "bodado", "rr")
	def test_Oseuteuriaheonggari_rr(self):
		return self.run_test("오스트리아-헝가리", "{{ko-IPA|cap=y}}", "Oseuteuriaheonggari", "rr")
	def test_hoegwi_ipa(self):
		return self.run_test("회귀", "{{ko-IPA}}", "[ɸwe̞ɡɥi] ~ [hø̞ɡɥi] ~ [ɸwe̞ɡy] ~ [hø̞ɡy]", "ipa")
	def test_eura_rr(self):
		return self.run_test("-으라", "{{ko-IPA}}", "eura", "rr")
	def test_meun_rr(self):
		return self.run_test("-믄", "{{ko-IPA}}", "meun", "rr")
	def test_gugeubwisaengcha_ipa(self):
		return self.run_test("구급위생차", "{{ko-ipa|l=y}}", "[ˈku(ː)ɡɯbɥisʰɛŋt͡ɕʰa̠] ~ [ˈku(ː)ɡɯbɥisʰe̞ŋt͡ɕʰa̠] ~ [ˈku(ː)ɡɯbysʰɛŋt͡ɕʰa̠] ~ [ˈku(ː)ɡɯbysʰe̞ŋt͡ɕʰa̠]", "ipa")
	def test_toewi_ipa(self):
		return self.run_test("퇴위", "{{ko-IPA}}", "[tʰwe̞ɥi] ~ [tʰø̞ɥi] ~ [tʰwe̞y] ~ [tʰø̞y]", "ipa")
	def test_ayaget_rr(self):
		return self.run_test("-아야겠-", "{{ko-IPA}}", "ayaget", "rr")
	def test_aegeupjwi_ipa(self):
		return self.run_test("애급쥐", "{{ko-IPA}}", "[ɛɡɯp̚t͡ɕ͈ɥi] ~ [e̞ɡɯp̚t͡ɕ͈ɥi] ~ [ɛɡɯp̚t͡ɕ͈y] ~ [e̞ɡɯp̚t͡ɕ͈y]", "ipa")
	def test_gwaengechaeita_ph(self):
		return self.run_test("괜게채잏다", "{{ko-IPA}}", "괜게채이타/괜게체이타/궨게채이타/궨게체이타", "ph")
	def test_gwaengechaeita_ipa(self):
		return self.run_test("괜게채잏다", "{{ko-IPA}}", "[kwɛnɡe̞t͡ɕʰɛitʰa̠] ~ [kwɛnɡe̞t͡ɕʰe̞itʰa̠] ~ [kwe̞nɡe̞t͡ɕʰɛitʰa̠] ~ [kwe̞nɡe̞t͡ɕʰe̞itʰa̠]", "ipa")
	def test_raeyo_rr(self):
		return self.run_test("-래요", "{{ko-IPA}}", "raeyo", "rr")
	def test_rau_rr(self):
		return self.run_test("-라우", "{{ko-IPA}}", "rau", "rr")
	def test_kkun_rr(self):
		return self.run_test("-꾼", "{{ko-IPA}}", "kkun", "rr")
	def test_nikka_rr(self):
		return self.run_test("-니까", "{{ko-IPA}}", "nikka", "rr")
	def test_eungkke_rr(self):
		return self.run_test("-응께", "{{ko-IPA}}", "eungkke", "rr")
	def test_eul_geot_gatda_ph(self):
		return self.run_test("-을 것 같다", "{{ko-IPA|com=3}}", "을 걷 갇따", "ph")
	def test_eul_geot_gatda_rr(self):
		return self.run_test("-을 것 같다", "{{ko-IPA|com=3}}", "eul geot gatda", "rr")
	def test_eul_geot_gatda_yr(self):
		return self.run_test("-을 것 같다", "{{ko-IPA|com=3}}", "ul keqs kathta", "yr")
	def test_eul_geot_gatda_ipa(self):
		return self.run_test("-을 것 같다", "{{ko-IPA|com=3}}", "[ɯɭ kʌ̹t̚ ka̠t̚t͈a̠]", "ipa")
	def test_eumjik_rr(self):
		return self.run_test("-음직", "{{ko-IPA}}", "eumjik", "rr")
	def test_Gussiheuruseuttallini_rr(self):
		return self.run_test("구씨-흐루스딸리니", "{{ko-IPA|cap=y}}", "Gussiheuruseuttallini", "rr")
	def test_iraseo_rr(self):
		return self.run_test("-이라서", "{{ko-IPA}}", "iraseo", "rr")
	def test_seumunida_rr(self):
		return self.run_test("-스무니다", "{{ko-IPA|com=0}}", "seumunida", "rr")
	def test_seumunikka_rr(self):
		return self.run_test("-스무니까", "{{ko-IPA|com=0}}", "seumunikka", "rr")
	def test_naeswida_ipa(self):
		return self.run_test("내쉬다", "{{ko-IPA|l=y}}", "[ˈnɛ(ː)ʃʰɥida̠] ~ [ˈne̞(ː)ʃʰɥida̠] ~ [ˈnɛ(ː)ʃʰyda̠] ~ [ˈne̞(ː)ʃʰyda̠]", "ipa")
	def test_edaga_rr(self):
		return self.run_test("-에다가", "{{ko-IPA}}", "edaga", "rr")
	def test_gwimagae_ipa(self):
		return self.run_test("귀마개", "{{ko-IPA}}", "[kɥima̠ɡɛ] ~ [kɥima̠ɡe̞] ~ [kyma̠ɡɛ] ~ [kyma̠ɡe̞]", "ipa")
	def test_kkiri_rr(self):
		return self.run_test("-끼리", "{{ko-IPA}}", "kkiri", "rr")
	def test_eneun_rr(self):
		return self.run_test("-에는", "{{ko-IPA}}", "eneun", "rr")
	def test_jamaja_rr(self):
		return self.run_test("-자마자", "{{ko-IPA}}", "jamaja", "rr")
	def test_iyeo_rr(self):
		return self.run_test("-이여", "{{ko-IPA}}", "iyeo", "rr")
	def test_isiyeo_rr(self):
		return self.run_test("-이시여", "{{ko-IPA}}", "isiyeo", "rr")
	def test_eupseda_rr(self):
		return self.run_test("-읍세다", "{{ko-IPA}}", "eupseda", "rr")
	def test_seokkeorang_rr(self):
		return self.run_test("-서꺼랑", "{{ko-IPA}}", "seokkeorang", "rr")
	def test_eulkkapsyo_rr(self):
		return self.run_test("-을깝쇼", "{{ko-IPA}}", "eulkkapsyo", "rr")
	def test_bungi_rr(self):
		return self.run_test("-붕이", "{{ko-IPA}}", "bung'i", "rr")
	def test_seokkeon_rr(self):
		return self.run_test("-서껀", "{{ko-IPA}}", "seokkeon", "rr")
	def test_eunikka_rr(self):
		return self.run_test("-으니까", "{{ko-IPA}}", "eunikka", "rr")
	def test_eumyeonseo_rr(self):
		return self.run_test("-으면서", "{{ko-IPA}}", "eumyeonseo", "rr")
	def test_kkeojeong_rr(self):
		return self.run_test("-꺼정", "{{ko-IPA}}", "kkeojeong", "rr")
	def test_sigyeo_rr(self):
		return self.run_test("-시겨", "{{ko-ipa}}", "sigyeo", "rr")
	def test_sikkya_rr(self):
		return self.run_test("-시꺄", "{{ko-IPA}}", "sikkya", "rr")
	def test_egi_rr(self):
		return self.run_test("-에기", "{{ko-IPA}}", "egi", "rr")
	def test_oekwi_ipa(self):
		return self.run_test("외퀴", "{{ko-IPA|l=y}}", "[ˈwe̞(ː)kʰɥi] ~ [ˈø̞(ː)kʰɥi] ~ [ˈwe̞(ː)kʰy] ~ [ˈø̞(ː)kʰy]", "ipa")
	def test_eul_rr(self):
		return self.run_test("-을", "{{ko-IPA}}", "eul", "rr")
	def test_sa_rr(self):
		return self.run_test("-사", "{{ko-IPA}}", "sa", "rr")
	def test_eusa_rr(self):
		return self.run_test("-으사", "{{ko-IPA}}", "eusa", "rr")
	def test_sae_rr(self):
		return self.run_test("-새", "{{ko-IPA}}", "sae", "rr")
	def test_sae_rr(self):
		return self.run_test("새-", "{{ko-IPA}}", "sae", "rr")
	def test_a_rr(self):
		return self.run_test("-아", "{{ko-IPA}}", "a", "rr")
	def test_eo_rr(self):
		return self.run_test("-어", "{{ko-IPA}}", "eo", "rr")
	def test_jjari_rr(self):
		return self.run_test("-짜리", "{{ko-IPA}}", "jjari", "rr")
	def test_neun_rr(self):
		return self.run_test("-는-", "{{ko-IPA}}", "neun", "rr")
	def test_neun_rr(self):
		return self.run_test("-는", "{{ko-IPA}}", "neun", "rr")
	def test_neun_rr_1(self):
		return self.run_test("-는", "{{ko-IPA}}", "neun", "rr")
	def test_eun_rr(self):
		return self.run_test("-은", "{{ko-IPA}}", "eun", "rr")
	def test_n_rr(self):
		return self.run_test("-ㄴ", "{{ko-IPA}}", "n", "rr")
	def test_na_rr(self):
		return self.run_test("-나", "{{ko-IPA}}", "na", "rr")
	def test_euna_rr(self):
		return self.run_test("-으나", "{{ko-IPA}}", "euna", "rr")
	def test_neunya_rr(self):
		return self.run_test("-느냐", "{{ko-IPA}}", "neunya", "rr")
	def test_eunya_rr(self):
		return self.run_test("-으냐", "{{ko-IPA}}", "eunya", "rr")
	def test_ne_rr(self):
		return self.run_test("-네", "{{ko-ipa}}", "ne", "rr")
	def test_neuni_rr(self):
		return self.run_test("-느니", "{{ko-IPA}}", "neuni", "rr")
	def test_ni_rr(self):
		return self.run_test("-니", "{{ko-IPA}}", "ni", "rr")
	def test_myeon_rr(self):
		return self.run_test("-면", "{{ko-IPA}}", "myeon", "rr")
	def test_eumyeon_rr(self):
		return self.run_test("-으면", "{{ko-IPA}}", "eumyeon", "rr")
	def test_euni_rr(self):
		return self.run_test("-으니", "{{ko-IPA}}", "euni", "rr")
	def test_ja_rr(self):
		return self.run_test("-자", "{{ko-IPA}}", "ja", "rr")
	def test_l_rr(self):
		return self.run_test("-ㄹ", "{{ko-IPA}}", "l", "rr")
	def test_llae_rr(self):
		return self.run_test("-ㄹ래", "{{ko-IPA}}", "llae", "rr")
	def test_euseyo_rr(self):
		return self.run_test("-으세요", "{{ko-ipa}}", "euseyo", "rr")
	def test_deusi_rr(self):
		return self.run_test("-듯이", "{{ko-IPA}}", "deusi", "rr")
	def test_deut_rr(self):
		return self.run_test("-듯", "{{ko-IPA}}", "deut", "rr")
	def test_n_rr(self):
		return self.run_test("-ㄴ-", "{{ko-IPA}}", "n", "rr")
	def test_doe_rr(self):
		return self.run_test("-되", "{{ko-IPA}}", "doe", "rr")
	def test_eudoe_rr(self):
		return self.run_test("-으되", "{{ko-IPA}}", "eudoe", "rr")
	def test_eusi_rr(self):
		return self.run_test("-으시-", "{{ko-IPA}}", "eusi", "rr")
	def test_irago_rr(self):
		return self.run_test("-이라고", "{{ko-IPA}}", "irago", "rr")
	def test_ra_rr(self):
		return self.run_test("-라", "{{ko-IPA}}", "ra", "rr")
	def test_eurago_rr(self):
		return self.run_test("-으라고", "{{ko-IPA}}", "eurago", "rr")
	def test_dani_rr(self):
		return self.run_test("-다니", "{{ko-IPA}}", "dani", "rr")
	def test_eurani_rr(self):
		return self.run_test("-으라니", "{{ko-IPA}}", "eurani", "rr")
	def test_eumyeo_rr(self):
		return self.run_test("-으며", "{{ko-IPA}}", "eumyeo", "rr")
	def test_eumae_rr(self):
		return self.run_test("-으매", "{{ko-IPA}}", "eumae", "rr")
	def test_darata_rr(self):
		return self.run_test("-다랗다", "{{ko-IPA}}", "darata", "rr")
	def test_deul_rr(self):
		return self.run_test("-들", "{{ko-IPA}}", "deul", "rr")
	def test_ari_rr(self):
		return self.run_test("-앓이", "{{ko-IPA}}", "ari", "rr")
	def test_seumdung_rr(self):
		return self.run_test("-슴둥", "{{ko-IPA}}", "seumdung", "rr")
	def test_mdung_rr(self):
		return self.run_test("-ㅁ둥", "{{ko-IPA}}", "mdung", "rr")
	def test_ssik_rr(self):
		return self.run_test("-씩", "{{ko-IPA}}", "ssik", "rr")
	def test_myeonseo_rr(self):
		return self.run_test("-면서", "{{ko-IPA}}", "myeonseo", "rr")
	def test_eurau_rr(self):
		return self.run_test("-으라우", "{{ko-IPA}}", "eurau", "rr")
	def test_doda_rr(self):
		return self.run_test("-도다", "{{ko-IPA}}", "doda", "rr")
	def test_neunguna_rr(self):
		return self.run_test("-는구나", "{{ko-IPA}}", "neun'guna", "rr")
	def test_eoseo_rr(self):
		return self.run_test("-어서", "{{ko-IPA}}", "eoseo", "rr")
	def test_rae_rr(self):
		return self.run_test("-래", "{{ko-IPA}}", "rae", "rr")
	def test_eyo_rr(self):
		return self.run_test("-에요", "{{ko-IPA}}", "eyo", "rr")
	def test_aseo_rr(self):
		return self.run_test("-아서", "{{ko-IPA}}", "aseo", "rr")
	def test_reo_rr(self):
		return self.run_test("-러", "{{ko-IPA}}", "reo", "rr")
	def test_eureo_rr(self):
		return self.run_test("-으러", "{{ko-IPA}}", "eureo", "rr")
	def test_dorok_rr(self):
		return self.run_test("-도록", "{{ko-IPA}}", "dorok", "rr")
	def test_euri_rr(self):
		return self.run_test("-으리", "{{ko-IPA}}", "euri", "rr")
	def test_b_rr(self):
		return self.run_test("-ㅂ", "{{ko-IPA}}", "b", "rr")
	def test_eoya_rr(self):
		return self.run_test("-어야", "{{ko-IPA}}", "eoya", "rr")
	def test_do_rr(self):
		return self.run_test("-도", "{{ko-IPA}}", "do", "rr")
	def test_eodo_rr(self):
		return self.run_test("-어도", "{{ko-IPA}}", "eodo", "rr")
	def test_mada_rr(self):
		return self.run_test("-마다", "{{ko-IPA}}", "mada", "rr")
	def test_ado_rr(self):
		return self.run_test("-아도", "{{ko-IPA}}", "ado", "rr")
	def test_aya_rr(self):
		return self.run_test("-아야", "{{ko-IPA}}", "aya", "rr")
	def test_gun_rr(self):
		return self.run_test("-군", "{{ko-IPA}}", "gun", "rr")
	def test_eora_rr(self):
		return self.run_test("-어라", "{{ko-IPA}}", "eora", "rr")
	def test_ara_rr(self):
		return self.run_test("-아라", "{{ko-IPA}}", "ara", "rr")
	def test_aya_hada_rr(self):
		return self.run_test("-아야 하다", "{{ko-ipa}}", "aya hada", "rr")
	def test_eoya_doeda_rr(self):
		return self.run_test("-어야 되다", "{{ko-IPA}}", "eoya doeda", "rr")
	def test_aya_doeda_rr(self):
		return self.run_test("-아야 되다", "{{ko-IPA}}", "aya doeda", "rr")
	def test_eoyaget_rr(self):
		return self.run_test("-어야겠-", "{{ko-IPA}}", "eoyaget", "rr")
	def test_hae_rr(self):
		return self.run_test("-해", "{{ko-IPA}}", "hae", "rr")
	def test_eot_rr(self):
		return self.run_test("-었-", "{{ko-IPA}}", "eot", "rr")
	def test_at_rr(self):
		return self.run_test("-았-", "{{ko-IPA}}", "at", "rr")
	def test_ya_rr(self):
		return self.run_test("-야", "{{ko-IPA}}", "ya", "rr")
	def test_iya_rr(self):
		return self.run_test("-이야", "{{ko-IPA}}", "iya", "rr")
	def test_eosseot_rr(self):
		return self.run_test("-었었-", "{{ko-IPA}}", "eosseot", "rr")
	def test_yeo_rr(self):
		return self.run_test("-여", "{{ko-IPA}}", "yeo", "rr")
	def test_yeoya_rr(self):
		return self.run_test("-여야", "{{ko-IPA}}", "yeoya", "rr")
	def test_u_rr(self):
		return self.run_test("-우-", "{{ko-IPA}}", "u", "rr")
	def test_u_rr(self):
		return self.run_test("-우", "{{ko-IPA}}", "u", "rr")
	def test_euu_rr(self):
		return self.run_test("-으우", "{{ko-IPA}}", "euu", "rr")
	def test_euo_rr(self):
		return self.run_test("-으오", "{{ko-IPA}}", "euo", "rr")
	def test_so_rr(self):
		return self.run_test("-소", "{{ko-IPA}}", "so", "rr")
	def test_o_rr(self):
		return self.run_test("-오", "{{ko-IPA}}", "o", "rr")
	def test_o_rr(self):
		return self.run_test("-오-", "{{ko-IPA}}", "o", "rr")
	def test_euop_rr(self):
		return self.run_test("-으옵-", "{{ko-IPA}}", "euop", "rr")
	def test_euo_rr(self):
		return self.run_test("-으오-", "{{ko-IPA}}", "euo", "rr")
	def test_i_rr(self):
		return self.run_test("-이", "{{ko-IPA}}", "i", "rr")
	def test_i_rr_1(self):
		return self.run_test("-이", "{{ko-IPA}}", "i", "rr")
	def test_i_rr_2(self):
		return self.run_test("-이", "{{ko-IPA}}", "i", "rr")
	def test_i_rr_3(self):
		return self.run_test("-이", "{{ko-IPA}}", "i", "rr")
	def test_eui_rr(self):
		return self.run_test("-으이", "{{ko-IPA}}", "eu'i", "rr")
	def test_jjae_rr(self):
		return self.run_test("-째", "{{ko-IPA}}", "jjae", "rr")
	def test_yeot_rr(self):
		return self.run_test("엿-", "{{ko-IPA|l=y}}", "yeot", "rr")
	def test_yeot_ipa(self):
		return self.run_test("엿-", "{{ko-IPA|l=y}}", "[jɘ(ː)t̚]", "ipa")
	def test_jjang_rr(self):
		return self.run_test("-짱", "{{ko-IPA}}", "jjang", "rr")
	def test_i_rr(self):
		return self.run_test("-이-", "{{ko-IPA}}", "i", "rr")
	def test_man_rr(self):
		return self.run_test("-만", "{{ko-ipa}}", "man", "rr")
	def test_irang_rr(self):
		return self.run_test("-이랑", "{{ko-IPA}}", "irang", "rr")
	def test_rang_rr(self):
		return self.run_test("-랑", "{{ko-IPA}}", "rang", "rr")
	def test_ro_rr(self):
		return self.run_test("-로", "{{ko-IPA}}", "ro", "rr")
	def test_boda_rr(self):
		return self.run_test("-보다", "{{ko-IPA}}", "boda", "rr")
	def test__rr(self):
		return self.run_test("-ㅇ", "{{ko-IPA}}", "'", "rr")
	def test_eohada_rr(self):
		return self.run_test("-어하다", "{{ko-IPA}}", "eohada", "rr")
	def test_eosseumyeon_hada_rr(self):
		return self.run_test("-었으면 하다", "{{ko-IPA}}", "eosseumyeon hada", "rr")
	def test_euro_hayeo_rr(self):
		return self.run_test("-으로 하여", "{{ko-IPA}}", "euro hayeo", "rr")
	def test_jjeum_haeseo_rr(self):
		return self.run_test("-쯤 해서", "{{ko-IPA}}", "jjeum haeseo", "rr")
	def test_chi_rr(self):
		return self.run_test("-치", "{{ko-IPA}}", "chi", "rr")
	def test_e_rr(self):
		return self.run_test("-에", "{{ko-IPA}}", "e", "rr")
	def test_hi_rr(self):
		return self.run_test("-히-", "{{ko-IPA}}", "hi", "rr")
	def test_ppun_rr(self):
		return self.run_test("-뿐", "{{ko-IPA}}", "ppun", "rr")
	def test_irado_rr(self):
		return self.run_test("-이라도", "{{ko-IPA}}", "irado", "rr")
	def test_eda_rr(self):
		return self.run_test("-에다", "{{ko-IPA}}", "eda", "rr")
	def test_inde_rr(self):
		return self.run_test("-인데", "{{ko-IPA}}", "inde", "rr")
	def test_gachi_rr(self):
		return self.run_test("-같이", "{{ko-IPA}}", "gachi", "rr")
	def test_wa_rr(self):
		return self.run_test("-와", "{{ko-IPA}}", "wa", "rr")
	def test_mak_rr(self):
		return self.run_test("막-", "{{ko-IPA}}", "mak", "rr")
	def test_chal_rr(self):
		return self.run_test("찰-", "{{ko-IPA}}", "chal", "rr")
	def test_eol_rr(self):
		return self.run_test("얼-", "{{ko-IPA}}", "eol", "rr")
	def test_jit_rr(self):
		return self.run_test("짓-", "{{ko-IPA}}", "jit", "rr")
	def test_sinikka_rr(self):
		return self.run_test("-시니까", "{{ko-IPA}}", "sinikka", "rr")
	def test_majeo_rr(self):
		return self.run_test("-마저", "{{ko-IPA}}", "majeo", "rr")
	def test_daeryukgeomeunjippagwi_ipa(self):
		return self.run_test("대륙검은지빠귀", "{{ko-ipa}}", "[tɛɾjuk̚k͈ʌ̹mɯɲd͡ʑip͈a̠ɡɥi] ~ [te̞ɾjuk̚k͈ʌ̹mɯɲd͡ʑip͈a̠ɡɥi] ~ [tɛɾjuk̚k͈ʌ̹mɯɲd͡ʑip͈a̠ɡy] ~ [te̞ɾjuk̚k͈ʌ̹mɯɲd͡ʑip͈a̠ɡy]", "ipa")
	def test_eot_rr(self):
		return self.run_test("-엇-", "{{ko-IPA}}", "eot", "rr")
	def test_at_rr(self):
		return self.run_test("-앗-", "{{ko-IPA}}", "at", "rr")
	def test_doejippagwi_ipa(self):
		return self.run_test("되지빠귀", "{{ko-ipa|l=y}}", "[ˈtwe̞(ː)d͡ʑip͈a̠ɡɥi] ~ [ˈtø̞(ː)d͡ʑip͈a̠ɡɥi] ~ [ˈtwe̞(ː)d͡ʑip͈a̠ɡy] ~ [ˈtø̞(ː)d͡ʑip͈a̠ɡy]", "ipa")
	def test_hwiparamsolgae_ipa(self):
		return self.run_test("휘파람솔개", "{{ko-ipa}}", "[hɥipʰa̠ɾa̠msʰo̞ɭɡɛ] ~ [hɥipʰa̠ɾa̠msʰo̞ɭɡe̞] ~ [hypʰa̠ɾa̠msʰo̞ɭɡɛ] ~ [hypʰa̠ɾa̠msʰo̞ɭɡe̞]", "ipa")
	def test_hwiparamsae_ipa(self):
		return self.run_test("휘파람새", "{{ko-ipa}}", "[hɥipʰa̠ɾa̠msʰɛ] ~ [hɥipʰa̠ɾa̠msʰe̞] ~ [hypʰa̠ɾa̠msʰɛ] ~ [hypʰa̠ɾa̠msʰe̞]", "ipa")
	def test_seomhwiparamsae_ipa(self):
		return self.run_test("섬휘파람새", "{{ko-ipa}}", "[sʰʌ̹mɦɥipʰa̠ɾa̠msʰɛ] ~ [sʰʌ̹mɦɥipʰa̠ɾa̠msʰe̞] ~ [sʰʌ̹mɦypʰa̠ɾa̠msʰɛ] ~ [sʰʌ̹mɦypʰa̠ɾa̠msʰe̞]", "ipa")
	def test_eulloda_rr(self):
		return self.run_test("-을로다", "{{ko-IPA}}", "eulloda", "rr")
	def test_a_rr(self):
		return self.run_test("-아-", "{{ko-IPA}}", "a", "rr")
	def test_ryeogo_rr(self):
		return self.run_test("-려고", "{{ko-IPA}}", "ryeogo", "rr")
	def test_hol_rr(self):
		return self.run_test("홀-", "{{ko-IPA}}", "hol", "rr")
	def test_gaedwaeji_ph(self):
		return self.run_test("개돼지", "{{ko-IPA|l=y}}", "개(ː)돼지/게(ː)돼지/개(ː)뒈지/게(ː)뒈지", "ph")
	def test_gaedwaeji_ipa(self):
		return self.run_test("개돼지", "{{ko-IPA|l=y}}", "[ˈkɛ(ː)dwɛd͡ʑi] ~ [ˈke̞(ː)dwɛd͡ʑi] ~ [ˈkɛ(ː)dwe̞d͡ʑi] ~ [ˈke̞(ː)dwe̞d͡ʑi]", "ipa")
	def test_deunji_rr(self):
		return self.run_test("-든지", "{{ko-IPA}}", "deunji", "rr")
	def test_eonneun_rr(self):
		return self.run_test("-었는", "{{ko-IPA}}", "eonneun", "rr")
	def test_dungi_rr(self):
		return self.run_test("-둥이", "{{ko-IPA}}", "dung'i", "rr")
	def test_euroseo_rr(self):
		return self.run_test("-으로서", "{{ko-IPA}}", "euroseo", "rr")
	def test_roseo_rr(self):
		return self.run_test("-로서", "{{ko-IPA}}", "roseo", "rr")
	def test_buchi_rr(self):
		return self.run_test("-붙이", "{{ko-IPA}}", "buchi", "rr")
	def test_eungge_rr(self):
		return self.run_test("-응게", "{{ko-IPA}}", "eungge", "rr")
	def test_kkajeong_rr(self):
		return self.run_test("-까정", "{{ko-IPA}}", "kkajeong", "rr")
	def test_sikka_rr(self):
		return self.run_test("-시까", "{{ko-IPA}}", "sikka", "rr")
	def test_jibi_rr(self):
		return self.run_test("-지비", "{{ko-IPA}}", "jibi", "rr")
	def test_beoteom_rr(self):
		return self.run_test("-버텀", "{{ko-IPA}}", "beoteom", "rr")
	def test_yayo_rr(self):
		return self.run_test("-야요", "{{ko-IPA}}", "yayo", "rr")
	def test_mo_rr(self):
		return self.run_test("-모", "{{ko-IPA}}", "mo", "rr")
	def test_maen_rr(self):
		return self.run_test("-맨", "{{ko-IPA}}", "maen", "rr")
	def test_suda_rr(self):
		return self.run_test("-수다", "{{ko-IPA}}", "suda", "rr")
	def test_eoyaji_rr(self):
		return self.run_test("-어야지", "{{ko-IPA}}", "eoyaji", "rr")
	def test_ayaji_rr(self):
		return self.run_test("-아야지", "{{ko-IPA}}", "ayaji", "rr")
	def test_eul_tende_rr(self):
		return self.run_test("-을 텐데", "{{ko-IPA}}", "eul tende", "rr")
	def test_neundi_rr(self):
		return self.run_test("-는디", "{{ko-IPA}}", "neundi", "rr")
	def test_seumkka_rr(self):
		return self.run_test("-슴까", "{{ko-IPA}}", "seumkka", "rr")
	def test_seumme_rr(self):
		return self.run_test("-슴메", "{{ko-IPA}}", "seumme", "rr")
	def test_rose_rr(self):
		return self.run_test("-로세", "{{ko-IPA}}", "rose", "rr")
	def test_daechwita_ipa(self):
		return self.run_test("대취타", "{{ko-IPA|l=y}}", "[ˈtɛ(ː)t͡ɕʰɥitʰa̠] ~ [ˈte̞(ː)t͡ɕʰɥitʰa̠] ~ [ˈtɛ(ː)t͡ɕʰytʰa̠] ~ [ˈte̞(ː)t͡ɕʰytʰa̠]", "ipa")
	def test_eumeun_rr(self):
		return self.run_test("-으믄", "{{ko-IPA}}", "eumeun", "rr")
	def test_kkeoji_rr(self):
		return self.run_test("-꺼지", "{{ko-IPA}}", "kkeoji", "rr")
	def test_euru_rr(self):
		return self.run_test("-으루", "{{ko-IPA}}", "euru", "rr")
	def test_Pampangga_rr(self):
		return self.run_test("팜팡가", "{{ko-IPA}}", "Pampangga", "rr")
	def test_Pampangga_rrr(self):
		return self.run_test("팜팡가", "{{ko-IPA}}", "Pampangga", "rrr")
	def test_Pampangga_mr(self):
		return self.run_test("팜팡가", "{{ko-IPA}}", "P'amp'angga", "mr")
	def test_sida_rr(self):
		return self.run_test("-시다", "{{ko-IPA}}", "sida", "rr")
	def test_neut_rr(self):
		return self.run_test("늦-", "{{ko-IPA}}", "neut", "rr")
	def test_haetgwi_ipa(self):
		return self.run_test("햇귀", "{{ko-IPA}}", "[hɛt̚k͈ɥi] ~ [he̞t̚k͈ɥi] ~ [hɛt̚k͈y] ~ [he̞t̚k͈y]", "ipa")
	def test_gwihwanbihaeng_ipa(self):
		return self.run_test("귀환비행", "{{ko-IPA|l=y}}", "[ˈkɥi(ː)βwa̠nbiɦɛŋ] ~ [ˈkɥi(ː)βwa̠nbiɦe̞ŋ] ~ [ˈky(ː)βwa̠nbiɦɛŋ] ~ [ˈky(ː)βwa̠nbiɦe̞ŋ]", "ipa")
	def test_siwidae_ipa(self):
		return self.run_test("시위대", "{{ko-IPA|l=y}}", "[ˈɕʰi(ː)ɥidɛ] ~ [ˈɕʰi(ː)ɥide̞] ~ [ˈɕʰi(ː)ydɛ] ~ [ˈɕʰi(ː)yde̞]", "ipa")
	def test_naegi_rr(self):
		return self.run_test("-내기", "{{ko-IPA}}", "naegi", "rr")
	def test_hat_rr(self):
		return self.run_test("핫-", "{{ko-IPA}}", "hat", "rr")
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
	def test_gio_rr(self):
		return self.run_test("-기오", "{{ko-IPA}}", "gio", "rr")
	def test_tuseongi_rr(self):
		return self.run_test("-투성이", "{{ko-IPA}}", "tuseong'i", "rr")
	def test_gyojojuui_ph(self):
		return self.run_test("교조주의", "{{ko-IPA|l=y|ui=5}}", "교(ː)조주의/교(ː)조주의이", "ph")
	def test_gyojojuui_ipa(self):
		return self.run_test("교조주의", "{{ko-IPA|l=y|ui=5}}", "[ˈkjo(ː)d͡ʑo̞d͡ʑuɰi] ~ [ˈkjo(ː)d͡ʑo̞d͡ʑuɰii]", "ipa")
	def test_maenwi_ipa(self):
		return self.run_test("맨위", "{{ko-IPA}}", "[mɛnɥi] ~ [me̞nɥi] ~ [mɛny] ~ [me̞ny]", "ipa")
	def test_haejida_rr(self):
		return self.run_test("-해지다", "{{ko-IPA}}", "haejida", "rr")
	def test_eulssonya_rr(self):
		return self.run_test("-을쏘냐", "{{ko-IPA}}", "eulssonya", "rr")
	def test_mu_rr(self):
		return self.run_test("-무", "{{ko-IPA}}", "mu", "rr")
	def test_chaechwi_ipa(self):
		return self.run_test("채취", "{{ko-IPA}}", "[t͡ɕʰɛt͡ɕʰɥi] ~ [t͡ɕʰe̞t͡ɕʰɥi] ~ [t͡ɕʰɛt͡ɕʰy] ~ [t͡ɕʰe̞t͡ɕʰy]", "ipa")
	def test_deoni_rr(self):
		return self.run_test("-더니", "{{ko-IPA}}", "deoni", "rr")
	def test_ragu_rr(self):
		return self.run_test("-라구", "{{ko-IPA}}", "ragu", "rr")
	def test_banggwijaengi_ipa(self):
		return self.run_test("방귀쟁이", "{{ko-IPA|l=y}}", "[ˈpa̠(ː)ŋɡɥid͡ʑɛŋi] ~ [ˈpa̠(ː)ŋɡɥid͡ʑe̞ŋi] ~ [ˈpa̠(ː)ŋɡyd͡ʑɛŋi] ~ [ˈpa̠(ː)ŋɡyd͡ʑe̞ŋi]", "ipa")
	def test_hanteseo_rr(self):
		return self.run_test("-한테서", "{{ko-IPA}}", "hanteseo", "rr")
	def test_chwijae_ipa(self):
		return self.run_test("취재", "{{ko-IPA}}", "[t͡ɕʰɥid͡ʑɛ] ~ [t͡ɕʰɥid͡ʑe̞] ~ [t͡ɕʰyd͡ʑɛ] ~ [t͡ɕʰyd͡ʑe̞]", "ipa")
	def test_geot_rr(self):
		return self.run_test("겉-", "{{ko-IPA}}", "geot", "rr")
	def test_baengi_rr(self):
		return self.run_test("-뱅이", "{{ko-IPA}}", "baeng'i", "rr")
	def test_iyamallo_rr(self):
		return self.run_test("-이야말로", "{{ko-IPA}}", "iyamallo", "rr")
	def test_yamallo_rr(self):
		return self.run_test("-야말로", "{{ko-IPA}}", "yamallo", "rr")
	def test_oeda_rr(self):
		return self.run_test("-외다", "{{ko-IPA}}", "oeda", "rr")
	def test_oida_rr(self):
		return self.run_test("-오이다", "{{ko-IPA}}", "oida", "rr")
	def test_sil_rr(self):
		return self.run_test("-실", "{{ko-IPA}}", "sil", "rr")
	def test_sil_rr_1(self):
		return self.run_test("-실", "{{ko-IPA}}", "sil", "rr")
	def test_dae_rr(self):
		return self.run_test("대-", "{{ko-IPA|l=1}}", "dae", "rr")
	def test_dae_ipa(self):
		return self.run_test("대-", "{{ko-IPA|l=1}}", "[tɛ(ː)] ~ [te̞(ː)]", "ipa")
	def test_dae_rr_1(self):
		return self.run_test("대-", "{{ko-IPA}}", "dae", "rr")
	def test_bae_rr(self):
		return self.run_test("-배", "{{ko-IPA}}", "bae", "rr")
	def test_jirong_rr(self):
		return self.run_test("-지롱", "{{ko-IPA}}", "jirong", "rr")
	def test_tang_rr(self):
		return self.run_test("-탕", "{{ko-IPA}}", "tang", "rr")
	def test_tong_rr(self):
		return self.run_test("통-", "{{ko-IPA}}", "tong", "rr")
	def test_pung_rr(self):
		return self.run_test("-풍", "{{ko-IPA}}", "pung", "rr")
	def test_han_rr(self):
		return self.run_test("한-", "{{ko-IPA}}", "han", "rr")
	def test_han_rr_1(self):
		return self.run_test("한-", "{{ko-IPA}}", "han", "rr")
	def test_jang_rr(self):
		return self.run_test("-장", "{{ko-IPA}}", "jang", "rr")
	def test_jang_rr_1(self):
		return self.run_test("-장", "{{ko-IPA}}", "jang", "rr")
	def test_jang_rr_2(self):
		return self.run_test("-장", "{{ko-IPA}}", "jang", "rr")
	def test_jang_rr_3(self):
		return self.run_test("-장", "{{ko-IPA}}", "jang", "rr")
	def test_jang_rr_4(self):
		return self.run_test("-장", "{{ko-IPA}}", "jang", "rr")
	def test_jang_rr_5(self):
		return self.run_test("-장", "{{ko-IPA}}", "jang", "rr")
	def test_jang_rr_6(self):
		return self.run_test("-장", "{{ko-IPA|com=0}}", "jang", "rr")
	def test_jang_rr_7(self):
		return self.run_test("-장", "{{ko-IPA}}", "jang", "rr")
	def test_jang_rr_8(self):
		return self.run_test("-장", "{{ko-IPA}}", "jang", "rr")
	def test_pa_rr(self):
		return self.run_test("-파", "{{ko-IPA}}", "pa", "rr")
	def test_pa_rr_1(self):
		return self.run_test("-파", "{{ko-IPA}}", "pa", "rr")
	def test_sin_rr(self):
		return self.run_test("신-", "{{ko-IPA}}", "sin", "rr")
	def test_ryu_rr(self):
		return self.run_test("-류", "{{ko-IPA}}", "ryu", "rr")
	def test_ryu_rr_1(self):
		return self.run_test("-류", "{{ko-IPA}}", "ryu", "rr")
	def test_ryu_rr_2(self):
		return self.run_test("-류", "{{ko-IPA}}", "ryu", "rr")
	def test_ssi_rr(self):
		return self.run_test("-씨", "{{ko-IPA}}", "ssi", "rr")
	def test_ssi_rr_1(self):
		return self.run_test("-씨", "{{ko-IPA}}", "ssi", "rr")
	def test_seupsik_rr(self):
		return self.run_test("습식-", "{{ko-IPA}}", "seupsik", "rr")
	def test_no_rr(self):
		return self.run_test("-노", "{{ko-IPA}}", "no", "rr")
	def test_euseoyo_rr(self):
		return self.run_test("-으서요", "{{ko-ipa}}", "euseoyo", "rr")
	def test_deorado_rr(self):
		return self.run_test("-더라도", "{{ko-IPA}}", "deorado", "rr")

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
