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



##	sequencia de tabelas Importantes

```bash
Person
Seller
InvoiceCategory
Customer
Invoice
InvoiceItem
InvoicePayment
	para a venda de produto -> Category
							-> Product
							-> SoldItem #	Produto vendido

	para a Prestacao de servico -> Category
								-> Product
								-> Subcategory
								-> Service
								-> ProvidedService #	Servico prestado

	Servico que o trabalhador prestou	-> Person
									 	-> Employee
										-> ProvidedServiceEnpl
```



###	So informacoes da fatura

**Person**

```
http://localhost:8000/api/person/add_person/
```
Corpo da Requisicao
```json
{
	"name": "Paulo Manuel",
	"address": "Luanda",
	"contact": "923349809",
	"email": "pm@gmail.com",
	"phone": "000000000"
}
```
Rota para listar
```
http://localhost:8000/api/person/people/
```

**Seller**

```
http://localhost:8000/api/sales/add_seller/
```
Corpo da Requisicao
```json
{
    "type": "Gerente",
    "person": 1
}
```
Rota para listar
```
http://localhost:8000/api/sales/sellers/
```

**InvoiceCategory**

```
http://localhost:8000/api/sales/add_invoice_category/
```
Corpo da Requisicao
```json
{
    "name": "servico prestado"
}
```
Rota para listar
```
http://localhost:8000/api/sales/invoice-categories/
```

**Customer**

```
http://localhost:8000/api/customers/add/
```
Corpo da Requisicao
```json
{
    "person": 1
}
```
Rota para listar
```
http://localhost:8000/api/customers/list/
```

**Invoice**

```
http://localhost:8000/api/sales/add_invoice/
```
Corpo da Requisicao
```json
{
    "invoice_number": 1,
    "issuance_date": "2024-03-02",
    "due_date": "2024-03-02",
    "payment_type": "Cartao",
    "total_amount": 50000,
    "seller": 1,
    "client": 1,
    "category": 1
}
```
Rota para listar
```
http://localhost:8000/api/sales/invoices/
```

**InvoiceItem** baseando-se em copiar o sevico ou produto e colar aqui

```
http://localhost:8000/api/sales/add_invoice_item/
```
Corpo da Requisicao
```json
{
    "description": "Product description",
    "quantity": 1,
    "unit_price": 100,
    "line_total": 100,
    "invoice": 1
}
```
Rota para listar
```
http://localhost:8000/api/sales/invoice-items/
```

**InvoicePayment**

```
http://localhost:8000/api/sales/add_invoice_payment/
```
Corpo da Requisicao
```json
{
    "payment_date": "2024-03-25",
    "amount_paid": 500,
    "invoice": 1
}
```
Rota para listar
```
http://localhost:8000/api/sales/invoice-payments/
```



###	do Produto Vendido

**Category**

```
http://localhost:8000/api/categories/add/
```
Corpo da Requisicao
```json
{
    "name": "Perucas"
    "description": "Perucas Brasileiras",
}
```
Rota para listar
```
http://localhost:8000/api/categories/list/
```

**Product**

```
http://localhost:8000/api/products/add/
```
Corpo da Requisicao
```json
{
    "name": "Product Name",
    "cost": 50,
    "description": "Product Description",
    "quantity": 10,
    "category": 1
}
```
Rota para listar
```
http://localhost:8000/api/products/list/
```

**SoldItem** Item Vendido

```
http://localhost:8000/api/sales/add_sold_item/
```
Corpo da Requisicao
```json
{
    "quantity": 1,
    "invoice": 1,
    "product": 1
}
```
Rota para listar
```
http://localhost:8000/api/sales/sold-items/
```



###	do Servico prestado

**Category**

```
http://localhost:8000/api/categories/add/
```
Corpo da Requisicao
```json
{
    "name": "Cabelereiro",
    "description": "Produtopar o trabalho de Cabelereiro"
}
```
Rota para listar
```
http://localhost:8000/api/categories/list/
```

**Product**

