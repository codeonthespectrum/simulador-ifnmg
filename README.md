# Simulador de Posição IFNMG - Processo Seletivo 2025

Simulador que permite aos candidatos verificar sua posição estimada no processo seletivo do IFNMG, baseado no Edital 1048/2025.

## 📋 Funcionalidades

- **Seleção de Curso e Campus/Polo**: Escolha entre todos os 47 cursos disponíveis
- **Modalidades de Concorrência**: AC, V_PCD, V_EFA, LB_PPI, LB_EP, LB_PCD, LB_Q, LI_PPI, LI_EP, LI_PCD, LI_Q
- **Simulação de Posição**: Veja sua posição na modalidade e no geral
- **Status de Aprovação**: Indica "Provável Aprovação" ou "Provável Reprovação"

## 🚀 Como Usar

### Opção 1: Servidor Python (Recomendado)

```bash
cd /Users/kimgomes/Desktop/simulador-ifnmg
source venv/bin/activate
python3 servidor.py
```

O navegador abrirá automaticamente em `http://localhost:8000`

### Opção 2: Abrir diretamente

Abra o arquivo `index.html` no navegador (alguns navegadores podem bloquear o carregamento do JSON por questões de segurança CORS).

## 📁 Estrutura do Projeto

```
simulador-ifnmg/
├── index.html              # Aplicação web principal
├── dados_simulador.json    # Dados extraídos dos PDFs
├── extrair_dados.py        # Script para extrair dados dos PDFs
├── servidor.py             # Servidor HTTP simples
├── venv/                   # Ambiente virtual Python
└── PDFs originais:
    ├── ANEXO-I-Cursos-e-Vagas-Ofertadas-Atualizado-com-3a-retificacao.pdf
    └── LISTA-PRELIMINAR-DE-INSCRICOES-DEFERIDAS-E-INDEFERIDAS-EDITAL-1048.pdf
```

## 📊 Dados Extraídos

### Cursos com código especial (conforme instrução):
- **3011** - Técnico em Inteligência Artificial (Polo: Campus Montes Claros) - **40 vagas**
- **3012** - Técnico em Inteligência Artificial (Polo: CEADi Montes Claros) - **160 vagas**

### Total de dados:
- **47 cursos/polos** diferentes
- **7.031 inscrições deferidas** processadas
- **11 modalidades de concorrência**

## 🔧 Atualizar Dados

Se houver uma nova lista de inscrições, execute:

```bash
cd /Users/kimgomes/Desktop/simulador-ifnmg
source venv/bin/activate
python3 extrair_dados.py
```

## ⚠️ Aviso Importante

Esta é uma **simulação não oficial** baseada na lista preliminar de inscrições deferidas. 
O resultado final pode variar após:
- Recursos
- Desistências
- Retificações do edital
- Outras alterações no processo seletivo

**Consulte sempre os canais oficiais do IFNMG para informações definitivas.**

## 📌 Legenda das Modalidades

| Código | Descrição |
|--------|-----------|
| AC | Ampla Concorrência |
| V_PCD | Pessoa com Deficiência |
| V_EFA | Egresso da Escola Família Agrícola |
| LB_PPI | Escola Pública, Renda ≤ 1SM, Preto/Pardo/Indígena |
| LB_EP | Escola Pública, Renda ≤ 1SM |
| LB_PCD | Escola Pública, Renda ≤ 1SM, PcD |
| LB_Q | Escola Pública, Renda ≤ 1SM, Quilombola |
| LI_PPI | Escola Pública, Independente de Renda, Preto/Pardo/Indígena |
| LI_EP | Escola Pública, Independente de Renda |
| LI_PCD | Escola Pública, Independente de Renda, PcD |
| LI_Q | Escola Pública, Independente de Renda, Quilombola |

---

Desenvolvido para auxiliar candidatos do processo seletivo IFNMG 2025.
