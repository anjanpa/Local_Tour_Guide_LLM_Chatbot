## testing mbart
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
mbart_model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
mbart_tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt",clean_up_tokenization_spaces=True)
if mbart_tokenizer.pad_token is None:
  mbart_tokenizer.add_special_tokens({'pad_token': '[PAD]'})
  mbart_model.resize_token_embeddings(len(mbart_tokenizer))

def translate(response,src_lang,tgt_lang):
    mbart_model.eval()
    mbart_tokenizer.src_lang = src_lang
    input_ids = mbart_tokenizer.encode(response, return_tensors='pt')
    output =mbart_model.generate(
        input_ids,
        forced_bos_token_id=mbart_tokenizer.lang_code_to_id[tgt_lang]
    )
    response=mbart_tokenizer.decode(output[0],skip_special_tokens=True)
    return response 