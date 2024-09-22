from transformers import T5Tokenizer, T5ForConditionalGeneration
from .view_load_lora_params import load_lora_params 

## Loading required model and tokenizer
var_model = T5ForConditionalGeneration.from_pretrained('t5-base')
tokenizer = T5Tokenizer.from_pretrained('t5-base',clean_up_tokenization_spaces=True,legacy=False)
if tokenizer.pad_token is None:
  tokenizer.add_special_tokens({'pad_token': '[PAD]'})
  var_model.resize_token_embeddings(len(tokenizer))

import os
current_dir=os.path.realpath(os.path.dirname(__file__))
checkpoint_path =os.path.join(current_dir,'checkpoint_epoch_25.pt')
load_lora_params(var_model, checkpoint_path,"context")

import os
json_path =os.path.join(current_dir,'final_model')
loaded_model = T5ForConditionalGeneration.from_pretrained(json_path)

def generate_response(prompt,test_model=loaded_model,max_length=128, num_return_sequences=1):
    test_model.eval()
    # Tokenize the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Generate response
    output =test_model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        no_repeat_ngram_size=2,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=1.0
    )

    print(tokenizer.decode(output[0], skip_special_tokens=True))
    # Decode and return the generated response
    return tokenizer.decode(output[0], skip_special_tokens=True)

