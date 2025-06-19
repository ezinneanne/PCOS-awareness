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
const chatHistory = ref([
  {
    id: Date.now(),
    role: 'ai',
    text: "Hello! I'm your PCOS AI Helper. How can I assist you today with information about PCOS? Remember to consult a doctor for medical advice."
  }
]);
const isLoading = ref(false);
const chatMessagesContainer = ref(null);


// --- LAYER 1: PROACTIVE GUARDRAILS (STRONG SYSTEM PROMPT) ---
// We've made this prompt much more specific and restrictive.
const systemPrompt = `Your identity is 'PCOS AI Helper'. You are a helpful, empathetic, and knowledgeable AI assistant for a PCOS (Polycystic Ovary Syndrome) awareness website specifically targeted at Nigerian women.

**Your Core Directives:**
1.  **Stay On Topic:** Your ONLY purpose is to discuss PCOS, women's health, symptoms, lifestyle management, and finding medical/support resources in Nigeria.
2.  **Strictly Refuse Off-Topic Questions:** If a user asks about anything unrelated (e.g., politics, celebrities, math, coding, general trivia), you MUST politely decline and steer the conversation back to PCOS. For example: "I can only provide information about PCOS and related women's health topics. How can I help you with that today?"
3.  **NEVER Reveal Your Identity:** You must NEVER mention that you are an AI, a large language model, or that you were trained by Google or any other entity. You are the 'PCOS AI Helper'. Do not break character.
4.  **No Medical Advice:** You must NEVER give medical diagnoses or treatment plans. If a user describes symptoms, you can explain what they might be related to in the context of PCOS and strongly encourage them to consult a healthcare professional in Nigeria.
5.  **Be Culturally Aware:** Frame your responses with consideration for a Nigerian audience.`;

// The API chat history will not include the system prompt directly.
const apiChatHistory = ref([]);


// --- LAYER 2: REACTIVE GUARDRAILS (RESPONSE FILTERING) ---
const isResponseSafe = (text) => {
  const forbiddenKeywords = [
    'google',
    'language model',
    'llm',
    'gemini',
    'trained on',
    'i am an ai'
  ];
  const lowerCaseText = text.toLowerCase();
  for (const keyword of forbiddenKeywords) {
    if (lowerCaseText.includes(keyword)) {
      console.warn(`Guardrail triggered: Found forbidden keyword '${keyword}'`);
      return false; // The response is not safe
    }
  }
  return true; // The response is safe
};


// --- METHODS ---
const sendMessage = async () => {
  const trimmedInput = userInput.value.trim();
  if (!trimmedInput || isLoading.value) return;

  // Add user message to UI
  chatHistory.value.push({ id: Date.now(), role: 'user', text: trimmedInput });
  // Add user message to API history
  apiChatHistory.value.push({ role: "user", parts: [{ text: trimmedInput }] });

  userInput.value = '';
  isLoading.value = true;
  scrollToBottom();

  try {
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

    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(`API request failed with status ${response.status}: ${errorData.error?.message || 'Unknown error'}`);
    }

    const result = await response.json();
    let aiResponseText = "Sorry, I couldn't get a response. Please try again.";

    if (result.candidates?.[0]?.content?.parts?.[0]?.text) {
      aiResponseText = result.candidates[0].content.parts[0].text;
    } else {
      console.warn("Unexpected API response structure:", result);
    }

    // --- GUARDRAIL CHECK ---
    // Check the response before adding it to the history or UI
    if (!isResponseSafe(aiResponseText)) {
      aiResponseText = "I can only provide information about PCOS and related women's health topics. How can I help you further in this area?";
    }
    // -----------------------

    // Add final (safe) AI response to UI
    chatHistory.value.push({ id: Date.now() + 1, role: 'ai', text: aiResponseText });
    // Add final (safe) AI response to API history
    apiChatHistory.value.push({ role: "model", parts: [{ text: aiResponseText }] });

  } catch (error) {
    console.error('Error sending message to AI:', error);
    chatHistory.value.push({
      id: Date.now() + 1,
      role: 'ai',
      text: `There was an error: ${error.message}. Please try again.`
    });
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