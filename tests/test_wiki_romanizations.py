import unittest
from src.wiktionary_romanization import WiktionaryRomanization

class TestWikiRomanizations(unittest.TestCase):
    def test_beomnyulhak_ph(self):
            self.run_test("법률학", "{{ko-IPA}}", "범뉼학", "ph")
    def test_beomnyulhak_rr(self):
            self.run_test("법률학", "{{ko-IPA}}", "beomnyulhak", "rr")
    def test_beomnyulhak_rrr(self):
            self.run_test("법률학", "{{ko-IPA}}", "beoblyulhag", "rrr")
    def test_beomnyulhak_mc(self):
            self.run_test("법률학", "{{ko-IPA}}", "pŏmnyurhak", "mr")
    def test_beomnyulhak_yr(self):
            self.run_test("법률학", "{{ko-IPA}}", "peplyul.hak", "yr")
    def test_beomnyulhak_ipa(self):
            self.run_test("법률학", "{{ko-IPA}}", "[pʌ̹mɲuɾɦa̠k̚]", "ipa")

    def test_pyeonchanta_ph(self):
            self.run_test("편찮다", "{{ko-IPA}}", "편찬타", "ph")
    def test_pyeonchanta_rr(self):
            self.run_test("편찮다", "{{ko-IPA}}", "pyeonchanta", "rr")
    def test_pyeonchanta_rrr(self):
            self.run_test("편찮다", "{{ko-IPA}}", "pyeonchanhda", "rrr")
    def test_pyeonchanta_mc(self):
            self.run_test("편찮다", "{{ko-IPA}}", "p'yŏnch'ant'a", "mr")
    def test_pyeonchanta_yr(self):
            self.run_test("편찮다", "{{ko-IPA}}", "phyen.chanhta", "yr")
    def test_pyeonchanta_ipa(self):
            self.run_test("편찮다", "{{ko-IPA}}", "[pʰjʌ̹ɲt͡ɕʰa̠ntʰa̠]", "ipa")

    def test_eumsikgap_ph(self):
            self.run_test("음식값", "{{ko-IPA|l=y}}", "음(ː)식깝", "ph")
    def test_eumsikgap_rr(self):
            self.run_test("음식값", "{{ko-IPA|l=y}}", "eumsikgap", "rr")
    def test_eumsikgap_rrr(self):
            self.run_test("음식값", "{{ko-IPA|l=y}}", "eumsiggabs", "rrr")
    def test_eumsikgap_mc(self):
            self.run_test("음식값", "{{ko-IPA|l=y}}", "ŭmsikkap", "mr")
    def test_eumsikgap_yr(self):
            self.run_test("음식값", "{{ko-IPA|l=y}}", "ūmsik.kaps", "yr")
    def test_eumsikgap_ipa(self):
            self.run_test("음식값", "{{ko-IPA|l=y}}", "[ˈɯ(ː)mɕʰik̚k͈a̠p̚]", "ipa")

    def test_eotteoke_ph(self):
            self.run_test("어떻게", "{{ko-IPA}}", "어떠케", "ph")
    def test_eotteoke_rr(self):
            self.run_test("어떻게", "{{ko-IPA}}", "eotteoke", "rr")
    def test_eotteoke_rrr(self):
            self.run_test("어떻게", "{{ko-IPA}}", "eo'tteohge", "rrr")
    def test_eotteoke_mc(self):
            self.run_test("어떻게", "{{ko-IPA}}", "ŏttŏk'e", "mr")
    def test_eotteoke_yr(self):
            self.run_test("어떻게", "{{ko-IPA}}", "e.ttehkey", "yr")
    def test_eotteoke_ipa(self):
            self.run_test("어떻게", "{{ko-IPA}}", "[ʌ̹t͈ʌ̹kʰe̞]", "ipa")

    def test_myeonmyeot_ph(self):
            self.run_test("몇몇", "{{ko-IPA}}", "면멷", "ph")
    def test_myeonmyeot_rr(self):
            self.run_test("몇몇", "{{ko-IPA}}", "myeonmyeot", "rr")
    def test_myeonmyeot_rrr(self):
            self.run_test("몇몇", "{{ko-IPA}}", "myeochmyeoch", "rrr")
    def test_myeonmyeot_mc(self):
            self.run_test("몇몇", "{{ko-IPA}}", "myŏnmyŏt", "mr")
    def test_myeonmyeot_yr(self):
            self.run_test("몇몇", "{{ko-IPA}}", "myechmyech", "yr")
    def test_myeonmyeot_ipa(self):
            self.run_test("몇몇", "{{ko-IPA}}", "[mjʌ̹nmjʌ̹t̚]", "ipa")

    def test_tteutbakke_ph(self):
            self.run_test("뜻밖에", "{{ko-IPA}}", "뜯빠께", "ph")
    def test_tteutbakke_rr(self):
            self.run_test("뜻밖에", "{{ko-IPA}}", "tteutbakke", "rr")
    def test_tteutbakke_rrr(self):
            self.run_test("뜻밖에", "{{ko-IPA}}", "tteusbakk'e", "rrr")
    def test_tteutbakke_mc(self):
            self.run_test("뜻밖에", "{{ko-IPA}}", "ttŭtpakke", "mr")
    def test_tteutbakke_yr(self):
            self.run_test("뜻밖에", "{{ko-IPA}}", "ttuspakk.ey", "yr")
    def test_tteutbakke_ipa(self):
            self.run_test("뜻밖에", "{{ko-IPA}}", "[t͈ɯt̚p͈a̠k͈e̞]", "ipa")

    def test_kkeunimeopda_ph(self):
            self.run_test("끊임없다", "{{ko-IPA}}", "끄니멉따", "ph")
    def test_kkeunimeopda_rr(self):
            self.run_test("끊임없다", "{{ko-IPA}}", "kkeunimeopda", "rr")
    def test_kkeunimeopda_rrr(self):
            self.run_test("끊임없다", "{{ko-IPA}}", "kkeunh'im'eobsda", "rrr")
    def test_kkeunimeopda_mc(self):
            self.run_test("끊임없다", "{{ko-IPA}}", "kkŭnimŏpta", "mr")
    def test_kkeunimeopda_yr(self):
            self.run_test("끊임없다", "{{ko-IPA}}", "kkunh.im.epsta", "yr")
    def test_kkeunimeopda_ipa(self):
            self.run_test("끊임없다", "{{ko-IPA}}", "[k͈ɯnimʌ̹p̚t͈a̠]", "ipa")

    def test_natseolda_ph(self):
            self.run_test("낯설다", "{{ko-IPA}}", "낟썰다", "ph")
    def test_natseolda_rr(self):
            self.run_test("낯설다", "{{ko-IPA}}", "natseolda", "rr")
    def test_natseolda_rrr(self):
            self.run_test("낯설다", "{{ko-IPA}}", "nachseolda", "rrr")
    def test_natseolda_mc(self):
            self.run_test("낯설다", "{{ko-IPA}}", "nassŏlda", "mr")
    def test_natseolda_yr(self):
            self.run_test("낯설다", "{{ko-IPA}}", "nachselta", "yr")
    def test_natseolda_ipa(self):
            self.run_test("낯설다", "{{ko-IPA}}", "[na̠ss͈ʌ̹ɭda̠]", "ipa")

    def test_gongsanjuui_ph(self):
            self.run_test("공산주의", "{{ko-IPA|l=y|ui=4}}", "공(ː)산주의/공(ː)산주이", "ph")
    def test_gongsanjuui_rr(self):
            self.run_test("공산주의", "{{ko-IPA|l=y|ui=4}}", "gongsanjuui", "rr")
    def test_gongsanjuui_rrr(self):
            self.run_test("공산주의", "{{ko-IPA|l=y|ui=4}}", "gongsanjuui", "rrr")
    def test_gongsanjuui_mc(self):
            self.run_test("공산주의", "{{ko-IPA|l=y|ui=4}}", "kongsanjuŭi", "mr")
    def test_gongsanjuui_yr(self):
            self.run_test("공산주의", "{{ko-IPA|l=y|ui=4}}", "kōngsan.cwuuy", "yr")
    def test_gongsanjuui_ipa(self):
            self.run_test("공산주의", "{{ko-IPA|l=y|ui=4}}", "[ˈko̞(ː)ŋsʰa̠ɲd͡ʑuɰi] ~ [ˈko̞(ː)ŋsʰa̠ɲd͡ʑui]", "ipa")

    def test_gochutgaru_ph(self):
            self.run_test("고춧가루", "{{ko-IPA|nobc=2}}", "고춛까루/고추까루", "ph")
    def test_gochutgaru_rr(self):
            self.run_test("고춧가루", "{{ko-IPA|nobc=2}}", "gochutgaru", "rr")
    def test_gochutgaru_rrr(self):
            self.run_test("고춧가루", "{{ko-IPA|nobc=2}}", "gochusgalu", "rrr")
    def test_gochutgaru_mc(self):
            self.run_test("고춧가루", "{{ko-IPA|nobc=2}}", "koch'utkaru", "mr")
    def test_gochutgaru_yr(self):
            self.run_test("고춧가루", "{{ko-IPA|nobc=2}}", "ko.chwuskalwu", "yr")
    def test_gochutgaru_ipa(self):
            self.run_test("고춧가루", "{{ko-IPA|nobc=2}}", "[ko̞t͡ɕʰut̚k͈a̠ɾu] ~ [ko̞t͡ɕʰuk͈a̠ɾu]", "ipa")

    def test_hapbeophwadoeda_ph(self):
            self.run_test("합법화되다", "{{ko-IPA}}", "합뻐퐈뒈다/합뻐퐈되다", "ph")
    def test_hapbeophwadoeda_rr(self):
            self.run_test("합법화되다", "{{ko-IPA}}", "hapbeophwadoeda", "rr")
    def test_hapbeophwadoeda_rrr(self):
            self.run_test("합법화되다", "{{ko-IPA}}", "habbeobhwadoeda", "rrr")
    def test_hapbeophwadoeda_mc(self):
            self.run_test("합법화되다", "{{ko-IPA}}", "happŏphwadoeda", "mr")
    def test_hapbeophwadoeda_yr(self):
            self.run_test("합법화되다", "{{ko-IPA}}", "hap.pep.hwatoyta", "yr")
    def test_hapbeophwadoeda_ipa(self):
            self.run_test("합법화되다", "{{ko-IPA}}", "[ha̠p̚p͈ʌ̹pʰwa̠dwe̞da̠] ~ [ha̠p̚p͈ʌ̹pʰwa̠dø̞da̠]", "ipa")

    def test_mongmoksi_ph(self):
            self.run_test("몫몫이", "{{ko-IPA}}", "몽목씨", "ph")
    def test_mongmoksi_rr(self):
            self.run_test("몫몫이", "{{ko-IPA}}", "mongmoksi", "rr")
    def test_mongmoksi_rrr(self):
            self.run_test("몫몫이", "{{ko-IPA}}", "mogsmogs'i", "rrr")
    def test_mongmoksi_mc(self):
            self.run_test("몫몫이", "{{ko-IPA}}", "mongmoksi", "mr")
    def test_mongmoksi_yr(self):
            self.run_test("몫몫이", "{{ko-IPA}}", "moksmoks.i", "yr")
    def test_mongmoksi_ipa(self):
            self.run_test("몫몫이", "{{ko-IPA}}", "[mo̞ŋmo̞kɕ͈i]", "ipa")

    def test_gukdarata_ph(self):
            self.run_test("굵다랗다", "{{ko-IPA|l=y}}", "국(ː)따라타", "ph")
    def test_gukdarata_rr(self):
            self.run_test("굵다랗다", "{{ko-IPA|l=y}}", "gukdarata", "rr")
    def test_gukdarata_rrr(self):
            self.run_test("굵다랗다", "{{ko-IPA|l=y}}", "gulgdalahda", "rrr")
    def test_gukdarata_mc(self):
            self.run_test("굵다랗다", "{{ko-IPA|l=y}}", "kuktarat'a", "mr")
    def test_gukdarata_yr(self):
            self.run_test("굵다랗다", "{{ko-IPA|l=y}}", "kwūlktalahta", "yr")
    def test_gukdarata_ipa(self):
            self.run_test("굵다랗다", "{{ko-IPA|l=y}}", "[ˈku(ː)k̚t͈a̠ɾa̠tʰa̠]", "ipa")

    def test_saehae_bongmani_badeuseyo_saehae_bok_mani_badeuseyo_ph(self):
            self.run_test("새해 복 많이 받으세요", "{{ko-IPA|새해 복많이 받으세요|새해 복 많이 받으세요}}", "새해 봉마니 바드세요/세헤 봉마니 바드세요/새해 복 마니 바드세요/세헤 복 마니 바드세요", "ph")
    def test_saehae_bongmani_badeuseyo_saehae_bok_mani_badeuseyo_rr(self):
            self.run_test("새해 복 많이 받으세요", "{{ko-IPA|새해 복많이 받으세요|새해 복 많이 받으세요}}", "saehae bongmani badeuseyo/saehae bok mani badeuseyo", "rr")
    def test_saehae_bongmani_badeuseyo_saehae_bok_mani_badeuseyo_rrr(self):
            self.run_test("새해 복 많이 받으세요", "{{ko-IPA|새해 복많이 받으세요|새해 복 많이 받으세요}}", "saehae bogmanh'i bad'euseyo/saehae bog manh'i bad'euseyo", "rrr")
    def test_saehae_bongmani_badeuseyo_saehae_bok_mani_badeuseyo_mc(self):
            self.run_test("새해 복 많이 받으세요", "{{ko-IPA|새해 복많이 받으세요|새해 복 많이 받으세요}}", "saehae pongmani padŭseyo/saehae pok mani padŭseyo", "mr")
    def test_saehae_bongmani_badeuseyo_saehae_bok_mani_badeuseyo_yr(self):
            self.run_test("새해 복 많이 받으세요", "{{ko-IPA|새해 복많이 받으세요|새해 복 많이 받으세요}}", "sayhay pokmanh.i pat.useyyo/sayhay pok manh.i pat.useyyo", "yr")
    def test_saehae_bongmani_badeuseyo_saehae_bok_mani_badeuseyo_ipa(self):
            self.run_test("새해 복 많이 받으세요", "{{ko-IPA|새해 복많이 받으세요|새해 복 많이 받으세요}}", "[sʰɛɦɛ po̞ŋma̠ni pa̠dɯsʰe̞jo] ~ [sʰe̞ɦe̞ po̞ŋma̠ni pa̠dɯsʰe̞jo] ~ [sʰɛɦɛ po̞k̚ ma̠nipa̠dɯsʰe̞jo] ~ [sʰe̞ɦe̞ po̞k̚ ma̠ni pa̠dɯsʰe̞jo]", "ipa")

    def test_Hanguk_ph(self):
            self.run_test("한국", "{{ko-IPA|l=y|cap=y}}", "한(ː)국", "ph")
    def test_Hanguk_rr(self):
            self.run_test("한국", "{{ko-IPA|l=y|cap=y}}", "Han'guk", "rr")
    def test_Hanguk_rrr(self):
            self.run_test("한국", "{{ko-IPA|l=y|cap=y}}", "Hangug", "rrr")
    def test_Hanguk_mc(self):
            self.run_test("한국", "{{ko-IPA|l=y|cap=y}}", "Han'guk", "mr")
    def test_Hanguk_yr(self):
            self.run_test("한국", "{{ko-IPA|l=y|cap=y}}", "hānkwuk", "yr")
    def test_Hanguk_ipa(self):
            self.run_test("한국", "{{ko-IPA|l=y|cap=y}}", "[ˈha̠(ː)nɡuk̚]", "ipa")

    def test_sangsabyeong_ph(self):
            self.run_test("상사병", "{{ko-IPA|com=2}}", "상사뼝", "ph")
    def test_sangsabyeong_rr(self):
            self.run_test("상사병", "{{ko-IPA|com=2}}", "sangsabyeong", "rr")
    def test_sangsabyeong_rrr(self):
            self.run_test("상사병", "{{ko-IPA|com=2}}", "sangsabyeong", "rrr")
    def test_sangsabyeong_mc(self):
            self.run_test("상사병", "{{ko-IPA|com=2}}", "sangsapyŏng", "mr")
    def test_sangsabyeong_yr(self):
            self.run_test("상사병", "{{ko-IPA|com=2}}", "sangsaqpyeng", "yr")
    def test_sangsabyeong_ipa(self):
            self.run_test("상사병", "{{ko-IPA|com=2}}", "[sʰa̠ŋsʰa̠p͈jʌ̹ŋ]", "ipa")

    def test_seokeul_ph(self):
            self.run_test("서클", "{{ko-IPA|com=0}}", "써클", "ph")
    def test_seokeul_rr(self):
            self.run_test("서클", "{{ko-IPA|com=0}}", "seokeul", "rr")
    def test_seokeul_rrr(self):
            self.run_test("서클", "{{ko-IPA|com=0}}", "seokeul", "rrr")
    def test_seokeul_mc(self):
            self.run_test("서클", "{{ko-IPA|com=0}}", "ssŏk'ŭl", "mr")
    def test_seokeul_yr(self):
            self.run_test("서클", "{{ko-IPA|com=0}}", "qse.khul", "yr")
    def test_seokeul_ipa(self):
            self.run_test("서클", "{{ko-IPA|com=0}}", "[s͈ʌ̹kxɯɭ]", "ipa")

    def test_uigyeonnan_ph(self):
            self.run_test("의견란", "{{ko-IPA|nn=3|l=y}}", "의(ː)견난", "ph")
    def test_uigyeonnan_rr(self):
            self.run_test("의견란", "{{ko-IPA|nn=3|l=y}}", "uigyeonnan", "rr")
    def test_uigyeonnan_rrr(self):
            self.run_test("의견란", "{{ko-IPA|nn=3|l=y}}", "uigyeonlan", "rrr")
    def test_uigyeonnan_mc(self):
            self.run_test("의견란", "{{ko-IPA|nn=3|l=y}}", "ŭigyŏnnan", "mr")
    def test_uigyeonnan_yr(self):
            self.run_test("의견란", "{{ko-IPA|nn=3|l=y}}", "ūykyenlan", "yr")
    def test_uigyeonnan_ipa(self):
            self.run_test("의견란", "{{ko-IPA|nn=3|l=y}}", "[ˈɰi(ː)ɡjʌ̹nna̠n]", "ipa")

    def test_ui_ph(self):
            self.run_test("의", "{{ko-IPA|uie=1}}", "의/에", "ph")
    def test_ui_rr(self):
            self.run_test("의", "{{ko-IPA|uie=1}}", "ui", "rr")
    def test_ui_rrr(self):
            self.run_test("의", "{{ko-IPA|uie=1}}", "ui", "rrr")
    def test_ui_mc(self):
            self.run_test("의", "{{ko-IPA|uie=1}}", "ŭi", "mr")
    def test_ui_yr(self):
            self.run_test("의", "{{ko-IPA|uie=1}}", "uy", "yr")
    def test_ui_ipa(self):
            self.run_test("의", "{{ko-IPA|uie=1}}", "[ɰi] ~ [e̞]", "ipa")

    def test_kkaennip_ph(self):
            self.run_test("깻잎", "{{ko-IPA|ni=2}}", "깬닙/껜닙", "ph")
    def test_kkaennip_rr(self):
            self.run_test("깻잎", "{{ko-IPA|ni=2}}", "kkaennip", "rr")
    def test_kkaennip_rrr(self):
            self.run_test("깻잎", "{{ko-IPA|ni=2}}", "kkaes'ip", "rrr")
    def test_kkaennip_mc(self):
            self.run_test("깻잎", "{{ko-IPA|ni=2}}", "kkaennip", "mr")
    def test_kkaennip_yr(self):
            self.run_test("깻잎", "{{ko-IPA|ni=2}}", "kkaysniph", "yr")
    def test_kkaennip_ipa(self):
            self.run_test("깻잎", "{{ko-IPA|ni=2}}", "[k͈ɛnnip̚] ~ [k͈e̞nnip̚]", "ipa")

    def test_gabeochi_ph(self):
            self.run_test("값어치", "{{ko-IPA|bcred=1}}", "가버치", "ph")
    def test_gabeochi_rr(self):
            self.run_test("값어치", "{{ko-IPA|bcred=1}}", "gabeochi", "rr")
    def test_gabeochi_rrr(self):
            self.run_test("값어치", "{{ko-IPA|bcred=1}}", "gabs'eochi", "rrr")
    def test_gabeochi_mc(self):
            self.run_test("값어치", "{{ko-IPA|bcred=1}}", "kabŏch'i", "mr")
    def test_gabeochi_yr(self):
            self.run_test("값어치", "{{ko-IPA|bcred=1}}", "kaps.e.chi", "yr")
    def test_gabeochi_ipa(self):
            self.run_test("값어치", "{{ko-IPA|bcred=1}}", "[ka̠bʌ̹t͡ɕʰi]", "ipa")

    def test_matheungjeong_ph(self):
            self.run_test("맞흥정", "{{ko-IPA|bcred=1}}", "마틍정", "ph")
    def test_matheungjeong_rr(self):
            self.run_test("맞흥정", "{{ko-IPA|bcred=1}}", "matheungjeong", "rr")
    def test_matheungjeong_rrr(self):
            self.run_test("맞흥정", "{{ko-IPA|bcred=1}}", "majheungjeong", "rrr")
    def test_matheungjeong_mc(self):
            self.run_test("맞흥정", "{{ko-IPA|bcred=1}}", "mathŭngjŏng", "mr")
    def test_matheungjeong_yr(self):
            self.run_test("맞흥정", "{{ko-IPA|bcred=1}}", "mac.hungceng", "yr")
    def test_matheungjeong_ipa(self):
            self.run_test("맞흥정", "{{ko-IPA|bcred=1}}", "[ma̠tʰɯŋd͡ʑʌ̹ŋ]", "ipa")

    def test_godieo_ph(self):
            self.run_test("곧이어", "{{ko-IPA|bcred=1}}", "고디어", "ph")
    def test_godieo_rr(self):
            self.run_test("곧이어", "{{ko-IPA|bcred=1}}", "godieo", "rr")
    def test_godieo_rrr(self):
            self.run_test("곧이어", "{{ko-IPA|bcred=1}}", "god'ieo", "rrr")
    def test_godieo_mc(self):
            self.run_test("곧이어", "{{ko-IPA|bcred=1}}", "kodiŏ", "mr")
    def test_godieo_yr(self):
            self.run_test("곧이어", "{{ko-IPA|bcred=1}}", "kot.ie", "yr")
    def test_godieo_ipa(self):
            self.run_test("곧이어", "{{ko-IPA|bcred=1}}", "[ko̞diʌ̹]", "ipa")

    def test_meositda_ph(self):
            self.run_test("멋있다", "{{ko-IPA|svar=1}}", "머싣따/머딛따", "ph")
    def test_meositda_rr(self):
            self.run_test("멋있다", "{{ko-IPA|svar=1}}", "meositda", "rr")
    def test_meositda_rrr(self):
            self.run_test("멋있다", "{{ko-IPA|svar=1}}", "meos'issda", "rrr")
    def test_meositda_mc(self):
            self.run_test("멋있다", "{{ko-IPA|svar=1}}", "mŏsitta", "mr")
    def test_meositda_yr(self):
            self.run_test("멋있다", "{{ko-IPA|svar=1}}", "mes.issta", "yr")
    def test_meositda_ipa(self):
            self.run_test("멋있다", "{{ko-IPA|svar=1}}", "[mʌ̹ɕʰit̚t͈a̠] ~ [mʌ̹dit̚t͈a̠]", "ipa")

    def test_ttwieodeulda_ph(self):
            self.run_test("뛰어들다", "{{ko-IPA|iot=2}}", "뛰어들다/뛰여들다", "ph")
    def test_ttwieodeulda_rr(self):
            self.run_test("뛰어들다", "{{ko-IPA|iot=2}}", "ttwieodeulda", "rr")
    def test_ttwieodeulda_rrr(self):
            self.run_test("뛰어들다", "{{ko-IPA|iot=2}}", "ttwieodeulda", "rrr")
    def test_ttwieodeulda_mc(self):
            self.run_test("뛰어들다", "{{ko-IPA|iot=2}}", "ttwiŏdŭlda", "mr")
    def test_ttwieodeulda_yr(self):
            self.run_test("뛰어들다", "{{ko-IPA|iot=2}}", "ttwietulta", "yr")
    def test_ttwieodeulda_ipa(self):
            self.run_test("뛰어들다", "{{ko-IPA|iot=2}}", "[t͈ɥiʌ̹dɯɭda̠] ~ [t͈ɥijʌ̹dɯɭda̠] ~ [t͈yʌ̹dɯɭda̠] ~ [t͈yjʌ̹dɯɭda̠]", "ipa")

    def test_gyesok_ph(self):
            self.run_test("계속", "{{ko-IPA|l=y}}", "계(ː)속/게(ː)속", "ph")
    def test_gyesok_rr(self):
            self.run_test("계속", "{{ko-IPA|l=y}}", "gyesok", "rr")
    def test_gyesok_rrr(self):
            self.run_test("계속", "{{ko-IPA|l=y}}", "gyesog", "rrr")
    def test_gyesok_mc(self):
            self.run_test("계속", "{{ko-IPA|l=y}}", "kyesok", "mr")
    def test_gyesok_yr(self):
            self.run_test("계속", "{{ko-IPA|l=y}}", "kyēysok", "yr")
    def test_gyesok_ipa(self):
            self.run_test("계속", "{{ko-IPA|l=y}}", "[ˈkje̞(ː)sʰo̞k̚] ~ [ˈke̞(ː)sʰo̞k̚]", "ipa")

    def test_gyesokdoeda_ph(self):
            self.run_test("계속되다", "{{ko-IPA|l=y}}", "계(ː)속뛔다/계(ː)속뙤다/게(ː)속뛔다/게(ː)속뙤다", "ph")
    def test_gyesokdoeda_rr(self):
            self.run_test("계속되다", "{{ko-IPA|l=y}}", "gyesokdoeda", "rr")
    def test_gyesokdoeda_rrr(self):
            self.run_test("계속되다", "{{ko-IPA|l=y}}", "gyesogdoeda", "rrr")
    def test_gyesokdoeda_mc(self):
            self.run_test("계속되다", "{{ko-IPA|l=y}}", "kyesoktoeda", "mr")
    def test_gyesokdoeda_yr(self):
            self.run_test("계속되다", "{{ko-IPA|l=y}}", "kyēysoktoyta", "yr")
    def test_gyesokdoeda_ipa(self):
            self.run_test("계속되다", "{{ko-IPA|l=y}}", "[ˈkje̞(ː)sʰo̞k̚t͈we̞da̠] ~ [ˈkje̞(ː)sʰo̞k̚t͈ø̞da̠] ~ [ˈke̞(ː)sʰo̞k̚t͈we̞da̠] ~ [ˈke̞(ː)sʰo̞k̚t͈ø̞da̠]", "ipa")

    def test_se_myeong_ph(self):
            self.run_test("세 명", "{{ko-IPA|l=y}}", "세(ː)(ː)(ː)", "ph")
    def test_se_myeong_rr(self):
            self.run_test("세 명", "{{ko-IPA|l=y}}", "se myeong", "rr")
    def test_se_myeong_rrr(self):
            self.run_test("세 명", "{{ko-IPA|l=y}}", "se myeong", "rrr")
    def test_se_myeong_mc(self):
            self.run_test("세 명", "{{ko-IPA|l=y}}", "se myŏng", "mr")
    def test_se_myeong_yr(self):
            self.run_test("세 명", "{{ko-IPA|l=y}}", "sēy myeng", "yr")
    def test_se_myeong_ipa(self):
            self.run_test("세 명", "{{ko-IPA|l=y}}", "[ˈsʰe̞(ː) mjʌ̹ŋ]", "ipa")

    def run_test(self, hangul, param_string, expected, system_name):
        wr = WiktionaryRomanization(hangul, param_string)
        value = wr.romanize_one(system_name)
        self.assertEqual(value, expected)