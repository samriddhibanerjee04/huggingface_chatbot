from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

class ModelLoader:
    def __init__(self, model_name="google/flan-t5-base"):
        print(f"Loading model: {model_name} on CPU")
        self.tokenizer = T5Tokenizer.from_pretrained(model_name, legacy=False)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        self.model.eval()

    def generate(self, prompt, max_length=100):
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            padding=True
        )

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=max_length,
                num_beams=5,      
                early_stopping=True,
                do_sample=False    
            )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
