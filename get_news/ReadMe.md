# Ứng dụng get news
Kịch bản như sau: người dùng yêu cầu chatbot cung cấp tin tức mới nhất theo từ khoá

- latest news in sports
- update me virus corona
- latest updates covid


Mục tiêu làm sao bóc tách được keyword trong đoạn hội thoại của người dùng.
Một số Entity Extractor Components được thử nghiệm cho thấy công dụng của từng loại như sau:

## Bóc tách từ khoá được định nghĩa trong nlu hoặc lookup table
- DIETClassifier: phù hợp khi từ khoá được đánh dấu là entity ngay trong nlu.md. Tuy nhiên DIETClassifier lại không thể bóc tác từ khoá được liệt kê trong Lookup Table [data/test/lookup_tables/topic_news.txt](data/test/lookup_tables/topic_news.txt)
  
```markdown
- what happend [covid](topic_news)
- news about [boris johnson](topic_news)
- Get me latest updates in [science](topic_news)
```

```json
latest news science
{
  "intent": {
    "name": "getNews",
    "confidence": 0.9999455213546753
  },
  "entities": [
    {
      "entity": "topic_news",
      "start": 12,
      "end": 19,
      "extractor": "DIETClassifier",
      "value": "science"
    }
  ],
```

- CRFEntityExtractor: bóc tách từ khoá trong nlu.md và cả Lookup table rất tốt

```markdown
  - name: WhitespaceTokenizer
  - name: RegexFeaturizer
  - name: LexicalSyntacticFeaturizer
  - name: CountVectorsFeaturizer
  - name: CountVectorsFeaturizer
  - name: CRFEntityExtractor
  - name: CountVectorsFeaturizer
  - name: CountVectorsFeaturizer
    analyzer: "char_wb"
    min_ngram: 1
    max_ngram: 4
  - name: DIETClassifier
    epochs: 100
  - name: EntitySynonymMapper
  - name: ResponseSelector
    epochs: 100
```

Ở đây từ khoá Hanoi được liệt kê trong lookup table [data/test/lookup_tables/topic_news.txt](data/test/lookup_tables/topic_news.txt)
```json
news in Hanoi
{
  "intent": {
    "name": "getNews",
    "confidence": 0.994597315788269
  },
  "entities": [
    {
      "start": 8,
      "end": 13,
      "value": "hanoi",
      "entity": "topic_news",
      "confidence": 0.9572906960782419,
      "extractor": "CRFEntityExtractor"
    }
  ],
```
## Bóc tách từ không có trong nlu.md hay lookup table
- SpacyEntityExtractor: để bóc tác các từ khoá không được liệt kê trong nlu.md hay Lookup table, nếu nhận dạng nó sẽ cho vào Entity 
```markdown
language: en
pipeline:
  - name: SpacyNLP
  - name: SpacyTokenizer
  - name: RegexFeaturizer
  - name: LexicalSyntacticFeaturizer
  - name: CountVectorsFeaturizer
  - name: CountVectorsFeaturizer
  - name: SpacyEntityExtractor
  - name: CRFEntityExtractor
  - name: CountVectorsFeaturizer
  - name: CountVectorsFeaturizer
    analyzer: "char_wb"
    min_ngram: 1
    max_ngram: 4
  - name: DIETClassifier
    epochs: 100
  - name: EntitySynonymMapper
  - name: ResponseSelector
    epochs: 100
```

Bóc tách được Donald Trump là tên người
```json
Latest news Donald Trump
{
  "intent": {
    "name": "getNews",
    "confidence": 0.9897345900535583
  },
  "entities": [
    {
      "entity": "PERSON",
      "value": "Donald Trump",
      "start": 12,
      "confidence": null,
      "end": 24,
      "extractor": "SpacyEntityExtractor"
    }
  ],
```

hoặc Tesla là tổ chức
```json
latest news Tesla
{
  "intent": {
    "name": "getNews",
    "confidence": 0.9991458654403687
  },
  "entities": [
    {
      "entity": "ORG",
      "value": "Tesla",
      "start": 12,
      "confidence": null,
      "end": 17,
      "extractor": "SpacyEntityExtractor"
    }
  ],
```
địa điểm
```json
latest news in Tokyo
{
  "intent": {
    "name": "getNews",
    "confidence": 0.9989216327667236
  },
  "entities": [
    {
      "entity": "GPE",
      "value": "Tokyo",
      "start": 15,
      "confidence": null,
      "end": 20,
      "extractor": "SpacyEntityExtractor"
    }
```