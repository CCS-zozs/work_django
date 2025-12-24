from django.db import models

#================================================================
# 化学品 (Chemical) テーブル
#================================================================
class Chemical(models.Model):
    # 化学品英文名
    # 使用CharField，长度设为255通常足够容纳大多数IUPAC名称
    name_en = models.CharField(
        max_length=255, 
        verbose_name="化学品英文名",
        help_text="Chemical Name (English)"
    )

    # 化学品日文名
    name_jp = models.CharField(
        max_length=255, 
        verbose_name="化学品日文名",
        help_text="化学物質名（日本語）"
    )

    # CAS号
    # 使用CharField而不是数字字段，因为CAS号包含连字符（如 7732-18-5）
    cas_number = models.CharField(
        max_length=20, 
        verbose_name="CAS号",
    )

    # SDS阈值
    # 使用FloatField以便于进行数值比较（例如：浓度 >= 阈值）
    # null=True, blank=True 允许该字段为空（并非所有化学品都有法定阈值）
    sds_threshold = models.FloatField(
        verbose_name="SDS阈值 (%)",
        null=True, 
        blank=True,
        help_text="通知対象物質の裾切値 (例: 0.1)"
    )

    # 标签阈值
    label_threshold = models.FloatField(
        verbose_name="标签阈值 (%)",
        null=True, 
        blank=True,
        help_text="表示対象物質の裾切値 (例: 1.0)"
    )

    # 备注
    # 使用TextField以容纳较长的文本内容
    note = models.TextField(
        verbose_name="备注",
        blank=True, 
        null=True
    )