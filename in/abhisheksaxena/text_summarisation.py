from cltk.stop.classical_hindi.stops import STOPS_LIST
from cltk.corpus.utils.importer import CorpusImporter
from cltk.tokenize.sentence import TokenizeSentence
from cltk.tokenize.word import WordTokenizer

import tkinter as tk
from tkinter.ttk import *
import tkinter.messagebox


def clearTextBox(textBox):
    textBox.delete(1.0, tk.END)


class TextSummarization:
    sentence = ""
    hindi_stop_words = set(STOPS_LIST)

    def __init__(self, hindi_text_input=""):
        self.sentence = hindi_text_input

    def word_tokenize(self):
        print("Word Tokenizer triggered")
        word_tokenizer = WordTokenizer('sanskrit')
        # print("word tokenize: ", word_tokenizer.tokenize(self.sentence))
        return word_tokenizer.tokenize(self.sentence)

    def wordTokenizerWithWordsAsString(self):
        words = self.word_tokenize()
        temp = "["
        for w in words:
            if w != "|":
                if len(temp) > 0 and temp != "[":
                    temp += ", "
                temp += w
        temp += "]"
        return temp

    def sentence_tokenizer(self):
        print("Sentence Tokenizer triggered")
        hindi_text_sentence_tokenize = TokenizeSentence('hindi').tokenize(self.sentence)
        # print(hindi_text_sentence_tokenize)
        temp_sentence = ""
        # print("\nHindi sentence tokenize")
        for i in hindi_text_sentence_tokenize:
            # print(i)
            if len(temp_sentence) > 0:
                temp_sentence = temp_sentence + "\n"

            temp_sentence = temp_sentence + i
        # print(temp_sentence)
        return temp_sentence.strip()

    def get_stop_words(self):
        return self.hindi_stop_words

    def print_stop_words(self):
        print("Stop words:", self.get_stop_words()[:10])

    def get_filtered_sentence(self):
        print("Removing Stop words.....")
        temp = ""
        filtered_sentence = []
        for w in self.word_tokenize():
            if w not in self.get_stop_words():
                filtered_sentence = filtered_sentence + w.split()

        # print("filtered sentence:", filtered_sentence)

        for w in filtered_sentence:
            temp = temp + " " + w
        self.sentence = temp
        print("Stop words removed...")
        # print("from get filtered sentence: " + self.sentence)

    hindi_text = [
        "भारत प्रशासित कश्मीर के शोपियां में हुए एक संदिग्ध चरमपंथी हमले में दो ट्रक ड्राइवरों की "
        "मौत हो गई है | श्रीनगर में मौजूद बीबीसी संवाददाता रियाज़ मसरूर के मुताबिक़ ये ट्रक "
        "ड्राइवर सेब लादने आए थे. ीते दो सप्ताह में ये इस तरह का तीसरा हमला  है| अभी तक किसी "
        "चरमपंथी समूह ने इस हमले की ज़िम्मेदारी नहीं ली है| पुलिस के  मुताबिक़ राजस्थान, "
        "पंजाब और हरियाणा से आए तीन ्रकों पर शोपियां ज़िले के चित्रा  गांव में सेब लादे जा रहे "
        "थे. इस दौरान संदिग्ध चरमपंथियों ने गोलीबारी की| "
        ,
        "बीजपी-शिवसेना गठबंधन को बहुमत मिलने के बावजूद महाराष्ट्र में नई सरकार शपथ नहीं ले पा रही "
        "है| 24 अक्टूबर को आए नतीजों के बाद प्रधानमंत्री नरेंद्र मोदी ने ऐलान किया था कि देवेंद्र "
        "फडणवीस की अगुवाई में महाराष्ट्र विकास करेगा| हालांकि इन सबके बीच बीजेपी और शिवसेना में "
        "50-50 फॉर्मूले को लेकर खींचतान जारी है और सरकार गठन पर पेच फंसा है| "
        ,
        "इस बीच शिवसेना प्रमुख उद्धव ठाकरे का बड़ा बयान सामने आया है| शिवसेना की मीटिंग में उद्धव "
        "ठाकरे ने कहा कि हमारी संख्या बल अच्छी है और सीएम पद पर हमारा हक है और हमारी ज़िद्द भी. "
        "उन्होंने कहा कि सीएम का पद हमेशा एक के लिए कायम नहीं रहता| बालासाहेब ठाकरे ने जिसे जो वचन "
        "दिया उसने उसका पालन किया| हम सत्ता के भूखे नहीं हैं, लेकिन बीजेपी से जो बात हुई उसका पालन "
        "होना चाहिए| "
    ]


# print("Choose a hindi sample text or enter it manually. Options: 1, 2 or 3")
# print("Enter choice: ")
# choice = input()

# sentence = ""
# if choice == "1" or choice == "2" or choice == "3":
#    sentence = hindi_text[int(choice) - 1]
# else:
#    sentence = choice

