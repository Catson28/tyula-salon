Para testar as rotas definidas no arquivo `urls.py` usando o Postman, siga estas etapas:

1. **Abrir o Postman**: Inicie o aplicativo Postman.

2. **Criar uma nova solicitação**: Clique em "Create a Request" (Criar uma solicitação) no canto superior esquerdo ou clique em "+" para criar uma nova solicitação.

3. **Definir o método e a URL**: Escolha o método HTTP desejado (GET, POST, PUT, DELETE) para a solicitação e insira a URL correspondente. Por exemplo, para listar todas as categorias, você usaria `GET` e a URL `http://localhost:8000/list/`.

4. **Enviar a solicitação**: Clique em "Send" (Enviar) para enviar a solicitação ao servidor.

5. **Analisar a resposta**: Após enviar a solicitação, o Postman exibirá a resposta do servidor. Verifique se a resposta está conforme o esperado.

Agora, para criar as solicitações Axios em um aplicativo React TypeScript, você pode seguir este exemplo:

```typescript
import axios from 'axios';
import { useState, useEffect } from 'react';

interface Category {
  id: number;
  name: string;
  description: string;
}

const YourComponent: React.FC = () => {
  const [categories, setCategories] = useState<Category[]>([]);

  useEffect(() => {
    // Função para carregar as categorias
    const fetchCategories = async () => {
      try {
        const response = await axios.get<Category[]>('http://localhost:8000/list/');
        setCategories(response.data);
      } catch (error) {
        console.error('Erro ao carregar categorias:', error);
      }
    };

    // Chamar a função para carregar as categorias quando o componente montar
    fetchCategories();
  }, []); // Dependência vazia para garantir que a solicitação só seja feita uma vez

  return (
    <div>
      <h1>Categorias</h1>
      <ul>
        {categories.map(category => (
          <li key={category.id}>
            <h3>{category.name}</h3>
            <p>{category.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default YourComponent;
```

Este exemplo usa o Axios para fazer uma solicitação GET para a rota `/list/` no servidor local. Ele define um componente React que carrega e exibe as categorias. Certifique-se de instalar o pacote Axios em seu projeto React usando `npm install axios` ou `yarn add axios`.




Para testar as rotas definidas em `urls.py` no Postman, você pode seguir estas etapas:

1. **Inicie o servidor Django**: Certifique-se de que o servidor Django esteja em execução localmente na porta 8000. Você pode fazer isso executando o comando `python manage.py runserver`.

