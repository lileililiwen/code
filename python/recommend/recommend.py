import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 读取文章数据
df_articles = pd.read_csv('recommend/articles.csv')

# 提取文章的关键词特征
vectorizer = TfidfVectorizer()
article_features = vectorizer.fit_transform(df_articles['content'])

# 计算文章相似度矩阵
article_similarities = cosine_similarity(article_features)

# 定义推荐函数，接受文章的 ID 和推荐数量
def recommend_articles(article_id, num_recommendations):
    # 根据文章 ID 找到相似度最高的文章
    similar_articles = list(enumerate(article_similarities[article_id]))
    sorted_similar_articles = sorted(similar_articles, key=lambda x: x[1], reverse=True)

    # 返回推荐的文章 ID 和标题
    recommended_articles = []
    for i in range(1, num_recommendations + 1):
        article_index = sorted_similar_articles[i][0]
        article_title = df_articles.iloc[article_index]['title']
        recommended_articles.append({'id': article_index, 'title': article_title})
    return recommended_articles


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/recommend_articles', methods=['GET'])
def recommend_articles_api():
    article_id = request.args.get('article_id')
    num_recommendations = int(request.args.get('num_recommendations'))
    recommended_articles = recommend_articles(article_id, num_recommendations)
    return jsonify(recommended_articles)

if __name__ == '__main__':
    app.run(debug=True)    