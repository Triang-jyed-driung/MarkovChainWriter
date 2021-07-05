# MarkovChainWriter
Creating rubbish using Markov chain.  
生活中，经常遇到要写各种文字（那啥），比如1000字检讨等。不想写、想摸鱼怎么办？试试这个基于Markov链的废话生成器。  
本生成器采用Python，仅不到1KB大小，却有亿亿种可能。  
本生成器还可用于搅和各种代码、论文等文(la)章(ji)。  

# Requirements
- A relatively modern computer
- Python 3.6+
- pip install jieba

# Usage
- 模板放入in.txt（建议100KB，太小了会词穷，太大了跑不动。示例为《三国演义》。）
- 代码中articlelength=...（改成你需要的长度）
- py ./markov.py
- 打开out.txt，稍加润色，大功告成！

# Warnings
查重不过关、词句不通顺等问题后果请自负。
