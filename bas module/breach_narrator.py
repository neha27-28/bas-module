from transformers import pipeline

# Use FLAN-T5 (lightweight) or any summarization model
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def narrate_breach(events):
    input_text = "Explain this attack in detail: " + " -> ".join(events)
    result = generator(input_text, max_length=200, do_sample=True)
    return result[0]['generated_text']
