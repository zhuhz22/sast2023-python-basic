import argparse
import json
import random

def parser_data():
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", help="题库文件", required=True)
    parser.add_argument("-t","--title",help="title",required=False)
    
    args = parser.parse_args()
    return args



def read_articles(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        data=json.load(f)
    return data



def get_inputs(hints):
    keys = []
    for hint in hints:
        print(f"请输入{hint}:")
        keys.append(input())
    return keys


def replace(article, keys):
    for i in range(len(keys)):
        tmp=str(i+1)
        article=article.replace("{{"+tmp+"}}",keys[i])
        # 将 article 中的 {{i}} 替换为 keys[i]
    return article


if __name__ == "__main__":
    args = parser_data()
    data = read_articles(args.file)
    articles = data["articles"]    #articles is a list

    # 根据参数或随机从 articles 中选择一篇文章    
    if args.title is not None:##！！！！注意写法，不能len()!=0,因为还是none而非str
        for _ in articles:
            if _['title']==args.title:
                title=_['title']
                article=_['article']
                hints=_['hints']
    else:
        index=random.randrange(len(articles))
        title=articles[index]['title']
        article=articles[index]['article']
        hints=articles[index]['hints']
        
    # 给出合适的输出，提示用户输入
    keys=get_inputs(hints)
    
    # 获取用户输入并进行替换
    result=replace(article, keys)
    # 给出结果
    print("The result is:\n",result)



