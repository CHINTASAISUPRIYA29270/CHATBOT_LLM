async function sendMessage() {

    const input = document.getElementById("user-input");

    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    // Show user message
    chatBox.innerHTML += `
        <div class="message user-message">
            ${message}
        </div>
    `;

    // Clear input
    input.value = "";

    // Send message to Python Flask
    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })

    });

    const data = await response.json();

    // Show bot response
    chatBox.innerHTML += `
        <div class="message bot-message">
            ${data.response}
        </div>
    `;

    // Scroll to latest message
    chatBox.scrollTop = chatBox.scrollHeight;
}


function handleKeyPress(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

}