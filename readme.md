#	In English

Here's the translation and Django models for the given entities:

### Entities and their attributes:

1. **Product:**
   - Name
   - Description
   - Price
   - Raw material
   - Category
   - Subcategory

2. **Category:**
   - Name
   - Description

3. **Subcategory:**
   - Name
   - Description
   - Belongs to Category

4. **Raw material:**
   - Name
   - Description
   - Category

5. **Professional:**
   - Name
   - Position
   - Email
   - Phone
   - Address

6. **Sale:**
   - Selected products
   - Responsible professional
   - Customer
   - Payment type
   - Date and time
   - Alternative price

7. **Image:**
   - URL
   - Description
   - Type (Product or Raw material)

8. **Customer:**
   - Name
   - Email
   - Phone
   - Address

### Functional Requirements:

1. **Product:**
   - Add product
   - Edit product
   - Delete product
   - Show product
   - Upload product images
   - Delete product image
   - Select product cover image
   - Select or upload raw material
   - Select or upload categories or subcategories

2. **Category:**
   - List categories
   - Add category
   - Update category
   - Read category
   - Delete category

3. **Subcategory:**
   - List subcategories
   - Add subcategory
   - Update subcategory
   - Read subcategory
   - Delete subcategory

4. **Raw material:**
   - List raw materials
   - Add raw material
   - Update raw material
   - Read raw material
   - Delete raw material
   - Upload raw material images
   - Delete raw material image
   - Upload raw material cover image

5. **Professional:**
   - Create professional
   - Edit professional
   - Delete professional
   - Show professional
   - List professionals

6. **Sale:**
   - Create sale
   - Select or register professional
   - Select or register customer
   - Select payment type
   - Search product
   - List product with cover

7. **Image:**
   - Add image
   - View image
   - Delete image
   - Associate image with product
   - Associate image with raw material
   - List images by type (Product or Raw material)
   - Update image description

8. **Customer:**
   - Add customer
   - Edit customer
   - Delete customer
   - Show customer
   - List customers
   - Search customer
   - Associate customer with sale

### Django Models:

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

