import nltk
import sumy

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.kl import KLSummarizer

# nltk.download('punkt') --> WHY IS THIS STALLING MY SERVER WTF --> ONE TIME USE ONLY
# WARNING: This is needed so open a py shell in the venv and type this line

#Load the models
def sumy_lex_summarize(input_text: str) -> str:
    lex_rank_summarizer = LexRankSummarizer()
    summ_text = ""
    parser = PlaintextParser.from_string(input_text, Tokenizer('english'))
    lexrank_summary = lex_rank_summarizer(parser.document, sentences_count=3)
    for sentence in lexrank_summary:
        summ_text += str(sentence)

    return summ_text
    
def sumy_luhn_summarize(input_text: str) -> str:
    luhn_summarizer = LuhnSummarizer()
    summ_text = ""
    parser = PlaintextParser.from_string(input_text, Tokenizer('english'))
    luhn_summary = luhn_summarizer(parser.document, sentences_count=3)

    for sentence in luhn_summary:
        summ_text += str(sentence)
    return summ_text

def sumy_kl_summarize(input_text: str) -> str:
    summ_text = ""
    kl_summarizer = KLSummarizer()
    parser = PlaintextParser.from_string(input_text, Tokenizer('english'))
    kl_summary = kl_summarizer(parser.document, sentences_count=3)

    for sentence in kl_summary:
        summ_text += str(sentence)

    return summ_text

def sumy_lsa_summarize(input_text: str) -> str:
    lsa_summarizer = LsaSummarizer()
    summ_text = ""
    parser = PlaintextParser.from_string(input_text, Tokenizer('english'))
    lsa_summary = lsa_summarizer(parser.document, sentences_count=3)

    for sentence in lsa_summary:
        summ_text += str(sentence)

    return summ_text