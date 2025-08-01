Um sistema de controle de estoque e ponto de venda (PDV) desenvolvido em Python com interface gráfica usando **Tkinter**, voltado para o gerenciamento de uma loja física. Foi criado para a **Donna Bella & Delícias e Malícias**, mas pode ser adaptado a qualquer pequeno comércio.

## 🧩 Funcionalidades

- Login de usuários com diferentes cargos
- Dashboard com visão geral do caixa e notificações
- Cadastro de produtos com categorias, validade e controle de estoque
- Busca de produtos com imagem e informações detalhadas
- Realização de vendas com aplicação de desconto por valor, porcentagem ou promoção
- Seleção de forma de pagamento e cálculo automático de troco
- Histórico de vendas e retiradas do caixa
- Controle de caixa com abertura, retirada, fechamento e impressão de relatórios
- Perfil do usuário com edição de dados e logout

## 🛠️ Tecnologias utilizadas

- **Python** – linguagem principal
- **Tkinter** – construção da interface gráfica
- **SQLite** – banco de dados local leve e simples
- **Datetime** – manipulação de datas e horários
- **Math** – cálculos de valores e totais
- **Matplotlib** – geração de gráficos (relatórios visuais)

## 📦 Estrutura sugerida do projeto
```
├── main.py
├── /screens
│ ├── login.py
│ ├── dashboard.py
│ ├── caixa.py
│ ├── vendas.py
│ └── ...
├── /database
│ └── db.sqlite
├── /assets
│ ├── imagens
│ └── estilos
├── LICENSE
└── README.md
```
> Desenvolvido por **Gustavo Henrique Lima Santos** para profissionalizar o atendimento e o controle da loja familiar, unindo aprendizado prático de programação com necessidades reais do comércio.