```
http://localhost:8000/api/products/add/
```
Corpo da Requisicao
```json
{
    "name": "Product Name",
    "cost": 50,
    "description": "Product Description",
    "quantity": 10,
    "category": 2
}
```
Rota para listar
```
http://localhost:8000/api/products/list/
```

**Subcategory**  

```
http://localhost:8000/api/subcategories/add/
```
Corpo da Requisicao
```json
{
    "name": "Product Name",
    "description": "Product Description",
    "category": 2
}
```
Rota para listar
```
http://localhost:8000/api/subcategories/list/
```

**Service** 

```
http://localhost:8000/api/services/add/
```
Corpo da Requisicao
```json
{
    "name": "Service Name",
    "description": "Service Description",
    "price": 50,
    "subcategory": 1,
    "hourly_rate": 25
}
```
Rota para listar
```
http://localhost:8000/api/services/list/
```

**ProvidedService** Servico prestado

```
http://localhost:8000/api/sales/add_provided_service/
```
Corpo da Requisicao
```json
{
    "service_date_duration": "2024-03-25 to 2024-03-27",
    "alternative_price": 200,
    "total_service_value": 500,
    "invoice": 1,
    "service": 1
}
```
Rota para listar
```
http://localhost:8000/api/sales/provided-services/
```


###	

###	do Servico que o trabalhador prestou

**Person**

```
http://localhost:8000/api/person/add_person/
```
Corpo da Requisicao
```json
{
    "name": "John Doe",
    "address": "123 Main Street",
    "contact": "John Doe",
    "email": "johndoe@example.com",
    "phone": "123-456-7890"
}
```
Rota para listar
```
http://localhost:8000/api/person/people/
```

**Employee**

```
http://localhost:8000/api/employee/add_employee/
```
Corpo da Requisicao
```json
{
    "position": "Developer",
    "work_schedule": "Full-time",
    "person": 2
}
```
Rota para listar
```
http://localhost:8000/api/employee/employees/
```

**ProvidedServiceEnpl**

