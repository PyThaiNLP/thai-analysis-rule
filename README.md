# Thai Analysis Rule

This is an implementation of the paper:

Sornlertlamvanich, V. and Phantachat, W., 1995. "Thai Analysis Rules, Technical Report, Machine Translation System Laboratory", Center of the International Cooperation for Computerization, Japan.

## Install

```
pip install https://github.com/PyThaiNLP/thai-analysis-rule/archive/master.zip
```

## Docs

### Generate Sentences

```python
from thaianalysisrule import generate_sent
print(generate_sent(n=1)) # Generate 1 Sentence
```

### Parser

#### From list word

```python
from thaianalysisrule import parser
print(parser(["ผม","เดิน"]))
```

#### From string

```python
from thaianalysisrule import word_seg_parser
print(word_seg_parser("ผมเดิน"))
```

## License

```
   Copyright 2020 Wannaphong Phatthiyaphaibun

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```