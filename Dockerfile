FROM python:3.10

# 不分阶段构建，直接安装全部
RUN pip install flask requests numpy

# 没有特意调优的安装步骤
COPY . /app
WORKDIR /app

EXPOSE 5000
CMD ["python", "app.py"]
