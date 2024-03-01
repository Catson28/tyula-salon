Entendi, você precisa instalar várias dependências para o seu projeto Django. Aqui está como você pode instalar cada uma delas usando o pip:

```bash
pip install asgiref==3.7.2
pip install certifi==2024.2.2
pip install cffi==1.16.0
pip install chardet==5.2.0
pip install charset-normalizer==3.3.2
pip install cryptography==42.0.2
pip install defusedxml==0.7.1
pip install Django==4.2.9
pip install django-allauth==0.60.1
pip install django-rest-auth==0.9.5
pip install djangorestframework==3.14.0
pip install djangorestframework-simplejwt==5.3.1
pip install drf-jwt==1.19.2
pip install drf-pyotp==0.6.0
pip install drf-writable-nested==0.7.0
pip install idna==3.6
pip install oauthlib==3.2.2
pip install pycparser==2.21
pip install PyJWT==2.8.0
pip install pyotp==2.9.0
pip install python3-openid==3.2.0
pip install pytz==2024.1
pip install requests==2.31.0
pip install requests-oauthlib==1.3.1
pip install six==1.16.0
pip install sqlparse==0.4.4
pip install typing-extensions==4.9.0
pip install urllib3==2.2.0
pip install django-cors-headers==4.3.0
pip install django-polymorphic==3.1.0
pip install mysqlclient==2.2.0
pip install Pillow==10.1.0
pip install typing-extensions==4.8.0
```

Isso instalará todas as dependências listadas para o seu projeto Django. Certifique-se de executar esses comandos no ambiente virtual do seu projeto, se estiver usando um.


#   script para criar os aplicativos dentro da pasta "apps" 

E fornecer instruções sobre como executá-lo.

Aqui está o script:

```python
import os
import subprocess

apps_names = ['product', 'category', 'subcategory', 'material', 'professional', 'sale', 'image', 'customer']  # Lista de nomes de aplicativos

# Diretório onde o script está localizado
diretorio_script = os.path.dirname(os.path.abspath(__file__))
print(diretorio_script)

# Diretório onde o projeto Django está localizado
# diretorio_projeto = os.path.dirname(diretorio_script)
diretorio_projeto = diretorio_script
print(diretorio_projeto)

# Diretório onde a pasta "apps" será criada
diretorio_apps = os.path.join(diretorio_projeto, 'apps')

# Cria a pasta "apps" se não existir
if not os.path.exists(diretorio_apps):
    os.mkdir(diretorio_apps)

# Navega para o diretório "apps" para criar os aplicativos dentro dela
os.chdir(diretorio_apps)

# Cria os aplicativos
for app_name in apps_names:
    subprocess.run(['python', '../manage.py', 'startapp', app_name])
```

Para executar este script, siga estes passos:

1. Salve o script em um arquivo Python, por exemplo, `create_apps.py`.
2. Coloque o script na raiz do seu projeto Django.
3. Abra um terminal ou prompt de comando na raiz do projeto.
4. Execute o script usando o comando:

```
python create_apps.py
```

Isso criará os aplicativos dentro da pasta "apps" do seu projeto Django, com os nomes especificados na lista `apps_names`. Certifique-se de ajustar os nomes dos aplicativos conforme necessário.