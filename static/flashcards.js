const container = document.getElementById('flashcard-container');
const addBtn = document.getElementById('create-flashcard');


addBtn.addEventListener('click', () => {
    const question = document.getElementById('question-input').value.trim();
    const answer = document.getElementById('answer-input').value.trim();
    if (!question || !answer) {
        alert("Please enter both question and answer!");
        return;
    }


    const card = document.createElement('div');
    card.className = 'flashcard';
    card.innerHTML = `
        <div class="front">${question}</div>
        <div class="back">${answer}</div>
    `;


    card.addEventListener('click', () => {
        card.classList.toggle('flipped');
    });


    container.appendChild(card);


    document.getElementById('question-input').value = '';
    document.getElementById('answer-input').value = '';
});

