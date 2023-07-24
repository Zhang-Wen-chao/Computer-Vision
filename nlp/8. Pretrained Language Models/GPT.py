import torch
import torch.nn as nn
from transformers import GPT2Model, GPT2Tokenizer

# Load pre-trained GPT model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
gpt = GPT2Model.from_pretrained(model_name)

# Tokenize input and convert it to tensors
input_sentence = "This is an example sentence."
input_ids = tokenizer.encode(input_sentence, return_tensors="pt")

# Define your own PyTorch model
class GPTClassifier(nn.Module):
    def __init__(self, gpt):
        super(GPTClassifier, self).__init__()
        self.gpt = gpt
        self.fc = nn.Linear(768, vocab_size)  # Adjust input size if needed
        
    def forward(self, input_ids):
        outputs = self.gpt(input_ids)['last_hidden_state']
        outputs = self.fc(outputs)
        return outputs

# Example usage
vocab_size = gpt.config.vocab_size  # Get the size of the GPT vocabulary

model = GPTClassifier(gpt)
outputs = model(input_ids)
print(outputs)