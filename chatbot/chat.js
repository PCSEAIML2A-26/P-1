function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    var chatMessages = document.getElementById("chat-messages");

    // Add user message to the chat
    chatMessages.innerHTML += `<div class="user-message">${userInput}</div>`;

    // You can replace the following line with your chatbot logic to get a response
    var chatbotResponse = "This is a sample response from the chatbot.";

    // Add chatbot response to the chat
    chatMessages.innerHTML += `<div class="chatbot-message">${chatbotResponse}</div>`;

    // Clear the user input
    document.getElementById("user-input").value = "";

    // Scroll to the bottom of the chat container
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
