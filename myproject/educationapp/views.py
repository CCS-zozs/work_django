from django.shortcuts import render
from .models import Student

# 生徒情報を全て取得するビュー関数
def get_all_student(request):
    # ★ SELECT * FROM Student; と同じ
    # Studentテーブルの全ての生徒データを取得し、student_listに格納
    student_list = Student.objects.all()
    
    # 'educationapp/student_list.html' テンプレートを表示する
    # {'students': student_list} でテンプレートにデータを渡している
    return render(request, 
                'educationapp/student_list.html', {'students': student_list})
