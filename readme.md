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



### Entidades e Atributos:

1. **Vendedores**:
   - ID_Vendedor (PK)
   - Nome_Vendedor
2. **Clientes**:
   - ID_Cliente (PK)
   - Nome_Cliente
3. **Produtos**:
   - ID_Produto (PK)
   - Nome_Produto
   - Preco_Unitario
4. **Servicos**:
   - ID_Servico (PK)
   - Descricao_Servico
   - Valor_Por_Hora
5. **Faturas**:
   - ID_Fatura (PK)
   - ID_Vendedor (FK)
   - ID_Cliente (FK)
   - Data_Fatura
   - Total_Pagar
6. **Itens_Vendidos** (para faturas de venda de produtos):
   - ID_Item (PK)
   - ID_Fatura (FK)
   - ID_Produto (FK)
   - Quantidade
7. **Servicos_Prestados** (para faturas de serviços prestados):
   - ID_Servico_Prestado (PK)
   - ID_Fatura (FK)
   - ID_Servico (FK)
   - Data_Duracao_Servico
   - Valor_Total_Servico
8. **Adiantamentos**:
   - ID_Adiantamento (PK)
   - ID_Vendedor (FK)
   - ID_Cliente (FK)
   - Valor_Adiantamento
   - Data_Adiantamento
   - Saldo_Restante
9. **Creditos**:
   - ID_Credito (PK)
   - ID_Vendedor (FK)
   - ID_Cliente (FK)
   - Motivo_Credito
   - Valor_Credito
   - Data_Credito
10. **Debitos**:
    - ID_Debito (PK)
    - ID_Vendedor (FK)
    - ID_Cliente (FK)
    - Motivo_Debito
    - Valor_Debito
    - Data_Debito
11. **Relatorios_Vendas**:
    - ID_Relatorio_Vendas (PK)
    - Data_Venda
    - ID_Cliente (FK)
    - Total_Venda
12. **Relatorios_Faturamento**:
    - ID_Relatorio_Faturamento (PK)
    - Periodo
    - Total_Faturas_Emitidas
    - Total_Faturas_Pagas
    - Total_Faturas_Pendentes
13. **Relatorios_Clientes_Frequentes**:
    - ID_Relatorio_Clientes (PK)
    - ID_Cliente (FK)
    - Num_Compras
    - Valor_Total_Compras
14. **Relatorios_Estoque**:
    - ID_Relatorio_Estoque (PK)
    - Produtos_Disponiveis
    - Quantidade_Vendida
    - Quantidade_Reposicao
    - Alertas_Estoque_Baixo
15. **Contas_Receber**:
    - ID_Conta_Receber (PK)
    - ID_Cliente (FK)
    - Valor_Total_Pendente
16. **Detalhes_Faturas_Pendentes**:
    - ID_Detalhe_Fatura_Pendente (PK)
    - ID_Conta_Receber (FK)
    - ID_Fatura (FK)
    - Data_Vencimento
    - Valor_Fatura

​			

Sure, here are the entities and attributes translated into English:

1. **Sellers**:
   - Seller_ID (PK)
   - Seller_Name

2. **Clients**:
   - Client_ID (PK)
   - Client_Name

3. **Products**:
   - Product_ID (PK)
   - Product_Name
   - Unit_Price

4. **Services**:
   - Service_ID (PK)
   - Service_Description
   - Hourly_Rate

5. **Invoices**:
   - Invoice_ID (PK)
   - Seller_ID (FK)
   - Client_ID (FK)
   - Invoice_Date
   - Total_Payable

6. **Items_Sold** (for product sales invoices):
   - Item_ID (PK)
   - Invoice_ID (FK)
   - Product_ID (FK)
   - Quantity

7. **Services_Provided** (for service invoices):
   - Service_Provided_ID (PK)
   - Invoice_ID (FK)
   - Service_ID (FK)
   - Service_Date_Duration
   - Total_Service_Value

8. **Advances**:
   - Advance_ID (PK)
   - Seller_ID (FK)
   - Client_ID (FK)
   - Advance_Amount
   - Advance_Date
   - Remaining_Balance

9. **Credits**:
   - Credit_ID (PK)
   - Seller_ID (FK)
   - Client_ID (FK)
   - Credit_Reason
   - Credit_Amount
   - Credit_Date

10. **Debits**:
    - Debit_ID (PK)
    - Seller_ID (FK)
    - Client_ID (FK)
    - Debit_Reason
    - Debit_Amount
    - Debit_Date

11. **Sales_Reports**:
    - Sales_Report_ID (PK)
    - Sale_Date
    - Client_ID (FK)
    - Total_Sale

