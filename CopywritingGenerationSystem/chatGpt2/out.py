from transformers import pipeline, BertTokenizer, BertForSequenceClassification

# 加载模型和分词器
tokenizer = BertTokenizer.from_pretrained('模型路径')
model = BertForSequenceClassification.from_pretrained('模型路径')

# 设置分类器
classifier = pipeline('text-classification', model=model, tokenizer=tokenizer)

# 对文本进行分类
text = '这家餐厅的食物很好吃。'
result = classifier(text)
print(result)