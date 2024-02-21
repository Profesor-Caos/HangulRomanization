import inspect
import unittest
from src.wiktionary_romanization import WiktionaryRomanization

class TestUniqueDBCases(unittest.TestCase):
	file = ''

	def set_file(self, file):
		self.file = file

	def test_koenihiseubereukeu_ph(self):
		return self.run_test("쾨니히스베르크", "{{ko-IPA|쾨니히스베르크}}", "퀘니히스베르크/쾨니히스베르크", "ph")
	def test_koenihiseubereukeu_rr(self):
		return self.run_test("쾨니히스베르크", "{{ko-IPA|쾨니히스베르크}}", "koenihiseubereukeu", "rr")
	def test_koenihiseubereukeu_rrr(self):
		return self.run_test("쾨니히스베르크", "{{ko-IPA|쾨니히스베르크}}", "koenihiseubeleukeu", "rrr")
	def test_koenihiseubereukeu_mr(self):
		return self.run_test("쾨니히스베르크", "{{ko-IPA|쾨니히스베르크}}", "k'oenihisŭberŭk'ŭ", "mr")
	def test_koenihiseubereukeu_yr(self):
		return self.run_test("쾨니히스베르크", "{{ko-IPA|쾨니히스베르크}}", "khoynihisupeylu.khu", "yr")
	def test_koenihiseubereukeu_ipa(self):
		return self.run_test("쾨니히스베르크", "{{ko-IPA|쾨니히스베르크}}", "[kʰwe̞niʝisʰɯbe̞ɾɯkxɯ] ~ [kʰø̞niʝisʰɯbe̞ɾɯkxɯ]", "ipa")

	def test_boon_jangchi_ph(self):
		return self.run_test("보온장치", "{{ko-IPA|보온 장치|l=y}}", "보(ː)온 장치", "ph")
	def test_boon_jangchi_rr(self):
		return self.run_test("보온장치", "{{ko-IPA|보온 장치|l=y}}", "boon jangchi", "rr")
	def test_boon_jangchi_rrr(self):
		return self.run_test("보온장치", "{{ko-IPA|보온 장치|l=y}}", "boon jangchi", "rrr")
	def test_boon_jangchi_mr(self):
		return self.run_test("보온장치", "{{ko-IPA|보온 장치|l=y}}", "poon changch'i", "mr")
	def test_boon_jangchi_yr(self):
		return self.run_test("보온장치", "{{ko-IPA|보온 장치|l=y}}", "pōon cangchi", "yr")
	def test_boon_jangchi_ipa(self):
		return self.run_test("보온장치", "{{ko-IPA|보온 장치|l=y}}", "[ˈpo̞(ː)o̞n t͡ɕa̠ŋt͡ɕʰi]", "ipa")

	def test_kyual_kodeu_ph(self):
		return self.run_test("QR 코드", "{{ko-IPA|큐알 코드|com=1}}", "큐알 코드", "ph")
	def test_kyual_kodeu_rr(self):
		return self.run_test("QR 코드", "{{ko-IPA|큐알 코드|com=1}}", "kyual kodeu", "rr")
	def test_kyual_kodeu_rrr(self):
		return self.run_test("QR 코드", "{{ko-IPA|큐알 코드|com=1}}", "kyual kodeu", "rrr")
	def test_kyual_kodeu_mr(self):
		return self.run_test("QR 코드", "{{ko-IPA|큐알 코드|com=1}}", "k'yual k'odŭ", "mr")
	def test_kyual_kodeu_yr(self):
		return self.run_test("QR 코드", "{{ko-IPA|큐알 코드|com=1}}", "khyuqal khotu", "yr")
	def test_kyual_kodeu_ipa(self):
		return self.run_test("QR 코드", "{{ko-IPA|큐알 코드|com=1}}", "[cçua̠ɭ kʰo̞dɯ]", "ipa")

	def test_gabot_ph(self):
		return self.run_test("갑옷", "{{ko-ipa|a=Ko-갑옷.ogg}}", "가볻", "ph")
	def test_gabot_rr(self):
		return self.run_test("갑옷", "{{ko-ipa|a=Ko-갑옷.ogg}}", "gabot", "rr")
	def test_gabot_rrr(self):
		return self.run_test("갑옷", "{{ko-ipa|a=Ko-갑옷.ogg}}", "gab'os", "rrr")
	def test_gabot_mr(self):
		return self.run_test("갑옷", "{{ko-ipa|a=Ko-갑옷.ogg}}", "kabot", "mr")
	def test_gabot_yr(self):
		return self.run_test("갑옷", "{{ko-ipa|a=Ko-갑옷.ogg}}", "kap.os", "yr")
	def test_gabot_ipa(self):
		return self.run_test("갑옷", "{{ko-ipa|a=Ko-갑옷.ogg}}", "[ka̠bo̞t̚]", "ipa")

	def test_Bakgeunhye_ph(self):
		return self.run_test("박ㄹ혜", "{{ko-IPA|박근혜|cap=y}}", "박끈혜/박끈헤", "ph")
	def test_Bakgeunhye_rr(self):
		return self.run_test("박ㄹ혜", "{{ko-IPA|박근혜|cap=y}}", "Bakgeunhye", "rr")
	def test_Bakgeunhye_rrr(self):
		return self.run_test("박ㄹ혜", "{{ko-IPA|박근혜|cap=y}}", "Baggeunhye", "rrr")
	def test_Bakgeunhye_mr(self):
		return self.run_test("박ㄹ혜", "{{ko-IPA|박근혜|cap=y}}", "Pakkŭnhye", "mr")
	def test_Bakgeunhye_yr(self):
		return self.run_test("박ㄹ혜", "{{ko-IPA|박근혜|cap=y}}", "pak.kun.hyey", "yr")
	def test_Bakgeunhye_ipa(self):
		return self.run_test("박ㄹ혜", "{{ko-IPA|박근혜|cap=y}}", "[pa̠k̚k͈ɯnʝe̞] ~ [pa̠k̚k͈ɯnɦe̞]", "ipa")


	def test_Buhwal_juil_ph(self):
		return self.run_test("부활주일", "{{ko-IPA|l=y|cap=y|부활 주일}}", "부(ː)활 주일", "ph")
	def test_Buhwal_juil_rr(self):
		return self.run_test("부활주일", "{{ko-IPA|l=y|cap=y|부활 주일}}", "Buhwal ju'il", "rr")
	def test_Buhwal_juil_rrr(self):
		return self.run_test("부활주일", "{{ko-IPA|l=y|cap=y|부활 주일}}", "Buhwal ju'il", "rrr")
	def test_Buhwal_juil_mr(self):
		return self.run_test("부활주일", "{{ko-IPA|l=y|cap=y|부활 주일}}", "Puhwal chuil", "mr")
	def test_Buhwal_juil_yr(self):
		return self.run_test("부활주일", "{{ko-IPA|l=y|cap=y|부활 주일}}", "pūhwal cwuil", "yr")
	def test_Buhwal_juil_ipa(self):
		return self.run_test("부활주일", "{{ko-IPA|l=y|cap=y|부활 주일}}", "[ˈpu(ː)βwa̠ɭ t͡ɕuiɭ]", "ipa")

	def test_anda_ph(self):
		return self.run_test("안다", "{{ko-IPA|l=y|com=1|a=Ko-안따.ogg}}", "안(ː)따", "ph")
	def test_anda_rr(self):
		return self.run_test("안다", "{{ko-IPA|l=y|com=1|a=Ko-안따.ogg}}", "anda", "rr")
	def test_anda_rrr(self):
		return self.run_test("안다", "{{ko-IPA|l=y|com=1|a=Ko-안따.ogg}}", "anda", "rrr")
	def test_anda_mr(self):
		return self.run_test("안다", "{{ko-IPA|l=y|com=1|a=Ko-안따.ogg}}", "anta", "mr")
	def test_anda_yr(self):
		return self.run_test("안다", "{{ko-IPA|l=y|com=1|a=Ko-안따.ogg}}", "ānqta", "yr")
	def test_anda_ipa(self):
		return self.run_test("안다", "{{ko-IPA|l=y|com=1|a=Ko-안따.ogg}}", "[ˈa̠(ː)nt͈a̠]", "ipa")

	def test_ganeungseong_ph(self):
		return self.run_test("가능성", "{{ko-IPA|l=y|com=2}}", "가(ː)능썽", "ph")
	def test_ganeungseong_rr(self):
		return self.run_test("가능성", "{{ko-IPA|l=y|com=2}}", "ganeungseong", "rr")
	def test_ganeungseong_rrr(self):
		return self.run_test("가능성", "{{ko-IPA|l=y|com=2}}", "ganeungseong", "rrr")
	def test_ganeungseong_mr(self):
		return self.run_test("가능성", "{{ko-IPA|l=y|com=2}}", "kanŭngssŏng", "mr")
	def test_ganeungseong_yr(self):
		return self.run_test("가능성", "{{ko-IPA|l=y|com=2}}", "kānungqseng", "yr")
	def test_ganeungseong_ipa(self):
		return self.run_test("가능성", "{{ko-IPA|l=y|com=2}}", "[ˈka̠(ː)nɯŋs͈ʌ̹ŋ]", "ipa")

	def test_gom_ph(self):
		return self.run_test("곰", "{{ko-ipa|l=y|a=곰.wav}}", "곰(ː)", "ph")
	def test_gom_rr(self):
		return self.run_test("곰", "{{ko-ipa|l=y|a=곰.wav}}", "gom", "rr")
	def test_gom_rrr(self):
		return self.run_test("곰", "{{ko-ipa|l=y|a=곰.wav}}", "gom", "rrr")
	def test_gom_mr(self):
		return self.run_test("곰", "{{ko-ipa|l=y|a=곰.wav}}", "kom", "mr")
	def test_gom_yr(self):
		return self.run_test("곰", "{{ko-ipa|l=y|a=곰.wav}}", "kōm", "yr")
	def test_gom_ipa(self):
		return self.run_test("곰", "{{ko-ipa|l=y|a=곰.wav}}", "[ko̞(ː)m]", "ipa")

	def test_sin_ph(self):
		return self.run_test("신", "{{ko-IPA|com=0}}", "씬", "ph")
	def test_sin_rr(self):
		return self.run_test("신", "{{ko-IPA|com=0}}", "sin", "rr")
	def test_sin_rrr(self):
		return self.run_test("신", "{{ko-IPA|com=0}}", "sin", "rrr")
	def test_sin_mr(self):
		return self.run_test("신", "{{ko-IPA|com=0}}", "ssin", "mr")
	def test_sin_yr(self):
		return self.run_test("신", "{{ko-IPA|com=0}}", "qsin", "yr")
	def test_sin_ipa(self):
		return self.run_test("신", "{{ko-IPA|com=0}}", "[ɕ͈in]", "ipa")

	def test_jeotgarak_ph(self):
		return self.run_test("젓가락", "{{ko-IPA|nobc=1}}", "젇까락/저까락", "ph")
	def test_jeotgarak_rr(self):
		return self.run_test("젓가락", "{{ko-IPA|nobc=1}}", "jeotgarak", "rr")
	def test_jeotgarak_rrr(self):
		return self.run_test("젓가락", "{{ko-IPA|nobc=1}}", "jeosgalag", "rrr")
	def test_jeotgarak_mr(self):
		return self.run_test("젓가락", "{{ko-IPA|nobc=1}}", "chŏtkarak", "mr")
	def test_jeotgarak_yr(self):
		return self.run_test("젓가락", "{{ko-IPA|nobc=1}}", "ceskalak", "yr")
	def test_jeotgarak_ipa(self):
		return self.run_test("젓가락", "{{ko-IPA|nobc=1}}", "[t͡ɕʌ̹t̚k͈a̠ɾa̠k̚] ~ [t͡ɕʌ̹k͈a̠ɾa̠k̚]", "ipa")

	def test_Pyeongyang_ph(self):
		return self.run_test("평양", "{{ko-IPA|cap=y|a=Ko-{{PAGENAME}}.oga}}", "평양", "ph")
	def test_Pyeongyang_rr(self):
		return self.run_test("평양", "{{ko-IPA|cap=y|a=Ko-{{PAGENAME}}.oga}}", "Pyeong'yang", "rr")
	def test_Pyeongyang_rrr(self):
		return self.run_test("평양", "{{ko-IPA|cap=y|a=Ko-{{PAGENAME}}.oga}}", "Pyeong'yang", "rrr")
	def test_Pyeongyang_mr(self):
		return self.run_test("평양", "{{ko-IPA|cap=y|a=Ko-{{PAGENAME}}.oga}}", "P'yŏngyang", "mr")
	def test_Pyeongyang_yr(self):
		return self.run_test("평양", "{{ko-IPA|cap=y|a=Ko-{{PAGENAME}}.oga}}", "phyengyang", "yr")
	def test_Pyeongyang_ipa(self):
		return self.run_test("평양", "{{ko-IPA|cap=y|a=Ko-{{PAGENAME}}.oga}}", "[pʰjʌ̹ŋja̠ŋ]", "ipa")

	def test_Seoul_gonghwaguk_ph(self):
		return self.run_test("서울공화국", "{{ko-IPA|서울 공화국|l=4|cap=y}}", "서울 공(ː)화국", "ph")
	def test_Seoul_gonghwaguk_rr(self):
		return self.run_test("서울공화국", "{{ko-IPA|서울 공화국|l=4|cap=y}}", "Seoul gonghwaguk", "rr")
	def test_Seoul_gonghwaguk_rrr(self):
		return self.run_test("서울공화국", "{{ko-IPA|서울 공화국|l=4|cap=y}}", "Seoul gonghwagug", "rrr")
	def test_Seoul_gonghwaguk_mr(self):
		return self.run_test("서울공화국", "{{ko-IPA|서울 공화국|l=4|cap=y}}", "Sŏul konghwaguk", "mr")
	def test_Seoul_gonghwaguk_yr(self):
		return self.run_test("서울공화국", "{{ko-IPA|서울 공화국|l=4|cap=y}}", "sewul kōnghwakwuk", "yr")
	def test_Seoul_gonghwaguk_ipa(self):
		return self.run_test("서울공화국", "{{ko-IPA|서울 공화국|l=4|cap=y}}", "[sʰʌ̹uɭ ko̞(ː)ŋβwa̠ɡuk̚]", "ipa")

	def test_sagwa_ph(self):
		return self.run_test("사과", "{{ko-IPA|l=ˈsʰa̠gwa̠}}", "사과", "ph")
	def test_sagwa_rr(self):
		return self.run_test("사과", "{{ko-IPA|l=ˈsʰa̠gwa̠}}", "sagwa", "rr")
	def test_sagwa_rrr(self):
		return self.run_test("사과", "{{ko-IPA|l=ˈsʰa̠gwa̠}}", "sagwa", "rrr")
	def test_sagwa_mr(self):
		return self.run_test("사과", "{{ko-IPA|l=ˈsʰa̠gwa̠}}", "sagwa", "mr")
	def test_sagwa_yr(self):
		return self.run_test("사과", "{{ko-IPA|l=ˈsʰa̠gwa̠}}", "sakwa", "yr")
	def test_sagwa_ipa(self):
		return self.run_test("사과", "{{ko-IPA|l=ˈsʰa̠gwa̠}}", "[sʰa̠ɡwa̠]", "ipa")

	def test_naui_ph(self):
		return self.run_test("나의", "{{ko-IPA|ui=2}}", "나의/나이", "ph")
	def test_naui_rr(self):
		return self.run_test("나의", "{{ko-IPA|ui=2}}", "naui", "rr")
	def test_naui_rrr(self):
		return self.run_test("나의", "{{ko-IPA|ui=2}}", "naui", "rrr")
	def test_naui_mr(self):
		return self.run_test("나의", "{{ko-IPA|ui=2}}", "naŭi", "mr")
	def test_naui_yr(self):
		return self.run_test("나의", "{{ko-IPA|ui=2}}", "nauy", "yr")
	def test_naui_ipa(self):
		return self.run_test("나의", "{{ko-IPA|ui=2}}", "[na̠ɰi] ~ [na̠i]", "ipa")

	def test_Jang_ph(self):
		return self.run_test("장", "{{ko-ipa|cap=y}}", "장", "ph")
	def test_Jang_rr(self):
		return self.run_test("장", "{{ko-ipa|cap=y}}", "Jang", "rr")
	def test_Jang_rrr(self):
		return self.run_test("장", "{{ko-ipa|cap=y}}", "Jang", "rrr")
	def test_Jang_mr(self):
		return self.run_test("장", "{{ko-ipa|cap=y}}", "Chang", "mr")
	def test_Jang_yr(self):
		return self.run_test("장", "{{ko-ipa|cap=y}}", "cang", "yr")
	def test_Jang_ipa(self):
		return self.run_test("장", "{{ko-ipa|cap=y}}", "[t͡ɕa̠ŋ]", "ipa")

	def test_yeogwon_ph(self):
		return self.run_test("여권", "{{ko-IPA|com=1|l=y}}", "여(ː)꿘", "ph")
	def test_yeogwon_rr(self):
		return self.run_test("여권", "{{ko-IPA|com=1|l=y}}", "yeogwon", "rr")
	def test_yeogwon_rrr(self):
		return self.run_test("여권", "{{ko-IPA|com=1|l=y}}", "yeogwon", "rrr")
	def test_yeogwon_mr(self):
		return self.run_test("여권", "{{ko-IPA|com=1|l=y}}", "yŏkwŏn", "mr")
	def test_yeogwon_yr(self):
		return self.run_test("여권", "{{ko-IPA|com=1|l=y}}", "yēqkwen", "yr")
	def test_yeogwon_ipa(self):
		return self.run_test("여권", "{{ko-IPA|com=1|l=y}}", "[ˈjɘ(ː)k͈wʌ̹n]", "ipa")

	def test_jungibyeong_ph(self):
		return self.run_test("중2병", "{{ko-IPA|중이병|com=2}}", "중이뼝", "ph")
	def test_jungibyeong_rr(self):
		return self.run_test("중2병", "{{ko-IPA|중이병|com=2}}", "jung'ibyeong", "rr")
	def test_jungibyeong_rrr(self):
		return self.run_test("중2병", "{{ko-IPA|중이병|com=2}}", "jung'ibyeong", "rrr")
	def test_jungibyeong_mr(self):
		return self.run_test("중2병", "{{ko-IPA|중이병|com=2}}", "chungipyŏng", "mr")
	def test_jungibyeong_yr(self):
		return self.run_test("중2병", "{{ko-IPA|중이병|com=2}}", "cwungiqpyeng", "yr")
	def test_jungibyeong_ipa(self):
		return self.run_test("중2병", "{{ko-IPA|중이병|com=2}}", "[t͡ɕuŋip͈jʌ̹ŋ]", "ipa")

	def test_gongsanjuui_ph(self):
		return self.run_test("공산주의", "{{ko-IPA|l=y|ui=4}}", "공(ː)산주의/공(ː)산주이", "ph")
	def test_gongsanjuui_rr(self):
		return self.run_test("공산주의", "{{ko-IPA|l=y|ui=4}}", "gongsanjuui", "rr")
	def test_gongsanjuui_rrr(self):
		return self.run_test("공산주의", "{{ko-IPA|l=y|ui=4}}", "gongsanjuui", "rrr")
	def test_gongsanjuui_mr(self):
		return self.run_test("공산주의", "{{ko-IPA|l=y|ui=4}}", "kongsanjuŭi", "mr")
	def test_gongsanjuui_yr(self):
		return self.run_test("공산주의", "{{ko-IPA|l=y|ui=4}}", "kōngsan.cwuuy", "yr")
	def test_gongsanjuui_ipa(self):
		return self.run_test("공산주의", "{{ko-IPA|l=y|ui=4}}", "[ˈko̞(ː)ŋsʰa̠ɲd͡ʑuɰi] ~ [ˈko̞(ː)ŋsʰa̠ɲd͡ʑui]", "ipa")

	def test_dwitdari_ph(self):
		return self.run_test("뒷다리", "{{ko-IPA|l=y|nobc=1}}", "뒫(ː)따리/뒤(ː)따리", "ph")
	def test_dwitdari_rr(self):
		return self.run_test("뒷다리", "{{ko-IPA|l=y|nobc=1}}", "dwitdari", "rr")
	def test_dwitdari_rrr(self):
		return self.run_test("뒷다리", "{{ko-IPA|l=y|nobc=1}}", "dwisdali", "rrr")
	def test_dwitdari_mr(self):
		return self.run_test("뒷다리", "{{ko-IPA|l=y|nobc=1}}", "twittari", "mr")
	def test_dwitdari_yr(self):
		return self.run_test("뒷다리", "{{ko-IPA|l=y|nobc=1}}", "twīstali", "yr")
	def test_dwitdari_ipa(self):
		return self.run_test("뒷다리", "{{ko-IPA|l=y|nobc=1}}", "[ˈtɥi(ː)t̚t͈a̠ɾi] ~ [ˈtɥi(ː)t͈a̠ɾi] ~ [ˈty(ː)t̚t͈a̠ɾi] ~ [ˈty(ː)t͈a̠ɾi]", "ipa")

	def test_nakcheonjuuija_ph(self):
		return self.run_test("낙천주의자", "{{ko-IPA|ui=4}}", "낙천주의자/낙천주이자", "ph")
	def test_nakcheonjuuija_rr(self):
		return self.run_test("낙천주의자", "{{ko-IPA|ui=4}}", "nakcheonjuuija", "rr")
	def test_nakcheonjuuija_rrr(self):
		return self.run_test("낙천주의자", "{{ko-IPA|ui=4}}", "nagcheonjuuija", "rrr")
	def test_nakcheonjuuija_mr(self):
		return self.run_test("낙천주의자", "{{ko-IPA|ui=4}}", "nakch'ŏnjuŭija", "mr")
	def test_nakcheonjuuija_yr(self):
		return self.run_test("낙천주의자", "{{ko-IPA|ui=4}}", "nakchen.cwuuyca", "yr")
	def test_nakcheonjuuija_ipa(self):
		return self.run_test("낙천주의자", "{{ko-IPA|ui=4}}", "[na̠k̚t͡ɕʰʌ̹ɲd͡ʑuɰid͡ʑa̠] ~ [na̠k̚t͡ɕʰʌ̹ɲd͡ʑuid͡ʑa̠]", "ipa")

	def test_huinnimagireogi_ph(self):
		return self.run_test("흰이마기러기", "{{ko-IPA|ni=2}}", "힌니마기러기", "ph")
	def test_huinnimagireogi_rr(self):
		return self.run_test("흰이마기러기", "{{ko-IPA|ni=2}}", "huinnimagireogi", "rr")
	def test_huinnimagireogi_rrr(self):
		return self.run_test("흰이마기러기", "{{ko-IPA|ni=2}}", "huin'imagileogi", "rrr")
	def test_huinnimagireogi_mr(self):
		return self.run_test("흰이마기러기", "{{ko-IPA|ni=2}}", "hŭinnimagirŏgi", "mr")
	def test_huinnimagireogi_yr(self):
		return self.run_test("흰이마기러기", "{{ko-IPA|ni=2}}", "huynnimakileki", "yr")
	def test_huinnimagireogi_ipa(self):
		return self.run_test("흰이마기러기", "{{ko-IPA|ni=2}}", "[çinnima̠ɡiɾʌ̹ɡi]", "ipa")

	def test_hangon_dongmul_ph(self):
		return self.run_test("항온동물", "{{ko-IPA|항온 동물|l=4}}", "항온 동(ː)물", "ph")
	def test_hangon_dongmul_rr(self):
		return self.run_test("항온동물", "{{ko-IPA|항온 동물|l=4}}", "hang'on dongmul", "rr")
	def test_hangon_dongmul_rrr(self):
		return self.run_test("항온동물", "{{ko-IPA|항온 동물|l=4}}", "hang'on dongmul", "rrr")
	def test_hangon_dongmul_mr(self):
		return self.run_test("항온동물", "{{ko-IPA|항온 동물|l=4}}", "hangon tongmul", "mr")
	def test_hangon_dongmul_yr(self):
		return self.run_test("항온동물", "{{ko-IPA|항온 동물|l=4}}", "hangon tōngmul", "yr")
	def test_hangon_dongmul_ipa(self):
		return self.run_test("항온동물", "{{ko-IPA|항온 동물|l=4}}", "[ha̠ŋo̞n to̞(ː)ŋmuɭ]", "ipa")

	def test_badanmulgogi_ph(self):
		return self.run_test("바닷물고기", "{{ko-IPA|com=3}}", "바단물꼬기", "ph")
	def test_badanmulgogi_rr(self):
		return self.run_test("바닷물고기", "{{ko-IPA|com=3}}", "badanmulgogi", "rr")
	def test_badanmulgogi_rrr(self):
		return self.run_test("바닷물고기", "{{ko-IPA|com=3}}", "badasmulgogi", "rrr")
	def test_badanmulgogi_mr(self):
		return self.run_test("바닷물고기", "{{ko-IPA|com=3}}", "padanmulkogi", "mr")
	def test_badanmulgogi_yr(self):
		return self.run_test("바닷물고기", "{{ko-IPA|com=3}}", "patasmulqkoki", "yr")
	def test_badanmulgogi_ipa(self):
		return self.run_test("바닷물고기", "{{ko-IPA|com=3}}", "[pa̠da̠nmuɭk͈o̞ɡi]", "ipa")

	def test_siseutem_ph(self):
		return self.run_test("시스템", "{{ko-IPA|com=0}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "씨스템", "ph")
	def test_siseutem_rr(self):
		return self.run_test("시스템", "{{ko-IPA|com=0}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "siseutem", "rr")
	def test_siseutem_rrr(self):
		return self.run_test("시스템", "{{ko-IPA|com=0}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "siseutem", "rrr")
	def test_siseutem_mr(self):
		return self.run_test("시스템", "{{ko-IPA|com=0}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "ssisŭt'em", "mr")
	def test_siseutem_yr(self):
		return self.run_test("시스템", "{{ko-IPA|com=0}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "qsisu.theym", "yr")
	def test_siseutem_ipa(self):
		return self.run_test("시스템", "{{ko-IPA|com=0}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "[ɕ͈isʰɯtʰe̞m]", "ipa")

	def test_musinnon_ph(self):
		return self.run_test("무신론", "{{ko-IPA|nn=3}}", "무신논", "ph")
	def test_musinnon_rr(self):
		return self.run_test("무신론", "{{ko-IPA|nn=3}}", "musinnon", "rr")
	def test_musinnon_rrr(self):
		return self.run_test("무신론", "{{ko-IPA|nn=3}}", "musinlon", "rrr")
	def test_musinnon_mr(self):
		return self.run_test("무신론", "{{ko-IPA|nn=3}}", "musinnon", "mr")
	def test_musinnon_yr(self):
		return self.run_test("무신론", "{{ko-IPA|nn=3}}", "musinlon", "yr")
	def test_musinnon_ipa(self):
		return self.run_test("무신론", "{{ko-IPA|nn=3}}", "[muɕʰinno̞n]", "ipa")

	def test_beomsinnon_ph(self):
		return self.run_test("범신론", "{{ko-IPA|l=y|nn=3}}", "범(ː)신논", "ph")
	def test_beomsinnon_rr(self):
		return self.run_test("범신론", "{{ko-IPA|l=y|nn=3}}", "beomsinnon", "rr")
	def test_beomsinnon_rrr(self):
		return self.run_test("범신론", "{{ko-IPA|l=y|nn=3}}", "beomsinlon", "rrr")
	def test_beomsinnon_mr(self):
		return self.run_test("범신론", "{{ko-IPA|l=y|nn=3}}", "pŏmsinnon", "mr")
	def test_beomsinnon_yr(self):
		return self.run_test("범신론", "{{ko-IPA|l=y|nn=3}}", "pēmsinlon", "yr")
	def test_beomsinnon_ipa(self):
		return self.run_test("범신론", "{{ko-IPA|l=y|nn=3}}", "[ˈpɘ(ː)mɕʰinno̞n]", "ipa")

	def test_ilsinnon_ph(self):
		return self.run_test("일신론", "{{ko-IPA|com=1|nn=3}}", "일씬논", "ph")
	def test_ilsinnon_rr(self):
		return self.run_test("일신론", "{{ko-IPA|com=1|nn=3}}", "ilsinnon", "rr")
	def test_ilsinnon_rrr(self):
		return self.run_test("일신론", "{{ko-IPA|com=1|nn=3}}", "ilsinlon", "rrr")
	def test_ilsinnon_mr(self):
		return self.run_test("일신론", "{{ko-IPA|com=1|nn=3}}", "ilssinnon", "mr")
	def test_ilsinnon_yr(self):
		return self.run_test("일신론", "{{ko-IPA|com=1|nn=3}}", "ilqsinlon", "yr")
	def test_ilsinnon_ipa(self):
		return self.run_test("일신론", "{{ko-IPA|com=1|nn=3}}", "[iɭɕ͈inno̞n]", "ipa")

	def test_Roseuaenjelleseu_ph(self):
		return self.run_test("로스앤젤레스", "{{ko-IPA|cap=y|com=1,5}}", "로쓰앤젤레쓰/로쓰엔젤레쓰", "ph")
	def test_Roseuaenjelleseu_rr(self):
		return self.run_test("로스앤젤레스", "{{ko-IPA|cap=y|com=1,5}}", "Roseuaenjelleseu", "rr")
	def test_Roseuaenjelleseu_rrr(self):
		return self.run_test("로스앤젤레스", "{{ko-IPA|cap=y|com=1,5}}", "Loseuaenjelleseu", "rrr")
	def test_Roseuaenjelleseu_mr(self):
		return self.run_test("로스앤젤레스", "{{ko-IPA|cap=y|com=1,5}}", "Rossŭaenjellessŭ", "mr")
	def test_Roseuaenjelleseu_yr(self):
		return self.run_test("로스앤젤레스", "{{ko-IPA|cap=y|com=1,5}}", "loqsuayn.ceylleyqsu", "yr")
	def test_Roseuaenjelleseu_ipa(self):
		return self.run_test("로스앤젤레스", "{{ko-IPA|cap=y|com=1,5}}", "[ɾo̞s͈ɯɛɲd͡ʑe̞ɭɭe̞s͈ɯ] ~ [ɾo̞s͈ɯe̞ɲd͡ʑe̞ɭɭe̞s͈ɯ]", "ipa")

	def test_imiji_ph(self):
		return self.run_test("이미지", "{{ko-IPA|a=Ko-{{PAGENAME}}.oga}}", "이미지", "ph")
	def test_imiji_rr(self):
		return self.run_test("이미지", "{{ko-IPA|a=Ko-{{PAGENAME}}.oga}}", "imiji", "rr")
	def test_imiji_rrr(self):
		return self.run_test("이미지", "{{ko-IPA|a=Ko-{{PAGENAME}}.oga}}", "imiji", "rrr")
	def test_imiji_mr(self):
		return self.run_test("이미지", "{{ko-IPA|a=Ko-{{PAGENAME}}.oga}}", "imiji", "mr")
	def test_imiji_yr(self):
		return self.run_test("이미지", "{{ko-IPA|a=Ko-{{PAGENAME}}.oga}}", "imici", "yr")
	def test_imiji_ipa(self):
		return self.run_test("이미지", "{{ko-IPA|a=Ko-{{PAGENAME}}.oga}}", "[imid͡ʑi]", "ipa")

	def test_Saudi_ph(self):
		return self.run_test("사우디", "{{ko-IPA|사우디|cap=y|com=0}}", "싸우디", "ph")
	def test_Saudi_rr(self):
		return self.run_test("사우디", "{{ko-IPA|사우디|cap=y|com=0}}", "Saudi", "rr")
	def test_Saudi_rrr(self):
		return self.run_test("사우디", "{{ko-IPA|사우디|cap=y|com=0}}", "Saudi", "rrr")
	def test_Saudi_mr(self):
		return self.run_test("사우디", "{{ko-IPA|사우디|cap=y|com=0}}", "Ssaudi", "mr")
	def test_Saudi_yr(self):
		return self.run_test("사우디", "{{ko-IPA|사우디|cap=y|com=0}}", "qsawuti", "yr")
	def test_Saudi_ipa(self):
		return self.run_test("사우디", "{{ko-IPA|사우디|cap=y|com=0}}", "[s͈a̠udi]", "ipa")

	def test_Ulsan_ph(self):
		return self.run_test("울산", "{{ko-IPA|cap=y|com=1}}", "울싼", "ph")
	def test_Ulsan_rr(self):
		return self.run_test("울산", "{{ko-IPA|cap=y|com=1}}", "Ulsan", "rr")
	def test_Ulsan_rrr(self):
		return self.run_test("울산", "{{ko-IPA|cap=y|com=1}}", "Ulsan", "rrr")
	def test_Ulsan_mr(self):
		return self.run_test("울산", "{{ko-IPA|cap=y|com=1}}", "Ulssan", "mr")
	def test_Ulsan_yr(self):
		return self.run_test("울산", "{{ko-IPA|cap=y|com=1}}", "wulqsan", "yr")
	def test_Ulsan_ipa(self):
		return self.run_test("울산", "{{ko-IPA|cap=y|com=1}}", "[uɭs͈a̠n]", "ipa")

	def test_Banggeulladesi_ph(self):
		return self.run_test("방글라데시", "{{ko-IPA|cap=y|com=4}}", "방글라데씨", "ph")
	def test_Banggeulladesi_rr(self):
		return self.run_test("방글라데시", "{{ko-IPA|cap=y|com=4}}", "Banggeulladesi", "rr")
	def test_Banggeulladesi_rrr(self):
		return self.run_test("방글라데시", "{{ko-IPA|cap=y|com=4}}", "Banggeulladesi", "rrr")
	def test_Banggeulladesi_mr(self):
		return self.run_test("방글라데시", "{{ko-IPA|cap=y|com=4}}", "Panggŭlladessi", "mr")
	def test_Banggeulladesi_yr(self):
		return self.run_test("방글라데시", "{{ko-IPA|cap=y|com=4}}", "pangkullateyqsi", "yr")
	def test_Banggeulladesi_ipa(self):
		return self.run_test("방글라데시", "{{ko-IPA|cap=y|com=4}}", "[pa̠ŋɡɯɭɭa̠de̞ɕ͈i]", "ipa")

	def test_beoseu_ph(self):
		return self.run_test("버스", "{{ko-IPA|com=0,1|a=Ko-버스.ogg}}", "뻐쓰", "ph")
	def test_beoseu_rr(self):
		return self.run_test("버스", "{{ko-IPA|com=0,1|a=Ko-버스.ogg}}", "beoseu", "rr")
	def test_beoseu_rrr(self):
		return self.run_test("버스", "{{ko-IPA|com=0,1|a=Ko-버스.ogg}}", "beoseu", "rrr")
	def test_beoseu_mr(self):
		return self.run_test("버스", "{{ko-IPA|com=0,1|a=Ko-버스.ogg}}", "pŏssŭ", "mr")
	def test_beoseu_yr(self):
		return self.run_test("버스", "{{ko-IPA|com=0,1|a=Ko-버스.ogg}}", "qpeqsu", "yr")
	def test_beoseu_ipa(self):
		return self.run_test("버스", "{{ko-IPA|com=0,1|a=Ko-버스.ogg}}", "[p͈ʌ̹s͈ɯ]", "ipa")

	def test_seobiseu_ph(self):
		return self.run_test("서비스", "{{ko-IPA|com=0,2}}", "써비쓰", "ph")
	def test_seobiseu_rr(self):
		return self.run_test("서비스", "{{ko-IPA|com=0,2}}", "seobiseu", "rr")
	def test_seobiseu_rrr(self):
		return self.run_test("서비스", "{{ko-IPA|com=0,2}}", "seobiseu", "rrr")
	def test_seobiseu_mr(self):
		return self.run_test("서비스", "{{ko-IPA|com=0,2}}", "ssŏbissŭ", "mr")
	def test_seobiseu_yr(self):
		return self.run_test("서비스", "{{ko-IPA|com=0,2}}", "qsepiqsu", "yr")
	def test_seobiseu_ipa(self):
		return self.run_test("서비스", "{{ko-IPA|com=0,2}}", "[s͈ʌ̹bis͈ɯ]", "ipa")

	def test_bamsae_bamssae_ph(self):
		return self.run_test("밤새", "{{ko-IPA||밤쌔}}", "밤새/밤세/밤쌔/밤쎄", "ph")
	def test_bamsae_bamssae_rr(self):
		return self.run_test("밤새", "{{ko-IPA||밤쌔}}", "bamsae/bamssae", "rr")
	def test_bamsae_bamssae_rrr(self):
		return self.run_test("밤새", "{{ko-IPA||밤쌔}}", "bamsae/bamssae", "rrr")
	def test_bamsae_bamssae_mr(self):
		return self.run_test("밤새", "{{ko-IPA||밤쌔}}", "pamsae/pamssae", "mr")
	def test_bamsae_bamssae_yr(self):
		return self.run_test("밤새", "{{ko-IPA||밤쌔}}", "pamsay/pamssay", "yr")
	def test_bamsae_bamssae_ipa(self):
		return self.run_test("밤새", "{{ko-IPA||밤쌔}}", "[pa̠msʰɛ] ~ [pa̠msʰe̞] ~ [pa̠ms͈ɛ] ~ [pa̠ms͈e̞]", "ipa")

	def test_modeun_ph(self):
		return self.run_test("모든", "{{ko-IPA|l=y||a=y}}", "모(ː)든", "ph")
	def test_modeun_rr(self):
		return self.run_test("모든", "{{ko-IPA|l=y||a=y}}", "modeun", "rr")
	def test_modeun_rrr(self):
		return self.run_test("모든", "{{ko-IPA|l=y||a=y}}", "modeun", "rrr")
	def test_modeun_mr(self):
		return self.run_test("모든", "{{ko-IPA|l=y||a=y}}", "modŭn", "mr")
	def test_modeun_yr(self):
		return self.run_test("모든", "{{ko-IPA|l=y||a=y}}", "mōtun", "yr")
	def test_modeun_ipa(self):
		return self.run_test("모든", "{{ko-IPA|l=y||a=y}}", "[ˈmo̞(ː)dɯn]", "ipa")

	def test_hoeui_ph(self):
		return self.run_test("회의", "{{ko-IPA|l=y|ui=2}}", "훼(ː)의/훼(ː)의/회(ː)의/회(ː)이", "ph")
	def test_hoeui_rr(self):
		return self.run_test("회의", "{{ko-IPA|l=y|ui=2}}", "hoe'ui", "rr")
	def test_hoeui_rrr(self):
		return self.run_test("회의", "{{ko-IPA|l=y|ui=2}}", "hoe'ui", "rrr")
	def test_hoeui_mr(self):
		return self.run_test("회의", "{{ko-IPA|l=y|ui=2}}", "hoeŭi", "mr")
	def test_hoeui_yr(self):
		return self.run_test("회의", "{{ko-IPA|l=y|ui=2}}", "hōy.uy", "yr")
	def test_hoeui_ipa(self):
		return self.run_test("회의", "{{ko-IPA|l=y|ui=2}}", "[ˈɸwe̞(ː)ɰi] ~ [ˈɸwe̞(ː)ɰi] ~ [ˈhø̞(ː)ɰi] ~ [ˈhø̞(ː)i]", "ipa")

	def test_imgeum_ph(self):
		return self.run_test("임금", "{{ko-IPA|l=n}}", "임금", "ph")
	def test_imgeum_rr(self):
		return self.run_test("임금", "{{ko-IPA|l=n}}", "imgeum", "rr")
	def test_imgeum_rrr(self):
		return self.run_test("임금", "{{ko-IPA|l=n}}", "imgeum", "rrr")
	def test_imgeum_mr(self):
		return self.run_test("임금", "{{ko-IPA|l=n}}", "imgŭm", "mr")
	def test_imgeum_yr(self):
		return self.run_test("임금", "{{ko-IPA|l=n}}", "imkum", "yr")
	def test_imgeum_ipa(self):
		return self.run_test("임금", "{{ko-IPA|l=n}}", "[imɡɯm]", "ipa")

	def test_masitge_deuseyo_ph(self):
		return self.run_test("맛있게 드세요", "{{ko-IPA|svar=1|a=맛있게 드세요.ogg}}", "마싣께 드세요/마딛께 드세요", "ph")
	def test_masitge_deuseyo_rr(self):
		return self.run_test("맛있게 드세요", "{{ko-IPA|svar=1|a=맛있게 드세요.ogg}}", "masitge deuseyo", "rr")
	def test_masitge_deuseyo_rrr(self):
		return self.run_test("맛있게 드세요", "{{ko-IPA|svar=1|a=맛있게 드세요.ogg}}", "mas'issge deuseyo", "rrr")
	def test_masitge_deuseyo_mr(self):
		return self.run_test("맛있게 드세요", "{{ko-IPA|svar=1|a=맛있게 드세요.ogg}}", "masitke tŭseyo", "mr")
	def test_masitge_deuseyo_yr(self):
		return self.run_test("맛있게 드세요", "{{ko-IPA|svar=1|a=맛있게 드세요.ogg}}", "mas.isskey tuseyyo", "yr")
	def test_masitge_deuseyo_ipa(self):
		return self.run_test("맛있게 드세요", "{{ko-IPA|svar=1|a=맛있게 드세요.ogg}}", "[ma̠ɕʰit̚k͈e̞ tɯsʰe̞jo] ~ [ma̠dit̚k͈e̞ tɯsʰe̞jo]", "ipa")

	def test_badatga_ph(self):
		return self.run_test("바닷가", "{{ko-IPA|nobc=2}}", "바닫까/바다까", "ph")
	def test_badatga_rr(self):
		return self.run_test("바닷가", "{{ko-IPA|nobc=2}}", "badatga", "rr")
	def test_badatga_rrr(self):
		return self.run_test("바닷가", "{{ko-IPA|nobc=2}}", "badasga", "rrr")
	def test_badatga_mr(self):
		return self.run_test("바닷가", "{{ko-IPA|nobc=2}}", "padatka", "mr")
	def test_badatga_yr(self):
		return self.run_test("바닷가", "{{ko-IPA|nobc=2}}", "pataska", "yr")
	def test_badatga_ipa(self):
		return self.run_test("바닷가", "{{ko-IPA|nobc=2}}", "[pa̠da̠t̚k͈a̠] ~ [pa̠da̠k͈a̠]", "ipa")

	def test_seuteureseu_ph(self):
		return self.run_test("스트레스", "{{ko-IPA|com=3}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "스트레쓰", "ph")
	def test_seuteureseu_rr(self):
		return self.run_test("스트레스", "{{ko-IPA|com=3}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "seuteureseu", "rr")
	def test_seuteureseu_rrr(self):
		return self.run_test("스트레스", "{{ko-IPA|com=3}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "seuteuleseu", "rrr")
	def test_seuteureseu_mr(self):
		return self.run_test("스트레스", "{{ko-IPA|com=3}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "sŭt'ŭressŭ", "mr")
	def test_seuteureseu_yr(self):
		return self.run_test("스트레스", "{{ko-IPA|com=3}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "su.thuleyqsu", "yr")
	def test_seuteureseu_ipa(self):
		return self.run_test("스트레스", "{{ko-IPA|com=3}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "[sʰɯtʰɯɾe̞s͈ɯ]", "ipa")

	def test_ttwieonada_ph(self):
		return self.run_test("뛰어나다", "{{ko-IPA|iot=2}}", "뛰어나다/뛰여나다", "ph")
	def test_ttwieonada_rr(self):
		return self.run_test("뛰어나다", "{{ko-IPA|iot=2}}", "ttwieonada", "rr")
	def test_ttwieonada_rrr(self):
		return self.run_test("뛰어나다", "{{ko-IPA|iot=2}}", "ttwieonada", "rrr")
	def test_ttwieonada_mr(self):
		return self.run_test("뛰어나다", "{{ko-IPA|iot=2}}", "ttwiŏnada", "mr")
	def test_ttwieonada_yr(self):
		return self.run_test("뛰어나다", "{{ko-IPA|iot=2}}", "ttwienata", "yr")
	def test_ttwieonada_ipa(self):
		return self.run_test("뛰어나다", "{{ko-IPA|iot=2}}", "[t͈ɥiʌ̹na̠da̠] ~ [t͈ɥijʌ̹na̠da̠] ~ [t͈yʌ̹na̠da̠] ~ [t͈yjʌ̹na̠da̠]", "ipa")

	def test_geonmangjeung_ph(self):
		return self.run_test("건망증", "{{ko-IPA|com=2|l=y}}", "건(ː)망쯩", "ph")
	def test_geonmangjeung_rr(self):
		return self.run_test("건망증", "{{ko-IPA|com=2|l=y}}", "geonmangjeung", "rr")
	def test_geonmangjeung_rrr(self):
		return self.run_test("건망증", "{{ko-IPA|com=2|l=y}}", "geonmangjeung", "rrr")
	def test_geonmangjeung_mr(self):
		return self.run_test("건망증", "{{ko-IPA|com=2|l=y}}", "kŏnmangchŭng", "mr")
	def test_geonmangjeung_yr(self):
		return self.run_test("건망증", "{{ko-IPA|com=2|l=y}}", "kēnmangqcung", "yr")
	def test_geonmangjeung_ipa(self):
		return self.run_test("건망증", "{{ko-IPA|com=2|l=y}}", "[ˈkɘ(ː)nma̠ŋt͡ɕ͈ɯŋ]", "ipa")

	def test_Suragan_ph(self):
		return self.run_test("수라간", "{{ko-IPA|com=2|cap=y}}", "수라깐", "ph")
	def test_Suragan_rr(self):
		return self.run_test("수라간", "{{ko-IPA|com=2|cap=y}}", "Suragan", "rr")
	def test_Suragan_rrr(self):
		return self.run_test("수라간", "{{ko-IPA|com=2|cap=y}}", "Sulagan", "rrr")
	def test_Suragan_mr(self):
		return self.run_test("수라간", "{{ko-IPA|com=2|cap=y}}", "Surakan", "mr")
	def test_Suragan_yr(self):
		return self.run_test("수라간", "{{ko-IPA|com=2|cap=y}}", "swulaqkan", "yr")
	def test_Suragan_ipa(self):
		return self.run_test("수라간", "{{ko-IPA|com=2|cap=y}}", "[sʰuɾa̠k͈a̠n]", "ipa")

	def test_sasangui_jipyeongseon_ph(self):
		return self.run_test("사상의 지평선", "{{ko-IPA|l=y|uie=3}}", "사(ː)상의 지평선/사(ː)상에 지평선", "ph")
	def test_sasangui_jipyeongseon_rr(self):
		return self.run_test("사상의 지평선", "{{ko-IPA|l=y|uie=3}}", "sasang'ui jipyeongseon", "rr")
	def test_sasangui_jipyeongseon_rrr(self):
		return self.run_test("사상의 지평선", "{{ko-IPA|l=y|uie=3}}", "sasang'ui jipyeongseon", "rrr")
	def test_sasangui_jipyeongseon_mr(self):
		return self.run_test("사상의 지평선", "{{ko-IPA|l=y|uie=3}}", "sasangŭi chip'yŏngsŏn", "mr")
	def test_sasangui_jipyeongseon_yr(self):
		return self.run_test("사상의 지평선", "{{ko-IPA|l=y|uie=3}}", "sāsanguy ci.phyengsen", "yr")
	def test_sasangui_jipyeongseon_ipa(self):
		return self.run_test("사상의 지평선", "{{ko-IPA|l=y|uie=3}}", "[ˈsʰa̠(ː)sʰa̠ŋɰi t͡ɕipʰjʌ̹ŋsʰʌ̹n] ~ [ˈsʰa̠(ː)sʰa̠ŋe̞ t͡ɕipʰjʌ̹ŋsʰʌ̹n]", "ipa")

	def test_jeongsin_bunyeoljeung_ph(self):
		return self.run_test("정신분열증", "{{ko-IPA|정신 분열증|com=5}}", "정신 부녈쯩", "ph")
	def test_jeongsin_bunyeoljeung_rr(self):
		return self.run_test("정신분열증", "{{ko-IPA|정신 분열증|com=5}}", "jeongsin bunyeoljeung", "rr")
	def test_jeongsin_bunyeoljeung_rrr(self):
		return self.run_test("정신분열증", "{{ko-IPA|정신 분열증|com=5}}", "jeongsin bun'yeoljeung", "rrr")
	def test_jeongsin_bunyeoljeung_mr(self):
		return self.run_test("정신분열증", "{{ko-IPA|정신 분열증|com=5}}", "chŏngsin punyŏlchŭng", "mr")
	def test_jeongsin_bunyeoljeung_yr(self):
		return self.run_test("정신분열증", "{{ko-IPA|정신 분열증|com=5}}", "cengsin pun.yelqcung", "yr")
	def test_jeongsin_bunyeoljeung_ipa(self):
		return self.run_test("정신분열증", "{{ko-IPA|정신 분열증|com=5}}", "[t͡ɕʌ̹ŋɕʰin puɲʌ̹ʎt͡ɕ͈ɯŋ]", "ipa")

	def test_mokjeokgyeok_josa_ph(self):
		return self.run_test("목적격조사", "{{ko-IPA|목적격 조사|l=5}}", "목쩍껵 조(ː)사", "ph")
	def test_mokjeokgyeok_josa_rr(self):
		return self.run_test("목적격조사", "{{ko-IPA|목적격 조사|l=5}}", "mokjeokgyeok josa", "rr")
	def test_mokjeokgyeok_josa_rrr(self):
		return self.run_test("목적격조사", "{{ko-IPA|목적격 조사|l=5}}", "mogjeoggyeog josa", "rrr")
	def test_mokjeokgyeok_josa_mr(self):
		return self.run_test("목적격조사", "{{ko-IPA|목적격 조사|l=5}}", "mokchŏkkyŏk chosa", "mr")
	def test_mokjeokgyeok_josa_yr(self):
		return self.run_test("목적격조사", "{{ko-IPA|목적격 조사|l=5}}", "mokcek.kyek cōsa", "yr")
	def test_mokjeokgyeok_josa_ipa(self):
		return self.run_test("목적격조사", "{{ko-IPA|목적격 조사|l=5}}", "[mo̞k̚t͡ɕ͈ʌ̹k̚k͈jʌ̹k̚ t͡ɕo̞(ː)sʰa̠]", "ipa")

	def test_dakeuseokeul_ph(self):
		return self.run_test("다크서클", "{{ko-IPA|com=2}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "다크써클", "ph")
	def test_dakeuseokeul_rr(self):
		return self.run_test("다크서클", "{{ko-IPA|com=2}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "dakeuseokeul", "rr")
	def test_dakeuseokeul_rrr(self):
		return self.run_test("다크서클", "{{ko-IPA|com=2}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "dakeuseokeul", "rrr")
	def test_dakeuseokeul_mr(self):
		return self.run_test("다크서클", "{{ko-IPA|com=2}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "tak'ŭssŏk'ŭl", "mr")
	def test_dakeuseokeul_yr(self):
		return self.run_test("다크서클", "{{ko-IPA|com=2}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "ta.khuqse.khul", "yr")
	def test_dakeuseokeul_ipa(self):
		return self.run_test("다크서클", "{{ko-IPA|com=2}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "[ta̠kxɯs͈ʌ̹kxɯɭ]", "ipa")

	def test_Ijipteu_arap_gonghwaguk_ph(self):
		return self.run_test("이집트 아랍 공화국", "{{ko-IPA|cap=y|l=8}}", "이집트 아랍 공(ː)화국", "ph")
	def test_Ijipteu_arap_gonghwaguk_rr(self):
		return self.run_test("이집트 아랍 공화국", "{{ko-IPA|cap=y|l=8}}", "Ijipteu arap gonghwaguk", "rr")
	def test_Ijipteu_arap_gonghwaguk_rrr(self):
		return self.run_test("이집트 아랍 공화국", "{{ko-IPA|cap=y|l=8}}", "Ijibteu alab gonghwagug", "rrr")
	def test_Ijipteu_arap_gonghwaguk_mr(self):
		return self.run_test("이집트 아랍 공화국", "{{ko-IPA|cap=y|l=8}}", "Ijipt'ŭ arap konghwaguk", "mr")
	def test_Ijipteu_arap_gonghwaguk_yr(self):
		return self.run_test("이집트 아랍 공화국", "{{ko-IPA|cap=y|l=8}}", "icipthu alap kōnghwakwuk", "yr")
	def test_Ijipteu_arap_gonghwaguk_ipa(self):
		return self.run_test("이집트 아랍 공화국", "{{ko-IPA|cap=y|l=8}}", "[id͡ʑip̚tʰɯ a̠ɾa̠p̚ ko̞(ː)ŋβwa̠ɡuk̚]", "ipa")

	def test_kkamagwitgwa_ph(self):
		return self.run_test("까마귓과", "{{ko-IPA|nobc=3}}", "까마귇꽈/까마귀꽈", "ph")
	def test_kkamagwitgwa_rr(self):
		return self.run_test("까마귓과", "{{ko-IPA|nobc=3}}", "kkamagwitgwa", "rr")
	def test_kkamagwitgwa_rrr(self):
		return self.run_test("까마귓과", "{{ko-IPA|nobc=3}}", "kkamagwisgwa", "rrr")
	def test_kkamagwitgwa_mr(self):
		return self.run_test("까마귓과", "{{ko-IPA|nobc=3}}", "kkamagwitkwa", "mr")
	def test_kkamagwitgwa_yr(self):
		return self.run_test("까마귓과", "{{ko-IPA|nobc=3}}", "kkamakwiskwa", "yr")
	def test_kkamagwitgwa_ipa(self):
		return self.run_test("까마귓과", "{{ko-IPA|nobc=3}}", "[k͈a̠ma̠ɡɥit̚k͈wa̠] ~ [k͈a̠ma̠ɡɥik͈wa̠] ~ [k͈a̠ma̠ɡyt̚k͈wa̠] ~ [k͈a̠ma̠ɡyk͈wa̠]", "ipa")

	def test_Seonggyeong_ph(self):
		return self.run_test("성경", "{{ko-IPA|cap=y|l=y}}", "성(ː)경", "ph")
	def test_Seonggyeong_rr(self):
		return self.run_test("성경", "{{ko-IPA|cap=y|l=y}}", "Seonggyeong", "rr")
	def test_Seonggyeong_rrr(self):
		return self.run_test("성경", "{{ko-IPA|cap=y|l=y}}", "Seonggyeong", "rrr")
	def test_Seonggyeong_mr(self):
		return self.run_test("성경", "{{ko-IPA|cap=y|l=y}}", "Sŏnggyŏng", "mr")
	def test_Seonggyeong_yr(self):
		return self.run_test("성경", "{{ko-IPA|cap=y|l=y}}", "sēngkyeng", "yr")
	def test_Seonggyeong_ipa(self):
		return self.run_test("성경", "{{ko-IPA|cap=y|l=y}}", "[ˈsʰɘ(ː)ŋɡjʌ̹ŋ]", "ipa")

	def test_Taepyeongnyang_ph(self):
		return self.run_test("태평양", "{{ko-IPA|cap=y|ni=3}}", "태평냥/테평냥", "ph")
	def test_Taepyeongnyang_rr(self):
		return self.run_test("태평양", "{{ko-IPA|cap=y|ni=3}}", "Taepyeongnyang", "rr")
	def test_Taepyeongnyang_rrr(self):
		return self.run_test("태평양", "{{ko-IPA|cap=y|ni=3}}", "Taepyeong'yang", "rrr")
	def test_Taepyeongnyang_mr(self):
		return self.run_test("태평양", "{{ko-IPA|cap=y|ni=3}}", "T'aep'yŏngnyang", "mr")
	def test_Taepyeongnyang_yr(self):
		return self.run_test("태평양", "{{ko-IPA|cap=y|ni=3}}", "thay.phyengnyang", "yr")
	def test_Taepyeongnyang_ipa(self):
		return self.run_test("태평양", "{{ko-IPA|cap=y|ni=3}}", "[tʰɛpʰjʌ̹ŋɲa̠ŋ] ~ [tʰe̞pʰjʌ̹ŋɲa̠ŋ]", "ipa")

	def test_Joseon_minjujuui_inmin_gonghwaguk_ph(self):
		return self.run_test("조선민주주의인민공화국", "{{ko-IPA|조선 민주주의 인민 공화국|ui=7|l=12|cap=y}}", "조선 민주주의 인민 공(ː)화국/조선 민주주이 인민 공(ː)화국", "ph")
	def test_Joseon_minjujuui_inmin_gonghwaguk_rr(self):
		return self.run_test("조선민주주의인민공화국", "{{ko-IPA|조선 민주주의 인민 공화국|ui=7|l=12|cap=y}}", "Joseon minjujuui inmin gonghwaguk", "rr")
	def test_Joseon_minjujuui_inmin_gonghwaguk_rrr(self):
		return self.run_test("조선민주주의인민공화국", "{{ko-IPA|조선 민주주의 인민 공화국|ui=7|l=12|cap=y}}", "Joseon minjujuui inmin gonghwagug", "rrr")
	def test_Joseon_minjujuui_inmin_gonghwaguk_mr(self):
		return self.run_test("조선민주주의인민공화국", "{{ko-IPA|조선 민주주의 인민 공화국|ui=7|l=12|cap=y}}", "Chosŏn minjujuŭi inmin konghwaguk", "mr")
	def test_Joseon_minjujuui_inmin_gonghwaguk_yr(self):
		return self.run_test("조선민주주의인민공화국", "{{ko-IPA|조선 민주주의 인민 공화국|ui=7|l=12|cap=y}}", "cosen min.cwucwuuy inmin kōnghwakwuk", "yr")
	def test_Joseon_minjujuui_inmin_gonghwaguk_ipa(self):
		return self.run_test("조선민주주의인민공화국", "{{ko-IPA|조선 민주주의 인민 공화국|ui=7|l=12|cap=y}}", "[t͡ɕo̞sʰʌ̹n miɲd͡ʑud͡ʑuɰi inmin ko̞(ː)ŋβwa̠ɡuk̚] ~ [t͡ɕo̞sʰʌ̹n miɲd͡ʑud͡ʑui inmin ko̞(ː)ŋβwa̠ɡuk̚]", "ipa")

	def test_keurim_ph(self):
		return self.run_test("크림", "{{ko-IPA|l=2}}", "크림(ː)", "ph")
	def test_keurim_rr(self):
		return self.run_test("크림", "{{ko-IPA|l=2}}", "keurim", "rr")
	def test_keurim_rrr(self):
		return self.run_test("크림", "{{ko-IPA|l=2}}", "keulim", "rrr")
	def test_keurim_mr(self):
		return self.run_test("크림", "{{ko-IPA|l=2}}", "k'ŭrim", "mr")
	def test_keurim_yr(self):
		return self.run_test("크림", "{{ko-IPA|l=2}}", "khulīm", "yr")
	def test_keurim_ipa(self):
		return self.run_test("크림", "{{ko-IPA|l=2}}", "[kxɯɾi(ː)m]", "ipa")

	def test_simsannyugok_ph(self):
		return self.run_test("심산유곡", "{{ko-IPA|l=y|ni=3}}", "심(ː)산뉴곡", "ph")
	def test_simsannyugok_rr(self):
		return self.run_test("심산유곡", "{{ko-IPA|l=y|ni=3}}", "simsannyugok", "rr")
	def test_simsannyugok_rrr(self):
		return self.run_test("심산유곡", "{{ko-IPA|l=y|ni=3}}", "simsan'yugog", "rrr")
	def test_simsannyugok_mr(self):
		return self.run_test("심산유곡", "{{ko-IPA|l=y|ni=3}}", "simsannyugok", "mr")
	def test_simsannyugok_yr(self):
		return self.run_test("심산유곡", "{{ko-IPA|l=y|ni=3}}", "sīmsannyukok", "yr")
	def test_simsannyugok_ipa(self):
		return self.run_test("심산유곡", "{{ko-IPA|l=y|ni=3}}", "[ˈɕʰi(ː)msʰa̠nɲuɡo̞k̚]", "ipa")

	def test_maikeuropeuroseseo_ph(self):
		return self.run_test("마이크로프로세서", "{{ko-IPA|com=6,7}}", "마이크로프로쎄써", "ph")
	def test_maikeuropeuroseseo_rr(self):
		return self.run_test("마이크로프로세서", "{{ko-IPA|com=6,7}}", "maikeuropeuroseseo", "rr")
	def test_maikeuropeuroseseo_rrr(self):
		return self.run_test("마이크로프로세서", "{{ko-IPA|com=6,7}}", "maikeulopeuloseseo", "rrr")
	def test_maikeuropeuroseseo_mr(self):
		return self.run_test("마이크로프로세서", "{{ko-IPA|com=6,7}}", "maik'ŭrop'ŭrossessŏ", "mr")
	def test_maikeuropeuroseseo_yr(self):
		return self.run_test("마이크로프로세서", "{{ko-IPA|com=6,7}}", "mai.khulo.phuloqseyqse", "yr")
	def test_maikeuropeuroseseo_ipa(self):
		return self.run_test("마이크로프로세서", "{{ko-IPA|com=6,7}}", "[ma̠ikxɯɾo̞pʰɯɾo̞s͈e̞s͈ʌ̹]", "ipa")

	def test_yasaeng_dongmul_ph(self):
		return self.run_test("야생동물", "{{ko-IPA|야생 동물|l=1,4}}", "야(ː)생 동(ː)물/야(ː)셍 동(ː)물", "ph")
	def test_yasaeng_dongmul_rr(self):
		return self.run_test("야생동물", "{{ko-IPA|야생 동물|l=1,4}}", "yasaeng dongmul", "rr")
	def test_yasaeng_dongmul_rrr(self):
		return self.run_test("야생동물", "{{ko-IPA|야생 동물|l=1,4}}", "yasaeng dongmul", "rrr")
	def test_yasaeng_dongmul_mr(self):
		return self.run_test("야생동물", "{{ko-IPA|야생 동물|l=1,4}}", "yasaeng tongmul", "mr")
	def test_yasaeng_dongmul_yr(self):
		return self.run_test("야생동물", "{{ko-IPA|야생 동물|l=1,4}}", "yāsayng tōngmul", "yr")
	def test_yasaeng_dongmul_ipa(self):
		return self.run_test("야생동물", "{{ko-IPA|야생 동물|l=1,4}}", "[ˈja̠(ː)sʰɛŋ to̞(ː)ŋmuɭ] ~ [ˈja̠(ː)sʰe̞ŋ to̞(ː)ŋmuɭ]", "ipa")

	def test_jat_ph(self):
		return self.run_test("잣", "{{ko-IPA||l=y}}", "잗(ː)", "ph")
	def test_jat_rr(self):
		return self.run_test("잣", "{{ko-IPA||l=y}}", "jat", "rr")
	def test_jat_rrr(self):
		return self.run_test("잣", "{{ko-IPA||l=y}}", "jas", "rrr")
	def test_jat_mr(self):
		return self.run_test("잣", "{{ko-IPA||l=y}}", "chat", "mr")
	def test_jat_yr(self):
		return self.run_test("잣", "{{ko-IPA||l=y}}", "cās", "yr")
	def test_jat_ipa(self):
		return self.run_test("잣", "{{ko-IPA||l=y}}", "[t͡ɕa̠(ː)t̚]", "ipa")

	def test_yuga_jeunggwon_ph(self):
		return self.run_test("유가증권", "{{ko-IPA|유가 증권|l=y|com=1,4}}", "유(ː)까 증꿘", "ph")
	def test_yuga_jeunggwon_rr(self):
		return self.run_test("유가증권", "{{ko-IPA|유가 증권|l=y|com=1,4}}", "yuga jeunggwon", "rr")
	def test_yuga_jeunggwon_rrr(self):
		return self.run_test("유가증권", "{{ko-IPA|유가 증권|l=y|com=1,4}}", "yuga jeunggwon", "rrr")
	def test_yuga_jeunggwon_mr(self):
		return self.run_test("유가증권", "{{ko-IPA|유가 증권|l=y|com=1,4}}", "yuka chŭngkwŏn", "mr")
	def test_yuga_jeunggwon_yr(self):
		return self.run_test("유가증권", "{{ko-IPA|유가 증권|l=y|com=1,4}}", "yūqka cungqkwen", "yr")
	def test_yuga_jeunggwon_ipa(self):
		return self.run_test("유가증권", "{{ko-IPA|유가 증권|l=y|com=1,4}}", "[ˈju(ː)k͈a̠ t͡ɕɯŋk͈wʌ̹n]", "ipa")

	def test_seworeun_sarameul_gidaryeo_juji_anneunda_ph(self):
		return self.run_test("세월은 사람을 기다려 주지 않는다", "{{ko-ipa|l=1,5}}", "세(ː)워른 사(ː)라믈 기다려 주지 안는다", "ph")
	def test_seworeun_sarameul_gidaryeo_juji_anneunda_rr(self):
		return self.run_test("세월은 사람을 기다려 주지 않는다", "{{ko-ipa|l=1,5}}", "seworeun sarameul gidaryeo juji anneunda", "rr")
	def test_seworeun_sarameul_gidaryeo_juji_anneunda_rrr(self):
		return self.run_test("세월은 사람을 기다려 주지 않는다", "{{ko-ipa|l=1,5}}", "sewol'eun salam'eul gidalyeo juji anhneunda", "rrr")
	def test_seworeun_sarameul_gidaryeo_juji_anneunda_mr(self):
		return self.run_test("세월은 사람을 기다려 주지 않는다", "{{ko-ipa|l=1,5}}", "sewŏrŭn saramŭl kidaryŏ chuji annŭnda", "mr")
	def test_seworeun_sarameul_gidaryeo_juji_anneunda_yr(self):
		return self.run_test("세월은 사람을 기다려 주지 않는다", "{{ko-ipa|l=1,5}}", "sēywel.un sālam.ul kitalye cwuci anhnunta", "yr")
	def test_seworeun_sarameul_gidaryeo_juji_anneunda_ipa(self):
		return self.run_test("세월은 사람을 기다려 주지 않는다", "{{ko-ipa|l=1,5}}", "[ˈsʰe̞(ː)wʌ̹ɾɯn sʰa̠(ː)ɾa̠mɯɭ kida̠ɾjʌ̹ t͡ɕud͡ʑi a̠nnɯnda̠]", "ipa")

	def test_dakgalbi_ph(self):
		return self.run_test("닭갈비", "{{ko-IPA|bcred=1}}", "닥깔비", "ph")
	def test_dakgalbi_rr(self):
		return self.run_test("닭갈비", "{{ko-IPA|bcred=1}}", "dakgalbi", "rr")
	def test_dakgalbi_rrr(self):
		return self.run_test("닭갈비", "{{ko-IPA|bcred=1}}", "dalggalbi", "rrr")
	def test_dakgalbi_mr(self):
		return self.run_test("닭갈비", "{{ko-IPA|bcred=1}}", "takkalbi", "mr")
	def test_dakgalbi_yr(self):
		return self.run_test("닭갈비", "{{ko-IPA|bcred=1}}", "talk.kal.pi", "yr")
	def test_dakgalbi_ipa(self):
		return self.run_test("닭갈비", "{{ko-IPA|bcred=1}}", "[ta̠k̚k͈a̠ɭbi]", "ipa")

	def test_namjonnyeobi_ph(self):
		return self.run_test("남존여비", "{{ko-IPA|ni=3}}", "남존녀비", "ph")
	def test_namjonnyeobi_rr(self):
		return self.run_test("남존여비", "{{ko-IPA|ni=3}}", "namjonnyeobi", "rr")
	def test_namjonnyeobi_rrr(self):
		return self.run_test("남존여비", "{{ko-IPA|ni=3}}", "namjon'yeobi", "rrr")
	def test_namjonnyeobi_mr(self):
		return self.run_test("남존여비", "{{ko-IPA|ni=3}}", "namjonnyŏbi", "mr")
	def test_namjonnyeobi_yr(self):
		return self.run_test("남존여비", "{{ko-IPA|ni=3}}", "namconnyepi", "yr")
	def test_namjonnyeobi_ipa(self):
		return self.run_test("남존여비", "{{ko-IPA|ni=3}}", "[na̠md͡ʑo̞nɲʌ̹bi]", "ipa")

	def test_Seuwiseu_ph(self):
		return self.run_test("스위스", "{{ko-IPA|cap=y|com=2}}", "스위쓰", "ph")
	def test_Seuwiseu_rr(self):
		return self.run_test("스위스", "{{ko-IPA|cap=y|com=2}}", "Seuwiseu", "rr")
	def test_Seuwiseu_rrr(self):
		return self.run_test("스위스", "{{ko-IPA|cap=y|com=2}}", "Seuwiseu", "rrr")
	def test_Seuwiseu_mr(self):
		return self.run_test("스위스", "{{ko-IPA|cap=y|com=2}}", "Sŭwissŭ", "mr")
	def test_Seuwiseu_yr(self):
		return self.run_test("스위스", "{{ko-IPA|cap=y|com=2}}", "suwiqsu", "yr")
	def test_Seuwiseu_ipa(self):
		return self.run_test("스위스", "{{ko-IPA|cap=y|com=2}}", "[sʰɯɥis͈ɯ] ~ [sʰɯys͈ɯ]", "ipa")

	def test_motae_sollo_ph(self):
		return self.run_test("모태솔로", "{{ko-IPA|모태 솔로|l=y|com=3}}", "모(ː)태 쏠로/모(ː)테 쏠로", "ph")
	def test_motae_sollo_rr(self):
		return self.run_test("모태솔로", "{{ko-IPA|모태 솔로|l=y|com=3}}", "motae sollo", "rr")
	def test_motae_sollo_rrr(self):
		return self.run_test("모태솔로", "{{ko-IPA|모태 솔로|l=y|com=3}}", "motae sollo", "rrr")
	def test_motae_sollo_mr(self):
		return self.run_test("모태솔로", "{{ko-IPA|모태 솔로|l=y|com=3}}", "mot'ae ssollo", "mr")
	def test_motae_sollo_yr(self):
		return self.run_test("모태솔로", "{{ko-IPA|모태 솔로|l=y|com=3}}", "mō.thay qsollo", "yr")
	def test_motae_sollo_ipa(self):
		return self.run_test("모태솔로", "{{ko-IPA|모태 솔로|l=y|com=3}}", "[ˈmo̞(ː)tʰɛ s͈o̞ɭɭo̞] ~ [ˈmo̞(ː)tʰe̞ s͈o̞ɭɭo̞]", "ipa")

	def test_Namapeurika_gonghwaguk_ph(self):
		return self.run_test("남아프리카공화국", "{{ko-IPA|남아프리카 공화국|cap=y|l=7}}", "나마프리카 공(ː)화국", "ph")
	def test_Namapeurika_gonghwaguk_rr(self):
		return self.run_test("남아프리카공화국", "{{ko-IPA|남아프리카 공화국|cap=y|l=7}}", "Namapeurika gonghwaguk", "rr")
	def test_Namapeurika_gonghwaguk_rrr(self):
		return self.run_test("남아프리카공화국", "{{ko-IPA|남아프리카 공화국|cap=y|l=7}}", "Nam'apeulika gonghwagug", "rrr")
	def test_Namapeurika_gonghwaguk_mr(self):
		return self.run_test("남아프리카공화국", "{{ko-IPA|남아프리카 공화국|cap=y|l=7}}", "Namap'ŭrik'a konghwaguk", "mr")
	def test_Namapeurika_gonghwaguk_yr(self):
		return self.run_test("남아프리카공화국", "{{ko-IPA|남아프리카 공화국|cap=y|l=7}}", "nam.a.phuli.kha kōnghwakwuk", "yr")
	def test_Namapeurika_gonghwaguk_ipa(self):
		return self.run_test("남아프리카공화국", "{{ko-IPA|남아프리카 공화국|cap=y|l=7}}", "[na̠ma̠pʰɯɾikʰa̠ ko̞(ː)ŋβwa̠ɡuk̚]", "ipa")

	def test_Konggo_gonghwaguk_ph(self):
		return self.run_test("콩고 공화국", "{{ko-IPA|cap=y|l=4}}", "콩고 공(ː)화국", "ph")
	def test_Konggo_gonghwaguk_rr(self):
		return self.run_test("콩고 공화국", "{{ko-IPA|cap=y|l=4}}", "Konggo gonghwaguk", "rr")
	def test_Konggo_gonghwaguk_rrr(self):
		return self.run_test("콩고 공화국", "{{ko-IPA|cap=y|l=4}}", "Konggo gonghwagug", "rrr")
	def test_Konggo_gonghwaguk_mr(self):
		return self.run_test("콩고 공화국", "{{ko-IPA|cap=y|l=4}}", "K'onggo konghwaguk", "mr")
	def test_Konggo_gonghwaguk_yr(self):
		return self.run_test("콩고 공화국", "{{ko-IPA|cap=y|l=4}}", "khongko kōnghwakwuk", "yr")
	def test_Konggo_gonghwaguk_ipa(self):
		return self.run_test("콩고 공화국", "{{ko-IPA|cap=y|l=4}}", "[kʰo̞ŋɡo̞ ko̞(ː)ŋβwa̠ɡuk̚]", "ipa")

	def test_Dominika_gonghwaguk_ph(self):
		return self.run_test("도미니카 공화국", "{{ko-IPA|cap=y|l=6}}", "도미니카 공(ː)화국", "ph")
	def test_Dominika_gonghwaguk_rr(self):
		return self.run_test("도미니카 공화국", "{{ko-IPA|cap=y|l=6}}", "Dominika gonghwaguk", "rr")
	def test_Dominika_gonghwaguk_rrr(self):
		return self.run_test("도미니카 공화국", "{{ko-IPA|cap=y|l=6}}", "Dominika gonghwagug", "rrr")
	def test_Dominika_gonghwaguk_mr(self):
		return self.run_test("도미니카 공화국", "{{ko-IPA|cap=y|l=6}}", "Tominik'a konghwaguk", "mr")
	def test_Dominika_gonghwaguk_yr(self):
		return self.run_test("도미니카 공화국", "{{ko-IPA|cap=y|l=6}}", "tomini.kha kōnghwakwuk", "yr")
	def test_Dominika_gonghwaguk_ipa(self):
		return self.run_test("도미니카 공화국", "{{ko-IPA|cap=y|l=6}}", "[to̞minikʰa̠ ko̞(ː)ŋβwa̠ɡuk̚]", "ipa")

	def test_allaguija_ph(self):
		return self.run_test("안락의자", "{{ko-IPA|ui=3}}", "알라긔자/알라기자", "ph")
	def test_allaguija_rr(self):
		return self.run_test("안락의자", "{{ko-IPA|ui=3}}", "allaguija", "rr")
	def test_allaguija_rrr(self):
		return self.run_test("안락의자", "{{ko-IPA|ui=3}}", "anlag'uija", "rrr")
	def test_allaguija_mr(self):
		return self.run_test("안락의자", "{{ko-IPA|ui=3}}", "allagŭija", "mr")
	def test_allaguija_yr(self):
		return self.run_test("안락의자", "{{ko-IPA|ui=3}}", "anlak.uyca", "yr")
	def test_allaguija_ipa(self):
		return self.run_test("안락의자", "{{ko-IPA|ui=3}}", "[a̠ɭɭa̠ɡɰid͡ʑa̠] ~ [a̠ɭɭa̠ɡid͡ʑa̠]", "ipa")

	def test_bakkadeoreun_ph(self):
		return self.run_test("바깥어른", "{{ko-IPA|bcred=2}}", "바까더른", "ph")
	def test_bakkadeoreun_rr(self):
		return self.run_test("바깥어른", "{{ko-IPA|bcred=2}}", "bakkadeoreun", "rr")
	def test_bakkadeoreun_rrr(self):
		return self.run_test("바깥어른", "{{ko-IPA|bcred=2}}", "ba'kkat'eoleun", "rrr")
	def test_bakkadeoreun_mr(self):
		return self.run_test("바깥어른", "{{ko-IPA|bcred=2}}", "pakkadŏrŭn", "mr")
	def test_bakkadeoreun_yr(self):
		return self.run_test("바깥어른", "{{ko-IPA|bcred=2}}", "pa.kkath.elun", "yr")
	def test_bakkadeoreun_ipa(self):
		return self.run_test("바깥어른", "{{ko-IPA|bcred=2}}", "[pa̠k͈a̠dʌ̹ɾɯn]", "ipa")

	def test_unjeon_myeonheojeung_ph(self):
		return self.run_test("운전 면허증", "{{ko-IPA|l=y|com=5}}", "운(ː)전 면허쯩", "ph")
	def test_unjeon_myeonheojeung_rr(self):
		return self.run_test("운전 면허증", "{{ko-IPA|l=y|com=5}}", "unjeon myeonheojeung", "rr")
	def test_unjeon_myeonheojeung_rrr(self):
		return self.run_test("운전 면허증", "{{ko-IPA|l=y|com=5}}", "unjeon myeonheojeung", "rrr")
	def test_unjeon_myeonheojeung_mr(self):
		return self.run_test("운전 면허증", "{{ko-IPA|l=y|com=5}}", "unjŏn myŏnhŏchŭng", "mr")
	def test_unjeon_myeonheojeung_yr(self):
		return self.run_test("운전 면허증", "{{ko-IPA|l=y|com=5}}", "wūn.cen myen.heqcung", "yr")
	def test_unjeon_myeonheojeung_ipa(self):
		return self.run_test("운전 면허증", "{{ko-IPA|l=y|com=5}}", "[ˈu(ː)ɲd͡ʑʌ̹n mjʌ̹nɦʌ̹t͡ɕ͈ɯŋ]", "ipa")

	def test_seongeullaseu_ph(self):
		return self.run_test("선글라스", "{{ko-IPA|com=0,3}}", "썬글라쓰", "ph")
	def test_seongeullaseu_rr(self):
		return self.run_test("선글라스", "{{ko-IPA|com=0,3}}", "seon'geullaseu", "rr")
	def test_seongeullaseu_rrr(self):
		return self.run_test("선글라스", "{{ko-IPA|com=0,3}}", "seongeullaseu", "rrr")
	def test_seongeullaseu_mr(self):
		return self.run_test("선글라스", "{{ko-IPA|com=0,3}}", "ssŏn'gŭllassŭ", "mr")
	def test_seongeullaseu_yr(self):
		return self.run_test("선글라스", "{{ko-IPA|com=0,3}}", "qsenkullaqsu", "yr")
	def test_seongeullaseu_ipa(self):
		return self.run_test("선글라스", "{{ko-IPA|com=0,3}}", "[s͈ʌ̹nɡɯɭɭa̠s͈ɯ]", "ipa")

	def test_nansenseu_ph(self):
		return self.run_test("난센스", "{{ko-IPA|com=1,2}}", "난쎈쓰", "ph")
	def test_nansenseu_rr(self):
		return self.run_test("난센스", "{{ko-IPA|com=1,2}}", "nansenseu", "rr")
	def test_nansenseu_rrr(self):
		return self.run_test("난센스", "{{ko-IPA|com=1,2}}", "nansenseu", "rrr")
	def test_nansenseu_mr(self):
		return self.run_test("난센스", "{{ko-IPA|com=1,2}}", "nanssenssŭ", "mr")
	def test_nansenseu_yr(self):
		return self.run_test("난센스", "{{ko-IPA|com=1,2}}", "nanqseynqsu", "yr")
	def test_nansenseu_ipa(self):
		return self.run_test("난센스", "{{ko-IPA|com=1,2}}", "[na̠ns͈e̞ns͈ɯ]", "ipa")

	def test_minibeoseu_ph(self):
		return self.run_test("미니버스", "{{ko-IPA|com=2,3}}", "미니뻐쓰", "ph")
	def test_minibeoseu_rr(self):
		return self.run_test("미니버스", "{{ko-IPA|com=2,3}}", "minibeoseu", "rr")
	def test_minibeoseu_rrr(self):
		return self.run_test("미니버스", "{{ko-IPA|com=2,3}}", "minibeoseu", "rrr")
	def test_minibeoseu_mr(self):
		return self.run_test("미니버스", "{{ko-IPA|com=2,3}}", "minipŏssŭ", "mr")
	def test_minibeoseu_yr(self):
		return self.run_test("미니버스", "{{ko-IPA|com=2,3}}", "miniqpeqsu", "yr")
	def test_minibeoseu_ipa(self):
		return self.run_test("미니버스", "{{ko-IPA|com=2,3}}", "[minip͈ʌ̹s͈ɯ]", "ipa")

	def test_onnain_ph(self):
		return self.run_test("온라인", "{{ko-IPA|nn=2}}", "온나인", "ph")
	def test_onnain_rr(self):
		return self.run_test("온라인", "{{ko-IPA|nn=2}}", "onnain", "rr")
	def test_onnain_rrr(self):
		return self.run_test("온라인", "{{ko-IPA|nn=2}}", "onlain", "rrr")
	def test_onnain_mr(self):
		return self.run_test("온라인", "{{ko-IPA|nn=2}}", "onnain", "mr")
	def test_onnain_yr(self):
		return self.run_test("온라인", "{{ko-IPA|nn=2}}", "onlain", "yr")
	def test_onnain_ipa(self):
		return self.run_test("온라인", "{{ko-IPA|nn=2}}", "[o̞nna̠in]", "ipa")

	def test_dambaetdae_ph(self):
		return self.run_test("담뱃대", "{{ko-IPA|l=y|nobc=2}}", "담(ː)밷때/담(ː)배때/담(ː)벧떼/담(ː)베떼", "ph")
	def test_dambaetdae_rr(self):
		return self.run_test("담뱃대", "{{ko-IPA|l=y|nobc=2}}", "dambaetdae", "rr")
	def test_dambaetdae_rrr(self):
		return self.run_test("담뱃대", "{{ko-IPA|l=y|nobc=2}}", "dambaesdae", "rrr")
	def test_dambaetdae_mr(self):
		return self.run_test("담뱃대", "{{ko-IPA|l=y|nobc=2}}", "tambaettae", "mr")
	def test_dambaetdae_yr(self):
		return self.run_test("담뱃대", "{{ko-IPA|l=y|nobc=2}}", "tāmpaystay", "yr")
	def test_dambaetdae_ipa(self):
		return self.run_test("담뱃대", "{{ko-IPA|l=y|nobc=2}}", "[ˈta̠(ː)mbɛt̚t͈ɛ] ~ [ˈta̠(ː)mbɛt͈ɛ] ~ [ˈta̠(ː)mbe̞t̚t͈e̞] ~ [ˈta̠(ː)mbe̞t͈e̞]", "ipa")

	def test_syuteukeiseu_ph(self):
		return self.run_test("슈트케이스", "{{ko-IPA|com=4}}", "슈트케이쓰", "ph")
	def test_syuteukeiseu_rr(self):
		return self.run_test("슈트케이스", "{{ko-IPA|com=4}}", "syuteukeiseu", "rr")
	def test_syuteukeiseu_rrr(self):
		return self.run_test("슈트케이스", "{{ko-IPA|com=4}}", "syuteukeiseu", "rrr")
	def test_syuteukeiseu_mr(self):
		return self.run_test("슈트케이스", "{{ko-IPA|com=4}}", "syut'ŭk'eissŭ", "mr")
	def test_syuteukeiseu_yr(self):
		return self.run_test("슈트케이스", "{{ko-IPA|com=4}}", "syu.thu.kheyiqsu", "yr")
	def test_syuteukeiseu_ipa(self):
		return self.run_test("슈트케이스", "{{ko-IPA|com=4}}", "[ɕʰutʰɯkʰe̞is͈ɯ]", "ipa")

	def test_mareukeuseujuui_ph(self):
		return self.run_test("마르크스주의", "{{ko-IPA|ui=6}}", "마르크스주의/마르크스주이", "ph")
	def test_mareukeuseujuui_rr(self):
		return self.run_test("마르크스주의", "{{ko-IPA|ui=6}}", "mareukeuseujuui", "rr")
	def test_mareukeuseujuui_rrr(self):
		return self.run_test("마르크스주의", "{{ko-IPA|ui=6}}", "maleukeuseujuui", "rrr")
	def test_mareukeuseujuui_mr(self):
		return self.run_test("마르크스주의", "{{ko-IPA|ui=6}}", "marŭk'ŭsŭjuŭi", "mr")
	def test_mareukeuseujuui_yr(self):
		return self.run_test("마르크스주의", "{{ko-IPA|ui=6}}", "malu.khusucwuuy", "yr")
	def test_mareukeuseujuui_ipa(self):
		return self.run_test("마르크스주의", "{{ko-IPA|ui=6}}", "[ma̠ɾɯkxɯsʰɯd͡ʑuɰi] ~ [ma̠ɾɯkxɯsʰɯd͡ʑui]", "ipa")

	def test_ttwieoneomda_ph(self):
		return self.run_test("뛰어넘다", "{{ko-IPA|iot=2|com=3}}", "뛰어넘따/뛰여넘따", "ph")
	def test_ttwieoneomda_rr(self):
		return self.run_test("뛰어넘다", "{{ko-IPA|iot=2|com=3}}", "ttwieoneomda", "rr")
	def test_ttwieoneomda_rrr(self):
		return self.run_test("뛰어넘다", "{{ko-IPA|iot=2|com=3}}", "ttwieoneomda", "rrr")
	def test_ttwieoneomda_mr(self):
		return self.run_test("뛰어넘다", "{{ko-IPA|iot=2|com=3}}", "ttwiŏnŏmta", "mr")
	def test_ttwieoneomda_yr(self):
		return self.run_test("뛰어넘다", "{{ko-IPA|iot=2|com=3}}", "ttwienemqta", "yr")
	def test_ttwieoneomda_ipa(self):
		return self.run_test("뛰어넘다", "{{ko-IPA|iot=2|com=3}}", "[t͈ɥiʌ̹nʌ̹mt͈a̠] ~ [t͈ɥijʌ̹nʌ̹mt͈a̠] ~ [t͈yʌ̹nʌ̹mt͈a̠] ~ [t͈yjʌ̹nʌ̹mt͈a̠]", "ipa")

	def test_jeongsik_ph(self):
		return self.run_test("정식", "{{ko-IPA|l=1}}", "정(ː)식", "ph")
	def test_jeongsik_rr(self):
		return self.run_test("정식", "{{ko-IPA|l=1}}", "jeongsik", "rr")
	def test_jeongsik_rrr(self):
		return self.run_test("정식", "{{ko-IPA|l=1}}", "jeongsig", "rrr")
	def test_jeongsik_mr(self):
		return self.run_test("정식", "{{ko-IPA|l=1}}", "chŏngsik", "mr")
	def test_jeongsik_yr(self):
		return self.run_test("정식", "{{ko-IPA|l=1}}", "cēngsik", "yr")
	def test_jeongsik_ipa(self):
		return self.run_test("정식", "{{ko-IPA|l=1}}", "[ˈt͡ɕɘ(ː)ŋɕʰik̚]", "ipa")

	def test_Sollomon_jedo_ph(self):
		return self.run_test("솔로몬 제도", "{{ko-IPA|com=0|cap=y}}", "쏠로몬 제도", "ph")
	def test_Sollomon_jedo_rr(self):
		return self.run_test("솔로몬 제도", "{{ko-IPA|com=0|cap=y}}", "Sollomon jedo", "rr")
	def test_Sollomon_jedo_rrr(self):
		return self.run_test("솔로몬 제도", "{{ko-IPA|com=0|cap=y}}", "Sollomon jedo", "rrr")
	def test_Sollomon_jedo_mr(self):
		return self.run_test("솔로몬 제도", "{{ko-IPA|com=0|cap=y}}", "Ssollomon chedo", "mr")
	def test_Sollomon_jedo_yr(self):
		return self.run_test("솔로몬 제도", "{{ko-IPA|com=0|cap=y}}", "qsollomon ceyto", "yr")
	def test_Sollomon_jedo_ipa(self):
		return self.run_test("솔로몬 제도", "{{ko-IPA|com=0|cap=y}}", "[s͈o̞ɭɭo̞mo̞n t͡ɕe̞do̞]", "ipa")

	def test_gyoui_ph(self):
		return self.run_test("교의", "{{ko-IPA|ui=2|l=y}}", "교(ː)의/교(ː)이", "ph")
	def test_gyoui_rr(self):
		return self.run_test("교의", "{{ko-IPA|ui=2|l=y}}", "gyoui", "rr")
	def test_gyoui_rrr(self):
		return self.run_test("교의", "{{ko-IPA|ui=2|l=y}}", "gyoui", "rrr")
	def test_gyoui_mr(self):
		return self.run_test("교의", "{{ko-IPA|ui=2|l=y}}", "kyoŭi", "mr")
	def test_gyoui_yr(self):
		return self.run_test("교의", "{{ko-IPA|ui=2|l=y}}", "kyōuy", "yr")
	def test_gyoui_ipa(self):
		return self.run_test("교의", "{{ko-IPA|ui=2|l=y}}", "[ˈkjo(ː)ɰi] ~ [ˈkjo(ː)i]", "ipa")

	def test_Buhwaljeol_ph(self):
		return self.run_test("부활절", "{{ko-IPA|l=y|com=2|cap=y}}", "부(ː)활쩔", "ph")
	def test_Buhwaljeol_rr(self):
		return self.run_test("부활절", "{{ko-IPA|l=y|com=2|cap=y}}", "Buhwaljeol", "rr")
	def test_Buhwaljeol_rrr(self):
		return self.run_test("부활절", "{{ko-IPA|l=y|com=2|cap=y}}", "Buhwaljeol", "rrr")
	def test_Buhwaljeol_mr(self):
		return self.run_test("부활절", "{{ko-IPA|l=y|com=2|cap=y}}", "Puhwalchŏl", "mr")
	def test_Buhwaljeol_yr(self):
		return self.run_test("부활절", "{{ko-IPA|l=y|com=2|cap=y}}", "pūhwalqcel", "yr")
	def test_Buhwaljeol_ipa(self):
		return self.run_test("부활절", "{{ko-IPA|l=y|com=2|cap=y}}", "[ˈpu(ː)βwa̠ʎt͡ɕ͈ʌ̹ɭ]", "ipa")

	def test_wennil_ph(self):
		return self.run_test("웬일", "{{ko-IPA|l=y|ni=2}}", "웬(ː)닐", "ph")
	def test_wennil_rr(self):
		return self.run_test("웬일", "{{ko-IPA|l=y|ni=2}}", "wennil", "rr")
	def test_wennil_rrr(self):
		return self.run_test("웬일", "{{ko-IPA|l=y|ni=2}}", "wen'il", "rrr")
	def test_wennil_mr(self):
		return self.run_test("웬일", "{{ko-IPA|l=y|ni=2}}", "wennil", "mr")
	def test_wennil_yr(self):
		return self.run_test("웬일", "{{ko-IPA|l=y|ni=2}}", "wēynnil", "yr")
	def test_wennil_ipa(self):
		return self.run_test("웬일", "{{ko-IPA|l=y|ni=2}}", "[ˈwe̞(ː)nniɭ]", "ipa")

	def test_Sinuiju_ph(self):
		return self.run_test("신의주", "{{ko-IPA|cap=y|ui=2}}", "시늬주/시니주", "ph")
	def test_Sinuiju_rr(self):
		return self.run_test("신의주", "{{ko-IPA|cap=y|ui=2}}", "Sinuiju", "rr")
	def test_Sinuiju_rrr(self):
		return self.run_test("신의주", "{{ko-IPA|cap=y|ui=2}}", "Sin'uiju", "rrr")
	def test_Sinuiju_mr(self):
		return self.run_test("신의주", "{{ko-IPA|cap=y|ui=2}}", "Sinŭiju", "mr")
	def test_Sinuiju_yr(self):
		return self.run_test("신의주", "{{ko-IPA|cap=y|ui=2}}", "sin.uycwu", "yr")
	def test_Sinuiju_ipa(self):
		return self.run_test("신의주", "{{ko-IPA|cap=y|ui=2}}", "[ɕʰinɰid͡ʑu] ~ [ɕʰinid͡ʑu]", "ipa")

	def test_Sollomonui_jihye_ph(self):
		return self.run_test("솔로몬의 지혜", "{{ko-IPA|cap=y|uie=4}}", "솔로모늬 지혜/솔로모네 지혜/솔로모늬 지헤/솔로모네 지헤", "ph")
	def test_Sollomonui_jihye_rr(self):
		return self.run_test("솔로몬의 지혜", "{{ko-IPA|cap=y|uie=4}}", "Sollomonui jihye", "rr")
	def test_Sollomonui_jihye_rrr(self):
		return self.run_test("솔로몬의 지혜", "{{ko-IPA|cap=y|uie=4}}", "Sollomon'ui jihye", "rrr")
	def test_Sollomonui_jihye_mr(self):
		return self.run_test("솔로몬의 지혜", "{{ko-IPA|cap=y|uie=4}}", "Sollomonŭi chihye", "mr")
	def test_Sollomonui_jihye_yr(self):
		return self.run_test("솔로몬의 지혜", "{{ko-IPA|cap=y|uie=4}}", "sollomon.uy cihyey", "yr")
	def test_Sollomonui_jihye_ipa(self):
		return self.run_test("솔로몬의 지혜", "{{ko-IPA|cap=y|uie=4}}", "[sʰo̞ɭɭo̞mo̞nɰi t͡ɕiʝe̞] ~ [sʰo̞ɭɭo̞mo̞ne̞ t͡ɕiʝe̞] ~ [sʰo̞ɭɭo̞mo̞nɰi t͡ɕiɦe̞] ~ [sʰo̞ɭɭo̞mo̞ne̞ t͡ɕiɦe̞]", "ipa")

	def test_deobeullyu_ph(self):
		return self.run_test("더블유", "{{ko-IPA|com=0|ni=3}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "떠블류", "ph")
	def test_deobeullyu_rr(self):
		return self.run_test("더블유", "{{ko-IPA|com=0|ni=3}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "deobeullyu", "rr")
	def test_deobeullyu_rrr(self):
		return self.run_test("더블유", "{{ko-IPA|com=0|ni=3}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "deobeul'yu", "rrr")
	def test_deobeullyu_mr(self):
		return self.run_test("더블유", "{{ko-IPA|com=0|ni=3}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "tŏbŭllyu", "mr")
	def test_deobeullyu_yr(self):
		return self.run_test("더블유", "{{ko-IPA|com=0|ni=3}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "qtepullyu", "yr")
	def test_deobeullyu_ipa(self):
		return self.run_test("더블유", "{{ko-IPA|com=0|ni=3}}<ref>{{smallcaps|Jo}} Hyeong-Il and {{smallcaps|Nam}} Ju-Hye, {{lang|ko|외래어와 외국어 표현 3300}}, 2012, {{ISBN|978-89-5556-986-5}}", "[t͈ʌ̹bɯʎʎu]", "ipa")

	def test_hwahak_jeondal_muljil_ph(self):
		return self.run_test("화학전달물질", "{{ko-IPA|화학 전달 물질|com=7|l=y}}", "화(ː)학 전달 물찔", "ph")
	def test_hwahak_jeondal_muljil_rr(self):
		return self.run_test("화학전달물질", "{{ko-IPA|화학 전달 물질|com=7|l=y}}", "hwahak jeondal muljil", "rr")
	def test_hwahak_jeondal_muljil_rrr(self):
		return self.run_test("화학전달물질", "{{ko-IPA|화학 전달 물질|com=7|l=y}}", "hwahag jeondal muljil", "rrr")
	def test_hwahak_jeondal_muljil_mr(self):
		return self.run_test("화학전달물질", "{{ko-IPA|화학 전달 물질|com=7|l=y}}", "hwahak chŏndal mulchil", "mr")
	def test_hwahak_jeondal_muljil_yr(self):
		return self.run_test("화학전달물질", "{{ko-IPA|화학 전달 물질|com=7|l=y}}", "hwāhak cental mulqcil", "yr")
	def test_hwahak_jeondal_muljil_ipa(self):
		return self.run_test("화학전달물질", "{{ko-IPA|화학 전달 물질|com=7|l=y}}", "[ˈɸwa̠(ː)ɦa̠k̚ t͡ɕʌ̹nda̠ɭ muʎt͡ɕ͈iɭ]", "ipa")

	def test_hwaseok_yeollyo_hwaseogyeollyo_hwaseongnyeollyo_ph(self):
		return self.run_test("화석 연료", "{{ko-IPA|l=y||화석연료||화석년료}}", "화(ː)석 열료/화(ː)서결료/화(ː)성녈료", "ph")
	def test_hwaseok_yeollyo_hwaseogyeollyo_hwaseongnyeollyo_rr(self):
		return self.run_test("화석 연료", "{{ko-IPA|l=y||화석연료||화석년료}}", "hwaseok yeollyo/hwaseogyeollyo/hwaseongnyeollyo", "rr")
	def test_hwaseok_yeollyo_hwaseogyeollyo_hwaseongnyeollyo_rrr(self):
		return self.run_test("화석 연료", "{{ko-IPA|l=y||화석연료||화석년료}}", "hwaseog yeonlyo/hwaseog'yeonlyo/hwaseognyeonlyo", "rrr")
	def test_hwaseok_yeollyo_hwaseogyeollyo_hwaseongnyeollyo_mr(self):
		return self.run_test("화석 연료", "{{ko-IPA|l=y||화석연료||화석년료}}", "hwasŏk yŏllyo/hwasŏgyŏllyo/hwasŏngnyŏllyo", "mr")
	def test_hwaseok_yeollyo_hwaseogyeollyo_hwaseongnyeollyo_yr(self):
		return self.run_test("화석 연료", "{{ko-IPA|l=y||화석연료||화석년료}}", "hwāsek yenlyo/hwāsek.yenlyo/hwāseknyenlyo", "yr")
	def test_hwaseok_yeollyo_hwaseogyeollyo_hwaseongnyeollyo_ipa(self):
		return self.run_test("화석 연료", "{{ko-IPA|l=y||화석연료||화석년료}}", "[ˈɸwa̠(ː)sʰʌ̹k̚ jʌ̹ʎʎo] ~ [ˈɸwa̠(ː)sʰʌ̹ɡjʌ̹ʎʎo] ~ [ˈɸwa̠(ː)sʰʌ̹ŋɲʌ̹ʎʎo]", "ipa")

	def test_Guyak_seonggyeong_ph(self):
		return self.run_test("구약성경", "{{ko-IPA|구약 성경|l=1,4|cap=y}}", "구(ː)약 성(ː)경", "ph")
	def test_Guyak_seonggyeong_rr(self):
		return self.run_test("구약성경", "{{ko-IPA|구약 성경|l=1,4|cap=y}}", "Guyak seonggyeong", "rr")
	def test_Guyak_seonggyeong_rrr(self):
		return self.run_test("구약성경", "{{ko-IPA|구약 성경|l=1,4|cap=y}}", "Guyag seonggyeong", "rrr")
	def test_Guyak_seonggyeong_mr(self):
		return self.run_test("구약성경", "{{ko-IPA|구약 성경|l=1,4|cap=y}}", "Kuyak sŏnggyŏng", "mr")
	def test_Guyak_seonggyeong_yr(self):
		return self.run_test("구약성경", "{{ko-IPA|구약 성경|l=1,4|cap=y}}", "kwū.yak sēngkyeng", "yr")
	def test_Guyak_seonggyeong_ipa(self):
		return self.run_test("구약성경", "{{ko-IPA|구약 성경|l=1,4|cap=y}}", "[ˈku(ː)ja̠k̚ sʰɘ(ː)ŋɡjʌ̹ŋ]", "ipa")

	def test_Reunesangseu_ph(self):
		return self.run_test("르네상스", "{{ko-IPA|cap=y|com=2,3}}", "르네쌍쓰", "ph")
	def test_Reunesangseu_rr(self):
		return self.run_test("르네상스", "{{ko-IPA|cap=y|com=2,3}}", "Reunesangseu", "rr")
	def test_Reunesangseu_rrr(self):
		return self.run_test("르네상스", "{{ko-IPA|cap=y|com=2,3}}", "Leunesangseu", "rrr")
	def test_Reunesangseu_mr(self):
		return self.run_test("르네상스", "{{ko-IPA|cap=y|com=2,3}}", "Rŭnessangssŭ", "mr")
	def test_Reunesangseu_yr(self):
		return self.run_test("르네상스", "{{ko-IPA|cap=y|com=2,3}}", "luneyqsangqsu", "yr")
	def test_Reunesangseu_ipa(self):
		return self.run_test("르네상스", "{{ko-IPA|cap=y|com=2,3}}", "[ɾɯne̞s͈a̠ŋs͈ɯ]", "ipa")

	def test_kong_simeun_de_kong_nago_pat_simeun_de_pat_nanda_ph(self):
		return self.run_test("콩 심은 데 콩 나고 팥 심은 데 팥 난다", "{{ko-IPA|l=3,15}}", "콩 시(ː)믄 데 콩 나고 팓 시(ː)믄 데 팓 난다", "ph")
	def test_kong_simeun_de_kong_nago_pat_simeun_de_pat_nanda_rr(self):
		return self.run_test("콩 심은 데 콩 나고 팥 심은 데 팥 난다", "{{ko-IPA|l=3,15}}", "kong simeun de kong nago pat simeun de pat nanda", "rr")
	def test_kong_simeun_de_kong_nago_pat_simeun_de_pat_nanda_rrr(self):
		return self.run_test("콩 심은 데 콩 나고 팥 심은 데 팥 난다", "{{ko-IPA|l=3,15}}", "kong sim'eun de kong nago pat sim'eun de pat nanda", "rrr")
	def test_kong_simeun_de_kong_nago_pat_simeun_de_pat_nanda_mr(self):
		return self.run_test("콩 심은 데 콩 나고 팥 심은 데 팥 난다", "{{ko-IPA|l=3,15}}", "k'ong simŭn te k'ong nago p'at simŭn te p'at nanda", "mr")
	def test_kong_simeun_de_kong_nago_pat_simeun_de_pat_nanda_yr(self):
		return self.run_test("콩 심은 데 콩 나고 팥 심은 데 팥 난다", "{{ko-IPA|l=3,15}}", "khong sīm.un tey khong nako phath sīm.un tey phath nanta", "yr")
	def test_kong_simeun_de_kong_nago_pat_simeun_de_pat_nanda_ipa(self):
		return self.run_test("콩 심은 데 콩 나고 팥 심은 데 팥 난다", "{{ko-IPA|l=3,15}}", "[kʰo̞ŋ ɕʰi(ː)mɯn te̞ kʰo̞ŋ na̠ɡo̞ pʰa̠t̚ ɕʰi(ː)mɯn te̞ pʰa̠t̚ na̠nda̠]", "ipa")

	def test_selpeu_diseu_ph(self):
		return self.run_test("셀프 디스", "{{ko-IPA|com=0,4}}", "쎌프 디쓰", "ph")
	def test_selpeu_diseu_rr(self):
		return self.run_test("셀프 디스", "{{ko-IPA|com=0,4}}", "selpeu diseu", "rr")
	def test_selpeu_diseu_rrr(self):
		return self.run_test("셀프 디스", "{{ko-IPA|com=0,4}}", "selpeu diseu", "rrr")
	def test_selpeu_diseu_mr(self):
		return self.run_test("셀프 디스", "{{ko-IPA|com=0,4}}", "sselp'ŭ tissŭ", "mr")
	def test_selpeu_diseu_yr(self):
		return self.run_test("셀프 디스", "{{ko-IPA|com=0,4}}", "qseyl.phu tiqsu", "yr")
	def test_selpeu_diseu_ipa(self):
		return self.run_test("셀프 디스", "{{ko-IPA|com=0,4}}", "[s͈e̞ɭpʰɯ tis͈ɯ]", "ipa")

	def test_Yugio_jeonjaeng_ph(self):
		return self.run_test("육이오전쟁", "{{ko-IPA|cap=y|육이오 전쟁|l=5}}", "유기오 전(ː)쟁/유기오 전(ː)젱", "ph")
	def test_Yugio_jeonjaeng_rr(self):
		return self.run_test("육이오전쟁", "{{ko-IPA|cap=y|육이오 전쟁|l=5}}", "Yugio jeonjaeng", "rr")
	def test_Yugio_jeonjaeng_rrr(self):
		return self.run_test("육이오전쟁", "{{ko-IPA|cap=y|육이오 전쟁|l=5}}", "Yug'io jeonjaeng", "rrr")
	def test_Yugio_jeonjaeng_mr(self):
		return self.run_test("육이오전쟁", "{{ko-IPA|cap=y|육이오 전쟁|l=5}}", "Yugio chŏnjaeng", "mr")
	def test_Yugio_jeonjaeng_yr(self):
		return self.run_test("육이오전쟁", "{{ko-IPA|cap=y|육이오 전쟁|l=5}}", "yuk.io cēn.cayng", "yr")
	def test_Yugio_jeonjaeng_ipa(self):
		return self.run_test("육이오전쟁", "{{ko-IPA|cap=y|육이오 전쟁|l=5}}", "[juɡio̞ t͡ɕɘ(ː)ɲd͡ʑɛŋ] ~ [juɡio̞ t͡ɕɘ(ː)ɲd͡ʑe̞ŋ]", "ipa")

	def test_Geuriseudoui_jeok_ph(self):
		return self.run_test("그리스도의 적", "{{ko-IPA|cap=y|uie=5}}", "그리스도의 적/그리스도에 적", "ph")
	def test_Geuriseudoui_jeok_rr(self):
		return self.run_test("그리스도의 적", "{{ko-IPA|cap=y|uie=5}}", "Geuriseudoui jeok", "rr")
	def test_Geuriseudoui_jeok_rrr(self):
		return self.run_test("그리스도의 적", "{{ko-IPA|cap=y|uie=5}}", "Geuliseudoui jeog", "rrr")
	def test_Geuriseudoui_jeok_mr(self):
		return self.run_test("그리스도의 적", "{{ko-IPA|cap=y|uie=5}}", "Kŭrisŭdoŭi chŏk", "mr")
	def test_Geuriseudoui_jeok_yr(self):
		return self.run_test("그리스도의 적", "{{ko-IPA|cap=y|uie=5}}", "kulisutouy cek", "yr")
	def test_Geuriseudoui_jeok_ipa(self):
		return self.run_test("그리스도의 적", "{{ko-IPA|cap=y|uie=5}}", "[kɯɾisʰɯdo̞ɰi t͡ɕʌ̹k̚] ~ [kɯɾisʰɯdo̞e̞ t͡ɕʌ̹k̚]", "ipa")

	def test_geondal_ph(self):
		return self.run_test("건달", "{{ko-IPA|l=}}", "건달", "ph")
	def test_geondal_rr(self):
		return self.run_test("건달", "{{ko-IPA|l=}}", "geondal", "rr")
	def test_geondal_rrr(self):
		return self.run_test("건달", "{{ko-IPA|l=}}", "geondal", "rrr")
	def test_geondal_mr(self):
		return self.run_test("건달", "{{ko-IPA|l=}}", "kŏndal", "mr")
	def test_geondal_yr(self):
		return self.run_test("건달", "{{ko-IPA|l=}}", "kental", "yr")
	def test_geondal_ipa(self):
		return self.run_test("건달", "{{ko-IPA|l=}}", "[kʌ̹nda̠ɭ]", "ipa")

	def test_geurimui_tteok_ph(self):
		return self.run_test("그림의 떡", "{{ko-IPA|uie=3|l=y}}", "그(ː)리믜 떡/그(ː)리메 떡", "ph")
	def test_geurimui_tteok_rr(self):
		return self.run_test("그림의 떡", "{{ko-IPA|uie=3|l=y}}", "geurimui tteok", "rr")
	def test_geurimui_tteok_rrr(self):
		return self.run_test("그림의 떡", "{{ko-IPA|uie=3|l=y}}", "geulim'ui tteog", "rrr")
	def test_geurimui_tteok_mr(self):
		return self.run_test("그림의 떡", "{{ko-IPA|uie=3|l=y}}", "kŭrimŭi ttŏk", "mr")
	def test_geurimui_tteok_yr(self):
		return self.run_test("그림의 떡", "{{ko-IPA|uie=3|l=y}}", "kūlim.uy ttek", "yr")
	def test_geurimui_tteok_ipa(self):
		return self.run_test("그림의 떡", "{{ko-IPA|uie=3|l=y}}", "[ˈkɯ(ː)ɾimɰi t͈ʌ̹k̚] ~ [ˈkɯ(ː)ɾime̞ t͈ʌ̹k̚]", "ipa")

	def test_namapeurikaui_oechim_ph(self):
		return self.run_test("남아프리카의 외침", "{{ko-IPA|uie=6}}", "나마프리카의 웨침/나마프리카의 웨침/나마프리카의 외침/나마프리카에 외침", "ph")
	def test_namapeurikaui_oechim_rr(self):
		return self.run_test("남아프리카의 외침", "{{ko-IPA|uie=6}}", "namapeurikaui oechim", "rr")
	def test_namapeurikaui_oechim_rrr(self):
		return self.run_test("남아프리카의 외침", "{{ko-IPA|uie=6}}", "nam'apeulikaui oechim", "rrr")
	def test_namapeurikaui_oechim_mr(self):
		return self.run_test("남아프리카의 외침", "{{ko-IPA|uie=6}}", "namap'ŭrik'aŭi oech'im", "mr")
	def test_namapeurikaui_oechim_yr(self):
		return self.run_test("남아프리카의 외침", "{{ko-IPA|uie=6}}", "nam.a.phuli.khauy oy.chim", "yr")
	def test_namapeurikaui_oechim_ipa(self):
		return self.run_test("남아프리카의 외침", "{{ko-IPA|uie=6}}", "[na̠ma̠pʰɯɾikʰa̠ɰi we̞t͡ɕʰim] ~ [na̠ma̠pʰɯɾikʰa̠ɰi we̞t͡ɕʰim] ~ [na̠ma̠pʰɯɾikʰa̠ɰi ø̞t͡ɕʰim] ~ [na̠ma̠pʰɯɾikʰa̠e̞ ø̞t͡ɕʰim]", "ipa")

	def test_bansinbanin_ph(self):
		return self.run_test("반신반인", "{{ko-IPA|l=1,3}}", "반(ː)신바(ː)닌", "ph")
	def test_bansinbanin_rr(self):
		return self.run_test("반신반인", "{{ko-IPA|l=1,3}}", "bansinbanin", "rr")
	def test_bansinbanin_rrr(self):
		return self.run_test("반신반인", "{{ko-IPA|l=1,3}}", "bansinban'in", "rrr")
	def test_bansinbanin_mr(self):
		return self.run_test("반신반인", "{{ko-IPA|l=1,3}}", "pansinbanin", "mr")
	def test_bansinbanin_yr(self):
		return self.run_test("반신반인", "{{ko-IPA|l=1,3}}", "pānsinpān.in", "yr")
	def test_bansinbanin_ipa(self):
		return self.run_test("반신반인", "{{ko-IPA|l=1,3}}", "[ˈpa̠(ː)nɕʰinba̠(ː)nin]", "ipa")

	def test_chulsannyul_ph(self):
		return self.run_test("출산율", "{{ko-IPA|com=1|ni=3}}", "출싼뉼", "ph")
	def test_chulsannyul_rr(self):
		return self.run_test("출산율", "{{ko-IPA|com=1|ni=3}}", "chulsannyul", "rr")
	def test_chulsannyul_rrr(self):
		return self.run_test("출산율", "{{ko-IPA|com=1|ni=3}}", "chulsan'yul", "rrr")
	def test_chulsannyul_mr(self):
		return self.run_test("출산율", "{{ko-IPA|com=1|ni=3}}", "ch'ulssannyul", "mr")
	def test_chulsannyul_yr(self):
		return self.run_test("출산율", "{{ko-IPA|com=1|ni=3}}", "chwulqsannyul", "yr")
	def test_chulsannyul_ipa(self):
		return self.run_test("출산율", "{{ko-IPA|com=1|ni=3}}", "[t͡ɕʰuɭs͈a̠nɲuɭ]", "ipa")

	def test_koronabaireoseu_ph(self):
		return self.run_test("코로나바이러스", "{{ko-IPA|com=6}}", "코로나바이러쓰", "ph")
	def test_koronabaireoseu_rr(self):
		return self.run_test("코로나바이러스", "{{ko-IPA|com=6}}", "koronabaireoseu", "rr")
	def test_koronabaireoseu_rrr(self):
		return self.run_test("코로나바이러스", "{{ko-IPA|com=6}}", "kolonabaileoseu", "rrr")
	def test_koronabaireoseu_mr(self):
		return self.run_test("코로나바이러스", "{{ko-IPA|com=6}}", "k'oronabairŏssŭ", "mr")
	def test_koronabaireoseu_yr(self):
		return self.run_test("코로나바이러스", "{{ko-IPA|com=6}}", "kholonapaileqsu", "yr")
	def test_koronabaireoseu_ipa(self):
		return self.run_test("코로나바이러스", "{{ko-IPA|com=6}}", "[kʰo̞ɾo̞na̠ba̠iɾʌ̹s͈ɯ]", "ipa")

	def test_mujeongbujuui_ph(self):
		return self.run_test("무정부주의", "{{ko-IPA|ui=5}}", "무정부주의/무정부주이", "ph")
	def test_mujeongbujuui_rr(self):
		return self.run_test("무정부주의", "{{ko-IPA|ui=5}}", "mujeongbujuui", "rr")
	def test_mujeongbujuui_rrr(self):
		return self.run_test("무정부주의", "{{ko-IPA|ui=5}}", "mujeongbujuui", "rrr")
	def test_mujeongbujuui_mr(self):
		return self.run_test("무정부주의", "{{ko-IPA|ui=5}}", "mujŏngbujuŭi", "mr")
	def test_mujeongbujuui_yr(self):
		return self.run_test("무정부주의", "{{ko-IPA|ui=5}}", "mucengpucwuuy", "yr")
	def test_mujeongbujuui_ipa(self):
		return self.run_test("무정부주의", "{{ko-IPA|ui=5}}", "[mud͡ʑʌ̹ŋbud͡ʑuɰi] ~ [mud͡ʑʌ̹ŋbud͡ʑui]", "ipa")

	def test_Paldo_ph(self):
		return self.run_test("팔도", "{{ko-IPA|com=1|cap=y}}", "팔또", "ph")
	def test_Paldo_rr(self):
		return self.run_test("팔도", "{{ko-IPA|com=1|cap=y}}", "Paldo", "rr")
	def test_Paldo_rrr(self):
		return self.run_test("팔도", "{{ko-IPA|com=1|cap=y}}", "Paldo", "rrr")
	def test_Paldo_mr(self):
		return self.run_test("팔도", "{{ko-IPA|com=1|cap=y}}", "P'alto", "mr")
	def test_Paldo_yr(self):
		return self.run_test("팔도", "{{ko-IPA|com=1|cap=y}}", "phalqto", "yr")
	def test_Paldo_ipa(self):
		return self.run_test("팔도", "{{ko-IPA|com=1|cap=y}}", "[pʰa̠ɭt͈o̞]", "ipa")

	def test_naetga_ph(self):
		return self.run_test("냇가", "{{ko-IPA|nobc=1|l=y}}", "낻(ː)까/내(ː)까/넫(ː)까/네(ː)까", "ph")
	def test_naetga_rr(self):
		return self.run_test("냇가", "{{ko-IPA|nobc=1|l=y}}", "naetga", "rr")
	def test_naetga_rrr(self):
		return self.run_test("냇가", "{{ko-IPA|nobc=1|l=y}}", "naesga", "rrr")
	def test_naetga_mr(self):
		return self.run_test("냇가", "{{ko-IPA|nobc=1|l=y}}", "naetka", "mr")
	def test_naetga_yr(self):
		return self.run_test("냇가", "{{ko-IPA|nobc=1|l=y}}", "nāyska", "yr")
	def test_naetga_ipa(self):
		return self.run_test("냇가", "{{ko-IPA|nobc=1|l=y}}", "[ˈnɛ(ː)t̚k͈a̠] ~ [ˈnɛ(ː)k͈a̠] ~ [ˈne̞(ː)t̚k͈a̠] ~ [ˈne̞(ː)k͈a̠]", "ipa")

	def test_jiseongimyeon_gamcheonida_ph(self):
		return self.run_test("지성이면 감천이다", "{{ko-IPA|l=6}}", "지성이면 감(ː)처니다", "ph")
	def test_jiseongimyeon_gamcheonida_rr(self):
		return self.run_test("지성이면 감천이다", "{{ko-IPA|l=6}}", "jiseong'imyeon gamcheonida", "rr")
	def test_jiseongimyeon_gamcheonida_rrr(self):
		return self.run_test("지성이면 감천이다", "{{ko-IPA|l=6}}", "jiseong'imyeon gamcheon'ida", "rrr")
	def test_jiseongimyeon_gamcheonida_mr(self):
		return self.run_test("지성이면 감천이다", "{{ko-IPA|l=6}}", "chisŏngimyŏn kamch'ŏnida", "mr")
	def test_jiseongimyeon_gamcheonida_yr(self):
		return self.run_test("지성이면 감천이다", "{{ko-IPA|l=6}}", "cisengimyen kāmchen.ita", "yr")
	def test_jiseongimyeon_gamcheonida_ipa(self):
		return self.run_test("지성이면 감천이다", "{{ko-IPA|l=6}}", "[t͡ɕisʰʌ̹ŋimjʌ̹n ka̠(ː)mt͡ɕʰʌ̹nida̠]", "ipa")

	def test_saengsallyeotalgwon_ph(self):
		return self.run_test("생살여탈권", "{{ko-IPA|ni=3|com=4}}", "생살려탈꿘/셍살려탈꿘", "ph")
	def test_saengsallyeotalgwon_rr(self):
		return self.run_test("생살여탈권", "{{ko-IPA|ni=3|com=4}}", "saengsallyeotalgwon", "rr")
	def test_saengsallyeotalgwon_rrr(self):
		return self.run_test("생살여탈권", "{{ko-IPA|ni=3|com=4}}", "saengsal'yeotalgwon", "rrr")
	def test_saengsallyeotalgwon_mr(self):
		return self.run_test("생살여탈권", "{{ko-IPA|ni=3|com=4}}", "saengsallyŏt'alkwŏn", "mr")
	def test_saengsallyeotalgwon_yr(self):
		return self.run_test("생살여탈권", "{{ko-IPA|ni=3|com=4}}", "sayngsallye.thalqkwen", "yr")
	def test_saengsallyeotalgwon_ipa(self):
		return self.run_test("생살여탈권", "{{ko-IPA|ni=3|com=4}}", "[sʰɛŋsʰa̠ʎʎʌ̹tʰa̠ɭk͈wʌ̹n] ~ [sʰe̞ŋsʰa̠ʎʎʌ̹tʰa̠ɭk͈wʌ̹n]", "ipa")

	def test_mije_sageon_ph(self):
		return self.run_test("미제 사건", "{{ko-IPA|l=1,4|com=4}}", "미(ː)제 사(ː)껀", "ph")
	def test_mije_sageon_rr(self):
		return self.run_test("미제 사건", "{{ko-IPA|l=1,4|com=4}}", "mije sageon", "rr")
	def test_mije_sageon_rrr(self):
		return self.run_test("미제 사건", "{{ko-IPA|l=1,4|com=4}}", "mije sageon", "rrr")
	def test_mije_sageon_mr(self):
		return self.run_test("미제 사건", "{{ko-IPA|l=1,4|com=4}}", "mije sakŏn", "mr")
	def test_mije_sageon_yr(self):
		return self.run_test("미제 사건", "{{ko-IPA|l=1,4|com=4}}", "mīcey sāqken", "yr")
	def test_mije_sageon_ipa(self):
		return self.run_test("미제 사건", "{{ko-IPA|l=1,4|com=4}}", "[ˈmi(ː)d͡ʑe̞ sʰa̠(ː)k͈ʌ̹n]", "ipa")

	def test_Joguk_haebang_jeonjaeng_ph(self):
		return self.run_test("조국해방전쟁", "{{ko-IPA|cap=y|조국 해방 전쟁|l=4,7}}", "조국 해(ː)방 전(ː)쟁/조국 헤(ː)방 전(ː)젱", "ph")
	def test_Joguk_haebang_jeonjaeng_rr(self):
		return self.run_test("조국해방전쟁", "{{ko-IPA|cap=y|조국 해방 전쟁|l=4,7}}", "Joguk haebang jeonjaeng", "rr")
	def test_Joguk_haebang_jeonjaeng_rrr(self):
		return self.run_test("조국해방전쟁", "{{ko-IPA|cap=y|조국 해방 전쟁|l=4,7}}", "Jogug haebang jeonjaeng", "rrr")
	def test_Joguk_haebang_jeonjaeng_mr(self):
		return self.run_test("조국해방전쟁", "{{ko-IPA|cap=y|조국 해방 전쟁|l=4,7}}", "Choguk haebang chŏnjaeng", "mr")
	def test_Joguk_haebang_jeonjaeng_yr(self):
		return self.run_test("조국해방전쟁", "{{ko-IPA|cap=y|조국 해방 전쟁|l=4,7}}", "cokwuk hāypang cēn.cayng", "yr")
	def test_Joguk_haebang_jeonjaeng_ipa(self):
		return self.run_test("조국해방전쟁", "{{ko-IPA|cap=y|조국 해방 전쟁|l=4,7}}", "[t͡ɕo̞ɡuk̚ hɛ(ː)ba̠ŋ t͡ɕɘ(ː)ɲd͡ʑɛŋ] ~ [t͡ɕo̞ɡuk̚ he̞(ː)ba̠ŋ t͡ɕɘ(ː)ɲd͡ʑe̞ŋ]", "ipa")

	def test_onsil_sogui_hwacho_ph(self):
		return self.run_test("온실 속의 화초", "{{ko-IPA|uie=5}}", "온실 소긔 화초/온실 소게 화초", "ph")
	def test_onsil_sogui_hwacho_rr(self):
		return self.run_test("온실 속의 화초", "{{ko-IPA|uie=5}}", "onsil sogui hwacho", "rr")
	def test_onsil_sogui_hwacho_rrr(self):
		return self.run_test("온실 속의 화초", "{{ko-IPA|uie=5}}", "onsil sog'ui hwacho", "rrr")
	def test_onsil_sogui_hwacho_mr(self):
		return self.run_test("온실 속의 화초", "{{ko-IPA|uie=5}}", "onsil sogŭi hwach'o", "mr")
	def test_onsil_sogui_hwacho_yr(self):
		return self.run_test("온실 속의 화초", "{{ko-IPA|uie=5}}", "onsil sok.uy hwa.cho", "yr")
	def test_onsil_sogui_hwacho_ipa(self):
		return self.run_test("온실 속의 화초", "{{ko-IPA|uie=5}}", "[o̞nɕʰiɭ sʰo̞ɡɰi ɸwa̠t͡ɕʰo̞] ~ [o̞nɕʰiɭ sʰo̞ɡe̞ ɸwa̠t͡ɕʰo̞]", "ipa")

	def test_siljonjuui_ph(self):
		return self.run_test("실존주의", "{{ko-IPA|com=1|ui=4}}", "실쫀주의/실쫀주이", "ph")
	def test_siljonjuui_rr(self):
		return self.run_test("실존주의", "{{ko-IPA|com=1|ui=4}}", "siljonjuui", "rr")
	def test_siljonjuui_rrr(self):
		return self.run_test("실존주의", "{{ko-IPA|com=1|ui=4}}", "siljonjuui", "rrr")
	def test_siljonjuui_mr(self):
		return self.run_test("실존주의", "{{ko-IPA|com=1|ui=4}}", "silchonjuŭi", "mr")
	def test_siljonjuui_yr(self):
		return self.run_test("실존주의", "{{ko-IPA|com=1|ui=4}}", "silqcon.cwuuy", "yr")
	def test_siljonjuui_ipa(self):
		return self.run_test("실존주의", "{{ko-IPA|com=1|ui=4}}", "[ɕʰiʎt͡ɕ͈o̞ɲd͡ʑuɰi] ~ [ɕʰiʎt͡ɕ͈o̞ɲd͡ʑui]", "ipa")

	def test_seonmudangi_saram_jamneunda_ph(self):
		return self.run_test("선무당이 사람 잡는다", "{{ko-IPA|l=1,6}}", "선(ː)무당이 사(ː)람 잠는다", "ph")
	def test_seonmudangi_saram_jamneunda_rr(self):
		return self.run_test("선무당이 사람 잡는다", "{{ko-IPA|l=1,6}}", "seonmudang'i saram jamneunda", "rr")
	def test_seonmudangi_saram_jamneunda_rrr(self):
		return self.run_test("선무당이 사람 잡는다", "{{ko-IPA|l=1,6}}", "seonmudang'i salam jabneunda", "rrr")
	def test_seonmudangi_saram_jamneunda_mr(self):
		return self.run_test("선무당이 사람 잡는다", "{{ko-IPA|l=1,6}}", "sŏnmudangi saram chamnŭnda", "mr")
	def test_seonmudangi_saram_jamneunda_yr(self):
		return self.run_test("선무당이 사람 잡는다", "{{ko-IPA|l=1,6}}", "sēnmutangi sālam capnunta", "yr")
	def test_seonmudangi_saram_jamneunda_ipa(self):
		return self.run_test("선무당이 사람 잡는다", "{{ko-IPA|l=1,6}}", "[ˈsʰɘ(ː)nmuda̠ŋi sʰa̠(ː)ɾa̠m t͡ɕa̠mnɯnda̠]", "ipa")

	def test_Nikollaseu_ph(self):
		return self.run_test("니콜라스", "{{ko-IPA|cap=y|com=3}}", "니콜라쓰", "ph")
	def test_Nikollaseu_rr(self):
		return self.run_test("니콜라스", "{{ko-IPA|cap=y|com=3}}", "Nikollaseu", "rr")
	def test_Nikollaseu_rrr(self):
		return self.run_test("니콜라스", "{{ko-IPA|cap=y|com=3}}", "Nikollaseu", "rrr")
	def test_Nikollaseu_mr(self):
		return self.run_test("니콜라스", "{{ko-IPA|cap=y|com=3}}", "Nik'ollassŭ", "mr")
	def test_Nikollaseu_yr(self):
		return self.run_test("니콜라스", "{{ko-IPA|cap=y|com=3}}", "ni.khollaqsu", "yr")
	def test_Nikollaseu_ipa(self):
		return self.run_test("니콜라스", "{{ko-IPA|cap=y|com=3}}", "[nikʰo̞ɭɭa̠s͈ɯ]", "ipa")

	def test_goui_sagu_ph(self):
		return self.run_test("고의사구", "{{ko-IPA|고의 사구|ui=2|l=1,4}}", "고(ː)의 사(ː)구/고(ː)이 사(ː)구", "ph")
	def test_goui_sagu_rr(self):
		return self.run_test("고의사구", "{{ko-IPA|고의 사구|ui=2|l=1,4}}", "goui sagu", "rr")
	def test_goui_sagu_rrr(self):
		return self.run_test("고의사구", "{{ko-IPA|고의 사구|ui=2|l=1,4}}", "goui sagu", "rrr")
	def test_goui_sagu_mr(self):
		return self.run_test("고의사구", "{{ko-IPA|고의 사구|ui=2|l=1,4}}", "koŭi sagu", "mr")
	def test_goui_sagu_yr(self):
		return self.run_test("고의사구", "{{ko-IPA|고의 사구|ui=2|l=1,4}}", "kōuy sākwu", "yr")
	def test_goui_sagu_ipa(self):
		return self.run_test("고의사구", "{{ko-IPA|고의 사구|ui=2|l=1,4}}", "[ˈko̞(ː)ɰi sʰa̠(ː)ɡu] ~ [ˈko̞(ː)i sʰa̠(ː)ɡu]", "ipa")

	def test_sarangui_mae_ph(self):
		return self.run_test("사랑의 매", "{{ko-IPA|uie=3}}", "사랑의 매/사랑에 매/사랑의 메/사랑에 메", "ph")
	def test_sarangui_mae_rr(self):
		return self.run_test("사랑의 매", "{{ko-IPA|uie=3}}", "sarang'ui mae", "rr")
	def test_sarangui_mae_rrr(self):
		return self.run_test("사랑의 매", "{{ko-IPA|uie=3}}", "salang'ui mae", "rrr")
	def test_sarangui_mae_mr(self):
		return self.run_test("사랑의 매", "{{ko-IPA|uie=3}}", "sarangŭi mae", "mr")
	def test_sarangui_mae_yr(self):
		return self.run_test("사랑의 매", "{{ko-IPA|uie=3}}", "salanguy may", "yr")
	def test_sarangui_mae_ipa(self):
		return self.run_test("사랑의 매", "{{ko-IPA|uie=3}}", "[sʰa̠ɾa̠ŋɰi mɛ] ~ [sʰa̠ɾa̠ŋe̞ mɛ] ~ [sʰa̠ɾa̠ŋɰi me̞] ~ [sʰa̠ɾa̠ŋe̞ me̞]", "ipa")

	def test_Hanguk_jeonjaeng_ph(self):
		return self.run_test("한국전쟁", "{{ko-IPA|cap=y|한국 전쟁|l=1,4}}", "한(ː)국 전(ː)쟁/한(ː)국 전(ː)젱", "ph")
	def test_Hanguk_jeonjaeng_rr(self):
		return self.run_test("한국전쟁", "{{ko-IPA|cap=y|한국 전쟁|l=1,4}}", "Han'guk jeonjaeng", "rr")
	def test_Hanguk_jeonjaeng_rrr(self):
		return self.run_test("한국전쟁", "{{ko-IPA|cap=y|한국 전쟁|l=1,4}}", "Hangug jeonjaeng", "rrr")
	def test_Hanguk_jeonjaeng_mr(self):
		return self.run_test("한국전쟁", "{{ko-IPA|cap=y|한국 전쟁|l=1,4}}", "Han'guk chŏnjaeng", "mr")
	def test_Hanguk_jeonjaeng_yr(self):
		return self.run_test("한국전쟁", "{{ko-IPA|cap=y|한국 전쟁|l=1,4}}", "hānkwuk cēn.cayng", "yr")
	def test_Hanguk_jeonjaeng_ipa(self):
		return self.run_test("한국전쟁", "{{ko-IPA|cap=y|한국 전쟁|l=1,4}}", "[ˈha̠(ː)nɡuk̚ t͡ɕɘ(ː)ɲd͡ʑɛŋ] ~ [ˈha̠(ː)nɡuk̚ t͡ɕɘ(ː)ɲd͡ʑe̞ŋ]", "ipa")

	def test_Ellijabeseu_ph(self):
		return self.run_test("엘리자베스", "{{ko-IPA|cap=y|com=5}}", "엘리자베스", "ph")
	def test_Ellijabeseu_rr(self):
		return self.run_test("엘리자베스", "{{ko-IPA|cap=y|com=5}}", "Ellijabeseu", "rr")
	def test_Ellijabeseu_rrr(self):
		return self.run_test("엘리자베스", "{{ko-IPA|cap=y|com=5}}", "Ellijabeseu", "rrr")
	def test_Ellijabeseu_mr(self):
		return self.run_test("엘리자베스", "{{ko-IPA|cap=y|com=5}}", "Ellijabesŭ", "mr")
	def test_Ellijabeseu_yr(self):
		return self.run_test("엘리자베스", "{{ko-IPA|cap=y|com=5}}", "eyllicapeysu", "yr")
	def test_Ellijabeseu_ipa(self):
		return self.run_test("엘리자베스", "{{ko-IPA|cap=y|com=5}}", "[e̞ʎʎid͡ʑa̠be̞sʰɯ]", "ipa")

	def test_ingicheok_ph(self):
		return self.run_test("인기척", "{{ko-IPA||com=1}}", "인끼척", "ph")
	def test_ingicheok_rr(self):
		return self.run_test("인기척", "{{ko-IPA||com=1}}", "in'gicheok", "rr")
	def test_ingicheok_rrr(self):
		return self.run_test("인기척", "{{ko-IPA||com=1}}", "ingicheog", "rrr")
	def test_ingicheok_mr(self):
		return self.run_test("인기척", "{{ko-IPA||com=1}}", "inkich'ŏk", "mr")
	def test_ingicheok_yr(self):
		return self.run_test("인기척", "{{ko-IPA||com=1}}", "inqki.chek", "yr")
	def test_ingicheok_ipa(self):
		return self.run_test("인기척", "{{ko-IPA||com=1}}", "[ink͈it͡ɕʰʌ̹k̚]", "ipa")

	def test_Cheorui_jangmak_ph(self):
		return self.run_test("철의 장막", "{{ko-IPA|cap=y|uie=2}}", "처릐 장막/처레 장막", "ph")
	def test_Cheorui_jangmak_rr(self):
		return self.run_test("철의 장막", "{{ko-IPA|cap=y|uie=2}}", "Cheorui jangmak", "rr")
	def test_Cheorui_jangmak_rrr(self):
		return self.run_test("철의 장막", "{{ko-IPA|cap=y|uie=2}}", "Cheol'ui jangmag", "rrr")
	def test_Cheorui_jangmak_mr(self):
		return self.run_test("철의 장막", "{{ko-IPA|cap=y|uie=2}}", "Ch'ŏrŭi changmak", "mr")
	def test_Cheorui_jangmak_yr(self):
		return self.run_test("철의 장막", "{{ko-IPA|cap=y|uie=2}}", "chel.uy cangmak", "yr")
	def test_Cheorui_jangmak_ipa(self):
		return self.run_test("철의 장막", "{{ko-IPA|cap=y|uie=2}}", "[t͡ɕʰʌ̹ɾɰi t͡ɕa̠ŋma̠k̚] ~ [t͡ɕʰʌ̹ɾe̞ t͡ɕa̠ŋma̠k̚]", "ipa")

	def test_Sobieteu_sahoejuui_gonghwaguk_yeonbang_ph(self):
		return self.run_test("소비에트 사회주의 공화국 연방", "{{ko-IPA|cap=y|l=11|ui=9}}", "소비에트 사훼주의 공(ː)화국 연방/소비에트 사훼주의 공(ː)화국 연방/소비에트 사회주의 공(ː)화국 연방/소비에트 사회주이 공(ː)화국 연방", "ph")
	def test_Sobieteu_sahoejuui_gonghwaguk_yeonbang_rr(self):
		return self.run_test("소비에트 사회주의 공화국 연방", "{{ko-IPA|cap=y|l=11|ui=9}}", "Sobieteu sahoejuui gonghwaguk yeonbang", "rr")
	def test_Sobieteu_sahoejuui_gonghwaguk_yeonbang_rrr(self):
		return self.run_test("소비에트 사회주의 공화국 연방", "{{ko-IPA|cap=y|l=11|ui=9}}", "Sobieteu sahoejuui gonghwagug yeonbang", "rrr")
	def test_Sobieteu_sahoejuui_gonghwaguk_yeonbang_mr(self):
		return self.run_test("소비에트 사회주의 공화국 연방", "{{ko-IPA|cap=y|l=11|ui=9}}", "Sobiet'ŭ sahoejuŭi konghwaguk yŏnbang", "mr")
	def test_Sobieteu_sahoejuui_gonghwaguk_yeonbang_yr(self):
		return self.run_test("소비에트 사회주의 공화국 연방", "{{ko-IPA|cap=y|l=11|ui=9}}", "sopiey.thu sahoycwuuy kōnghwakwuk yenpang", "yr")
	def test_Sobieteu_sahoejuui_gonghwaguk_yeonbang_ipa(self):
		return self.run_test("소비에트 사회주의 공화국 연방", "{{ko-IPA|cap=y|l=11|ui=9}}", "[sʰo̞bie̞tʰɯ sʰa̠βwe̞d͡ʑuɰi ko̞(ː)ŋβwa̠ɡuk̚ jʌ̹nba̠ŋ] ~ [sʰo̞bie̞tʰɯ sʰa̠βwe̞d͡ʑuɰi ko̞(ː)ŋβwa̠ɡuk̚ jʌ̹nba̠ŋ] ~ [sʰo̞bie̞tʰɯ sʰa̠ɦø̞d͡ʑuɰi ko̞(ː)ŋβwa̠ɡuk̚ jʌ̹nba̠ŋ] ~ [sʰo̞bie̞tʰɯ sʰa̠ɦø̞d͡ʑui ko̞(ː)ŋβwa̠ɡuk̚ jʌ̹nba̠ŋ]", "ipa")

	def test_yennieung_ph(self):
		return self.run_test("옛이응", "{{ko-IPA|ni=2|l=y}}", "옌(ː)니응", "ph")
	def test_yennieung_rr(self):
		return self.run_test("옛이응", "{{ko-IPA|ni=2|l=y}}", "yennieung", "rr")
	def test_yennieung_rrr(self):
		return self.run_test("옛이응", "{{ko-IPA|ni=2|l=y}}", "yes'ieung", "rrr")
	def test_yennieung_mr(self):
		return self.run_test("옛이응", "{{ko-IPA|ni=2|l=y}}", "yenniŭng", "mr")
	def test_yennieung_yr(self):
		return self.run_test("옛이응", "{{ko-IPA|ni=2|l=y}}", "yēysniung", "yr")
	def test_yennieung_ipa(self):
		return self.run_test("옛이응", "{{ko-IPA|ni=2|l=y}}", "[ˈje̞(ː)nniɯŋ]", "ipa")

	def test_samyeongdangui_sacheotbang_ph(self):
		return self.run_test("사명당의 사첫방", "{{ko-IPA|l=y|uie=4|nobc=7}}", "사(ː)명당의 사첟빵/사(ː)명당에 사첟빵/사(ː)명당의 사처빵/사(ː)명당에 사처빵", "ph")
	def test_samyeongdangui_sacheotbang_rr(self):
		return self.run_test("사명당의 사첫방", "{{ko-IPA|l=y|uie=4|nobc=7}}", "samyeongdang'ui sacheotbang", "rr")
	def test_samyeongdangui_sacheotbang_rrr(self):
		return self.run_test("사명당의 사첫방", "{{ko-IPA|l=y|uie=4|nobc=7}}", "samyeongdang'ui sacheosbang", "rrr")
	def test_samyeongdangui_sacheotbang_mr(self):
		return self.run_test("사명당의 사첫방", "{{ko-IPA|l=y|uie=4|nobc=7}}", "samyŏngdangŭi sach'ŏtpang", "mr")
	def test_samyeongdangui_sacheotbang_yr(self):
		return self.run_test("사명당의 사첫방", "{{ko-IPA|l=y|uie=4|nobc=7}}", "sāmyengtanguy sa.chespang", "yr")
	def test_samyeongdangui_sacheotbang_ipa(self):
		return self.run_test("사명당의 사첫방", "{{ko-IPA|l=y|uie=4|nobc=7}}", "[ˈsʰa̠(ː)mjʌ̹ŋda̠ŋɰi sʰa̠t͡ɕʰʌ̹t̚p͈a̠ŋ] ~ [ˈsʰa̠(ː)mjʌ̹ŋda̠ŋe̞ sʰa̠t͡ɕʰʌ̹t̚p͈a̠ŋ] ~ [ˈsʰa̠(ː)mjʌ̹ŋda̠ŋɰi sʰa̠t͡ɕʰʌ̹p͈a̠ŋ] ~ [ˈsʰa̠(ː)mjʌ̹ŋda̠ŋe̞ sʰa̠t͡ɕʰʌ̹p͈a̠ŋ]", "ipa")

	def test_Noseuweseuteu_junju_ph(self):
		return self.run_test("노스웨스트 준주", "{{ko-IPA|l=7|com=1|cap=y}}", "노쓰웨스트 준(ː)주", "ph")
	def test_Noseuweseuteu_junju_rr(self):
		return self.run_test("노스웨스트 준주", "{{ko-IPA|l=7|com=1|cap=y}}", "Noseuweseuteu junju", "rr")
	def test_Noseuweseuteu_junju_rrr(self):
		return self.run_test("노스웨스트 준주", "{{ko-IPA|l=7|com=1|cap=y}}", "Noseuweseuteu junju", "rrr")
	def test_Noseuweseuteu_junju_mr(self):
		return self.run_test("노스웨스트 준주", "{{ko-IPA|l=7|com=1|cap=y}}", "Nossŭwesŭt'ŭ chunju", "mr")
	def test_Noseuweseuteu_junju_yr(self):
		return self.run_test("노스웨스트 준주", "{{ko-IPA|l=7|com=1|cap=y}}", "noqsuweysu.thu cwūn.cwu", "yr")
	def test_Noseuweseuteu_junju_ipa(self):
		return self.run_test("노스웨스트 준주", "{{ko-IPA|l=7|com=1|cap=y}}", "[no̞s͈ɯwe̞sʰɯtʰɯ t͡ɕu(ː)ɲd͡ʑu]", "ipa")

	def test_bansinbanui_ph(self):
		return self.run_test("반신반의", "{{ko-IPA|l=1,3|ui=4}}", "반(ː)신바(ː)늬/반(ː)신바(ː)니", "ph")
	def test_bansinbanui_rr(self):
		return self.run_test("반신반의", "{{ko-IPA|l=1,3|ui=4}}", "bansinbanui", "rr")
	def test_bansinbanui_rrr(self):
		return self.run_test("반신반의", "{{ko-IPA|l=1,3|ui=4}}", "bansinban'ui", "rrr")
	def test_bansinbanui_mr(self):
		return self.run_test("반신반의", "{{ko-IPA|l=1,3|ui=4}}", "pansinbanŭi", "mr")
	def test_bansinbanui_yr(self):
		return self.run_test("반신반의", "{{ko-IPA|l=1,3|ui=4}}", "pānsinpān.uy", "yr")
	def test_bansinbanui_ipa(self):
		return self.run_test("반신반의", "{{ko-IPA|l=1,3|ui=4}}", "[ˈpa̠(ː)nɕʰinba̠(ː)nɰi] ~ [ˈpa̠(ː)nɕʰinba̠(ː)ni]", "ipa")

	def test_hoheup_gyetong_ph(self):
		return self.run_test("호흡계통", "{{ko-ipa|호흡 계통|l=4}}", "호흡 계(ː)통/호흡 게(ː)통", "ph")
	def test_hoheup_gyetong_rr(self):
		return self.run_test("호흡계통", "{{ko-ipa|호흡 계통|l=4}}", "hoheup gyetong", "rr")
	def test_hoheup_gyetong_rrr(self):
		return self.run_test("호흡계통", "{{ko-ipa|호흡 계통|l=4}}", "hoheub gyetong", "rrr")
	def test_hoheup_gyetong_mr(self):
		return self.run_test("호흡계통", "{{ko-ipa|호흡 계통|l=4}}", "hohŭp kyet'ong", "mr")
	def test_hoheup_gyetong_yr(self):
		return self.run_test("호흡계통", "{{ko-ipa|호흡 계통|l=4}}", "hohup kyēy.thong", "yr")
	def test_hoheup_gyetong_ipa(self):
		return self.run_test("호흡계통", "{{ko-ipa|호흡 계통|l=4}}", "[ɸʷo̞ɣɯp̚ kje̞(ː)tʰo̞ŋ] ~ [ɸʷo̞ɣɯp̚ ke̞(ː)tʰo̞ŋ]", "ipa")

	def test_gwigatgil_ph(self):
		return self.run_test("귀갓길", "{{ko-IPA|com=2|l=y|nobc=2}}", "귀(ː)갇낄/귀(ː)가낄", "ph")
	def test_gwigatgil_rr(self):
		return self.run_test("귀갓길", "{{ko-IPA|com=2|l=y|nobc=2}}", "gwigatgil", "rr")
	def test_gwigatgil_rrr(self):
		return self.run_test("귀갓길", "{{ko-IPA|com=2|l=y|nobc=2}}", "gwigasgil", "rrr")
	def test_gwigatgil_mr(self):
		return self.run_test("귀갓길", "{{ko-IPA|com=2|l=y|nobc=2}}", "kwigatkil", "mr")
	def test_gwigatgil_yr(self):
		return self.run_test("귀갓길", "{{ko-IPA|com=2|l=y|nobc=2}}", "kwīkasqkil", "yr")
	def test_gwigatgil_ipa(self):
		return self.run_test("귀갓길", "{{ko-IPA|com=2|l=y|nobc=2}}", "[ˈkɥi(ː)ɡa̠t̚k͈iɭ] ~ [ˈkɥi(ː)ɡa̠k͈iɭ] ~ [ˈky(ː)ɡa̠t̚k͈iɭ] ~ [ˈky(ː)ɡa̠k͈iɭ]", "ipa")

	def test_hagyotgil_ph(self):
		return self.run_test("하굣길", "{{ko-IPA|nobc=2|l=y}}", "하(ː)굗낄/하(ː)교낄", "ph")
	def test_hagyotgil_rr(self):
		return self.run_test("하굣길", "{{ko-IPA|nobc=2|l=y}}", "hagyotgil", "rr")
	def test_hagyotgil_rrr(self):
		return self.run_test("하굣길", "{{ko-IPA|nobc=2|l=y}}", "hagyosgil", "rrr")
	def test_hagyotgil_mr(self):
		return self.run_test("하굣길", "{{ko-IPA|nobc=2|l=y}}", "hagyotkil", "mr")
	def test_hagyotgil_yr(self):
		return self.run_test("하굣길", "{{ko-IPA|nobc=2|l=y}}", "hākyoskil", "yr")
	def test_hagyotgil_ipa(self):
		return self.run_test("하굣길", "{{ko-IPA|nobc=2|l=y}}", "[ˈha̠(ː)ɡjot̚k͈iɭ] ~ [ˈha̠(ː)ɡjok͈iɭ]", "ipa")

	def test_Yeongnyeonbang_ph(self):
		return self.run_test("영연방", "{{ko-IPA|cap=y|ni=2}}", "영년방", "ph")
	def test_Yeongnyeonbang_rr(self):
		return self.run_test("영연방", "{{ko-IPA|cap=y|ni=2}}", "Yeongnyeonbang", "rr")
	def test_Yeongnyeonbang_rrr(self):
		return self.run_test("영연방", "{{ko-IPA|cap=y|ni=2}}", "Yeong'yeonbang", "rrr")
	def test_Yeongnyeonbang_mr(self):
		return self.run_test("영연방", "{{ko-IPA|cap=y|ni=2}}", "Yŏngnyŏnbang", "mr")
	def test_Yeongnyeonbang_yr(self):
		return self.run_test("영연방", "{{ko-IPA|cap=y|ni=2}}", "yengnyenpang", "yr")
	def test_Yeongnyeonbang_ipa(self):
		return self.run_test("영연방", "{{ko-IPA|cap=y|ni=2}}", "[jʌ̹ŋɲʌ̹nba̠ŋ]", "ipa")

	def test_samga_goinui_myeongbogeul_bimnida_ph(self):
		return self.run_test("삼가 고인의 명복을 빕니다", "{{ko-IPA|l=4,12|uie=6}}", "삼가 고(ː)이늬 명보글 빔(ː)니다/삼가 고(ː)이네 명보글 빔(ː)니다", "ph")
	def test_samga_goinui_myeongbogeul_bimnida_rr(self):
		return self.run_test("삼가 고인의 명복을 빕니다", "{{ko-IPA|l=4,12|uie=6}}", "samga goinui myeongbogeul bimnida", "rr")
	def test_samga_goinui_myeongbogeul_bimnida_rrr(self):
		return self.run_test("삼가 고인의 명복을 빕니다", "{{ko-IPA|l=4,12|uie=6}}", "samga goin'ui myeongbog'eul bibnida", "rrr")
	def test_samga_goinui_myeongbogeul_bimnida_mr(self):
		return self.run_test("삼가 고인의 명복을 빕니다", "{{ko-IPA|l=4,12|uie=6}}", "samga koinŭi myŏngbogŭl pimnida", "mr")
	def test_samga_goinui_myeongbogeul_bimnida_yr(self):
		return self.run_test("삼가 고인의 명복을 빕니다", "{{ko-IPA|l=4,12|uie=6}}", "samka kōin.uy myengpok.ul pīpnita", "yr")
	def test_samga_goinui_myeongbogeul_bimnida_ipa(self):
		return self.run_test("삼가 고인의 명복을 빕니다", "{{ko-IPA|l=4,12|uie=6}}", "[sʰa̠mɡa̠ ko̞(ː)inɰi mjʌ̹ŋbo̞ɡɯɭ pi(ː)mnida̠] ~ [sʰa̠mɡa̠ ko̞(ː)ine̞ mjʌ̹ŋbo̞ɡɯɭ pi(ː)mnida̠]", "ipa")

	def test_jeomjeomjeom_ph(self):
		return self.run_test("점점점", "{{ko-IPA|com=0,1,2}}", "쩜쩜쩜", "ph")
	def test_jeomjeomjeom_rr(self):
		return self.run_test("점점점", "{{ko-IPA|com=0,1,2}}", "jeomjeomjeom", "rr")
	def test_jeomjeomjeom_rrr(self):
		return self.run_test("점점점", "{{ko-IPA|com=0,1,2}}", "jeomjeomjeom", "rrr")
	def test_jeomjeomjeom_mr(self):
		return self.run_test("점점점", "{{ko-IPA|com=0,1,2}}", "chŏmchŏmchŏm", "mr")
	def test_jeomjeomjeom_yr(self):
		return self.run_test("점점점", "{{ko-IPA|com=0,1,2}}", "qcemqcemqcem", "yr")
	def test_jeomjeomjeom_ipa(self):
		return self.run_test("점점점", "{{ko-IPA|com=0,1,2}}", "[t͡ɕ͈ʌ̹mt͡ɕ͈ʌ̹mt͡ɕ͈ʌ̹m]", "ipa")

	def test_Hwaiteuhoseu_ph(self):
		return self.run_test("화이트호스", "{{ko-IPA|com=4|cap=y}}", "화이트호쓰", "ph")
	def test_Hwaiteuhoseu_rr(self):
		return self.run_test("화이트호스", "{{ko-IPA|com=4|cap=y}}", "Hwaiteuhoseu", "rr")
	def test_Hwaiteuhoseu_rrr(self):
		return self.run_test("화이트호스", "{{ko-IPA|com=4|cap=y}}", "Hwaiteuhoseu", "rrr")
	def test_Hwaiteuhoseu_mr(self):
		return self.run_test("화이트호스", "{{ko-IPA|com=4|cap=y}}", "Hwait'ŭhossŭ", "mr")
	def test_Hwaiteuhoseu_yr(self):
		return self.run_test("화이트호스", "{{ko-IPA|com=4|cap=y}}", "hwai.thuhoqsu", "yr")
	def test_Hwaiteuhoseu_ipa(self):
		return self.run_test("화이트호스", "{{ko-IPA|com=4|cap=y}}", "[ɸwa̠itʰɯβo̞s͈ɯ]", "ipa")

	def test_sangho_hwaksil_pagoe_ph(self):
		return self.run_test("상호확실파괴", "{{ko-IPA|상호 확실 파괴|l=7}}", "상호 확씰 파(ː)궤/상호 확씰 파(ː)괴", "ph")
	def test_sangho_hwaksil_pagoe_rr(self):
		return self.run_test("상호확실파괴", "{{ko-IPA|상호 확실 파괴|l=7}}", "sangho hwaksil pagoe", "rr")
	def test_sangho_hwaksil_pagoe_rrr(self):
		return self.run_test("상호확실파괴", "{{ko-IPA|상호 확실 파괴|l=7}}", "sangho hwagsil pagoe", "rrr")
	def test_sangho_hwaksil_pagoe_mr(self):
		return self.run_test("상호확실파괴", "{{ko-IPA|상호 확실 파괴|l=7}}", "sangho hwaksil p'agoe", "mr")
	def test_sangho_hwaksil_pagoe_yr(self):
		return self.run_test("상호확실파괴", "{{ko-IPA|상호 확실 파괴|l=7}}", "sangho hwak.sil phākoy", "yr")
	def test_sangho_hwaksil_pagoe_ipa(self):
		return self.run_test("상호확실파괴", "{{ko-IPA|상호 확실 파괴|l=7}}", "[sʰa̠ŋβo̞ ɸwa̠kɕ͈iɭ pʰa̠(ː)ɡwe̞] ~ [sʰa̠ŋβo̞ ɸwa̠kɕ͈iɭ pʰa̠(ː)ɡø̞]", "ipa")

	def test_hando_kkeutdo_eopda_ph(self):
		return self.run_test("한도 끝도 없다", "{{ko-IPA|l=1,7}}", "한(ː)도 끋또 업(ː)따", "ph")
	def test_hando_kkeutdo_eopda_rr(self):
		return self.run_test("한도 끝도 없다", "{{ko-IPA|l=1,7}}", "hando kkeutdo eopda", "rr")
	def test_hando_kkeutdo_eopda_rrr(self):
		return self.run_test("한도 끝도 없다", "{{ko-IPA|l=1,7}}", "hando kkeutdo eobsda", "rrr")
	def test_hando_kkeutdo_eopda_mr(self):
		return self.run_test("한도 끝도 없다", "{{ko-IPA|l=1,7}}", "hando kkŭtto ŏpta", "mr")
	def test_hando_kkeutdo_eopda_yr(self):
		return self.run_test("한도 끝도 없다", "{{ko-IPA|l=1,7}}", "hānto kkuthto ēpsta", "yr")
	def test_hando_kkeutdo_eopda_ipa(self):
		return self.run_test("한도 끝도 없다", "{{ko-IPA|l=1,7}}", "[ˈha̠(ː)ndo̞ k͈ɯt̚t͈o̞ ɘ(ː)p̚t͈a̠]", "ipa")

	def test_Gangwondo_posu_ph(self):
		return self.run_test("강원도 포수", "{{ko-IPA|l=5|cap=y}}", "강원도 포(ː)수", "ph")
	def test_Gangwondo_posu_rr(self):
		return self.run_test("강원도 포수", "{{ko-IPA|l=5|cap=y}}", "Gang'wondo posu", "rr")
	def test_Gangwondo_posu_rrr(self):
		return self.run_test("강원도 포수", "{{ko-IPA|l=5|cap=y}}", "Gang'wondo posu", "rrr")
	def test_Gangwondo_posu_mr(self):
		return self.run_test("강원도 포수", "{{ko-IPA|l=5|cap=y}}", "Kangwŏndo p'osu", "mr")
	def test_Gangwondo_posu_yr(self):
		return self.run_test("강원도 포수", "{{ko-IPA|l=5|cap=y}}", "kangwento phōswu", "yr")
	def test_Gangwondo_posu_ipa(self):
		return self.run_test("강원도 포수", "{{ko-IPA|l=5|cap=y}}", "[ka̠ŋwʌ̹ndo̞ pʰo̞(ː)sʰu]", "ipa")

	def test_horangineun_jugeoseo_gajugeul_namgigo_sarameun_jugeoseo_ireumeul_namginda_ph(self):
		return self.run_test("호랑이는 죽어서 가죽을 남기고 사람은 죽어서 이름을 남긴다", "{{ko-IPA|l=1,14,18}}", "호(ː)랑이는 주거서 가주글 남(ː)기고 사(ː)라믄 주거서 이르믈 남긴다", "ph")
	def test_horangineun_jugeoseo_gajugeul_namgigo_sarameun_jugeoseo_ireumeul_namginda_rr(self):
		return self.run_test("호랑이는 죽어서 가죽을 남기고 사람은 죽어서 이름을 남긴다", "{{ko-IPA|l=1,14,18}}", "horang'ineun jugeoseo gajugeul namgigo sarameun jugeoseo ireumeul namginda", "rr")
	def test_horangineun_jugeoseo_gajugeul_namgigo_sarameun_jugeoseo_ireumeul_namginda_rrr(self):
		return self.run_test("호랑이는 죽어서 가죽을 남기고 사람은 죽어서 이름을 남긴다", "{{ko-IPA|l=1,14,18}}", "holang'ineun jug'eoseo gajug'eul namgigo salam'eun jug'eoseo ileum'eul namginda", "rrr")
	def test_horangineun_jugeoseo_gajugeul_namgigo_sarameun_jugeoseo_ireumeul_namginda_mr(self):
		return self.run_test("호랑이는 죽어서 가죽을 남기고 사람은 죽어서 이름을 남긴다", "{{ko-IPA|l=1,14,18}}", "horanginŭn chugŏsŏ kajugŭl namgigo saramŭn chugŏsŏ irŭmŭl namginda", "mr")
	def test_horangineun_jugeoseo_gajugeul_namgigo_sarameun_jugeoseo_ireumeul_namginda_yr(self):
		return self.run_test("호랑이는 죽어서 가죽을 남기고 사람은 죽어서 이름을 남긴다", "{{ko-IPA|l=1,14,18}}", "hōlanginun cwuk.ese kacwuk.ul nāmkiko sālam.un cwuk.ese ilum.ul namkinta", "yr")
	def test_horangineun_jugeoseo_gajugeul_namgigo_sarameun_jugeoseo_ireumeul_namginda_ipa(self):
		return self.run_test("호랑이는 죽어서 가죽을 남기고 사람은 죽어서 이름을 남긴다", "{{ko-IPA|l=1,14,18}}", "[ˈɸʷo̞(ː)ɾa̠ŋinɯn t͡ɕuɡʌ̹sʰʌ̹ ka̠d͡ʑuɡɯɭ na̠(ː)mɡiɡo̞ sʰa̠(ː)ɾa̠mɯn t͡ɕuɡʌ̹sʰʌ̹ iɾɯmɯɭ na̠mɡinda̠]", "ipa")

	def test_geupjinjeok_yeoseongjuui_ph(self):
		return self.run_test("급진적 여성주의", "{{ko-IPA|ui=8}}", "급찐적 여성주의/급찐적 여성주이", "ph")
	def test_geupjinjeok_yeoseongjuui_rr(self):
		return self.run_test("급진적 여성주의", "{{ko-IPA|ui=8}}", "geupjinjeok yeoseongjuui", "rr")
	def test_geupjinjeok_yeoseongjuui_rrr(self):
		return self.run_test("급진적 여성주의", "{{ko-IPA|ui=8}}", "geubjinjeog yeoseongjuui", "rrr")
	def test_geupjinjeok_yeoseongjuui_mr(self):
		return self.run_test("급진적 여성주의", "{{ko-IPA|ui=8}}", "kŭpchinjŏk yŏsŏngjuŭi", "mr")
	def test_geupjinjeok_yeoseongjuui_yr(self):
		return self.run_test("급진적 여성주의", "{{ko-IPA|ui=8}}", "kupcin.cek yesengcwuuy", "yr")
	def test_geupjinjeok_yeoseongjuui_ipa(self):
		return self.run_test("급진적 여성주의", "{{ko-IPA|ui=8}}", "[kɯp̚t͡ɕ͈iɲd͡ʑʌ̹k̚ jʌ̹sʰʌ̹ŋd͡ʑuɰi] ~ [kɯp̚t͡ɕ͈iɲd͡ʑʌ̹k̚ jʌ̹sʰʌ̹ŋd͡ʑui]", "ipa")

	def test_gungihullyeon_ph(self):
		return self.run_test("군기훈련", "{{ko-IPA|l=3}}", "군기훌(ː)련", "ph")
	def test_gungihullyeon_rr(self):
		return self.run_test("군기훈련", "{{ko-IPA|l=3}}", "gun'gihullyeon", "rr")
	def test_gungihullyeon_rrr(self):
		return self.run_test("군기훈련", "{{ko-IPA|l=3}}", "gungihunlyeon", "rrr")
	def test_gungihullyeon_mr(self):
		return self.run_test("군기훈련", "{{ko-IPA|l=3}}", "kun'gihullyŏn", "mr")
	def test_gungihullyeon_yr(self):
		return self.run_test("군기훈련", "{{ko-IPA|l=3}}", "kwunkihwūnlyen", "yr")
	def test_gungihullyeon_ipa(self):
		return self.run_test("군기훈련", "{{ko-IPA|l=3}}", "[kunɡiβu(ː)ʎʎʌ̹n]", "ipa")

	def test_hubang_juui_ph(self):
		return self.run_test("후방주의", "{{ko-IPA|후방 주의|l=1,4|ui=5}}", "후(ː)방 주(ː)의/후(ː)방 주(ː)이", "ph")
	def test_hubang_juui_rr(self):
		return self.run_test("후방주의", "{{ko-IPA|후방 주의|l=1,4|ui=5}}", "hubang juui", "rr")
	def test_hubang_juui_rrr(self):
		return self.run_test("후방주의", "{{ko-IPA|후방 주의|l=1,4|ui=5}}", "hubang juui", "rrr")
	def test_hubang_juui_mr(self):
		return self.run_test("후방주의", "{{ko-IPA|후방 주의|l=1,4|ui=5}}", "hubang chuŭi", "mr")
	def test_hubang_juui_yr(self):
		return self.run_test("후방주의", "{{ko-IPA|후방 주의|l=1,4|ui=5}}", "hwūpang cwūuy", "yr")
	def test_hubang_juui_ipa(self):
		return self.run_test("후방주의", "{{ko-IPA|후방 주의|l=1,4|ui=5}}", "[ˈɸʷu(ː)ba̠ŋ t͡ɕu(ː)ɰi] ~ [ˈɸʷu(ː)ba̠ŋ t͡ɕu(ː)i]", "ipa")

	def test_choejeo_imgeum_ph(self):
		return self.run_test("최저임금", "{{ko-ipa|최저 임금|l=1,4}}", "췌(ː)저 임(ː)금/최(ː)저 임(ː)금", "ph")
	def test_choejeo_imgeum_rr(self):
		return self.run_test("최저임금", "{{ko-ipa|최저 임금|l=1,4}}", "choejeo imgeum", "rr")
	def test_choejeo_imgeum_rrr(self):
		return self.run_test("최저임금", "{{ko-ipa|최저 임금|l=1,4}}", "choejeo imgeum", "rrr")
	def test_choejeo_imgeum_mr(self):
		return self.run_test("최저임금", "{{ko-ipa|최저 임금|l=1,4}}", "ch'oejŏ imgŭm", "mr")
	def test_choejeo_imgeum_yr(self):
		return self.run_test("최저임금", "{{ko-ipa|최저 임금|l=1,4}}", "chōyce īmkum", "yr")
	def test_choejeo_imgeum_ipa(self):
		return self.run_test("최저임금", "{{ko-ipa|최저 임금|l=1,4}}", "[ˈt͡ɕʰwe̞(ː)d͡ʑʌ̹ i(ː)mɡɯm] ~ [ˈt͡ɕʰø̞(ː)d͡ʑʌ̹ i(ː)mɡɯm]", "ipa")

	def test_jeongsingwaui_ph(self):
		return self.run_test("정신과의", "{{ko-IPA|com=2|ui=4}}", "정신꽈의/정신꽈이", "ph")
	def test_jeongsingwaui_rr(self):
		return self.run_test("정신과의", "{{ko-IPA|com=2|ui=4}}", "jeongsin'gwaui", "rr")
	def test_jeongsingwaui_rrr(self):
		return self.run_test("정신과의", "{{ko-IPA|com=2|ui=4}}", "jeongsingwaui", "rrr")
	def test_jeongsingwaui_mr(self):
		return self.run_test("정신과의", "{{ko-IPA|com=2|ui=4}}", "chŏngsinkwaŭi", "mr")
	def test_jeongsingwaui_yr(self):
		return self.run_test("정신과의", "{{ko-IPA|com=2|ui=4}}", "cengsinqkwauy", "yr")
	def test_jeongsingwaui_ipa(self):
		return self.run_test("정신과의", "{{ko-IPA|com=2|ui=4}}", "[t͡ɕʌ̹ŋɕʰink͈wa̠ɰi] ~ [t͡ɕʌ̹ŋɕʰink͈wa̠i]", "ipa")

	def test_jeoui_ph(self):
		return self.run_test("저의", "{{ko-IPA|uie=2}}", "저의/저에", "ph")
	def test_jeoui_rr(self):
		return self.run_test("저의", "{{ko-IPA|uie=2}}", "jeoui", "rr")
	def test_jeoui_rrr(self):
		return self.run_test("저의", "{{ko-IPA|uie=2}}", "jeoui", "rrr")
	def test_jeoui_mr(self):
		return self.run_test("저의", "{{ko-IPA|uie=2}}", "chŏŭi", "mr")
	def test_jeoui_yr(self):
		return self.run_test("저의", "{{ko-IPA|uie=2}}", "ceuy", "yr")
	def test_jeoui_ipa(self):
		return self.run_test("저의", "{{ko-IPA|uie=2}}", "[t͡ɕʌ̹ɰi] ~ [t͡ɕʌ̹e̞]", "ipa")

	def test_goso_gongpojeung_ph(self):
		return self.run_test("고소공포증", "{{ko-IPA|고소 공포증|l=4|com=5}}", "고소 공(ː)포쯩", "ph")
	def test_goso_gongpojeung_rr(self):
		return self.run_test("고소공포증", "{{ko-IPA|고소 공포증|l=4|com=5}}", "goso gongpojeung", "rr")
	def test_goso_gongpojeung_rrr(self):
		return self.run_test("고소공포증", "{{ko-IPA|고소 공포증|l=4|com=5}}", "goso gongpojeung", "rrr")
	def test_goso_gongpojeung_mr(self):
		return self.run_test("고소공포증", "{{ko-IPA|고소 공포증|l=4|com=5}}", "koso kongp'ochŭng", "mr")
	def test_goso_gongpojeung_yr(self):
		return self.run_test("고소공포증", "{{ko-IPA|고소 공포증|l=4|com=5}}", "koso kōngphoqcung", "yr")
	def test_goso_gongpojeung_ipa(self):
		return self.run_test("고소공포증", "{{ko-IPA|고소 공포증|l=4|com=5}}", "[ko̞sʰo̞ ko̞(ː)ŋpʰo̞t͡ɕ͈ɯŋ]", "ipa")

	def test_jeongjeom_ph(self):
		return self.run_test("정점", "{{ko-IPA|l=n|com=1}}", "정쩜", "ph")
	def test_jeongjeom_rr(self):
		return self.run_test("정점", "{{ko-IPA|l=n|com=1}}", "jeongjeom", "rr")
	def test_jeongjeom_rrr(self):
		return self.run_test("정점", "{{ko-IPA|l=n|com=1}}", "jeongjeom", "rrr")
	def test_jeongjeom_mr(self):
		return self.run_test("정점", "{{ko-IPA|l=n|com=1}}", "chŏngchŏm", "mr")
	def test_jeongjeom_yr(self):
		return self.run_test("정점", "{{ko-IPA|l=n|com=1}}", "cengqcem", "yr")
	def test_jeongjeom_ipa(self):
		return self.run_test("정점", "{{ko-IPA|l=n|com=1}}", "[t͡ɕʌ̹ŋt͡ɕ͈ʌ̹m]", "ipa")

	def test_torandae_ph(self):
		return self.run_test("토란대", "{{ko-IPA|l=n|com=2}}", "토란때/토란떼", "ph")
	def test_torandae_rr(self):
		return self.run_test("토란대", "{{ko-IPA|l=n|com=2}}", "torandae", "rr")
	def test_torandae_rrr(self):
		return self.run_test("토란대", "{{ko-IPA|l=n|com=2}}", "tolandae", "rrr")
	def test_torandae_mr(self):
		return self.run_test("토란대", "{{ko-IPA|l=n|com=2}}", "t'orantae", "mr")
	def test_torandae_yr(self):
		return self.run_test("토란대", "{{ko-IPA|l=n|com=2}}", "tholanqtay", "yr")
	def test_torandae_ipa(self):
		return self.run_test("토란대", "{{ko-IPA|l=n|com=2}}", "[tʰo̞ɾa̠nt͈ɛ] ~ [tʰo̞ɾa̠nt͈e̞]", "ipa")

	def test_gayatgo_ph(self):
		return self.run_test("가얏고", "{{ko-IPA|l=n|nobc=2}}", "가얃꼬/가야꼬", "ph")
	def test_gayatgo_rr(self):
		return self.run_test("가얏고", "{{ko-IPA|l=n|nobc=2}}", "gayatgo", "rr")
	def test_gayatgo_rrr(self):
		return self.run_test("가얏고", "{{ko-IPA|l=n|nobc=2}}", "gayasgo", "rrr")
	def test_gayatgo_mr(self):
		return self.run_test("가얏고", "{{ko-IPA|l=n|nobc=2}}", "kayatko", "mr")
	def test_gayatgo_yr(self):
		return self.run_test("가얏고", "{{ko-IPA|l=n|nobc=2}}", "ka.yasko", "yr")
	def test_gayatgo_ipa(self):
		return self.run_test("가얏고", "{{ko-IPA|l=n|nobc=2}}", "[ka̠ja̠t̚k͈o̞] ~ [ka̠ja̠k͈o̞]", "ipa")

	def test_Guyugoseullabia_makedonia_gonghwaguk_ph(self):
		return self.run_test("구유고슬라비아 마케도니아 공화국", "{{ko-IPA|cap=y|l=1,15}}", "구(ː)유고슬라비아 마케도니아 공(ː)화국", "ph")
	def test_Guyugoseullabia_makedonia_gonghwaguk_rr(self):
		return self.run_test("구유고슬라비아 마케도니아 공화국", "{{ko-IPA|cap=y|l=1,15}}", "Guyugoseullabia makedonia gonghwaguk", "rr")
	def test_Guyugoseullabia_makedonia_gonghwaguk_rrr(self):
		return self.run_test("구유고슬라비아 마케도니아 공화국", "{{ko-IPA|cap=y|l=1,15}}", "Guyugoseullabia makedonia gonghwagug", "rrr")
	def test_Guyugoseullabia_makedonia_gonghwaguk_mr(self):
		return self.run_test("구유고슬라비아 마케도니아 공화국", "{{ko-IPA|cap=y|l=1,15}}", "Kuyugosŭllabia mak'edonia konghwaguk", "mr")
	def test_Guyugoseullabia_makedonia_gonghwaguk_yr(self):
		return self.run_test("구유고슬라비아 마케도니아 공화국", "{{ko-IPA|cap=y|l=1,15}}", "kwū.yukosullapia ma.kheytonia kōnghwakwuk", "yr")
	def test_Guyugoseullabia_makedonia_gonghwaguk_ipa(self):
		return self.run_test("구유고슬라비아 마케도니아 공화국", "{{ko-IPA|cap=y|l=1,15}}", "[ˈku(ː)juɡo̞sʰɯɭɭa̠bia̠ ma̠kʰe̞do̞nia̠ ko̞(ː)ŋβwa̠ɡuk̚]", "ipa")

	def test_banjiseongjuui_ph(self):
		return self.run_test("반지성주의", "{{ko-IPA|l=y|ui=5}}", "반(ː)지성주의/반(ː)지성주이", "ph")
	def test_banjiseongjuui_rr(self):
		return self.run_test("반지성주의", "{{ko-IPA|l=y|ui=5}}", "banjiseongjuui", "rr")
	def test_banjiseongjuui_rrr(self):
		return self.run_test("반지성주의", "{{ko-IPA|l=y|ui=5}}", "banjiseongjuui", "rrr")
	def test_banjiseongjuui_mr(self):
		return self.run_test("반지성주의", "{{ko-IPA|l=y|ui=5}}", "panjisŏngjuŭi", "mr")
	def test_banjiseongjuui_yr(self):
		return self.run_test("반지성주의", "{{ko-IPA|l=y|ui=5}}", "pān.cisengcwuuy", "yr")
	def test_banjiseongjuui_ipa(self):
		return self.run_test("반지성주의", "{{ko-IPA|l=y|ui=5}}", "[ˈpa̠(ː)ɲd͡ʑisʰʌ̹ŋd͡ʑuɰi] ~ [ˈpa̠(ː)ɲd͡ʑisʰʌ̹ŋd͡ʑui]", "ipa")

	def test_suhaeng_pyeongga_ph(self):
		return self.run_test("수행평가", "{{ko-IPA|수행 평가|l=4|com=4}}", "수행 평(ː)까/수헹 평(ː)까", "ph")
	def test_suhaeng_pyeongga_rr(self):
		return self.run_test("수행평가", "{{ko-IPA|수행 평가|l=4|com=4}}", "suhaeng pyeongga", "rr")
	def test_suhaeng_pyeongga_rrr(self):
		return self.run_test("수행평가", "{{ko-IPA|수행 평가|l=4|com=4}}", "suhaeng pyeongga", "rrr")
	def test_suhaeng_pyeongga_mr(self):
		return self.run_test("수행평가", "{{ko-IPA|수행 평가|l=4|com=4}}", "suhaeng p'yŏngka", "mr")
	def test_suhaeng_pyeongga_yr(self):
		return self.run_test("수행평가", "{{ko-IPA|수행 평가|l=4|com=4}}", "swuhayng phyēngqka", "yr")
	def test_suhaeng_pyeongga_ipa(self):
		return self.run_test("수행평가", "{{ko-IPA|수행 평가|l=4|com=4}}", "[sʰuɦɛŋ pʰjɘ(ː)ŋk͈a̠] ~ [sʰuɦe̞ŋ pʰjɘ(ː)ŋk͈a̠]", "ipa")

	def test_pyouimunja_ph(self):
		return self.run_test("표의문자", "{{ko-IPA|ui=2|com=3}}", "표의문짜/표이문짜", "ph")
	def test_pyouimunja_rr(self):
		return self.run_test("표의문자", "{{ko-IPA|ui=2|com=3}}", "pyouimunja", "rr")
	def test_pyouimunja_rrr(self):
		return self.run_test("표의문자", "{{ko-IPA|ui=2|com=3}}", "pyouimunja", "rrr")
	def test_pyouimunja_mr(self):
		return self.run_test("표의문자", "{{ko-IPA|ui=2|com=3}}", "p'yoŭimuncha", "mr")
	def test_pyouimunja_yr(self):
		return self.run_test("표의문자", "{{ko-IPA|ui=2|com=3}}", "phyouymunqca", "yr")
	def test_pyouimunja_ipa(self):
		return self.run_test("표의문자", "{{ko-IPA|ui=2|com=3}}", "[pʰjoɰimuɲt͡ɕ͈a̠] ~ [pʰjoimuɲt͡ɕ͈a̠]", "ipa")

	def test_Geumgangsan_ph(self):
		return self.run_test("금강산", "{{ko-IPA|l=n|cap=y}}", "금강산", "ph")
	def test_Geumgangsan_rr(self):
		return self.run_test("금강산", "{{ko-IPA|l=n|cap=y}}", "Geumgangsan", "rr")
	def test_Geumgangsan_rrr(self):
		return self.run_test("금강산", "{{ko-IPA|l=n|cap=y}}", "Geumgangsan", "rrr")
	def test_Geumgangsan_mr(self):
		return self.run_test("금강산", "{{ko-IPA|l=n|cap=y}}", "Kŭmgangsan", "mr")
	def test_Geumgangsan_yr(self):
		return self.run_test("금강산", "{{ko-IPA|l=n|cap=y}}", "kumkangsan", "yr")
	def test_Geumgangsan_ipa(self):
		return self.run_test("금강산", "{{ko-IPA|l=n|cap=y}}", "[kɯmɡa̠ŋsʰa̠n]", "ipa")

	def test_sageonui_jipyeongseon_ph(self):
		return self.run_test("사건의 지평선", "{{ko-IPA|l=y|com=1|uie=3}}", "사(ː)꺼늬 지평선/사(ː)꺼네 지평선", "ph")
	def test_sageonui_jipyeongseon_rr(self):
		return self.run_test("사건의 지평선", "{{ko-IPA|l=y|com=1|uie=3}}", "sageonui jipyeongseon", "rr")
	def test_sageonui_jipyeongseon_rrr(self):
		return self.run_test("사건의 지평선", "{{ko-IPA|l=y|com=1|uie=3}}", "sageon'ui jipyeongseon", "rrr")
	def test_sageonui_jipyeongseon_mr(self):
		return self.run_test("사건의 지평선", "{{ko-IPA|l=y|com=1|uie=3}}", "sakŏnŭi chip'yŏngsŏn", "mr")
	def test_sageonui_jipyeongseon_yr(self):
		return self.run_test("사건의 지평선", "{{ko-IPA|l=y|com=1|uie=3}}", "sāqken.uy ci.phyengsen", "yr")
	def test_sageonui_jipyeongseon_ipa(self):
		return self.run_test("사건의 지평선", "{{ko-IPA|l=y|com=1|uie=3}}", "[ˈsʰa̠(ː)k͈ʌ̹nɰi t͡ɕipʰjʌ̹ŋsʰʌ̹n] ~ [ˈsʰa̠(ː)k͈ʌ̹ne̞ t͡ɕipʰjʌ̹ŋsʰʌ̹n]", "ipa")

	def test_duppulkoppulso_ph(self):
		return self.run_test("두뿔코뿔소", "{{ko-IPA|l=y|com=4}}", "두(ː)뿔코뿔쏘", "ph")
	def test_duppulkoppulso_rr(self):
		return self.run_test("두뿔코뿔소", "{{ko-IPA|l=y|com=4}}", "duppulkoppulso", "rr")
	def test_duppulkoppulso_rrr(self):
		return self.run_test("두뿔코뿔소", "{{ko-IPA|l=y|com=4}}", "du'ppulko'ppulso", "rrr")
	def test_duppulkoppulso_mr(self):
		return self.run_test("두뿔코뿔소", "{{ko-IPA|l=y|com=4}}", "tuppulk'oppulsso", "mr")
	def test_duppulkoppulso_yr(self):
		return self.run_test("두뿔코뿔소", "{{ko-IPA|l=y|com=4}}", "twū.ppul.kho.ppulqso", "yr")
	def test_duppulkoppulso_ipa(self):
		return self.run_test("두뿔코뿔소", "{{ko-IPA|l=y|com=4}}", "[ˈtu(ː)p͈uɭkʰo̞p͈uɭs͈o̞]", "ipa")

	def test_Apeurikaui_ppul_ph(self):
		return self.run_test("아프리카의 뿔", "{{ko-IPA|uie=5|cap=y}}", "아프리카의 뿔/아프리카에 뿔", "ph")
	def test_Apeurikaui_ppul_rr(self):
		return self.run_test("아프리카의 뿔", "{{ko-IPA|uie=5|cap=y}}", "Apeurikaui ppul", "rr")
	def test_Apeurikaui_ppul_rrr(self):
		return self.run_test("아프리카의 뿔", "{{ko-IPA|uie=5|cap=y}}", "Apeulikaui ppul", "rrr")
	def test_Apeurikaui_ppul_mr(self):
		return self.run_test("아프리카의 뿔", "{{ko-IPA|uie=5|cap=y}}", "Ap'ŭrik'aŭi ppul", "mr")
	def test_Apeurikaui_ppul_yr(self):
		return self.run_test("아프리카의 뿔", "{{ko-IPA|uie=5|cap=y}}", "a.phuli.khauy ppul", "yr")
	def test_Apeurikaui_ppul_ipa(self):
		return self.run_test("아프리카의 뿔", "{{ko-IPA|uie=5|cap=y}}", "[a̠pʰɯɾikʰa̠ɰi p͈uɭ] ~ [a̠pʰɯɾikʰa̠e̞ p͈uɭ]", "ipa")

	def test_gollibwonchuri_ph(self):
		return self.run_test("골잎원추리", "{{ko-IPA|ni=2|bcred=2}}", "골리붠추리", "ph")
	def test_gollibwonchuri_rr(self):
		return self.run_test("골잎원추리", "{{ko-IPA|ni=2|bcred=2}}", "gollibwonchuri", "rr")
	def test_gollibwonchuri_rrr(self):
		return self.run_test("골잎원추리", "{{ko-IPA|ni=2|bcred=2}}", "gol'ip'wonchuli", "rrr")
	def test_gollibwonchuri_mr(self):
		return self.run_test("골잎원추리", "{{ko-IPA|ni=2|bcred=2}}", "kollibwŏnch'uri", "mr")
	def test_gollibwonchuri_yr(self):
		return self.run_test("골잎원추리", "{{ko-IPA|ni=2|bcred=2}}", "kolliph.wen.chwuli", "yr")
	def test_gollibwonchuri_ipa(self):
		return self.run_test("골잎원추리", "{{ko-IPA|ni=2|bcred=2}}", "[ko̞ʎʎibwʌ̹ɲt͡ɕʰuɾi]", "ipa")

	def test_nambuk_ph(self):
		return self.run_test("남북", "{{ko-IPA|cap=n}}", "남북", "ph")
	def test_nambuk_rr(self):
		return self.run_test("남북", "{{ko-IPA|cap=n}}", "nambuk", "rr")
	def test_nambuk_rrr(self):
		return self.run_test("남북", "{{ko-IPA|cap=n}}", "nambug", "rrr")
	def test_nambuk_mr(self):
		return self.run_test("남북", "{{ko-IPA|cap=n}}", "nambuk", "mr")
	def test_nambuk_yr(self):
		return self.run_test("남북", "{{ko-IPA|cap=n}}", "nampuk", "yr")
	def test_nambuk_ipa(self):
		return self.run_test("남북", "{{ko-IPA|cap=n}}", "[na̠mbuk̚]", "ipa")

	def test_Deinno_ph(self):
		return self.run_test("데인로", "{{ko-IPA|cap=y|nn=3}}", "데인노", "ph")
	def test_Deinno_rr(self):
		return self.run_test("데인로", "{{ko-IPA|cap=y|nn=3}}", "Deinno", "rr")
	def test_Deinno_rrr(self):
		return self.run_test("데인로", "{{ko-IPA|cap=y|nn=3}}", "Deinlo", "rrr")
	def test_Deinno_mr(self):
		return self.run_test("데인로", "{{ko-IPA|cap=y|nn=3}}", "Teinno", "mr")
	def test_Deinno_yr(self):
		return self.run_test("데인로", "{{ko-IPA|cap=y|nn=3}}", "teyinlo", "yr")
	def test_Deinno_ipa(self):
		return self.run_test("데인로", "{{ko-IPA|cap=y|nn=3}}", "[te̞inno̞]", "ipa")

	def test_geongang_yeomnyeojeung_ph(self):
		return self.run_test("건강염려증", "{{ko-ipa|건강 염려증|l=1,4|com=5}}", "건(ː)강 염(ː)녀쯩", "ph")
	def test_geongang_yeomnyeojeung_rr(self):
		return self.run_test("건강염려증", "{{ko-ipa|건강 염려증|l=1,4|com=5}}", "geon'gang yeomnyeojeung", "rr")
	def test_geongang_yeomnyeojeung_rrr(self):
		return self.run_test("건강염려증", "{{ko-ipa|건강 염려증|l=1,4|com=5}}", "geongang yeomlyeojeung", "rrr")
	def test_geongang_yeomnyeojeung_mr(self):
		return self.run_test("건강염려증", "{{ko-ipa|건강 염려증|l=1,4|com=5}}", "kŏn'gang yŏmnyŏchŭng", "mr")
	def test_geongang_yeomnyeojeung_yr(self):
		return self.run_test("건강염려증", "{{ko-ipa|건강 염려증|l=1,4|com=5}}", "kēnkang yēmlyeqcung", "yr")
	def test_geongang_yeomnyeojeung_ipa(self):
		return self.run_test("건강염려증", "{{ko-ipa|건강 염려증|l=1,4|com=5}}", "[ˈkɘ(ː)nɡa̠ŋ jɘ(ː)mɲʌ̹t͡ɕ͈ɯŋ]", "ipa")

	def test_jeoneun_hanguk_saramieyo_ph(self):
		return self.run_test("저는 한국 사람이에요", "{{ko-IPA|l=4,7}}", "저는 한(ː)국 사(ː)라미에요", "ph")
	def test_jeoneun_hanguk_saramieyo_rr(self):
		return self.run_test("저는 한국 사람이에요", "{{ko-IPA|l=4,7}}", "jeoneun han'guk saramieyo", "rr")
	def test_jeoneun_hanguk_saramieyo_rrr(self):
		return self.run_test("저는 한국 사람이에요", "{{ko-IPA|l=4,7}}", "jeoneun hangug salam'ieyo", "rrr")
	def test_jeoneun_hanguk_saramieyo_mr(self):
		return self.run_test("저는 한국 사람이에요", "{{ko-IPA|l=4,7}}", "chŏnŭn han'guk saramieyo", "mr")
	def test_jeoneun_hanguk_saramieyo_yr(self):
		return self.run_test("저는 한국 사람이에요", "{{ko-IPA|l=4,7}}", "cenun hānkwuk sālam.ieyyo", "yr")
	def test_jeoneun_hanguk_saramieyo_ipa(self):
		return self.run_test("저는 한국 사람이에요", "{{ko-IPA|l=4,7}}", "[t͡ɕʌ̹nɯn ha̠(ː)nɡuk̚ sʰa̠(ː)ɾa̠mie̞jo]", "ipa")

	def test_tupiseu_ph(self):
		return self.run_test("투피스", "{{ko-IPA|l=1,2}}", "투(ː)피(ː)스", "ph")
	def test_tupiseu_rr(self):
		return self.run_test("투피스", "{{ko-IPA|l=1,2}}", "tupiseu", "rr")
	def test_tupiseu_rrr(self):
		return self.run_test("투피스", "{{ko-IPA|l=1,2}}", "tupiseu", "rrr")
	def test_tupiseu_mr(self):
		return self.run_test("투피스", "{{ko-IPA|l=1,2}}", "t'up'isŭ", "mr")
	def test_tupiseu_yr(self):
		return self.run_test("투피스", "{{ko-IPA|l=1,2}}", "thwū.phīsu", "yr")
	def test_tupiseu_ipa(self):
		return self.run_test("투피스", "{{ko-IPA|l=1,2}}", "[ˈtʰu(ː)pʰi(ː)sʰɯ]", "ipa")

	def test_ijo_ph(self):
		return self.run_test("이조", "{{ko-IPA|l=1|com=1}}", "이(ː)쪼", "ph")
	def test_ijo_rr(self):
		return self.run_test("이조", "{{ko-IPA|l=1|com=1}}", "ijo", "rr")
	def test_ijo_rrr(self):
		return self.run_test("이조", "{{ko-IPA|l=1|com=1}}", "ijo", "rrr")
	def test_ijo_mr(self):
		return self.run_test("이조", "{{ko-IPA|l=1|com=1}}", "icho", "mr")
	def test_ijo_yr(self):
		return self.run_test("이조", "{{ko-IPA|l=1|com=1}}", "īqco", "yr")
	def test_ijo_ipa(self):
		return self.run_test("이조", "{{ko-IPA|l=1|com=1}}", "[ˈi(ː)t͡ɕ͈o̞]", "ipa")

	def test_sonagineun_pihaneun_ge_sangchaek_ph(self):
		return self.run_test("소나기는 피하는 게 상책", "{{ko-IPA|l=6,12}}", "소나기는 피(ː)하는 게 상(ː)책/소나기는 피(ː)하는 게 상(ː)첵", "ph")
	def test_sonagineun_pihaneun_ge_sangchaek_rr(self):
		return self.run_test("소나기는 피하는 게 상책", "{{ko-IPA|l=6,12}}", "sonagineun pihaneun ge sangchaek", "rr")
	def test_sonagineun_pihaneun_ge_sangchaek_rrr(self):
		return self.run_test("소나기는 피하는 게 상책", "{{ko-IPA|l=6,12}}", "sonagineun pihaneun ge sangchaeg", "rrr")
	def test_sonagineun_pihaneun_ge_sangchaek_mr(self):
		return self.run_test("소나기는 피하는 게 상책", "{{ko-IPA|l=6,12}}", "sonaginŭn p'ihanŭn ke sangch'aek", "mr")
	def test_sonagineun_pihaneun_ge_sangchaek_yr(self):
		return self.run_test("소나기는 피하는 게 상책", "{{ko-IPA|l=6,12}}", "sonakinun phīhanun key sāngchayk", "yr")
	def test_sonagineun_pihaneun_ge_sangchaek_ipa(self):
		return self.run_test("소나기는 피하는 게 상책", "{{ko-IPA|l=6,12}}", "[sʰo̞na̠ɡinɯn pʰi(ː)ɦa̠nɯn ke̞ sʰa̠(ː)ŋt͡ɕʰɛk̚] ~ [sʰo̞na̠ɡinɯn pʰi(ː)ɦa̠nɯn ke̞ sʰa̠(ː)ŋt͡ɕʰe̞k̚]", "ipa")

	def test_kareul_ppobasseumyeon_murado_sseoreora_ph(self):
		return self.run_test("칼을 뽑았으면 무라도 썰어라", "{{ko-IPA|l=9}}", "카를 뽀바쓰면 무(ː)라도 써러라", "ph")
	def test_kareul_ppobasseumyeon_murado_sseoreora_rr(self):
		return self.run_test("칼을 뽑았으면 무라도 썰어라", "{{ko-IPA|l=9}}", "kareul ppobasseumyeon murado sseoreora", "rr")
	def test_kareul_ppobasseumyeon_murado_sseoreora_rrr(self):
		return self.run_test("칼을 뽑았으면 무라도 썰어라", "{{ko-IPA|l=9}}", "kal'eul ppob'ass'eumyeon mulado sseol'eola", "rrr")
	def test_kareul_ppobasseumyeon_murado_sseoreora_mr(self):
		return self.run_test("칼을 뽑았으면 무라도 썰어라", "{{ko-IPA|l=9}}", "k'arŭl ppobassŭmyŏn murado ssŏrŏra", "mr")
	def test_kareul_ppobasseumyeon_murado_sseoreora_yr(self):
		return self.run_test("칼을 뽑았으면 무라도 썰어라", "{{ko-IPA|l=9}}", "khal.ul ppop.ass.umyen mūlato ssel.ela", "yr")
	def test_kareul_ppobasseumyeon_murado_sseoreora_ipa(self):
		return self.run_test("칼을 뽑았으면 무라도 썰어라", "{{ko-IPA|l=9}}", "[kʰa̠ɾɯɭ p͈o̞ba̠s͈ɯmjʌ̹n mu(ː)ɾa̠do̞ s͈ʌ̹ɾʌ̹ɾa̠]", "ipa")

	def test_yagu_dongnyeongsang_ph(self):
		return self.run_test("야구 동영상", "{{ko-IPA|l=1,4|ni=5}}", "야(ː)구 동(ː)녕상", "ph")
	def test_yagu_dongnyeongsang_rr(self):
		return self.run_test("야구 동영상", "{{ko-IPA|l=1,4|ni=5}}", "yagu dongnyeongsang", "rr")
	def test_yagu_dongnyeongsang_rrr(self):
		return self.run_test("야구 동영상", "{{ko-IPA|l=1,4|ni=5}}", "yagu dong'yeongsang", "rrr")
	def test_yagu_dongnyeongsang_mr(self):
		return self.run_test("야구 동영상", "{{ko-IPA|l=1,4|ni=5}}", "yagu tongnyŏngsang", "mr")
	def test_yagu_dongnyeongsang_yr(self):
		return self.run_test("야구 동영상", "{{ko-IPA|l=1,4|ni=5}}", "yākwu tōngnyengsang", "yr")
	def test_yagu_dongnyeongsang_ipa(self):
		return self.run_test("야구 동영상", "{{ko-IPA|l=1,4|ni=5}}", "[ˈja̠(ː)ɡu to̞(ː)ŋɲʌ̹ŋsʰa̠ŋ]", "ipa")

	def test_Jeicha_segye_daejeon_ph(self):
		return self.run_test("제2차 세계 대전", "{{ko-IPA|제이차 세계 대전|cap=y|l=1,5,8}}", "제(ː)이차 세(ː)계 대(ː)전/제(ː)이차 세(ː)게 대(ː)전/제(ː)이차 세(ː)계 데(ː)전/제(ː)이차 세(ː)게 데(ː)전", "ph")
	def test_Jeicha_segye_daejeon_rr(self):
		return self.run_test("제2차 세계 대전", "{{ko-IPA|제이차 세계 대전|cap=y|l=1,5,8}}", "Jeicha segye daejeon", "rr")
	def test_Jeicha_segye_daejeon_rrr(self):
		return self.run_test("제2차 세계 대전", "{{ko-IPA|제이차 세계 대전|cap=y|l=1,5,8}}", "Jeicha segye daejeon", "rrr")
	def test_Jeicha_segye_daejeon_mr(self):
		return self.run_test("제2차 세계 대전", "{{ko-IPA|제이차 세계 대전|cap=y|l=1,5,8}}", "Cheich'a segye taejŏn", "mr")
	def test_Jeicha_segye_daejeon_yr(self):
		return self.run_test("제2차 세계 대전", "{{ko-IPA|제이차 세계 대전|cap=y|l=1,5,8}}", "cēyi.cha sēykyey tāycen", "yr")
	def test_Jeicha_segye_daejeon_ipa(self):
		return self.run_test("제2차 세계 대전", "{{ko-IPA|제이차 세계 대전|cap=y|l=1,5,8}}", "[ˈt͡ɕe̞(ː)it͡ɕʰa̠ sʰe̞(ː)ɡje̞ tɛ(ː)d͡ʑʌ̹n] ~ [ˈt͡ɕe̞(ː)it͡ɕʰa̠ sʰe̞(ː)ɡe̞ tɛ(ː)d͡ʑʌ̹n] ~ [ˈt͡ɕe̞(ː)it͡ɕʰa̠ sʰe̞(ː)ɡje̞ te̞(ː)d͡ʑʌ̹n] ~ [ˈt͡ɕe̞(ː)it͡ɕʰa̠ sʰe̞(ː)ɡe̞ te̞(ː)d͡ʑʌ̹n]", "ipa")


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
