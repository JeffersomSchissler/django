# Sistema Financeiro Pessoal - Lista de Tarefas

## Status Atual do Projeto
- **Modelo de dados:** Parcialmente implementado (Categorias e Movimentacao)
- **Dashboard:**Template existe, mas com dados hardcoded (não conecta ao banco)
- **Autenticação:** Não implementada
- **CRUD:** Não implementado

---

## PRIORIDADE 1 - Funcionalidades Essenciais (MVP)

### 1. Sistema de Autenticação
- [ ] Criar sistema de login/logout
- [ ] Criar registro de usuários
- [ ] Configurar autenticação requerida para acessar dashboard

### 2. Melhorar Modelos de Dados
- [ ] Adicionar campo de conta bancária ao modelo Movimentacao
- [ ] Adicionar campo de pago/pendente às transações
- [ ] Adicionar campo de observações às transações

### 3. CRUD de Categorias
- [ ] View para listar categorias
- [ ] View para criar nova categoria
- [ ] View para editar categoria
- [ ] View para excluir categoria

### 4. CRUD de Transações (Movimentações)
- [ ] View para listar transações
- [ ] View para criar nova transação (receita/despesa)
- [ ] View para editar transação
- [ ] View para excluir transação
- [ ] Marcar transação como paga/pendente

### 5. Dashboard Dinâmico
- [ ] Conectar dashboard ao banco de dados
- [ ] Calcular saldo total automaticamente
- [ ] Calcular receitas do mês atual
- [ ] Calcular despesas do mês atual
- [ ] Exibir gráfico de fluxo mensal (dados reais)
- [ ] Exibir gráfico de categorias (dados reais)

---

## PRIORIDADE 2 - Funcionalidades Avançadas

### 6. Gestão de Contas Bancárias
- [ ] Criar modelo ContaBancaria
- [ ] CRUD de contas bancárias
- [ ] Visualizar saldo por conta
- [ ] Transferências entre contas

### 7. Relatórios
- [ ] Exportar transações para Excel
- [ ] Exportar transações para PDF
- [ ] Filtros por período e categoria

### 8. Controle de Contas a Pagar/Receber
- [ ] Listar contas a pagar pendentes
- [ ] Listar contas a receber pendentes
- [ ] Alertas de contas vencidas

---

## PRIORIDADE 3 - Melhorias de Interface

### 9. Interface do Usuário
- [ ] Melhorar design do dashboard
- [ ] Tornar sidebar responsiva
- [ ] Adicionar indicadores visuais de saldo
- [ ] Adicionar filtros na página de transações

### 10. Simulador CDI (Melhorias)
- [ ] Melhorar validação dos campos
- [ ] Adicionar mais opções de investimento

---

## Como Executar as Tarefas

### Preparar ambiente:
```
bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Acessar:
- Dashboard: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
