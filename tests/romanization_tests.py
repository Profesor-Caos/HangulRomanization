import unittest
from src.wiktionary_romanization import WiktionaryRomanization

# import pkgutil
# search_path = ['..'] # set to None to see all modules importable from sys.path
# all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
# print(all_modules)


class TestWikiRomanizations(unittest.TestCase):
    error_count = 0

    def wiki_test_cases(self):
        self.run_test('법률학', '{{ko-IPA}}', '범뉼학', 'beomnyulhak', 'beoblyulhag', 'pŏmnyurhak', 'peplyul.hak', '[pʌ̹mɲuɾɦa̠k̚]')
        self.run_test('편찮다', '{{ko-IPA}}', '편찬타', 'pyeonchanta', 'pyeonchanhda', "p'yŏnch'ant'a", 'phyen.chanhta', '[pʰjʌ̹ɲt͡ɕʰa̠ntʰa̠]')
        self.run_test('음식값', '{{ko-IPA|l=y}}', '음(ː)식깝', 'eumsikgap', 'eumsiggabs', 'ŭmsikkap', 'ūmsik.kaps', '[ˈɯ(ː)mɕʰik̚k͈a̠p̚]')
        self.run_test('어떻게', '{{ko-IPA}}', '어떠케', 'eotteoke', "eo'tteohge", "ŏttŏk'e", 'e.ttehkey', '[ʌ̹t͈ʌ̹kʰe̞]')
        self.run_test('몇몇', '{{ko-IPA}}', '면멷', 'myeonmyeot', 'myeochmyeoch', 'myŏnmyŏt', 'myechmyech', '[mjʌ̹nmjʌ̹t̚]')
        self.run_test('뜻밖에', '{{ko-IPA}}', '뜯빠께', 'tteutbakke', "tteusbakk'e", 'ttŭtpakke', 'ttuspakk.ey', '[t͈ɯt̚p͈a̠k͈e̞]')
        self.run_test('끊임없다', '{{ko-IPA}}', '끄니멉따', 'kkeunimeopda', "kkeunh'im'eobsda", 'kkŭnimŏpta', 'kkunh.im.epsta', '[k͈ɯnimʌ̹p̚t͈a̠]')
        self.run_test('낯설다', '{{ko-IPA}}', '낟썰다', 'natseolda', 'nachseolda', 'nassŏlda', 'nachselta', '[na̠ss͈ʌ̹ɭda̠]')
        self.run_test('공산주의', '{{ko-IPA|l=y|ui=4}}', '공(ː)산주의/공(ː)산주이', 'gongsanjuui', 'gongsanjuui', 'kongsanjuŭi', 'kōngsan.cwuuy', '[ˈko̞(ː)ŋsʰa̠ɲd͡ʑuɰi] ~ [ˈko̞(ː)ŋsʰa̠ɲd͡ʑui]')
        self.run_test('고춧가루', '{{ko-IPA|nobc=2}}', '고춛까루/고추까루', 'gochutgaru', 'gochusgalu', "koch'utkaru", 'ko.chwuskalwu', '[ko̞t͡ɕʰut̚k͈a̠ɾu] ~ [ko̞t͡ɕʰuk͈a̠ɾu]')
        self.run_test('합법화되다', '{{ko-IPA}}', '합뻐퐈뒈다/합뻐퐈되다', 'hapbeophwadoeda', 'habbeobhwadoeda', 'happŏphwadoeda', 'hap.pep.hwatoyta', '[ha̠p̚p͈ʌ̹pʰwa̠dwe̞da̠] ~ [ha̠p̚p͈ʌ̹pʰwa̠dø̞da̠]')
        self.run_test('몫몫이', '{{ko-IPA}}', '몽목씨', 'mongmoksi', "mogsmogs'i", 'mongmoksi', 'moksmoks.i', '[mo̞ŋmo̞kɕ͈i]')
        self.run_test('굵다랗다', '{{ko-IPA|l=y}}', '국(ː)따라타', 'gukdarata', 'gulgdalahda', "kuktarat'a", 'kwūlktalahta', '[ˈku(ː)k̚t͈a̠ɾa̠tʰa̠]')
        self.run_test('새해 복 많이 받으세요', '{{ko-IPA|새해 복많이 받으세요|새해 복 많이 받으세요}}', '새해 봉마니 바드세요/세헤 봉마니 바드세요/새해 복 마니 바드세요/세헤 복 마니 바드세요', 'saehae bongmani badeuseyo/saehae bok mani badeuseyo', "saehae bogmanh'i bad'euseyo/saehae bog manh'i bad'euseyo", 'saehae pongmani padŭseyo/saehae pok mani padŭseyo', 'sayhay pokmanh.i pat.useyyo/sayhay pok manh.i pat.useyyo', '[sʰɛɦɛ po̞ŋma̠ni pa̠dɯsʰe̞jo] ~ [sʰe̞ɦe̞ po̞ŋma̠ni pa̠dɯsʰe̞jo] ~ [sʰɛɦɛ po̞k̚ ma̠ni pa̠dɯsʰe̞jo] ~ [sʰe̞ɦe̞ po̞k̚ ma̠ni pa̠dɯsʰe̞jo]')
        self.run_test('한국', '{{ko-IPA|l=y|cap=y}}', '한(ː)국', "Han'guk", 'Hangug', "Han'guk", 'hānkwuk', '[ˈha̠(ː)nɡuk̚]')
        self.run_test('상사병', '{{ko-IPA|com=2}}', '상사뼝', 'sangsabyeong', 'sangsabyeong', 'sangsapyŏng', 'sangsaqpyeng', '[sʰa̠ŋsʰa̠p͈jʌ̹ŋ]')
        self.run_test('서클', '{{ko-IPA|com=0}}', '써클', 'seokeul', 'seokeul', "ssŏk'ŭl", 'qse.khul', '[s͈ʌ̹kxɯɭ]')
        self.run_test('의견란', '{{ko-IPA|nn=3|l=y}}', '의(ː)견난', 'uigyeonnan', 'uigyeonlan', 'ŭigyŏnnan', 'ūykyenlan', '[ˈɰi(ː)ɡjʌ̹nna̠n]')
        self.run_test('의', '{{ko-IPA|uie=1}}', '의/에', 'ui', 'ui', 'ŭi', 'uy', '[ɰi] ~ [e̞]')
        self.run_test('깻잎', '{{ko-IPA|ni=2}}', '깬닙/껜닙', 'kkaennip', "kkaes'ip", 'kkaennip', 'kkaysniph', '[k͈ɛnnip̚] ~ [k͈e̞nnip̚]')
        self.run_test('값어치', '{{ko-IPA|bcred=1}}', '가버치', 'gabeochi', "gabs'eochi", "kabŏch'i", 'kaps.e.chi', '[ka̠bʌ̹t͡ɕʰi]')
        self.run_test('맞흥정', '{{ko-IPA|bcred=1}}', '마틍정', 'matheungjeong', 'majheungjeong', 'mathŭngjŏng', 'mac.hungceng', '[ma̠tʰɯŋd͡ʑʌ̹ŋ]')
        self.run_test('곧이어', '{{ko-IPA|bcred=1}}', '고디어', 'godieo', "god'ieo", 'kodiŏ', 'kot.ie', '[ko̞diʌ̹]')
        self.run_test('멋있다', '{{ko-IPA|svar=1}}', '머싣따/머딛따', 'meositda', "meos'issda", 'mŏsitta', 'mes.issta', '[mʌ̹ɕʰit̚t͈a̠] ~ [mʌ̹dit̚t͈a̠]')
        self.run_test('뛰어들다', '{{ko-IPA|iot=2}}', '뛰어들다/뛰여들다', 'ttwieodeulda', 'ttwieodeulda', 'ttwiŏdŭlda', 'ttwietulta', '[t͈ɥiʌ̹dɯɭda̠] ~ [t͈ɥijʌ̹dɯɭda̠] ~ [t͈yʌ̹dɯɭda̠] ~ [t͈yjʌ̹dɯɭda̠]')
        self.run_test('계속', '{{ko-IPA|l=y}}', '계(ː)속/게(ː)속', 'gyesok', 'gyesog', 'kyesok', 'kyēysok', '[ˈkje̞(ː)sʰo̞k̚] ~ [ˈke̞(ː)sʰo̞k̚]')
        self.run_test('계속되다', '{{ko-IPA|l=y}}', '계(ː)속뛔다/계(ː)속뙤다/게(ː)속뛔다/게(ː)속뙤다', 'gyesokdoeda', 'gyesogdoeda', 'kyesoktoeda', 'kyēysoktoyta', '[ˈkje̞(ː)sʰo̞k̚t͈we̞da̠] ~ [ˈkje̞(ː)sʰo̞k̚t͈ø̞da̠] ~ [ˈke̞(ː)sʰo̞k̚t͈we̞da̠] ~ [ˈke̞(ː)sʰo̞k̚t͈ø̞da̠]')
        self.run_test('세 명', '{{ko-IPA|l=y}}', '세(ː)(ː)(ː)', 'se myeong', 'se myeong', 'se myŏng', 'sēy myeng', '[ˈsʰe̞(ː) mjʌ̹ŋ]')
        print(f"Error count: {self.error_count}")

    def run_test(self, hangul, param_string, ph, rr, rrr, mc, yr, ipa) :
        wr = WiktionaryRomanization(hangul, param_string)
        values = wr.make()
        expected = [ph, rr, rrr, mc, yr, ipa]
        for value, i in zip(values, range(0, len(values))):
            if (value != expected[i]):
                print(f"For {hangul} expected {WiktionaryRomanization.system_list[i]['abbreviation']} value of {expected[i]} but received {value}")
                self.error_count += 1