2. **Abra o Postman**: Se você ainda não tiver o Postman instalado, baixe e instale a versão apropriada para o seu sistema operacional em [getpostman.com](https://www.getpostman.com/).

3. **Crie uma nova solicitação**: No Postman, clique no botão "New" para criar uma nova solicitação.

4. **Defina o método e a URL da solicitação**: Selecione o método HTTP desejado (por exemplo, POST, GET, PUT, DELETE) e insira a URL correspondente à rota que deseja testar. Por exemplo, para testar a rota de adicionar um novo cliente, você usaria `http://localhost:8000/add/`.

5. **Adicione os parâmetros da solicitação (se aplicável)**: Dependendo da rota que está testando, você pode precisar adicionar parâmetros à sua solicitação. Por exemplo, ao adicionar um novo cliente, você precisará incluir os dados do cliente no corpo da solicitação.

6. **Envie a solicitação**: Depois de configurar todos os detalhes necessários, clique no botão "Send" para enviar a solicitação ao servidor.

Quanto ao código Axios para o React TypeScript, você pode usá-lo para fazer solicitações HTTP para o servidor Django. Aqui está um exemplo de como você pode usar o Axios para fazer uma solicitação POST para adicionar um novo cliente:

```typescript
import axios from 'axios';

// Defina a URL base do servidor
const baseURL = 'http://localhost:8000';

// Função para adicionar um novo cliente
const addCustomer = async (customerData: any) => {
  try {
    const response = await axios.post(`${baseURL}/add/`, customerData);
    return response.data;
  } catch (error) {
    console.error('Error adding customer:', error);
    throw error;
  }
};

// Exemplo de uso da função addCustomer
const newCustomerData = {
  name: 'John Doe',
  email: 'john@example.com',
  phone: '1234567890',
  address: '123 Main St'
};

addCustomer(newCustomerData)
  .then((data) => {
    console.log('Customer added successfully:', data);
  })
  .catch((error) => {
    console.error('Failed to add customer:', error);
  });
```

Este é um exemplo simples de como você pode usar o Axios no React TypeScript para fazer uma solicitação POST para adicionar um novo cliente ao servidor Django. Certifique-se de instalar o pacote Axios no seu projeto React usando `npm install axios`.




Para testar as rotas definidas em `urls.py` no Postman, você pode seguir os seguintes passos:

1. Abra o Postman e crie uma nova solicitação.
2. Selecione o método de solicitação desejado (GET, POST, PUT, DELETE) e insira a URL correspondente, por exemplo, `http://localhost:8000/add/` para adicionar uma nova imagem.
3. Se necessário, adicione os parâmetros ou corpo da solicitação conforme necessário para a operação que deseja realizar.
4. Clique em "Enviar" para fazer a solicitação ao servidor.

Agora, vamos criar uma chamada de API usando Axios em um aplicativo React TypeScript:

1. Certifique-se de ter o Axios instalado no seu projeto React. Se ainda não estiver instalado, você pode fazê-lo executando `npm install axios` no terminal do seu projeto.

2. Supondo que você tenha uma função em um componente React onde deseja fazer a solicitação, você pode fazer algo assim:

```typescript
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MyComponent: React.FC = () => {
  const [responseData, setResponseData] = useState<any>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.post('http://localhost:8000/add/', { /* dados do corpo da solicitação, se necessário */ });
        setResponseData(response.data);
      } catch (error) {
        console.error('Erro ao fazer a solicitação:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      {/* Renderize os dados da resposta conforme necessário */}
    </div>
  );
};

export default MyComponent;
```

Este é um exemplo simples de como você pode usar o Axios para fazer uma solicitação POST para `http://localhost:8000/add/`. Certifique-se de substituir `{/* dados do corpo da solicitação, se necessário */}` pelos dados que você deseja enviar no corpo da solicitação. Além disso, lembre-se de lidar com os dados da resposta de acordo com sua lógica de aplicativo.




Claro! Vou mostrar como você pode usar o Postman para fazer solicitações para as URLs fornecidas no `urls.py`, e então criar um exemplo de como usar o Axios no React com TypeScript para fazer solicitações para essas mesmas URLs no servidor local (localhost:8000).

### Postman:

1. Abra o Postman.
2. Selecione o método de solicitação desejado (GET, POST, PUT, DELETE).
3. Insira a URL completa correspondente à rota que deseja acessar (por exemplo, http://localhost:8000/add/ para adicionar um novo material bruto).
4. Selecione o corpo da solicitação e insira os dados necessários, se aplicável.
5. Selecione 'Enviar' para fazer a solicitação.

Repita esse processo para cada uma das rotas definidas no `urls.py`.

### Exemplo de uso do Axios no React com TypeScript:

Supondo que você tenha um componente React onde deseja fazer solicitações para o servidor local:

```tsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const YourComponent: React.FC = () => {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/list/');
        setData(response.data);
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Dados recebidos:</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default YourComponent;
```

Este exemplo utiliza o Axios para fazer uma solicitação GET para http://localhost:8000/list/ assim que o componente é montado. Ele então exibe os dados recebidos na página.

Você pode adaptar esse código para fazer solicitações POST, PUT ou DELETE, e também para outras rotas do seu backend Django conforme necessário. Certifique-se de instalar o pacote Axios em seu projeto React usando `npm install axios`.



Para testar as URLs em Django no Postman, siga estas etapas:

1. Abra o Postman.
2. Crie uma nova solicitação.
3. Especifique o método HTTP (GET, POST, PUT, DELETE) e a URL correspondente.
4. Selecione os parâmetros necessários (por exemplo, no caso de um POST, você pode precisar adicionar os dados no corpo da solicitação).
5. Clique em "Send" para enviar a solicitação e ver a resposta.

Aqui está um exemplo de como solicitar a URL `/add/`:

- Método: POST
- URL: `http://localhost:8000/add/`
- Corpo da solicitação: (se necessário, dependendo da lógica de sua visão)

Agora, para criar uma solicitação axios no React com TypeScript, você pode fazer o seguinte:

```typescript
import axios from 'axios';

// Função para adicionar um novo produto
const addProduct = async () => {
  try {
    const response = await axios.post('http://localhost:8000/add/', {
      // Incluir dados aqui, se necessário
    });
    console.log('Response:', response.data);
    // Tratar a resposta conforme necessário
  } catch (error) {
    console.error('Error:', error);
    // Tratar erros conforme necessário
  }
};
```

Lembre-se de que você precisa instalar o pacote axios no seu projeto React para usar a biblioteca axios:

```bash
npm install axios
```

Esta função `addProduct` enviará uma solicitação POST para `http://localhost:8000/add/`. Certifique-se de ajustar os dados na solicitação de acordo com o que é esperado pela sua visão do Django.


Claro! Vou mostrar como você pode testar essas rotas usando o Postman e como criar uma solicitação HTTP equivalente usando Axios no React TypeScript.

### Postman:

1. Abra o Postman.
2. Crie uma nova solicitação do tipo POST e insira a URL completa para a rota `create_professional` (por exemplo, `http://localhost:8000/create/`).
3. No corpo da solicitação, insira os dados JSON que deseja enviar para criar um novo profissional. Certifique-se de que os dados estejam no formato esperado pelo endpoint.
4. Clique em "Send" para enviar a solicitação e ver a resposta do servidor.

### Axios no React TypeScript:

```tsx
import React, { useState } from 'react';
import axios from 'axios';

const YourComponent: React.FC = () => {
  const [name, setName] = useState('');
  const [position, setPosition] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [address, setAddress] = useState('');

  const handleCreateProfessional = async () => {
    try {
      const response = await axios.post('http://localhost:8000/create/', {
        name,
        position,
        email,
        phone,
        address,
      });
      console.log('Professional created:', response.data);
      // Aqui você pode fazer algo com a resposta, como atualizar o estado do componente ou mostrar uma mensagem de sucesso.
    } catch (error) {
      console.error('Error creating professional:', error);
      // Aqui você pode lidar com erros, como exibir uma mensagem de erro ao usuário.
    }
  };

  return (
    <div>
      <input type="text" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} />
      <input type="text" placeholder="Position" value={position} onChange={(e) => setPosition(e.target.value)} />
      <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
      <input type="text" placeholder="Phone" value={phone} onChange={(e) => setPhone(e.target.value)} />
      <input type="text" placeholder="Address" value={address} onChange={(e) => setAddress(e.target.value)} />
      <button onClick={handleCreateProfessional}>Create Professional</button>
    </div>
  );
};

export default YourComponent;
```

Este é um exemplo básico de como usar Axios no React TypeScript para fazer uma solicitação POST para o endpoint `create_professional` no servidor local em `localhost:8000`. Certifique-se de instalar o Axios em seu projeto React usando `npm install axios`.

Claro, vou mostrar como você pode fazer requisições usando o Postman para as rotas definidas no arquivo `urls.py`. E então, vou criar exemplos de requisições usando Axios em um aplicativo React TypeScript.

### Requisições no Postman

1. **Criar uma nova venda:**
   - Método: POST
   - URL: `http://localhost:8000/create/`
   - Body: (JSON)
     ```json
     {
       "products": [1, 2, 3],
       "professional": 1,
       "customer": 1,
       "payment_type": "Credit Card",
       "date_time": "2024-03-03T12:00:00",
       "alternative_price": 100.50
     }
     ```

2. **Selecionar ou registrar um profissional para uma venda:**
   - Método: POST
   - URL: `http://localhost:8000/select-or-register-professional/`
   - Body: (JSON)
     ```json
     {
       "name": "John Doe",
       "position": "Sales Manager",
       "email": "john@example.com",
       "phone": "1234567890",
       "address": "123 Main St, Anytown, USA"
     }
     ```

3. **Selecionar ou registrar um cliente para uma venda:**
   - Método: POST
   - URL: `http://localhost:8000/select-or-register-customer/`
   - Body: (JSON)
     ```json
     {
       "name": "Alice Smith",
       "email": "alice@example.com",
       "phone": "9876543210",
       "address": "456 Elm St, Anytown, USA"
     }
     ```

4. **Selecionar o tipo de pagamento para uma venda:**
   - Método: POST
   - URL: `http://localhost:8000/select-payment-type/`
   - Body: (JSON)
     ```json
     {
       "payment_type": "Debit Card"
     }
     ```

5. **Procurar por um produto:**
   - Método: GET
   - URL: `http://localhost:8000/search-product/?query=product_name`

6. **Listar produtos com imagens de capa:**
   - Método: GET
   - URL: `http://localhost:8000/list-product-with-cover/`

### Exemplo de Axios no React TypeScript

Para usar Axios em um aplicativo React TypeScript, primeiro você precisa instalá-lo via npm ou yarn:

```bash
npm install axios
```

ou

```bash
yarn add axios
```

Aqui está um exemplo de como você pode usar o Axios para fazer uma requisição para uma das rotas:

```typescript
import axios from 'axios';

// Criar uma nova venda
const createSale = async () => {
  try {
    const response = await axios.post('http://localhost:8000/create/', {
      products: [1, 2, 3],
      professional: 1,
      customer: 1,
      payment_type: 'Credit Card',
      date_time: '2024-03-03T12:00:00',
      alternative_price: 100.50,
    });
    console.log(response.data);
  } catch (error) {
    console.error('Error:', error);
  }
};

// Chamar a função
createSale();
```

Você pode replicar esse exemplo para as outras rotas fazendo as modificações necessárias nas URLs e nos corpos das requisições.

Para testar as rotas definidas no `urls.py` usando o Postman, você precisa seguir os seguintes passos:

1. **Instale o Postman**: Se você ainda não tiver o Postman instalado, você pode baixá-lo [aqui](https://www.postman.com/downloads/).

2. **Abra o Postman**: Depois de instalado, abra o Postman em seu computador.

3. **Crie uma nova solicitação**: Clique em "New" para criar uma nova solicitação.

4. **Defina o método HTTP e a URL**: Escolha o método HTTP adequado (GET, POST, PUT, DELETE) e insira a URL correspondente à rota que você deseja testar. Por exemplo, se você deseja testar a rota "list/" que lista todas as subcategorias, a URL seria "http://localhost:8000/list-subcategories/".

5. **Envie a solicitação**: Clique no botão "Send" para enviar a solicitação e ver a resposta do servidor.

Aqui está um exemplo de como você pode usar o Axios no React TypeScript para fazer uma solicitação para o servidor local em localhost:8000:

```typescript
import axios from 'axios';

// Função para listar todas as subcategorias
const listSubcategories = async () => {
  try {
    const response = await axios.get('http://localhost:8000/list-subcategories/');
    return response.data;
  } catch (error) {
    console.error('Erro ao listar subcategorias:', error);
    return null;
  }
};

// Exemplo de uso da função listSubcategories
const exampleUsage = async () => {
  const subcategories = await listSubcategories();
  if (subcategories) {
    console.log('Subcategorias:', subcategories);
  }
};

// Chamada da função de exemplo
exampleUsage();
```

Lembre-se de substituir 'list-subcategories' pela rota que você deseja testar no servidor Django. Certifique-se também de que o servidor Django esteja em execução localmente na porta 8000.