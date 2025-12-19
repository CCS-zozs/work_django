from . import models # 現在のアプリケーションのモデルをインポート

# Djangoのクラスベースビューをインポート
from django.views.generic import ListView

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