12. **Billing_Reports**:
    - Billing_Report_ID (PK)
    - Period
    - Total_Invoices_Issued
    - Total_Invoices_Paid
    - Total_Invoices_Pending

13. **Frequent_Customers_Reports**:
    - Frequent_Customers_Report_ID (PK)
    - Client_ID (FK)
    - Num_Purchases
    - Total_Purchase_Value

14. **Inventory_Reports**:
    - Inventory_Report_ID (PK)
    - Available_Products
    - Quantity_Sold
    - Replenishment_Quantity
    - Low_Stock_Alerts

15. **Accounts_Receivable**:
    - Receivable_Account_ID (PK)
    - Client_ID (FK)
    - Total_Amount_Pending

16. **Pending_Invoice_Details**:
    - Pending_Invoice_Detail_ID (PK)
    - Receivable_Account_ID (FK)
    - Invoice_ID (FK)
    - Due_Date
    - Invoice_Amount

These tables represent the entities and attributes in English, following normalization up to the third normal form for the proposed billing system.





```py
from django.db import models

class Seller(models.Model):# Representa um vendedor que pode realizar vendas.
    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=100)

    

class Client(models.Model):# Representa um cliente que pode fazer compras ou contratar serviços.
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)

    

class Product(models.Model):# Representa um produto que pode ser vendido.
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    

class Service(models.Model):# Representa um serviço que pode ser prestado.
    service_id = models.AutoField(primary_key=True)
    service_description = models.TextField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)

    

class Invoice(models.Model):# Representa uma fatura emitida para um cliente.
    invoice_id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    total_payable = models.DecimalField(max_digits=10, decimal_places=2)

    

class SoldItem(models.Model):# Representa um item vendido em uma fatura de venda de produtos.
    item_id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    

class ProvidedService(models.Model):# Representa um serviço prestado em uma fatura de serviços.

    service_provided_id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    service_date_duration = models.CharField(max_length=100)
    total_service_value = models.DecimalField(max_digits=10, decimal_places=2)
    
    

from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    work_schedule = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Sale(models.Model):
    sale_date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    total_value = models.DecimalField(max_digits=10, decimal_places=2)

class Absence(models.Model):
    absence_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reason = models.TextField()

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payment_period = models.CharField(max_length=255)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)

class Payment(models.Model):
    payment_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)


```



​	

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

Claro, abaixo estão os exemplos de como você pode definir as requisições Axios para cada uma dessas rotas usando React com TypeScript:

