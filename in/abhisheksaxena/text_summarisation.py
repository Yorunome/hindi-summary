from cltk.stop.classical_hindi.stops import STOPS_LIST
from cltk.corpus.utils.importer import CorpusImporter
from cltk.tokenize.sentence import TokenizeSentence
from cltk.tokenize.word import WordTokenizer


class TextSummarization:
    sentence = ""
    hindi_stop_words = set(STOPS_LIST)
    sentence_tokenizer = TokenizeSentence('hindi')

    def __init__(self, hindi_text_input):
        self.sentence = hindi_text_input

    def word_tokenize(self):
        word_tokenizer = WordTokenizer('sanskrit')
        return word_tokenizer.tokenize(self.sentence)
        # print(hindi_text_words

    def sentence_tokenizer(self):
        hindi_text_sentence_tokenize = TokenizeSentence('hindi').tokenize(self.sentence)
        # print(hindi_text_sentence_tokenize)
        print("\nHindi sentence tokenize")
        for i in hindi_text_sentence_tokenize:
            print(i)

    def get_stop_words(self):
        return self.hindi_stop_words

    def print_stop_words(self):
        print("Stop words:", self.get_stop_words()[:10])

    def get_filtered_sentence(self):
        filtered_sentence = []
        for w in self.word_tokenize():
            if w not in self.get_stop_words():
                filtered_sentence = filtered_sentence + w.split()

        print("filtered sentence:", filtered_sentence)


hindi_text = [
    "भारत प्रशासित कश्मीर के शोपियां में हुए एक संदिग्ध चरमपंथी हमले में दो ट्रक ड्राइवरों की मौत "
    "हो गई है | श्रीनगर में मौजूद बीबीसी संवाददाता रियाज़ मसरूर के मुताबिक़ ये ट्रक ड्राइवर सेब "
    "लादने आए थे. ीते दो सप्ताह में ये इस तरह का तीसरा हमला  है| अभी तक किसी चरमपंथी समूह ने इस "
    "हमले की ज़िम्मेदारी नहीं ली है| पुलिस के  मुताबिक़ राजस्थान, पंजाब और हरियाणा से आए तीन "
    "ट्रकों पर शोपियां ज़िले के चित्रा  गांव में सेब लादे जा रहे थे. इस दौरान संदिग्ध चरमपंथियों "
    "ने गोलीबारी की| "
    , "बीजपी-शिवसेना गठबंधन को बहुमत मिलने के बावजूद महाराष्ट्र में नई सरकार शपथ नहीं ले पा रही "
      "है| 24 अक्टूबर को आए नतीजों के बाद प्रधानमंत्री नरेंद्र मोदी ने ऐलान किया था कि देवेंद्र "
      "फडणवीस की अगुवाई में महाराष्ट्र विकास करेगा| हालांकि इन सबके बीच बीजेपी और शिवसेना में "
      "50-50 फॉर्मूले को लेकर खींचतान जारी है और सरकार गठन पर पेच फंसा है| "
    , "इस बीच शिवसेना प्रमुख उद्धव ठाकरे का बड़ा बयान सामने आया है| शिवसेना की मीटिंग में उद्धव "
      "ठाकरे ने कहा कि हमारी संख्या बल अच्छी है और सीएम पद पर हमारा हक है और हमारी ज़िद्द भी. "
      "उन्होंने कहा कि सीएम का पद हमेशा एक के लिए कायम नहीं रहता| बालासाहेब ठाकरे ने जिसे जो वचन "
      "दिया उसने उसका पालन किया| हम सत्ता के भूखे नहीं हैं, लेकिन बीजेपी से जो बात हुई उसका पालन "
      "होना चाहिए| "
]

print("Choose a hindi sample text or enter it manually. Options: 1, 2 or 3")
print("Enter choice: ")
choice = input()

sentence = ""
if choice == "1" or choice == "2" or choice == "3":
    sentence = hindi_text[int(choice) - 1]
else:
    sentence = choice

textSummarization = TextSummarization(sentence)
textSummarization.sentence_tokenizer()
textSummarization.get_filtered_sentence()