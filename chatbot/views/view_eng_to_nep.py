# from transformers import MT5ForConditionalGeneration, T5Tokenizer


# # Load the tokenizer and model
# model = MT5ForConditionalGeneration.from_pretrained("d2niraj555/mt5-eng2nep")
# tokenizer = T5Tokenizer.from_pretrained("d2niraj555/mt5-eng2nep")

# def convert(english_text):
#     # Example English text
#     english_text = "There are several popular trekking routes near Kathmandu, including the Langtang Valley Trek, Gosainkunda Trek and Helambu Trek."

#     # Tokenize the input
#     inputs = tokenizer.encode(english_text, return_tensors="pt")

#     # Generate translation
#     outputs = model.generate(inputs,max_length=200)

#     # Decode the translated text
#     translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return translated_text