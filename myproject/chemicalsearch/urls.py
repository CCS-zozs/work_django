from django.urls import path
from . import views
from django.views.generic import TemplateView

# URLパターンのリストを定義

app_name = 'chemicalsearch'

urlpatterns = [
    # 化学物質を学習するindex画面を表示するURLパターン
    # 例: /exe05/
    path('', TemplateView.as_view(template_name='chemicalsearch/orm_index.html'),
        name='orm_index'),

    # 化学物質の一覧表示ビューに対応するURLパターン
    # 例: /exe05/chemical_list/
    path('chemical_list/', views.get_all_chemicals, name='chemical_list'), 
]