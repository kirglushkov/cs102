import nltk
from bayes import NaiveBayesClassifier
from bottle import redirect, request, route, run, template
from db import News, session
from scraputils import get_news

nltk.download("punkt")

domain = "https://news.ycombinator.com/"


def clean(s):
    for x in ",.!?;#$%^*-=":
        s = s.replace(x, "")
    for x in '/()"+':
        s = s.replace(x, " ")
    return s

@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template("news_template", rows=rows)


@route("/add_label/", method="GET")
def add_label():
    s = session()
    label = request.GET.get("label", "")
    id = int(request.GET.get("id", ""))
    row = s.query(News).filter(News.id == id).one()
    row.label = label
    s.add(row)
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    late_news = get_news(domain + "front", n_pages=1)
    s = session()
    for record in late_news:
        if (
            s.query(News)
            .filter(News.title == record["title"] and News.author == record["author"])
            .first()
            == None
        ):
            data = News(
                title=record["title"],
                author=record["author"],
                url=record["url"],
                comments=record["comments"],
                points=record["points"],
                label=None,
            )
            s.add(data)
    s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    s = session()
    labeled = s.query(News).filter(News.label != None).all()
    x = [row.title for row in labeled]
    y = [row.label for row in labeled]
    x = [clean(title) for title in x]
    x_train, y_train = x[: round(len(labeled) * 0.7)], y[: round(len(labeled) * 0.7)]
    x_test, y_test = x[round(len(labeled) * 0.7)], y[round(len(labeled) * 0.7)]
    model = NaiveBayesClassifier(1)
    model.fit(x_train, y_train)
    print(model.score(x_test, y_test))
    unlabeled = s.query(News).filter(News.label == None).all()
    x_class = [clean(row.title) for row in unlabeled]
    predictions = model.predict(x_class)
    classified_news = []
    second_priority = []
    third_priority = []
    for i, row in enumerate(unlabeled):
        if predictions[i] == "good":
            classified_news.append(row)
        elif predictions[i] == "maybe":
            second_priority.append(row)
        else:
            third_priority.append(row)
    classified_news.extend(second_priority)
    classified_news.extend(third_priority)
    return template("news_recommends", rows=classified_news)


if __name__ == "__main__":
    run(host="localhost", port=8080)
