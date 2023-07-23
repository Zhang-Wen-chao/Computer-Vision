import torch
import torch.nn as nn
import torch.optim as optim
from torch.nn.modules.transformer import Transformer, TransformerEncoder, TransformerDecoder

class TransformerWithCrossAttention(nn.Module):
    def __init__(self, input_vocab_size, output_vocab_size, d_model, nhead, num_encoder_layers, num_decoder_layers,
                 dim_feedforward, dropout):
        super(TransformerWithCrossAttention, self).__init__()

        self.encoder = TransformerEncoder(nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout),
                                          num_encoder_layers)
        self.decoder = TransformerDecoder(nn.TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout),
                                          num_decoder_layers)
        self.fc = nn.Linear(d_model, output_vocab_size)

    def forward(self, src, tgt):
        src = src.permute(1, 0)  # shape: (src_len, batch_size)
        tgt = tgt.permute(1, 0)  # shape: (tgt_len, batch_size)

        encoder_outputs = self.encoder(src)
        decoder_outputs = self.decoder(tgt, encoder_outputs)

        outputs = self.fc(decoder_outputs)  # shape: (tgt_len, batch_size, output_vocab_size)
        outputs = outputs.permute(1, 0, 2)  # shape: (batch_size, tgt_len, output_vocab_size)

        return outputs

# Test the model
input_vocab_size = 100  # Input vocabulary size
output_vocab_size = 200  # Output vocabulary size
d_model = 256  # Model dimension
nhead = 8  # Number of attention heads
num_encoder_layers = 4  # Number of encoder layers
num_decoder_layers = 4  # Number of decoder layers
dim_feedforward = 1024  # Feedforward dimension
dropout = 0.1  # Dropout rate

model = TransformerWithCrossAttention(input_vocab_size, output_vocab_size, d_model, nhead, num_encoder_layers,
                                      num_decoder_layers, dim_feedforward, dropout)
print(model)