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
src/
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
└── utils/  # Funções utilitárias
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

- Autenticação com validação de campos.
- Design moderno e responsivo.

### **Dashboard**

- Gráficos dinâmicos representando dados de desempenho e metas.
- Calendário interativo para gestão de eventos e datas importantes.
- Indicadores intuitivos para acompanhar o progresso dos cursos.

### **Gestão de Docentes**

- Listagem de professores com suas respectivas cargas horárias.
- Edição e remoção de docentes em tempo real.
- Filtros avançados para busca e organização.

### **Gestão de Cursos**

- Cadastro e gerenciamento de cursos.
- Configuração de datas de início e término.
- Ferramentas para controlar a carga horária de cada curso.

---

## **Contribuindo**

Contribuições são bem-vindas!

1. Faça um fork do projeto.
2. Crie uma branch para sua feature ou correção (`git checkout -b feature/nova-feature`).
3. Faça o commit das suas mudanças (`git commit -m 'Adicionei nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/nova-feature`).
5. Abra um pull request.

---

## **Licença**

Este projeto está licenciado sob a [MIT License](./LICENSE).
