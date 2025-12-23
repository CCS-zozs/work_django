from . import models # 現在のアプリケーションのモデルをインポート

# Djangoのクラスベースビューをインポート
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.timezone import localtime
from .forms import TodoForm
from django.contrib.messages.views import SuccessMessageMixin

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
    
class TodoCreateView(SuccessMessageMixin, CreateView):
    model = models.Todo
    template_name = 'todoapp/todo_create.html'
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    success_message = "Todo項目が作成されました。"

class TodoUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Todo
    template_name = 'todoapp/todo_update.html'
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    success_message = "Todo項目が更新されました。"

    def form_valid(self, form):
        todo = form.save()
        print(f"Todo項目が更新されました: {todo.title} (更新日時: {localtime(todo.updated)})")
        return super().form_valid(form)

class TodoDeleteView(SuccessMessageMixin, DeleteView):
    model = models.Todo
    template_name = 'todoapp/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')
    success_message = "Todo項目が削除されました。"