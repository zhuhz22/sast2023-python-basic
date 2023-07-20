
import json
import streamlit as st

def read_articles(filename):
    data=json.load(filename)
    return data

def replace(article, keys):
    for i in range(len(keys)):
        tmp=str(i+1)
        article=article.replace("{{"+tmp+"}}",keys[i])
    return article


if __name__ == "__main__":

    st.title("Filling Word Game")
    file=st.file_uploader("选择题库",type='json')
    
    if file is not None:
        data = read_articles(file)
        articles = data["articles"] 
        
        options=[]
        index={}
        for num in range(len(articles)):
            options.append(articles[num]['title'])
            index[articles[num]['title']]=num
        option=st.selectbox("Title of the article you choose is: ",options)
    
        title=articles[index[option]]['title']
        article=articles[index[option]]['article']
        hints=articles[index[option]]['hints']
        
        st.write("bacis information of the article:\n")
        st.write("title:    ",title)
        st.write("article:    ",article)
        
        keys = []
        _=0
        flag=False
        for hint in hints:
            _+=1
            keys.append(st.text_input(f"请输入{hint}:",key=str(_)))
        if len(keys[-1])>0:
            flag=True
         
        if flag==True:    
            result=replace(article, keys)
            st.write("The result is:\n",result)


