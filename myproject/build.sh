#!/usr/bin/env bash
# 遇到错误即停止
set -o errexit 

pip install -r requirements.txt

# 收集静态文件
python manage.py collectstatic --no-input

# 执行数据库迁移
python manage.py migrate