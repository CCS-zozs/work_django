from django.contrib import admin
from .models import Chemical

@admin.register(Chemical)
class ChemicalAdmin(admin.ModelAdmin):
    # 在列表中显示的字段：CAS号，英文名，日文名，SDS阈值
    list_display = ('cas_number', 'name_en', 'name_jp', 'sds_threshold', 'label_threshold')
    
    # 允许搜索的字段：可以搜CAS号，也可以搜中日文名
    search_fields = ('cas_number', 'name_en', 'name_jp')
    
    # 过滤器：可以按是否有SDS阈值进行筛选
    list_filter = ('sds_threshold', 'label_threshold')
    
    # 每页显示多少条
    list_per_page = 20