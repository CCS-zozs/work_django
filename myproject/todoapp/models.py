from django.db import models # Djangoのモデル機能をインポート
import pandas as pd
from django_pandas.io import read_frame

# ToDoモデルを定義
class Todo(models.Model):
    # タイトル：最大30文字の文字列フィールド
    title = models.CharField(max_length=30)

    # メモ：長文テキストフィールド（空でもOK）
    memo = models.TextField(null=True, blank=True)

    # 完了フラグ：真偽値（Boolean）フィールド（デフォルトは未完了=False）
    completed = models.BooleanField(default=False)

    # 作成日時：日時フィールド（自動的に現在時刻が設定される）
    created = models.DateTimeField(auto_now_add=True)

    # 更新日時：日時フィールド（自動的に現在時刻が設定される）
    updated = models.DateTimeField(auto_now=True)

    # オブジェクトの文字列表現を定義（管理画面などでの表示に使用）
    def __str__(self):
        # タイトルを返す
        return self.title

    # モデルのメタ情報を定義
    class Meta:
        # 作成日時の降順でソート（最新が最初）
        ordering = ['-created']
    
    # --------------- データ分析用メソッド ---------------
    # クラスメソッドとは、インスタンスを作成しなくても呼び出せるメソッドです。
    # cls はクラス自身を表す引数で、インスタンスメソッドの self に相当します。
    @classmethod
    def get_completion_stats(cls):
        """完了済みおよび未完了のタスク数を集計して返します"""

        # すべてのタスクを取得
        todos = cls.objects.all()

        # 完了済みタスクの数をカウント（completed=True のフィルターを適用）
        completed = todos.filter(completed=True).count()

        # 未完了タスクの数をカウント（completed=False のフィルターを適用）
        not_completed = todos.filter(completed=False).count()

        # 総タスク数
        total = completed + not_completed

        # 完了率を計算（パーセンテージで小数点以下2桁まで）
        # タスクが0件の場合はゼロ除算を避けて 0 を返す
        if total > 0:
            completion_rate = round((completed / total) * 100, 2)
        else:
            completion_rate = 0

        # 統計情報を辞書として返す
        return {
            'completed': completed, # 完了済みタスク数
            'not_completed': not_completed, # 未完了タスク数
            'total': total, # 総タスク数
            'completion_rate': completion_rate # 完了率
        }

    @classmethod
    def get_todos_dataframe(cls):
        """ToDo データを Pandas の DataFrame に変換します"""

        # すべてのタスクを取得する（QuerySet）
        todos = cls.objects.all()
        
        # Django の QuerySet を Pandas の DataFrame に変換
        # DataFrame はスプレッドシートのような表形式のデータ構造であり、
        # データ分析や可視化を行う際に使用します
        return read_frame(todos)