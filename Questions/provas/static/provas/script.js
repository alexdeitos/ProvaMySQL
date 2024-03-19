document.addEventListener('DOMContentLoaded', function () {
    const scrollToBottomBtn = document.getElementById('scroll-to-bottom');
    scrollToBottomBtn.addEventListener('click', () => {
        window.scrollTo(0, document.body.scrollHeight);
    });
    const scrollToTopBtn = document.getElementById('scroll-to-top');
    scrollToTopBtn.addEventListener('click', () => {
        window.scrollTo(0, 0);
    });
    const UpdateFuture = document.getElementById('future');
    UpdateFuture.addEventListener('click', () => {
        window.location.reload();
    });

    let perguntasCorretas = 0;
    let perguntasIncorretas = 0;
    let perguntasNaoRespondidas = 0;

    const enviarRespostasBtn = document.getElementById('enviar-respostas');
    enviarRespostasBtn.addEventListener('click', validarRespostas);

    const limparRespostasBtn = document.getElementById('limpar-respostas');
    limparRespostasBtn.addEventListener('click', limparRespostas);

    const marcarCorretasBtn = document.getElementById('marcar-corretas');
    marcarCorretasBtn.addEventListener('click', marcarRespostasCorretas);

    function marcarRespostasCorretas() {
        const respostas = document.querySelectorAll('input[type="checkbox"]');
        respostas.forEach(resposta => {
            const perguntaId = resposta.name;
            const respostaLabel = document.getElementById(`resposta-label-${perguntaId}-${resposta.value}`);
            if (resposta.getAttribute('data-correta')) {
                resposta.checked = true;
                respostaLabel.style.color = 'blue';
            }
        });
    }

    function limparRespostas() {
        perguntasCorretas = 0;
        perguntasIncorretas = 0;
        perguntasNaoRespondidas = 0;

        const respostas = document.querySelectorAll('input[type="checkbox"]');
        respostas.forEach(resposta => {
            resposta.checked = false;
            const perguntaId = resposta.name;
            const respostaLabel = document.getElementById(`resposta-label-${perguntaId}-${resposta.value}`);
            respostaLabel.style.color = '';
        });
    }

    function validarRespostas() {
        perguntasNaoRespondidas = 0;
        perguntasCorretas = 0;
        perguntasIncorretas = 0;

        const totalPerguntas = document.querySelectorAll('.pergunta').length;
        const respostasMarcadas = document.querySelectorAll('input[type="checkbox"]:checked');

        respostasMarcadas.forEach(resposta => {
            const perguntaId = resposta.name;
            const respostaLabel = document.getElementById(`resposta-label-${perguntaId}-${resposta.value}`);

            if (resposta.getAttribute('data-correta')) {
                respostaLabel.style.color = 'blue'; // Marca a resposta como correta (azul)
                perguntasCorretas++;
            } else {
                respostaLabel.style.color = 'red'; // Marca a resposta como incorreta (vermelha)
                perguntasIncorretas++;
                const respostasDaPergunta = document.querySelectorAll(`input[name="${perguntaId}"]`);
                respostasDaPergunta.forEach(respostaCorreta => {
                    if (respostaCorreta.getAttribute('data-correta')) {
                        const respostaCorretaLabel = document.getElementById(`resposta-label-${perguntaId}-${respostaCorreta.value}`);
                        respostaCorretaLabel.style.color = 'blue'; // Marca a resposta correta como azul
                    }
                });
            }
        });

        perguntasNaoRespondidas = totalPerguntas - respostasMarcadas.length;
        const mensagem = `Você respondeu corretamente ${perguntasCorretas} pergunta(s).\n`
            + `Você respondeu incorretamente ${perguntasIncorretas} pergunta(s).\n`
            + `Você não respondeu ${perguntasNaoRespondidas} pergunta(s).`;
        alert(mensagem);

        // Marca as respostas corretas após o usuário ter visto o alerta
        marcarRespostasCorretas();
    }
});