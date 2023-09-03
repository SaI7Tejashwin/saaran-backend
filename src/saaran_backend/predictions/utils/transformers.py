from transformers import (
    T5Tokenizer,
    T5Config,
    T5ForConditionalGeneration
)

from transformers import (
    BartForConditionalGeneration,
    BartTokenizer,
    BartConfig
)

def summarize_t5(input_text: str) -> str:
    model = T5ForConditionalGeneration.from_pretrained('t5-small')
    tokenizer = T5Tokenizer.from_pretrained('t5-small')

    text = "summarize:" + input_text
    #encoding the input text
    input_ids = tokenizer.encode(text, return_tensors='pt', max_length=512)

    #generate summary ids
    summary_ids = model.generate(input_ids)
    t5_summary: str = tokenizer.decode(summary_ids[0])

    return t5_summary

def summarize_bart(input_text: str) -> str:
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

    inputs = tokenizer.batch_encode_plus([input_text], return_tensors='pt')
    summary_ids = model.generate(inputs['input_ids'], early_stopping = True)

    #Decoding and returning the sumamary
    bart_summary = tokenizer.decode(summary_ids[0], skip_special_tokens = True)
    
    return bart_summary
