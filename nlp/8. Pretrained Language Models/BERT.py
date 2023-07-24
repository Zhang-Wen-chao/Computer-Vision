import torch
import torch.nn as nn
from transformers import BertModel, BertTokenizer

# Load pre-trained BERT model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
bert = BertModel.from_pretrained(model_name)

# Tokenize inputs and convert them to tensors
input_sentences = ["This is sentence 1.", "This is sentence 2."]
encoded_inputs = tokenizer(input_sentences, padding=True, truncation=True, return_tensors="pt")
input_ids = encoded_inputs['input_ids']
attention_mask = encoded_inputs['attention_mask']

# Define your own PyTorch model
class BertClassifier(nn.Module):
    def __init__(self, bert):
        super(BertClassifier, self).__init__()
        self.bert = bert
        self.fc = nn.Linear(768, num_classes)  # Adjust input size if needed
        
    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids, attention_mask=attention_mask)['last_hidden_state']
        cls_embedding = outputs[:, 0, :]  # Extract the CLS token embedding
        outputs = self.fc(cls_embedding)
        return outputs

# Example usage
num_classes = 2  # Number of classes for binary classification

model = BertClassifier(bert).cuda()
outputs = model(input_ids.cuda(), attention_mask.cuda())
print(outputs)