# Evertale Manager

Organizador independente de coleção para **Evertale**, em português.

## Funcionalidades
- Cadastro e edição de personagens: nível, limite, elemento, raridade, despertares e arma equipada.
- Inventário de armas com nome, tipo, nível, habilidade passiva e condição de ativação.
- Inventário de materiais e quantidades.
- Calculadora de poções de limite SSR de 80 a 200 com custos ajustáveis.
- Montador de batalhões de oito integrantes, quatro iniciais e quatro reforços.
- Importação e exportação do inventário em JSON.

## Como usar
Abra `index.html` no navegador ou ative **GitHub Pages** em **Settings → Pages → Deploy from a branch → main → /(root)**.

A interface salva os dados em `localStorage` do navegador. Não é necessário instalar dependências.

## Importante
Esta primeira versão **não** acessa dados da conta de Evertale e **não** usa uma API oficial. O catálogo incluído é uma lista inicial, baseada nas informações informadas pelo usuário, e pode conter níveis ou versões que precisam ser corrigidos. Confirme cada habilidade e os custos diretamente no jogo. Os custos de poções são valores de referência configuráveis.

O backup em JSON permite transferir informações para outro dispositivo e protege contra perda de dados do navegador. Não envie backups contendo informações pessoais a fontes não confiáveis.

## Próximas melhorias
- Armazenamento em PostgreSQL (Neon) com autenticação.
- Biblioteca de habilidades e recomendações de armas baseadas em suas passivas.
- Upload e leitura assistida de capturas de tela.
- Filtros avançados por status e sinergia.
- Testes automatizados e migração futura para Next.js.

Este é um projeto de fãs independente, sem afiliação com a ZigZaGame.
