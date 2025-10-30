from django.shortcuts import render,HttpResponse,redirect
from .models import Topic,Entry
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.
def index(request):
    return render(request,'learning_logs/index.html')
    # return HttpResponse('index.html OK!')  

@login_required # ログイン確認処理が割り込む
def topics(request):
    # トピックレコード全件検索
    # where owner=request.user
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

#'topics/<int:topic_id>/'
@login_required
def topic(request, topic_id):
    # トピックレコード1件検索
    topic = Topic.objects.get(id=topic_id)
    # トピックの持ち主がログインユーザーではない？
    if topic.owner != request.user:
        # ページが見つかりませんという例外を発生
        raise Http404



    # モデルクラス名を小文字化_set
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request,'learning_logs/topic.html',context)

from .forms import TopicForm, EntryForm
@login_required
def new_topic(request):
    context = None
    # get:画面の初期表示

    # GETの場合    
    if request.method != 'POST':
        form = TopicForm()#無入力状態のフォーム部品
        
    else:# POSTの場合
         # 入力・送信値のセット
         form = TopicForm(data=request.POST)
         if form.is_valid():
             # データベースには保存せず、Topicデータを取得
             new_topic =form.save(commit=False)
             # 持ち主のセット
             new_topic.owner = request.user
             # insert => モデルクラスのsave()
             new_topic.save()

             #insert,update,delete,login
             return redirect('learning_logs:topics')

    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

# 'new_entry/<int:topic_id>/'
@login_required
def new_entry(request, topic_id):
    # 記事のトピックを検索
    topic = Topic.objects.get(id=topic_id)
    
    # トピックの持ち主がログインユーザーではない？
    if topic.owner != request.user:
        # ページが見つかりませんという例外を発生
        raise Http404    
    
        # GETの場合    
    if request.method != 'POST':
        form = EntryForm()#無入力状態のフォーム部品
        
    else:# POSTの場合
         # 入力・送信値のセット
         form = EntryForm(data=request.POST)
         if form.is_valid():
             #EntryModelクラスの戻り値
             # 送信値のテキストデータが格納
             new_entry = form.save(commit=False)
             # 不足分のトピックデータを追加
             new_entry.topic = topic
             new_entry.save()
             # 記事一覧
             # path('topics/<int:topic_id>/', views.topic, name='topic'),
             return redirect('learning_logs:topic',topic_id=topic_id)


    context = {'topic':topic, 'form':form}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request, entry_id):
    """既存の記事を編集する"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # トピックの持ち主がログインユーザーではない？
    if topic.owner != request.user:
        # ページが見つかりませんという例外を発生
        raise Http404

    if request.method != 'POST':
        # 初回リクエスト時は現在の記事の内容がフォームに埋め込まれている
        form = EntryForm(instance=entry)
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)