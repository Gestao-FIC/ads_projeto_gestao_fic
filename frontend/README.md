# **Sistema de Gerenciamento de Cursos FIC - Frontend**

Este repositório abriga o frontend do Sistema de Gerenciamento de Cursos de Formação Inicial e Continuada (FIC). Desenvolvido com **Next.js**, combina o poder do **shadcn/ui** e a flexibilidade do **Tailwind CSS** para entregar uma interface moderna, intuitiva e totalmente responsiva, garantindo uma experiência de uso otimizada e visualmente atraente.

## **Índice**

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Recursos Principais](#recursos-principais)
3. [Instalação e Configuração](#instalação-e-configuração)
4. [Estrutura de Pastas](#estrutura-de-pastas)
5. [Tecnologias Utilizadas](#tecnologias-utilizadas)
6. [Funcionalidades](#funcionalidades)
   - [Tela de Login](#tela-de-login)
   - [Dashboard](#dashboard)
   - [Gestão de Docentes](#gestão-de-docentes)
   - [Gestão de Cursos](#gestão-de-cursos)
7. [Contribuindo](#contribuindo)
8. [Licença](#licença)

---

## **Sobre o Projeto**

O projeto tem como objetivo desenvolver uma plataforma inovadora de gestão de cursos e docentes para o SENAI. A solução permitirá o gerenciamento eficiente de aulas e horários, possibilitando o vínculo de aulas aos docentes, com monitoramento do tempo de trabalho disponível para facilitar a alocação em outros horários de forma estratégica.

Além disso, a plataforma oferecerá recursos para a administração de cursos, como a abertura de vagas e o acompanhamento do início e progresso dos cursos, garantindo uma experiência mais ágil e organizada tanto para os gestores quanto para os alunos. Este sistema integrará as operações de forma centralizada, otimizando processos e promovendo uma gestão mais eficaz e transparente.a.

## **Recursos Principais**

- Interface moderna, amigável e totalmente responsiva.  
- Integração com gráficos e indicadores de metas para melhor visualização de dados.  
- Sistema de rotas dinâmicas e performáticas, aproveitando o potencial do **Next.js**.  
- Componentes altamente reutilizáveis e personalizados, desenvolvidos com **shadcn/ui** e **Tailwind CSS**.  
- Ferramentas avançadas para edição e configuração de dados em tempo real, proporcionando maior agilidade e flexibilidade na gestão.  

## **Instalação e Configuração**

### **Pré-requisitos**

- Node.js (v16 ou superior)
- npm ou yarn

### **Passos para instalação**

1. Clone o repositório:
   ```bash
   git clone https://github.com/Gestao-FIC/ads_projeto_gestao_fic.git
   cd frontend
   ```
2. Instale as dependências:
   ```bash
   npm install
   # ou
   yarn install
   ```
3. Execute o servidor de desenvolvimento:
   ```bash
   npm run dev
   # ou
   yarn dev
   ```
4. Acesse o projeto em [http://localhost:3000](http://localhost:3000).

---

## **Estrutura de Pastas**

A organização do projeto segue as boas práticas do Next.js:

```plaintext
.
├── app/
│   ├── dashboard/
│   │   └── page.tsx
│   ├── docentes/
│   │   └── page.tsx
│   ├── cursos/
│   │   └── page.tsx
├── components/
│   ├── ui/  # Componentes reutilizáveis com shadcn
│   ├── charts/  # Componentes de gráficos
│   └── forms/  # Componentes de formulários
├── styles/  # Configuração do Tailwind CSS
├── utils/  # Funções utilitárias
├── public/
├── lib/
├── mocks/
├── .eslintrc.json
├── package.json
├── tailwind.config.ts
├── tsconfig.json
```

---

## **Tecnologias Utilizadas**

- [Next.js](https://nextjs.org/)
- [shadcn/ui](https://ui.shadcn.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [React Hook Form](https://react-hook-form.com/)
- [Day.js](https://day.js.org/) para manipulação de datas
- [Chart.js](https://www.chartjs.org/) para gráficos

---

## **Funcionalidades**

### **Tela de Login**

- Autenticação Segura: Sistema robusto de validação de campos e proteção contra acessos não autorizados.
- Design Moderno e Responsivo: Interface adaptável a diferentes dispositivos e tamanhos de tela, garantindo uma experiência de uso consistente.

### **Dashboard**

- Visualização de Dados em Tempo Real: Gráficos interativos que apresentam informações de desempenho, metas e indicadores-chave.
- Calendário Interativo: Ferramenta prática para organizar eventos, prazos e compromissos importantes.
- Indicadores Intuitivos: Monitore o progresso dos cursos de forma clara e objetiva, com métricas visuais acessíveis.

### **Gestão de Docentes**

- Controle Completo de Professores: Listagem detalhada com informações como carga horária e áreas de atuação.
- Edição e Remoção em Tempo Real: Alterações rápidas e sem interrupções.
- Filtros Avançados: Sistema de busca otimizado para localizar e organizar docentes com base em critérios específicos.

### **Gestão de Cursos**

- Cadastro e Gerenciamento Simplificado: Interface intuitiva para criação, edição e exclusão de cursos.
- Configuração de Datas: Defina com precisão as datas de início, término e intervalos.
- Gestão de Carga Horária: Ferramentas inteligentes para acompanhar e ajustar a duração e o cronograma de cada curso.

---
   
