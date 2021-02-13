<h1><strong>webscraping_api_test</strong></h1>
<p>Teste de implementa&ccedil;&atilde;o com Selenium, BS4, MongoDB e Flask.&nbsp;</p>
<p>O teste consiste em realizar extra&ccedil;&atilde;o de dados do Stackoverflow capturando informa&ccedil;&otilde;es do post, respostas e coment&aacute;rios com Selenium e Beautiful Soup 4. Em seguida, armazenar os dados no Mongodb e deixar os dados dispon&iacute;veis acess&iacute;veis a um end-poind de API atrav&eacute;s do Flask.&nbsp;</p>
<p>&nbsp;</p>
<p>Veja <a title="Demonstra&ccedil;&atilde;o" href="https://drive.google.com/drive/folders/1Z-l4vQEHAVA5WAgNf1pAjJSLxTiJOyhK?usp=sharing" target="_blank" rel="noopener">aqui</a> algumas demos.&nbsp;</p>
<p>&nbsp;</p>
<h2>Requisitos</h2>
<ul>
<li>Ap&oacute;s baixar o reposit&oacute;rio, crie um ambiente virtual <strong>VENV dentro a pasta ra&iacute;z do projeto</strong></li>
<li>Instala&ccedil;&atilde;o de <strong>requirements.txt</strong> via pip</li>
<li>Configura&ccedil;&atilde;o de diret&oacute;rio de pasta ra&iacute;z e de webdriver em <strong>config&gt;config.json</strong></li>
<li>Instale o <a href="https://www.mozilla.org/pt-BR/firefox/new/" target="_blank" rel="noopener">FIREFOX</a> ou certifique-se que o browser esteja atualizado</li>
<li>Instale o <a href="https://www.mongodb.com/try/download/community" target="_blank" rel="noopener">Mongodb Community Server</a> e <a href="https://www.mongodb.com/try/download/compass" target="_blank" rel="noopener">Mongodb Compass</a></li>
<li>Intale o <a href="https://www.postman.com/downloads/" target="_blank" rel="noopener">Postman</a> (opcional) para fazer os requests</li>
</ul>
<p>&nbsp;</p>
<h2>Execu&ccedil;&atilde;o</h2>
<ul>
<li><strong>1_start_webscraping.bat -&nbsp;</strong>Executa a extra&ccedil;&atilde;o de dados</li>
<li><strong>2_start_flask.bat -&nbsp;</strong>Inicializa o Flask</li>
<li>Requests no postman:
<ul>
<li><code>http://localhost:5000/table_stack_posts</code></li>
<li><code>http://localhost:5000/table_stack_answers</code></li>
<li><code>http://localhost:5000/table_stack_comments</code></li>
<li><code>http://localhost:5000/search_name?autor=digite%algum%nome</code></li>
</ul>
</li>
</ul>
<h2>Observa&ccedil;&otilde;es</h2>
<ul>
<li>Todos os testes foram feitos em windows</li>
<li>Op&ccedil;&atilde;o de solucionar captchas est&aacute; pronto para ser habilitado (mas precisa da sua chave de acesso em config&gt;config.json)</li>
<li>Todo c&oacute;digo est&aacute; em ingl&ecirc;s. A id&eacute;ia &eacute; de futuramente deixar todo o readme em ingl&ecirc;s tamb&eacute;m.</li>
<li>O firefox n&atilde;o est&aacute; em Headlless apenas por motivos de apresenta&ccedil;&atilde;o</li>
</ul>
<p>&nbsp;</p>
<h2>Features</h2>
<ul>
  <li><s>Fun&ccedil;&otilde;es auxiliares</s>></li>
  <li><s>Configura&ccedil;&otilde;es separadas em um arquivo Json</s>></li>
<li><s>Solucionador de captcha dispon&iacute;vel em fun&ccedil;&atilde;o</s></li>
<li>English Version of readme</li>
<li>Pequenas melhorias na documenta&ccedil;&atilde;o em c&oacute;digo</li>
<li>Tratamento de erros no web-scraping</li>
<li>Tratamento de erros no parser</li>
<li>Melhorias nos Logs</li>
<li>Captura de mais informa&ccedil;&otilde;es</li>
</ul>
<p>&nbsp;</p>
<p>Como est&aacute; organizado o banco de dados e as informa&ccedil;&otilde;es dispon&iacute;veis:&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
