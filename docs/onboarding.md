### Documento de Referência para Futuros Desenvolvedores do Projeto  

#### 1. **Visão Geral do Projeto**  
Este sistema foi desenvolvido para otimizar a alocação de docentes e o gerenciamento de turmas dos cursos de formação inicial e continuada (FIC) do SENAI. Ele integra dados do sistema legado SGSET em um dashboard visual, permitindo:  
- Centralizar informações sobre cursos e docentes.  
- Facilitar a tomada de decisão sobre abertura de turmas com base em critérios de quórum.  
- Gerenciar a alocação e substituição de docentes.  
- Simplificar o planejamento de infraestrutura e materiais.  

#### 2. **Principais Funcionalidades**  
- Dashboard visual para acompanhamento e aprovação de cursos.  
- Sistema para alocação eficiente de docentes.  
- Módulo para gestão de turmas baseado em quórum.  
- Integração com SGSET para sincronização de dados.  

---

#### 3. **Arquitetura e Tecnologias**  

##### Tecnologias Principais:  
- **Backend:** Python, Django Rest Framework, banco de dados SQLite.  
- **Frontend:** Next.js, ShadCN UI, Tailwind CSS.  

##### Arquitetura:  
- O sistema segue o padrão **MVT (Model-View-Template)** no backend.  

##### Decisões Técnicas Importantes:  
- Uso de Docker para simplificar a configuração e replicação do ambiente.  
- Integração direta com SGSET para extração de dados do sistema legado.  

---

#### 4. **Configuração do Ambiente de Desenvolvimento**  

##### Pré-requisitos:  
- Docker instalado.  

##### Passos para Configuração:  
1. Clone o repositório do projeto:  
   ```bash
   git clone https://github.com/Gestao-FIC/ads_projeto_gestao_fic
   cd ads_projeto_gestao_fic
   ```  
2. Inicialize o ambiente com Docker:  
   ```bash
   docker-compose up --build
   ```  
3. Acesse o sistema:  
   - Backend: `http://localhost:8000`  
   - Frontend: `http://localhost:3000`
   - Postgree: `http://localhost:5432`  

##### Dependências Específicas:  
- Docker e Docker Compose.  

##### Arquivos de Configuração:  
- Não há arquivos `.env` para configurar. Todas as configurações estão incluídas no Docker Compose.  

---

#### 5. **Padrões de Codificação e Práticas**  
- **Clareza e Documentação:** Sempre manter o código bem documentado para facilitar a leitura e manutenção.  
- **Conformidade com o Guia de Estilo:** Use boas práticas de desenvolvimento, especialmente para Python (PEP 8) e React.  

##### Partes Complexas do Código:  
- A integração com SGSET pode exigir um entendimento prévio desse sistema interno.  

---

#### 6. **Processos e Práticas de Desenvolvimento**  

##### Controle de Versão:  
- Repositório Git gerenciado em uma organização específica no GitHub.  

##### Revisões de Código:  
- As revisões são realizadas por um **Tech Lead** designado.  

##### Testes Automatizados:  
- Não há testes automatizados atualmente implementados.  

---

#### 7. **Documentação e Recursos Adicionais**  

##### Documentação Existente:  
- Diagramas e manuais estão disponíveis no repositório Git.  

##### Contatos Importantes:  
- **Cainã Antunes (Professor)** – Para dúvidas ou problemas relacionados ao projeto.  

---

#### 8. **Próximos Passos e Funcionalidades Planejadas**  
- Integração entre o sistema de frontend e backend.  
- Melhorias de performance e interatividade do sistema.  
- Incremento na segurança do sistema.  
- Atendimento aos pedidos específicos do cliente.  

---

#### 9. **Dívidas Técnicas e Pontos de Atenção**  
- **Conhecimento prévio do SGSET:** É importante que os novos desenvolvedores compreendam o funcionamento básico do sistema SGSET para lidar com a integração de dados.  
