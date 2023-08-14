import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

# 检查计算机是否支持 GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')



# 加载GPT-2模型和分词器
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')


# 加载数据集
train_dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="data/data.txt",
    block_size=128
)


# 将模型移动到 GPU 上
model.cuda()

# 将数据移动到 GPU 上
train_dataset.cuda()


# 定义数据收集器
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False
)

# 定义训练参数
training_args = TrainingArguments(
    output_dir='./results',          # 训练结果输出目录
    overwrite_output_dir=True,
    num_train_epochs=5,              # 训练轮数
    per_device_train_batch_size=16,  # 批次大小
    save_steps=5000,
    save_total_limit=2,
    save_strategy='steps'
)

# 创建Trainer对象并开始训练
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    data_collator=data_collator,
    # device=device #启用gpu
)

trainer.train()