```typescript
import axios from 'axios';

const API_URL = 'http://localhost:8000/';

// Rotas relacionadas aos produtos
export const addProduct = (productData: any) => axios.post(`${API_URL}product/add/`, productData);
export const editProduct = (productId: number, productData: any) => axios.put(`${API_URL}product/edit/${productId}/`, productData);
export const deleteProduct = (productId: number) => axios.delete(`${API_URL}product/delete/${productId}/`);
export const showProduct = (productId: number) => axios.get(`${API_URL}product/show/${productId}/`);
export const uploadProductImage = (imageData: any) => axios.post(`${API_URL}product/upload-image/`, imageData);
export const deleteProductImage = (imageId: number) => axios.delete(`${API_URL}product/delete-image/${imageId}/`);
export const selectProductCoverImage = (imageId: number) => axios.put(`${API_URL}product/select-cover-image/${imageId}/`);
export const selectOrUploadRawMaterial = (materialData: any) => axios.post(`${API_URL}product/select-or-upload-raw-material/`, materialData);
export const selectOrUploadCategories = (categoryData: any) => axios.post(`${API_URL}product/select-or-upload-categories/`, categoryData);

// Rotas relacionadas às categorias
export const listCategories = () => axios.get(`${API_URL}category/list/`);
export const addCategory = (categoryData: any) => axios.post(`${API_URL}category/add/`, categoryData);
export const updateCategory = (categoryId: number, categoryData: any) => axios.put(`${API_URL}category/update/${categoryId}/`, categoryData);
export const readCategory = (categoryId: number) => axios.get(`${API_URL}category/read/${categoryId}/`);
export const deleteCategory = (categoryId: number) => axios.delete(`${API_URL}category/delete/${categoryId}/`);

// Rotas relacionadas às subcategorias
export const listSubcategories = () => axios.get(`${API_URL}subcategory/list/`);
export const addSubcategory = (subcategoryData: any) => axios.post(`${API_URL}subcategory/add/`, subcategoryData);
export const updateSubcategory = (subcategoryId: number, subcategoryData: any) => axios.put(`${API_URL}subcategory/update/${subcategoryId}/`, subcategoryData);
export const readSubcategory = (subcategoryId: number) => axios.get(`${API_URL}subcategory/read/${subcategoryId}/`);
export const deleteSubcategory = (subcategoryId: number) => axios.delete(`${API_URL}subcategory/delete/${subcategoryId}/`);

// Rotas relacionadas aos materiais brutos
export const listRawMaterials = () => axios.get(`${API_URL}raw-material/list/`);
export const addRawMaterial = (materialData: any) => axios.post(`${API_URL}raw-material/add/`, materialData);
export const updateRawMaterial = (materialId: number, materialData: any) => axios.put(`${API_URL}raw-material/update/${materialId}/`, materialData);
export const readRawMaterial = (materialId: number) => axios.get(`${API_URL}raw-material/read/${materialId}/`);
export const deleteRawMaterial = (materialId: number) => axios.delete(`${API_URL}raw-material/delete/${materialId}/`);
export const uploadRawMaterialImage = (imageData: any) => axios.post(`${API_URL}raw-material/upload-image/`, imageData);
export const deleteRawMaterialImage = (imageId: number) => axios.delete(`${API_URL}raw-material/delete-image/${imageId}/`);
export const uploadRawMaterialCoverImage = (imageData: any) => axios.post(`${API_URL}raw-material/upload-cover-image/`, imageData);

// Rotas relacionadas aos profissionais
export const createProfessional = (professionalData: any) => axios.post(`${API_URL}professional/create/`, professionalData);
export const editProfessional = (professionalId: number, professionalData: any) => axios.put(`${API_URL}professional/edit/${professionalId}/`, professionalData);
export const deleteProfessional = (professionalId: number) => axios.delete(`${API_URL}professional/delete/${professionalId}/`);
export const showProfessional = (professionalId: number) => axios.get(`${API_URL}professional/show/${professionalId}/`);
export const listProfessionals = () => axios.get(`${API_URL}professional/list/`);

// Rotas relacionadas às vendas
export const createSale = (saleData: any) => axios.post(`${API_URL}sale/create/`, saleData);
export const selectOrRegisterProfessional = (professionalData: any) => axios.post(`${API_URL}sale/select-or-register-professional/`, professionalData);
export const selectOrRegisterCustomer = (customerData: any) => axios.post(`${API_URL}sale/select-or-register-customer/`, customerData);
export const selectPaymentType = (paymentData: any) => axios.post(`${API_URL}sale/select-payment-type/`, paymentData);
export const searchProduct = (query: string) => axios.get(`${API_URL}sale/search-product/?q=${query}`);
export const listProductWithCover = () => axios.get(`${API_URL}sale/list-product-with-cover/`);

// Rotas relacionadas às imagens
export const addImage = (imageData: any) => axios.post(`${API_URL}image/add/`, imageData);
export const viewImage = (imageId: number) => axios.get(`${API_URL}image/view/${imageId}/`);
export const deleteImage = (imageId: number) => axios.delete(`${API_URL}image/delete/${imageId}/`);
export const associateImageWithProduct = (imageData: any) => axios.post(`${API_URL}image/associate-with-product/`, imageData);
export const associateImageWithRawMaterial = (imageData: any) => axios.post(`${API_URL}image/associate-with-raw-material/`, imageData);
export const listImagesByType = (type: string) => axios.get(`${API_URL}image/list-by-type/?type=${type}`);
export const updateImageDescription = (imageId: number, description: string) => axios.put(`${API_URL}image/update-description/${imageId}/`, { description });

// Rotas relacionadas aos clientes
export const addCustomer = (customerData: any) => axios.post(`${API_URL}customer/add/`, customerData);
export const editCustomer = (customerId: number, customerData: any) => axios.put(`${API_URL}customer/edit/${customerId}/`, customerData);
export const deleteCustomer = (customerId: number) => axios.delete(`${API_URL}customer/delete/${customerId}/`);
export const showCustomer = (customerId: number) => axios.get(`${API_URL}customer/show/${customerId}/`);
export const listCustomers = () => axios.get(`${API_URL}customer/list/`);
export const searchCustomer = (query: string) => axios.get(`${API_URL}customer/search/?q=${query}`);
export const associateCustomerWithSale = (customerId: number, saleId: number) => axios.post(`${API_URL}customer/associate-with-sale/`, { customerId, saleId });
```

Isso deve criar funções Axios para cada rota especificada na sua API Django, permitindo que

 você faça solicitações HTTP a esses endpoints a partir do seu aplicativo React com TypeScript.