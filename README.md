# 宜家爬虫

抓去了宜家所有商品信息，并生成商品列表等信息。

## 安装

``` sh
pip install scrapy
```

## 爬数据

``` sh
scrapy crawl ikea -o result.csv
```

## 输出示例

| category | name | broad | price | feature | discount | link | new |
| ------- | ----- | ----- | ----- | ------ | ------- | ----- | ----- |
| 内配件 | 中高抽屉分隔件 | MAXIMERA 马斯麦 | ¥ 49.00 |  | False | http://www.ikea.com/cn/zh/catalog/categories/departments/ikea_kitchens/24255/ | False| 
| 床上用品 | 被套和枕套 | 法耶恩斯特 | ¥ 149.00 |  | False | http://www.ikea.com/cn/zh/catalog/products/00337479/ | True |
| 挂钩和衣架 | 自粘挂钩 | 普鲁特 | ¥ 6.90 | 室内/户外 | True | http://www.ikea.com/cn/zh/catalog/products/10291471/ | False |


## 解析结果，生成词条

``` sh
python analysis.py
```
