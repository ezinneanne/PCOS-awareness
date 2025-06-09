<template>
  <section class="font container mx-auto max-w-3xl p-4 bg-white shadow-lg rounded-lg mt-6 mb-6">
    <h2 class="text-3xl font-semibold text-pink-700 mb-4">Chat with PCOS AI Helper</h2>
    <div 
      ref="chatMessagesContainer"
      class="h-96 overflow-y-auto bg-pink-50 p-4 rounded-lg border border-pink-200 mb-4 space-y-4 chat-messages"
    >
      <div 
        v-for="message in chatHistory" 
        :key="message.id"
        class="flex"
        :class="message.role === 'ai' ? 'justify-start' : 'justify-end'"
      >
        <div 
          :class="[
            'inline-block px-4 py-2 rounded-lg text-sm max-w-[80%]',
            message.role === 'ai' ? 'bg-white text-gray-800 border border-pink-200' : 'bg-pink-600 text-white'
          ]"
        >
          {{ message.text }}
        </div>
      </div>
       <div v-if="isLoading" class="flex justify-start">
          <div class="inline-block px-4 py-2 rounded-lg text-sm bg-white text-gray-800 border border-pink-200">
             <div class="flex items-center">
                <div class="loader mr-2"></div>
                <span>AI is typing...</span>
             </div>
          </div>
       </div>
    </div>

    <form @submit.prevent="sendMessage" class="flex space-x-2">
      <input 
        v-model="userInput"
        type="text"
        placeholder="Type your message..."
        class="flex-1 px-4 py-2 rounded-lg border border-pink-300 focus:ring-2 focus:ring-pink-400 focus:outline-none"
        :disabled="isLoading"
      />
      <button 
        type="submit"
        class="bg-pink-600 hover:bg-pink-500 text-white px-4 py-2 rounded-lg disabled:opacity-50"
        :disabled="isLoading || !userInput.trim()"
      >
        Send
      </button>
    </form>
  </section>
</template>

<script setup>
import { ref, nextTick, onMounted } from 'vue';

// --- STATE ---
const userInput = ref('');
const chatHistory = ref([ // For UI display only
  {
    id: Date.now(),
    role: 'ai',
    text: "Hello! I'm your PCOS AI Helper. How can I assist you today with information about PCOS? Remember to consult a doctor for medical advice."
  }
]);
const isLoading = ref(false);
const chatMessagesContainer = ref(null);

// --- API CONFIGURATION ---
// Storing the system prompt separately
const systemPrompt = "You are a helpful, empathetic, and knowledgeable AI assistant for a PCOS (Polycystic Ovary Syndrome) awareness website specifically targeted at Nigerian women. Your goal is to provide accurate information about PCOS, answer questions clearly, and gently encourage users to consult with healthcare professionals in Nigeria for diagnosis and treatment. Be mindful of potential cultural sensitivities and local context. Do not provide medical diagnoses or treatment plans. If asked for medical advice, politely decline and reiterate the importance of seeing a doctor. Keep responses concise and easy to understand. You can mention common symptoms, lifestyle adjustments, and the importance of medical consultation. Refer to 'Nigerian women' or 'women in Nigeria' when relevant and appropriate to personalize the interaction.";

// API history should start empty and only contain user/model turns
const apiChatHistory = ref([]);

// --- METHODS ---
const sendMessage = async () => {
  const trimmedInput = userInput.value.trim();
  if (!trimmedInput || isLoading.value) return;

  // 1. Update UI and API History immediately
  chatHistory.value.push({
    id: Date.now(),
    role: 'user',
    text: trimmedInput
  });

  apiChatHistory.value.push({
    role: "user",
    parts: [{ text: trimmedInput }]
  });

  userInput.value = '';
  isLoading.value = true;
  scrollToBottom();

  try {
    // 2. Prepare API request
    const apiKey = import.meta.env.VITE_GEMINI_API_KEY;
    const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;

    const payload = {
      contents: apiChatHistory.value,
      systemInstruction: {
        parts: [{ text: systemPrompt }]
      },
      generationConfig: {
        temperature: 0.7,
        topP: 0.9,
        topK: 40,
        candidateCount: 1
      }
    };

    // 3. Make the API call
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const errorData = await response.json();
      console.error("API Error:", errorData);
      throw new Error(errorData.error?.message || 'An unknown API error occurred');
    }

    const result = await response.json();
    let aiResponseText = "Sorry, I couldn't get a response. Please try again.";

    if (result.candidates?.[0]?.content?.parts?.[0]?.text) {
      aiResponseText = result.candidates[0].content.parts[0].text;
    } else {
      console.warn("Unexpected API response structure:", result);
    }

    // 4. Update UI and API History with the AI's response
    chatHistory.value.push({
      id: Date.now() + 1,
      role: 'ai',
      text: aiResponseText
    });

    apiChatHistory.value.push({
      role: "model",
      parts: [{ text: aiResponseText }]
    });

  } catch (error) {
    console.error('Error sending message to AI:', error);
    // Display error in the chat UI
    chatHistory.value.push({
      id: Date.now() + 1,
      role: 'ai',
      text: `There was an error: ${error.message}. Please try again.`
    });
    // IMPORTANT: Remove the last user message from the API history to prevent a broken conversation
    apiChatHistory.value.pop();
  } finally {
    isLoading.value = false;
    scrollToBottom();
  }
};

const scrollToBottom = () => {
  nextTick(() => {
    if (chatMessagesContainer.value) {
      chatMessagesContainer.value.scrollTop = chatMessagesContainer.value.scrollHeight;
    }
  });
};

onMounted(() => {
  scrollToBottom();
});
</script>

<style scoped>

.font {
  font-family: 'Kiwi Maru', serif;
}

/* Custom scrollbar for chat */
.chat-messages::-webkit-scrollbar {
    width: 8px;
}
.chat-messages::-webkit-scrollbar-track {
    background: #ffeef2;
}
.chat-messages::-webkit-scrollbar-thumb {
    background: #ffc0cb;
    border-radius: 10px;
}
.chat-messages::-webkit-scrollbar-thumb:hover {
    background: #ffb3c1;
}

/* Loading spinner */
.loader {
    border: 3px solid #fde7ea;
    border-top: 3px solid #ff8fab;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    animation: spin 1s linear infinite;
}
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
</style>