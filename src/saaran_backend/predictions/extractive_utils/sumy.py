import nltk
import sumy

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

nltk.download('punkt')

lex_rank_summarizer = LexRankSummarizer()

def sumy_lex_summarize(input_text: str) -> str:
    summ_text = ""
    my_parser = PlaintextParser.from_string(input_text, Tokenizer('english'))
    lexrank_summary = lex_rank_summarizer(my_parser.document, sentences_count=3)

    for sentence in lexrank_summary:
        summ_text += str(sentence)

    return summ_text
    