# textSummarization = TextSummarization(sentence)
# textSummarization.sentence_tokenizer()
# textSummarization.get_filtered_sentence()


class UI:
    textSampleOne = "This is text sample one!!!!"
    textSummarization = TextSummarization()

    def __init__(self):
        titleLabel = tk.Label(text="Hindi Text Summarization")
        titleLabel.grid(row=0, column=2, columnspan=50, pady=(10, 20))

        rootFrame = tk.Frame(root)
        rootFrame.grid(row=1, column=0, padx=(30, 10), columnspan=100)

        inputLabel = tk.Label(rootFrame, text="Input")
        inputLabel.grid(row=0, column=0, sticky=tk.W)

        self.hindiInputBox = tk.Text(rootFrame, height=10)
        self.hindiInputBox.grid(row=1, column=0, pady=10, columnspan=100, sticky=tk.W, padx=(0, 10))

        buttonFrame = Frame(rootFrame)
        buttonFrame.grid(row=2, column=0, pady=(0, 20))

        sampleButton_1 = tk.Button(buttonFrame, text="Sample 1", command=lambda: self.setSample(0))
        sampleButton_2 = tk.Button(buttonFrame, text="Sample 2", command=lambda: self.setSample(1))
        sampleButton_3 = tk.Button(buttonFrame, text="Sample 3", command=lambda: self.setSample(2))
        processButton = tk.Button(buttonFrame, text="Process", command=lambda: self.processData())
        sampleButton_1.grid(row=0, column=2)
        sampleButton_2.grid(row=0, column=3, padx=20)
        sampleButton_3.grid(row=0, column=4)
        processButton.grid(row=1, column=3, pady=20)

        stopWordRemovalFrame = tk.Frame(rootFrame)
        stopWordRemovalFrame.grid(row=3, column=0, pady=(0, 20))

        wordTokenizerLabel = tk.Label(stopWordRemovalFrame, text="Stop Words Removed")
        wordTokenizerLabel.grid(row=0, column=0)

        self.stopWordRemovalText = tk.Text(stopWordRemovalFrame, height=10, bg="#F0F0F0")
        self.stopWordRemovalText.grid(row=1, column=0, columnspan=100, sticky=tk.W, padx=(0, 10))

        wordTokenizerFrame = tk.Frame(rootFrame)
        wordTokenizerFrame.grid(row=4, column=0, pady=(0, 20))

        wordTokenizerLabel = tk.Label(wordTokenizerFrame, text="Word Tokenizer")
        wordTokenizerLabel.grid(row=0, column=0)

        self.wordTokenizerText = tk.Text(wordTokenizerFrame, height=10, bg="#F0F0F0")
        self.wordTokenizerText.grid(row=1, column=0, columnspan=100, sticky=tk.W, padx=(0, 10))

        sentenceTokenizerFrame = tk.Frame(rootFrame)
        sentenceTokenizerFrame.grid(row=5, column=0, pady=(0, 20))

        sentenceTokenizerLabel = Label(sentenceTokenizerFrame, text="Sentence Tokenizer")
        sentenceTokenizerLabel.grid(row=0, column=0)

        self.sentenceTokenizerText = tk.Text(sentenceTokenizerFrame, height=10, bg="#F0F0F0")
        self.sentenceTokenizerText.grid(row=1, column=0, columnspan=100, sticky=tk.W, padx=(0, 10))

    def setSample(self, value):
        # self.hindiInputBox.delete(1.0, tk.END)
        self.clearAllTextBoxes()
        self.hindiInputBox.insert(tk.INSERT, self.textSummarization.hindi_text[value], "")

    def processData(self):
        inputData = self.hindiInputBox.get("1.0", "end-1c")
        print("Sentence: " + inputData)
        if not inputData:
            tkinter.messagebox.showinfo("Empty Input", "Please enter input that is to be "
                                                       "processed in the text box.")
        else:
            self.textSummarization.sentence = inputData
            self.textSummarization.get_filtered_sentence()
            self.stopWordRemovalText.insert(tk.INSERT, self.textSummarization.sentence.strip(),
                                            "Failed to process Data")
            self.wordTokenizerText.insert(tk.INSERT,
                                          self.textSummarization.wordTokenizerWithWordsAsString()
                                          .strip(),
                                          "Failed to process Data")
            self.sentenceTokenizerText.insert(tk.INSERT, self.textSummarization.sentence_tokenizer()
                                              .strip()
                                              , 'Failed to process Data')

    def clearAllTextBoxes(self):
        clearTextBox(self.hindiInputBox)
        clearTextBox(self.stopWordRemovalText)
        clearTextBox(self.wordTokenizerText)
        clearTextBox(self.sentenceTokenizerText)


root = tk.Tk()

uiClass = UI()
root.mainloop()
