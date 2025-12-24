from django.urls import path
from . import views
from django.views.generic import TemplateView

# URLパターンのリストを定義
app_name = 'education'
urlpatterns = [
    # ORMを学習するindex画面を表示するURLパターン
    # 例: /exe04/
    path('', TemplateView.as_view(template_name='educationapp/orm_index.html'),
        name='orm_index'),
    
    # 生徒の一覧表示ビューに対応するURLパターン
    # 例: /exe04/student_list/
    path('student_list/', views.get_all_student, name='student_list'), 
]
