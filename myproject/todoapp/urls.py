from django.urls import path
from . import views # 現在のディレクトリからviewsモジュールをインポート

urlpatterns = [
    # 'list'というURLにアクセスすると、views.pyのTodoListViewクラスが呼び出される
    # name='todo_list'は、このURLパターンに名前を付けている（テンプレートなどで参照可能）
    path('list/', views.TodoListView.as_view(), name='todo_list'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('new/', views.TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/edit/', views.TodoUpdateView.as_view(), name='todo_update'),
]