# 本项目基于知识图谱 + 检索增强生成（RAG）技术，构建电商智能客服全流程数据系统。

# 核心功能

# 多源数据处理

MySQL 商品结构化数据清洗、标准化、质量校验

商品描述、评论等非结构化文本预处理

# NER 实体抽取

基于 BERT 训练商品标签实体抽取模型

精确率、召回率、F1 量化评估

# 知识图谱构建

电商 Schema 设计：分类 → 属性 → SPU → SKU → 品牌 → 标签

MySQL → Neo4j 自动化数据同步

# 检索增强问答

向量检索 + 全文检索 混合检索

大模型自动生成 Cypher 查询

# 服务部署

FastAPI 封装接口

可演示智能客服交互系统


# 技术栈

语言：Python

深度学习：PyTorch、Transformers、Datasets

数据库：MySQL、Neo4j

框架：FastAPI、LangChain

核心能力：NER、知识图谱、向量检索、RAG
