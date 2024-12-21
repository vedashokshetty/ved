const input = document.querySelector('input');
const btn = document.querySelector('button');
const dictionary = document.querySelector('.dictionary-app');

// Base URL for the dictionary API
const API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/";

async function dictionaryFn(word) {
    try {
        const res = await fetch(`${API_URL}${word}`);
        if (!res.ok) {
            throw new Error('Word not found');
        }
        const data = await res.json();
        return data[0];
    } catch (error) {
        console.error('Error fetching the word:', error);
        dictionary.innerHTML = `<p class="error">Error: ${error.message}</p>`;
    }
}

btn.addEventListener('click', fetchandCreate);

async function fetchandCreate() {
    const word = input.value.trim();
    if (!word) {
        dictionary.innerHTML = `<p class="error">Please enter a word!</p>`;
        return;
    }
    const data = await dictionaryFn(word);
    if (!data) return; // If the fetch failed or the word was not found

    console.log(data);

    // Extract parts of speech
    let partOfSpeech = data.meanings.map((meaning) => meaning.partOfSpeech).join(', ');

    // Generate HTML
    dictionary.innerHTML = `
    <div class="card">
        <div class="property">
            <span>Word: </span>
            <span>${data.word}</span>
        </div>
        <div class="property">
            <span>Pronunciation: </span>
            <span>${data.phonetic || 'N/A'}</span>
        </div>
        <div class="property">
            <span>Audio: </span>
            <span>
                ${data.phonetics[0]?.audio 
                    ? `<audio controls src="${data.phonetics[0].audio}"></audio>` 
                    : 'No audio available'}
            </span>
        </div>
        <div class="property">
            <span>Definition: </span>
            <span>1.  ${data.meanings[0]?.definitions[0]?.definition || 'No definition available'}</span>
             <span>2.  ${data.meanings[1]?.definitions[1]?.definition || 'No definition available'}</span>
        </div>
        <div class="property">
            <span>Example: </span>
            <span>${data.meanings[0]?.definitions[0]?.example || 'No example available'}</span>
        </div>
        <div class="property">
            <span>Parts of Speech: </span>
            <span>${partOfSpeech}</span>
        </div>
    </div>`;
}
