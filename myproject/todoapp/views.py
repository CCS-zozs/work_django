from . import models # 現在のアプリケーションのモデルをインポート

# Djangoのクラスベースビューをインポート
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# ============================================================
# ToDo一覧表示用のビュー：継承元はListView
# ============================================================
class TodoListView(ListView):
    # 使用するモデルを指定（Todoモデル）
    model = models.Todo
    # 使用するテンプレートファイルを指定
    template_name = 'todoapp/todo_list.html'
    # テンプレートで使用するオブジェクトリストの名前を指定
    context_object_name = 'todos'
    
class TodoDetailView(DetailView):
    model = models.Todo
    template_name = 'todoapp/todo_detail.html'
    context_object_name = 'todo'
    
class TodoCreateView(CreateView):
    model = models.Todo
    template_name = 'todoapp/todo_create.html'
    fields = ['title', 'memo', 'completed']
    success_url = reverse_lazy('todo_list')