class Professional(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

class Sale(models.Model):
    products = models.ManyToManyField(Product)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    alternative_price = models.DecimalField(max_digits=10, decimal_places=2)

class Image(models.Model):
    url = models.URLField()
    description = models.TextField()
    IMAGE_TYPES = (
        ('Product', 'Product'),
        ('Raw material', 'Raw material')
    )
    type = models.CharField(max_length=20, choices=IMAGE_TYPES)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

class RawMaterialImage(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

class Sale(models.Model):
    products = models.ManyToManyField(Product)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    alternative_price = models.DecimalField(max_digits=10, decimal_places=2)

class ClientSale(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)

class ProductSale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

class Professional(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
```

com relacionamento polimorfico

Sim, é possível criar um relacionamento polimórfico para o modelo `Image` no Django. Para isso, você pode usar o pacote `django-polymorphic` ou implementar sua própria lógica para isso. Aqui está um exemplo de como você pode implementar um relacionamento polimórfico usando a lógica própria:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class MateriaPrima(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class Cliente(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class Profissional(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class User(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class Image(models.Model):
    ImageID = models.AutoField(primary_key=True)
    Path = models.CharField(max_length=255)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('product', 'materiaprima', 'cliente', 'profissional', 'user')}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
```

Com essa implementação, você poderá associar uma imagem a qualquer uma das entidades que você listou anteriormente (`Product`, `MateriaPrima`, `Cliente`, `Profissional`, `User`). A escolha do tipo de entidade a ser associada à imagem seria feita definindo o `content_type` corretamente ao criar uma instância de `Image`.Sim, é possível criar um relacionamento polimórfico para o modelo `Image` no Django. Para isso, você pode usar o pacote `django-polymorphic` ou implementar sua própria lógica para isso. Aqui está um exemplo de como você pode implementar um relacionamento polimórfico usando a lógica própria:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class MateriaPrima(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class Cliente(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class Profissional(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class User(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class Image(models.Model):
    ImageID = models.AutoField(primary_key=True)
    Path = models.CharField(max_length=255)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('product', 'materiaprima', 'cliente', 'profissional', 'user')}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
```

Com essa implementação, você poderá associar uma imagem a qualquer uma das entidades que você listou anteriormente (`Product`, `MateriaPrima`, `Cliente`, `Profissional`, `User`). A escolha do tipo de entidade a ser associada à imagem seria feita definindo o `content_type` corretamente ao criar uma instância de `Image`.Sim, é possível criar um relacionamento polimórfico para o modelo `Image` no Django. Para isso, você pode usar o pacote `django-polymorphic` ou implementar sua própria lógica para isso. Aqui está um exemplo de como você pode implementar um relacionamento polimórfico usando a lógica própria:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class MateriaPrima(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class Cliente(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class Profissional(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class User(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class Image(models.Model):
    ImageID = models.AutoField(primary_key=True)
    Path = models.CharField(max_length=255)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('product', 'materiaprima', 'cliente', 'profissional', 'user')}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
```

Com essa implementação, você poderá associar uma imagem a qualquer uma das entidades que você listou anteriormente (`Product`, `MateriaPrima`, `Cliente`, `Profissional`, `User`). A escolha do tipo de entidade a ser associada à imagem seria feita definindo o `content_type` corretamente ao criar uma instância de `Image`.Sim, é possível criar um relacionamento polimórfico para o modelo `Image` no Django. Para isso, você pode usar o pacote `django-polymorphic` ou implementar sua própria lógica para isso. Aqui está um exemplo de como você pode implementar um relacionamento polimórfico usando a lógica própria:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class MateriaPrima(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class Cliente(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class Profissional(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class User(models.Model):
    name = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

class Image(models.Model):
    ImageID = models.AutoField(primary_key=True)
    Path = models.CharField(max_length=255)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('product', 'materiaprima', 'cliente', 'profissional', 'user')}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
```

Com essa implementação, você poderá associar uma imagem a qualquer uma das entidades que você listou anteriormente (`Product`, `MateriaPrima`, `Cliente`, `Profissional`, `User`). A escolha do tipo de entidade a ser associada à imagem seria feita definindo o `content_type` corretamente ao criar uma instância de `Image`.



# Em Portugues

Claro, aqui está a lista completa de entidades e seus atributos, juntamente com os requisitos funcionais associados:

### Entidades e seus atributos:

1. **Produto:**
   - Nome
   - Descrição
   - Preço
   - Matéria-prima
   - Categoria
   - Subcategoria

2. **Categoria:**
   - Nome
   - Descrição

3. **Subcategoria:**
   - Nome
   - Descrição
   - Pertence à Categoria

4. **Matéria-prima:**
   - Nome
   - Descrição
   - Categoria

5. **Profissional:**
   - Nome
   - Cargo
   - Email
   - Telefone
   - Endereço

6. **Venda:**
   - Produtos selecionados
   - Profissional responsável
   - Cliente
   - Tipo de pagamento
   - Data e hora
   - Preço alternativo

7. **Imagem:**
   - URL
   - Descrição
   - Tipo (Produto ou Matéria-prima)

8. **Cliente:**
   - Nome
   - Email
   - Telefone
   - Endereço

### Requisitos Funcionais:

1. **Produto:**
   - Adicionar produto
   - Editar produto
   - Eliminar produto
   - Mostrar produto
   - Carregar imagens de produto
   - Eliminar imagem de produto
   - Selecionar imagem de capa de produto
   - Selecionar ou carregar a matéria prima
   - Selecionar ou carregar categorias ou subcategorias

2. **Categoria:**
   - Listar categoria
   - Adicionar categoria
   - Atualizar categoria
   - Ler categoria
   - Eliminar categoria

3. **Subcategoria:**
   - Listar subcategoria
   - Adicionar subcategoria
   - Atualizar subcategoria
   - Ler subcategoria
   - Eliminar subcategoria

4. **Matéria-prima:**
   - Listar matéria-prima
   - Adicionar matéria-prima
   - Atualizar matéria-prima
   - Ler matéria-prima
   - Eliminar matéria-prima
   - Carregar imagens de matéria-prima
   - Eliminar imagem de matéria-prima
   - Carregar imagem de capa de matéria-prima

5. **Profissional:**
   - Criar profissional
   - Editar profissional
   - Eliminar profissional
   - Mostrar profissional
   - Listar profissional

6. **Venda:**
   - Criar venda
   - Selecionar ou cadastrar profissional
   - Selecionar ou cadastrar cliente
   - Selecionar tipo de pagamento
   - Procurar produto
   - Listar produto com capa

7. **Imagem:**
   - Adicionar imagem
   - Visualizar imagem
   - Eliminar imagem
   - Associar imagem a produto
   - Associar imagem a matéria-prima
   - Listar imagens por tipo (Produto ou Matéria-prima)
   - Atualizar descrição da imagem

8. **Cliente:**
   - Adicionar cliente
   - Editar cliente
   - Eliminar cliente
   - Mostrar cliente
   - Listar cliente
   - Procurar cliente
   - Associar cliente a venda


#  Instalacao do react tsx

Para instalar React com TypeScript, você pode seguir estes passos:

1. **Criar um novo projeto React**:
   Você pode iniciar um novo projeto React com TypeScript usando o `create-react-app`, que é uma ferramenta oficial para criar rapidamente projetos React.

   ```bash
   npx create-react-app frontend --template typescript
   ```

   Este comando cria um novo projeto React chamado `frontend` com o template TypeScript.

2. **Navegar para o diretório do projeto**:
   Depois que o projeto for criado, navegue para o diretório recém-criado:

   ```bash
   cd frontend
   ```

3. **Iniciar o aplicativo**:
   Inicie o aplicativo usando npm ou yarn:

   ```bash
   npm start
   # ou
   yarn start
   ```


# Backend

Claro, aqui está a resposta com os comandos para criação do ambiente virtual adicionados:

```bash
# Crie uma pasta chamada "backend"
mkdir backend

# Navegue até a pasta "backend"
cd backend
```

1. **Crie um ambiente virtual**: Antes de instalar o Django, é uma boa prática criar um ambiente virtual para o seu projeto. Isso isola as dependências do seu projeto das do sistema. No terminal, navegue até o diretório onde você deseja criar o ambiente virtual e execute o seguinte comando:
   ```
   python -m venv env
   ```

   Isso criará um ambiente virtual com o nome `env`.

2. **Ative o ambiente virtual**: Após criar o ambiente virtual, você precisa ativá-lo. No Windows, você pode fazer isso com o comando:
   ```
   env\Scripts\activate
   ```
   No macOS e Linux:
   ```
   source env/bin/activate
   ```

3. **Instale o Django**: Com o ambiente virtual ativado, você pode instalar o Django:
   ```
   pip install django
   ```

4. **Crie um novo projeto Django**: Agora que o Django está instalado, você pode criar um novo projeto Django. No terminal, navegue até o diretório onde você deseja criar seu projeto e execute o seguinte comando:
   ```
   django-admin startproject core .
   ```

   Isso criará uma pasta chamada `core` com a estrutura inicial do seu projeto Django.

5. **Navegue até a pasta do seu projeto**: Use o comando `cd` para entrar na pasta do seu projeto recém-criado:
   ```
   cd core
   ```

6. **Execute o servidor de desenvolvimento**: Para testar se seu projeto foi criado corretamente, você pode iniciar o servidor de desenvolvimento do Django. Use o seguinte comando:
   ```
   python manage.py runserver
   ```

   Isso iniciará um servidor de desenvolvimento local que você pode acessar no seu navegador.

A partir daí, você pode começar a desenvolver seu projeto Django, criando aplicativos, modelos, visualizações, etc. Para criar um aplicativo dentro do seu projeto, você pode usar o comando `python manage.py startapp users` e `python manage.py startapp authentication`.

Lembre-se de consultar a documentação oficial do Django (https://docs.djangoproject.com) para obter mais informações detalhadas sobre como iniciar e desenvolver projetos Django.