```
http://localhost:8000/api/sales/add_provided_service_enpl/
```
Corpo da Requisicao
```json
{
    "employee": 1,
    "provided_service": 1
}
```
Rota para listar
```
http://localhost:8000/api/sales/provided-service-enpl/
```
```
# Usaremos
```bash
python manage.py makemigrations category
python manage.py makemigrations image
python manage.py makemigrations polimorph
python manage.py makemigrations seller
python manage.py makemigrations customer
python manage.py makemigrations payment
python manage.py makemigrations product
python manage.py makemigrations service
python manage.py makemigrations employee
python manage.py makemigrations invoice
python manage.py makemigrations person
python manage.py makemigrations subcategory
python manage.py migrate
python manage.py runserver
```

#	Todas as routas

```bash
/api/categories/        rest_framework.routers.APIRootView      api-root
/api/categories/<category_id>/list/img/ apps.category.views.CategoryImageViewSet        category-images-list
/api/categories/<category_id>/list/img\.<format>/       apps.category.views.CategoryImageViewSet        category-images-list
/api/categories/\.<format>/     rest_framework.routers.APIRootView      api-root
/api/categories/add/    apps.category.views.add_category
/api/categories/delete/<int:category_id>/       apps.category.views.delete_category
/api/categories/deleteAll/      apps.category.views.delete_categories
/api/categories/list/   apps.category.views.list_categories
/api/categories/read/<int:category_id>/ apps.category.views.read_category
/api/categories/search  apps.category.views.search_category_by_name
/api/categories/update/<int:category_id>/       apps.category.views.update_category
/api/customers/add/     apps.customer.views.add_customer
/api/customers/associate-with-sale/     apps.customer.views.associate_customer_with_sale
/api/customers/delete/<int:customer_id>/        apps.customer.views.delete_customer
/api/customers/edit/<int:customer_id>/  apps.customer.views.edit_customer
/api/customers/list/    apps.customer.views.list_customers
/api/customers/search/  apps.customer.views.search_customer
/api/customers/show/<int:customer_id>/  apps.customer.views.show_customer
/api/employee/absence/<int:pk>/ apps.employee.views.AbsenceDetailView   absence-detail
/api/employee/absences/ apps.employee.views.absence_list        absence-list
/api/employee/add_absence/      apps.employee.views.create_absence      create_absence
/api/employee/add_advance/      apps.employee.views.create_advance      create_advance
/api/employee/add_bonus/        apps.employee.views.create_bonus        create_bonus
/api/employee/add_commission/   apps.employee.views.create_commission   create_commission
/api/employee/add_deduction/    apps.employee.views.create_deduction    create_deduction
/api/employee/add_employee/     apps.employee.views.create_employee     create_employee
/api/employee/add_employee_payment/     apps.employee.views.create_employee_payment     create_employee_payment
/api/employee/add_overtime_hours/       apps.employee.views.create_overtime_hours       create_overtime_hours
/api/employee/add_salary/       apps.employee.views.create_salary       create_salary
/api/employee/add_subsidy/      apps.employee.views.create_subsidy      create_subsidy
/api/employee/advance/<int:pk>/ apps.employee.views.AdvanceDetailView   advance-detail
/api/employee/advances/ apps.employee.views.advance_list        advance-list
/api/employee/bonus/<int:pk>/   apps.employee.views.BonusDetailView     bonus-detail
/api/employee/bonuses/  apps.employee.views.bonus_list  bonus-list
/api/employee/commission/<int:pk>/      apps.employee.views.CommissionDetailView        commission-detail
/api/employee/commissions/      apps.employee.views.commission_list     commission-list
/api/employee/deduction/<int:pk>/       apps.employee.views.DeductionDetailView deduction-detail
/api/employee/deductions/       apps.employee.views.deduction_list      deduction-list
/api/employee/employee-payment/<int:pk>/        apps.employee.views.EmployeePaymentDetailView   employee-payment-detail
/api/employee/employee-payments/        apps.employee.views.employee_payment_list       employee-payment-list
/api/employee/employee/<int:pk>/        apps.employee.views.EmployeeDetailView  employee-detail
/api/employee/employees/        apps.employee.views.employee_list       employee-list
/api/employee/overtime-hours/   apps.employee.views.overtime_hours_list overtime-hours-list
/api/employee/overtime-hours/<int:pk>/  apps.employee.views.OvertimeHoursDetailView     overtime-hours-detail
/api/employee/salaries/ apps.employee.views.salary_list salary-list
/api/employee/salary/<int:pk>/  apps.employee.views.SalaryDetailView    salary-detail
/api/employee/subsidies/        apps.employee.views.subsidy_list        subsidy-list
/api/employee/subsidy/<int:pk>/ apps.employee.views.SubsidyDetailView   subsidy-detail
/api/finance/accounts-receivable/       apps.finance.views.accounts_receivable_list     accounts-receivable-list
/api/finance/accounts-receivable/<int:pk>/      apps.finance.views.AccountsReceivableDetailView accounts-receivable-detail
/api/finance/add_accounts_receivable/   apps.finance.views.create_accounts_receivable   create_accounts_receivable
/api/finance/add_credit/        apps.finance.views.create_credit        create_credit
/api/finance/add_debit/ apps.finance.views.create_debit create_debit
/api/finance/add_pending_invoice_details/       apps.finance.views.create_pending_invoice_details       create_pending_invoice_details
/api/finance/credit/<int:pk>/   apps.finance.views.CreditDetailView     credit-detail
/api/finance/credits/   apps.finance.views.credit_list  credit-list
/api/finance/debit/<int:pk>/    apps.finance.views.DebitDetailView      debit-detail
/api/finance/debits/    apps.finance.views.debit_list   debit-list
/api/finance/pending-invoice-details/   apps.finance.views.pending_invoice_details_list pending-invoice-details-list
/api/finance/pending-invoice-details/<int:pk>/  apps.finance.views.PendingInvoiceDetailsDetailView      pending-invoice-details-detail
/api/images/add/        apps.image.views.add_image
/api/images/associate-with-raw-material/        apps.image.views.associate_image_with_raw_material
/api/images/associate-with-service/     apps.image.views.associate_image_with_service
/api/images/delete/<int:image_id>/      apps.image.views.delete_image
/api/images/list-by-type/       apps.image.views.list_images_by_type
/api/images/update-description/<int:image_id>/  apps.image.views.update_image_description
/api/images/upload-image/category/      apps.image.views.UploadCategoryImageView        upload_category_image
/api/images/upload-image/product/       apps.image.views.UploadProductImageView upload_product_image
/api/images/upload-image/service/       apps.image.views.UploadServiceImageView upload_service_image
/api/images/view/<int:image_id>/        apps.image.views.view_image
/api/payment/add_payment/       apps.payment.views.create_payment       create_payment
/api/payment/add_payment_report/        apps.payment.views.create_payment_report        create_payment_report
/api/payment/payment-report/<int:pk>/   apps.payment.views.PaymentReportDetailView      payment-report-detail
/api/payment/payment-reports/   apps.payment.views.payment_report_list  payment-report-list
/api/payment/payment/<int:pk>/  apps.payment.views.PaymentDetailView    payment-detail
/api/payment/payments/  apps.payment.views.payment_list payment-list
/api/person/add_person/ apps.person.views.create_person create_person
/api/person/people/     apps.person.views.person_list   person-list
/api/person/person/<int:pk>/    apps.person.views.PersonDetailView      person-detail
/api/poli/add/  apps.polimorph.views.FuncionarioCreate  comentario-list-create
/api/poli/comentarios/  apps.polimorph.views.ComentarioListCreate       comentario-list-create
/api/poli/fotos/        apps.polimorph.views.FotoListCreate     foto-list-create
/api/products/add/      apps.product.views.add_product
/api/products/delete-image/<int:image_id>/      apps.product.views.delete_product_image
/api/products/delete/<int:product_id>/  apps.product.views.delete_product
/api/products/list/     apps.product.views.list_products
/api/products/read/<int:product_id>/    apps.product.views.read_product
/api/products/update/<int:product_id>/  apps.product.views.update_product
/api/products/upload-cover-image/       apps.product.views.upload_product_cover_image
/api/products/upload-image/     apps.product.views.upload_product_image
/api/reports/add_billing_report/        apps.reports.views.create_billing_report        create_billing_report
/api/reports/add_frequent_customers_report/     apps.reports.views.create_frequent_customers_report     create_frequent_customers_report
/api/reports/add_inventory_report/      apps.reports.views.create_inventory_report      create_inventory_report
/api/reports/add_sales_report/  apps.reports.views.create_sales_report  create_sales_report
/api/reports/billing-report/<int:pk>/   apps.reports.views.BillingReportDetailView      billing-report-detail
/api/reports/billing-reports/   apps.reports.views.billing_report_list  billing-report-list
/api/reports/frequent-customers-report/<int:pk>/        apps.reports.views.FrequentCustomersReportDetailView    frequent-customers-report-detail
/api/reports/frequent-customers-reports/        apps.reports.views.frequent_customers_report_list       frequent-customers-report-list
/api/reports/inventory-report/<int:pk>/ apps.reports.views.InventoryReportDetailView    inventory-report-detail
/api/reports/inventory-reports/ apps.reports.views.inventory_report_list        inventory-report-list
/api/reports/sales-report/<int:pk>/     apps.reports.views.SalesReportDetailView        sales-report-detail
/api/reports/sales-reports/     apps.reports.views.sales_report_list    sales-report-list
/api/services/add-product/<int:service_id>/     apps.service.views.add_product
/api/services/add/      apps.service.views.create_service
/api/services/delete-image/<int:image_id>/      apps.service.views.delete_service_image
/api/services/delete-product/<int:product_id>/  apps.service.views.delete_product
/api/services/delete/<int:service_id>/  apps.service.views.delete_service
/api/services/deleteAll/        apps.service.views.delete_all_services
/api/services/list-products/<int:service_id>/   apps.service.views.list_products
/api/services/list/     apps.service.views.list_services
/api/services/retrieve-product/<int:product_id>/        apps.service.views.retrieve_product
/api/services/retrieve/<int:service_id>/        apps.service.views.retrieve_service
/api/services/select-cover-image/<int:service_id>/      apps.service.views.select_service_cover_image
/api/services/select-or-upload-categories/<int:service_id>/     apps.service.views.select_or_upload_categories
/api/services/select-or-upload-raw-material/<int:service_id>/   apps.service.views.select_or_upload_raw_material
/api/services/update-product/<int:product_id>/  apps.service.views.update_product
/api/services/update/<int:service_id>/  apps.service.views.update_service
/api/services/upload-image/<int:service_id>/    apps.service.views.upload_service_image
/api/subcategories/add/ apps.subcategory.views.add_subcategory
/api/subcategories/delete/<int:subcategory_id>/ apps.subcategory.views.delete_subcategory
/api/subcategories/deleteAll/   apps.subcategory.views.delete_subcategories
/api/subcategories/list/        apps.subcategory.views.list_subcategories
/api/subcategories/read/<int:subcategory_id>/   apps.subcategory.views.read_subcategory
/api/subcategories/search       apps.subcategory.views.search_subcategory_by_name
/api/subcategories/update/<int:subcategory_id>/ apps.subcategory.views.update_subcategory
/media/<path>   django.views.static.serve
```

**Rotas Importantes**

Listar

```bash
http://localhost:8000/api/employee/absences/
http://localhost:8000/api/employee/advances/
http://localhost:8000/api/employee/bonuses/
http://localhost:8000/api/employee/commissions/
http://localhost:8000/api/employee/deductions/
http://localhost:8000/api/employee/employee-payments/
http://localhost:8000/api/employee/employees/
http://localhost:8000/api/employee/salaries/
http://localhost:8000/api/employee/subsidies/
http://localhost:8000/api/finance/accounts-receivable/
http://localhost:8000/api/finance/add_accounts_receivable/
http://localhost:8000/api/finance/credits/
http://localhost:8000/api/finance/debits/
http://localhost:8000/api/images/add/
http://localhost:8000/api/payment/payment-reports/
http://localhost:8000/api/payment/payments/
http://localhost:8000/api/poli/add/
http://localhost:8000/api/reports/billing-reports/
http://localhost:8000/api/reports/frequent-customers-reports/
http://localhost:8000/api/reports/inventory-reports/
http://localhost:8000/api/reports/sales-reports/
```

Adicionar

```bash
http://localhost:8000/api/employee/add_absence/
http://localhost:8000/api/employee/add_advance/
http://localhost:8000/api/employee/add_bonus/
http://localhost:8000/api/employee/add_commission/
http://localhost:8000/api/employee/add_deduction/
http://localhost:8000/api/employee/add_employee/
http://localhost:8000/api/employee/add_employee_payment/
http://localhost:8000/api/employee/add_overtime_hours/
http://localhost:8000/api/employee/add_salary/
http://localhost:8000/api/employee/add_subsidy/
http://localhost:8000/api/finance/add_accounts_receivable/
http://localhost:8000/api/finance/add_credit/
http://localhost:8000/api/finance/add_debit/
http://localhost:8000/api/finance/add_pending_invoice_details/
http://localhost:8000/api/payment/add_payment/
http://localhost:8000/api/payment/add_payment_report/
http://localhost:8000/api/person/add_person/
http://localhost:8000/api/reports/add_billing_report/
http://localhost:8000/api/reports/add_frequent_customers_report/
http://localhost:8000/api/reports/add_inventory_report/
http://localhost:8000/api/reports/add_sales_report/
```



Ver Detalhe

```bash
http://localhost:8000/api/employee/absence/<int:pk>/
http://localhost:8000/api/employee/advance/<int:pk>/
http://localhost:8000/api/employee/bonus/<int:pk>/
http://localhost:8000/api/employee/commission/<int:pk>/
http://localhost:8000/api/employee/deduction/<int:pk>/
http://localhost:8000/api/employee/employee-payment/<int:pk>/
http://localhost:8000/api/employee/employee/<int:pk>/
http://localhost:8000/api/employee/overtime-hours/<int:pk>/
http://localhost:8000/api/employee/salary/<int:pk>/
http://localhost:8000/api/employee/subsidy/<int:pk>/
http://localhost:8000/api/finance/accounts-receivable/<int:pk>/
http://localhost:8000/api/finance/credit/<int:pk>/
http://localhost:8000/api/finance/debit/<int:pk>/
http://localhost:8000/api/finance/pending-invoice-details/<int:pk>/
http://localhost:8000/api/payment/payment-report/<int:pk>/
http://localhost:8000/api/payment/payment/<int:pk>/
http://localhost:8000/api/person/person/<int:pk>/
http://localhost:8000/api/reports/billing-report/<int:pk>/
http://localhost:8000/api/reports/frequent-customers-report/<int:pk>/
http://localhost:8000/api/reports/inventory-report/<int:pk>/
http://localhost:8000/api/reports/sales-report/<int:pk>/
```



Vamos comparar cada um dos modelos adicionais com os modelos originais e destacar suas semelhanças e diferenças:

1. `ProductCategory` com `Product` e `Service`:
   - **Semelhanças**:
     - Todos são modelos que representam entidades do sistema (categoria de produto, produto e serviço).
     - Cada um possui um campo para nome/descrição da entidade (`name` para `ProductCategory`, `product_name` para `Product`, `service_description` para `Service`).
   - **Diferenças**:
     - `ProductCategory` não possui campos relacionados a preço ou taxa como `Product` e `Service`.

2. `Employee` com `Seller`:
   - **Semelhanças**:
     - Ambos são modelos que representam entidades relacionadas à atividade comercial (funcionário e vendedor).
     - Cada um possui um campo para nome da entidade (`name` para `Employee`, `seller_name` para `Seller`).
   - **Diferenças**:
     - `Employee` possui campos adicionais como `position` e `work_schedule` que não são relevantes para `Seller`.

3. `Sale` com `SoldItem` e `ProvidedService`:
   - **Semelhanças**:
     - Todos são modelos relacionados a transações ou registros de atividades comerciais (venda, item vendido e serviço prestado).
     - Cada um possui campos para data da transação ou registro (`sale_date` para `Sale`, `invoice` com `service_date_duration` para `ProvidedService`, `invoice` com `product` e `quantity` para `SoldItem`).
   - **Diferenças**:
     - `Sale` possui um campo para o valor total da venda (`total_value`) que não está presente em `SoldItem` e `ProvidedService`.

4. `Absence` com `Invoice`:
   - **Semelhanças**:
     - Ambos são modelos que representam registros relacionados a atividades comerciais (ausência de funcionário e fatura emitida).
     - Cada um possui um campo para data do registro (`absence_date` para `Absence`, `invoice_date` para `Invoice`).
   - **Diferenças**:
     - `Absence` possui um campo para o motivo da ausência (`reason`) que não está presente em `Invoice`.

5. `Salary` com `Invoice` e `Payment`:
   - **Semelhanças**:
     - Todos são modelos relacionados a pagamentos ou registros financeiros (salário, fatura e pagamento).
     - Cada um possui campos para data do registro (`payment_date` para `Salary` e `Payment`, `invoice_date` para `Invoice`).
   - **Diferenças**:
     - `Salary` possui campos específicos para informações salariais como `payment_period`, `base_salary`, `deductions` e `net_salary`, que não estão presentes em `Invoice` e `Payment`.

Essas comparações destacam como cada modelo representa uma entidade específica no sistema, com campos e funcionalidades adaptados às necessidades dessa entidade.

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

![](/home/cand/Desktop/Atayene Space/img/Dicand-database.png)

![asmaioresseguradorasdeangola-01](/home/cand/Desktop/Atayene Space/img/asmaioresseguradorasdeangola-01.jpg)

![1711224077259](/home/cand/Desktop/Atayene Space/img/1711224077259.gif)

![Aintercalar componente](/home/cand/Desktop/Atayene Space/img/Aintercalar componente.jpg)

![adicionar no apicontext](/home/cand/Desktop/Atayene Space/img/adicionar no apicontext.jpg)

![Flowchart](/home/cand/Desktop/Atayene Space/img/Flowchart.jpeg)

![Flowchart(1)](/home/cand/Desktop/Atayene Space/img/Flowchart(1).jpeg)