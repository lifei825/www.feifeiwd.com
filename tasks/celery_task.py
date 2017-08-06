from celery import Celery, platforms
from datetime import timedelta
from script.django_news import djnew, Url, headers
from script.wycto_news import App
app = Celery('ffwd', broker='redis://:123@127.0.0.1:6379/10')

app.conf.update({
    'CELERY_TASK_SERIALIZER': 'json',
    "CELERYBEAT_SCHEDULE": {
        'add-every-15-minutes': {
            'task': 'tasks.celery_task.get_new',
            'schedule': timedelta(hours=6),
        },
    }
})


platforms.C_FORCE_ROOT = True


@app.task(bind=True)
def get_new(self):
    App("list1").get_data()
    App("list2").get_data()
    App("list3").get_data()
    App("list4").get_data()

    django_new=djnew(Url, headers, 'Django')
    # print django_new.getweb()
    # print "="*50
    # print django_new.getnew()
    django_new.toredis()

    Url1 = "https://www.oschina.net/search?q=python&scope=news&days=0&onlytitle=1&sort_by_time=1"
    python_new = djnew(Url1, headers, 'Python')
    # print python_new.getweb()
    python_new.toredis()


    Url2 = "https://www.oschina.net/search?q=tornado&scope=news&days=0&onlytitle=1&sort_by_time=1"
    tornado_new=djnew(Url2,headers,'Tornado')
    #print tornado_new.getnew()
    tornado_new.toredis()

    Url3="https://www.oschina.net/search?q=flask&scope=news&days=0&onlytitle=1&sort_by_time=1"
    flask_new=djnew(Url3,headers,'Flask')
    flask_new.toredis()

    Url4="https://www.oschina.net/search?q=javascript&scope=news&days=0&onlytitle=1&sort_by_time=1"
    js_new=djnew(Url4,headers,'Javascript')
    js_new.toredis()

    Url5="https://www.oschina.net/search?q=html5&scope=news&days=0&onlytitle=1&sort_by_time=1"
    h5_new=djnew(Url5,headers,'HTML5')
    h5_new.toredis()

    Url6="https://www.oschina.net/search?q=go&scope=news&days=0&onlytitle=1&sort_by_time=1"
    go_new=djnew(Url6,headers,'Go')
    go_new.toredis()

