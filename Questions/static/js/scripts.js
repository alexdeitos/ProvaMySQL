  const enviarRespostasBtn = document.getElementById('enviar-respostas');
  enviarRespostasBtn.addEventListener('click', validarRespostas);

  const limparRespostasBtn = document.getElementById('limpar-respostas');
  limparRespostasBtn.addEventListener('click', limparRespostas);

  function validarRespostas(event) {
    event.preventDefault();

    let perguntasCorretas = 0;
    const perguntasRespondidas = new Set();

    const respostasMarcadas = document.querySelectorAll('input[type="checkbox"]:checked');
    respostasMarcadas.forEach(resposta => {
      const perguntaId = resposta.name;
      if (!perguntasRespondidas.has(perguntaId)) {
        perguntasRespondidas.add(perguntaId);

        const respostaLabel = document.getElementById(`resposta-label-${resposta.name}-${resposta.value}`);
        respostaLabel.style.color = 'green';

        if (respostaLabel.classList.contains('correta')) {
          perguntasCorretas += 1;
        }
      }
    });

    alert(`Você acertou ${perguntasCorretas} de um total de ${perguntasRespondidas.size} perguntas.`);

  }

  function limparRespostas(event) {
    const respostas = document.querySelectorAll('input[type="checkbox"]');
    respostas.forEach(resposta => {
      resposta.checked = false;
      const respostaLabel = document.getElementById(`resposta-label-${resposta.name}-${resposta.value}`);
      respostaLabel.style.color = '';
    });
  }

