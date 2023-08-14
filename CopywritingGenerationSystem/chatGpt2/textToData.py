from transformers import GPT2Tokenizer, TextDataset, LineByLineTextDataset

# 加载分词器
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# 加载文本数据
with open('path/to/data.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 将文本转换为训练数据集
encoded_text = tokenizer.encode(text)
dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path=None,
    block_size=128,
    overwrite_cache=False,
    encoding="utf-8",
    text_lines=encoded_text,
)

# 打印训练数据集的样本数
print(len(dataset))