import torch
from transformers import T5ForConditionalGeneration
from peft import LoraConfig, get_peft_model

def load_lora_params(var_model, checkpoint_path,task="context"):

    if task=="context":

      # Define LoRA configuration
      lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        lora_dropout=0.1,
        target_modules=['q','v','k'],
        )
        # Apply LoRA to the T5 model
      var_model = get_peft_model(var_model, lora_config)

      # Load LoRA parameters from checkpoint
      device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
      lora_params = torch.load(checkpoint_path, map_location=device,weights_only=True)
      lora_params=lora_params['lora_params']
      # Update model parameters with the LoRA parameters
      model_state_dict = var_model.state_dict()

      for name, param in lora_params.items():
          if name in model_state_dict:
              # print("Done ")
              model_state_dict[name].copy_(param)
          else:
              print(f"Warning: {name} not found in the model's state dict")

      # Load updated state dict back into the model
      var_model.load_state_dict(model_state_dict)
    #   print(f"LoRA parameters loaded from {checkpoint_path}")

    else:
      lora_config = LoraConfig(
          r=4,
          lora_alpha=16,
          lora_dropout=0.1,
          target_modules=[
              'decoder.block.11.layer.0.SelfAttention.q',
              'decoder.block.11.layer.0.SelfAttention.k',
              'decoder.block.11.layer.0.SelfAttention.v',
              'decoder.block.11.layer.0.SelfAttention.o.base_layer',
              'decoder.block.11.layer.0.SelfAttention.o.lora_A.default',
              'decoder.block.11.layer.0.SelfAttention.o.lora_B.default',
              'decoder.block.11.layer.1.EncDecAttention.q',
              'decoder.block.11.layer.1.EncDecAttention.k',
              'decoder.block.11.layer.1.EncDecAttention.v',
              'decoder.block.11.layer.1.EncDecAttention.o',
              'decoder.block.11.layer.2.DenseReluDense.wi',
              'decoder.block.11.layer.2.DenseReluDense.wo',
          ]
      )
        # Apply LoRA to the T5 model
      var_model = get_peft_model(var_model, lora_config)

      # Load LoRA parameters from checkpoint
      device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
      lora_params = torch.load(checkpoint_path, map_location=device)

      # Update model parameters with the LoRA parameters
      model_state_dict = var_model.state_dict()

      for name, param in lora_params['lora_params'].items():
          if name in model_state_dict:
              # print("Done ")
              model_state_dict[name].copy_(param)
          else:
              print(f"Warning: {name} not found in the model's state dict")

      # Load updated state dict back into the model
      var_model.load_state_dict(model_state_dict)
      
