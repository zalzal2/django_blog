# djang_project

## 관리

### 프로젝트 생성

```shell
django-admin startproject do_it_django_prj .
```

### 서버 실행

```shell
python manage.py runserver
```

### 마이그레이션

```shell
python manage.py migrate
```

### 앱 생성

```shell
python manage.py startapp 앱이름
```

### 개발 순서

app/models.py -> app/templates/xxx.index -> views.py -> urls.py -> project/urls.py

http://127.0.0.1:8000/blog
http://127.0.0.1:8000/blog/pk
