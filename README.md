# Resumo do Projeto: MQTT para Monitoramento de Linhas de Produção em Redes Industriais

## Especificação do Projeto:
O projeto visa desenvolver uma aplicação para monitoramento de uma linha de produção, utilizando o protocolo MQTT. As principais funcionalidades incluem o controle da temperatura da máquina de processamento da matéria-prima, a monitorização da velocidade de processamento e o gerenciamento do estoque de matéria-prima. A comunicação entre os componentes é realizada por meio do protocolo MQTT, enquanto a lógica de controle é implementada em Python.

## Requisitos Funcionais:
1. **Monitoramento da entrada de matéria-prima:**
   - Adição de volumes (500g, 1kg, 5kg) ao processo, enviando mensagens MQTT para o servidor.
   - Detecção de diferentes quantidades de entrada de matéria-prima.
   
2. **Controle da temperatura:**
   - Sensores monitoram a temperatura da máquina, enviando dados ao servidor.
   - Ajuste dinâmico da velocidade de produção para redução da temperatura.
   - Bloqueio da entrada de matéria-prima em casos de alta temperatura.
   
3. **Controle da velocidade de processamento:**
   - Ajuste dinâmico da velocidade com base na temperatura e lógica definida.
   - Redução de velocidade em caso de alta temperatura.
   
4. **Relatório de estoque:**
   - Geração de relatórios contendo a quantidade de matéria-prima no estoque após cada operação.
   
5. **Comunicação MQTT:**
   - Estabelecimento de comunicação assíncrona entre clientes e servidor.

## Requisitos Não Funcionais:
1. **Desempenho:**
   - Tempo de resposta do sistema para ajuste de velocidade e bloqueio de entrada deve ser rápido.
   
2. **Confiabilidade:**
   - O sistema deve operar de forma confiável, mesmo em condições extremas de temperatura.
   
3. **Segurança:**
   - Implementação de mecanismos para evitar falhas de segurança no controle de entrada de matéria-prima.
   
4. **Escalabilidade:**
   - O sistema deve ser escalável para lidar com diferentes volumes de produção.
   
5. **Usabilidade:**
   - Interface de usuário intuitiva para monitoramento e ajuste de parâmetros.

## Diagrama de Blocos:
1. **Clientes (Adição de volumes, Monitoramento de temperatura):**
   - Enviam mensagens MQTT sobre a entrada de matéria-prima e a leitura do sensor de temperatura para o servidor.
   
2. **Servidor:**
   - Recebe mensagens MQTT dos clientes.
   - Controla o estoque de matéria-prima.
   - Monitora a temperatura e ajusta a velocidade de produção.
   - Gera relatórios de estoque.

3. **Código em Python:**
   - Aplicativo de adição de volumes: Publica mensagens MQTT sobre a entrada de matéria-prima com diferentes volumes.
   - Aplicativo do servidor: Recebe mensagens MQTT, controla estoque, monitora temperatura e ajusta velocidade.
   - Aplicativo de leitura de temperatura: Publica mensagens MQTT simulando a leitura de temperatura.

## Observações:
- O projeto utiliza o protocolo MQTT para comunicação assíncrona entre os componentes.
- O servidor toma decisões com base nas informações recebidas, ajustando dinamicamente a produção.
- O código em Python implementa a lógica de controle e a comunicação MQTT nos diferentes componentes do sistema.

# Planejamento do Projeto: Monitoramento de Linha de Produção com MQTT

## Divisão de Tarefas

### Análise e Definição de Requisitos
- Identificar e detalhar requisitos funcionais e não funcionais.
- Especificar detalhes do protocolo MQTT a ser utilizado.
- Definir a lógica de controle e parâmetros de ajuste.

### Projeto de Arquitetura
- Criar diagrama de blocos atualizado, incorporando requisitos e especificações.
- Design da interface do usuário para monitoramento e ajuste de parâmetros.
- Especificação técnica para implementação em Python.

### Desenvolvimento do Cliente (Adição de Volumes e Monitoramento de Temperatura)
- Implementar lógica de adição de volumes e envio de mensagens MQTT.
- Desenvolver leitura do sensor de temperatura e envio de dados MQTT.

### Desenvolvimento do Servidor
- Implementar lógica de recebimento e processamento de mensagens MQTT.
- Controle de estoque e geração de relatórios.
- Lógica de ajuste dinâmico de velocidade baseada na temperatura.

### Desenvolvimento do Aplicativo de Leitura de Temperatura
- Simular leitura de temperatura e enviar dados MQTT.
- Integrar com lógica de controle de velocidade no servidor.

### Testes Unitários
- Testar cada componente individualmente.
- Verificar a comunicação MQTT entre clientes e servidor.
- Validar lógica de controle e ajuste dinâmico de velocidade.

### Integração e Testes do Sistema
- Realizar testes de integração entre os componentes.
- Simular cenários completos de entrada de matéria-prima, monitoramento de temperatura e ajuste de produção.
- Identificar e corrigir possíveis problemas de integração.

### Implementação de Recursos Adicionais
- Reforçar segurança na comunicação MQTT.
- Implementar mecanismos de escalabilidade, se necessário.
- Aprimorar usabilidade da interface do usuário.

### Documentação
- Preparar documentação técnica.
- Criar manuais de usuário e administrador.
- Descrever o processo de instalação e configuração.

## Cronograma/Backlog

- **Semana 1-2:** Análise e Definição de Requisitos
- **Semana 3-4:** Projeto de Arquitetura
- **Semana 5-6:** Desenvolvimento do Cliente (Adição de Volumes e Monitoramento de Temperatura)
- **Semana 7-8:** Desenvolvimento do Servidor
- **Semana 9-10:** Desenvolvimento do Aplicativo de Leitura de Temperatura
- **Semana 11:** Testes Unitários
- **Semana 12:** Integração e Testes do Sistema
- **Semana 13-14:** Implementação de Recursos Adicionais
- **Semana 15:** Documentação
- **Semana 16:** Revisão Final e Entrega
