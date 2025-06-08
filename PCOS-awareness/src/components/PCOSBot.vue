<template>
  <section class="font container mx-auto max-w-3xl p-4 bg-white shadow-lg rounded-lg mt-6 mb-6">
    <h2 class="text-3xl font-semibold text-pink-700 mb-4">Chat with PCOS AI Helper</h2>
    <div 
      ref="chatMessagesContainer"
      class="h-96 overflow-y-auto bg-pink-50 p-4 rounded-lg border border-pink-200 mb-4 space-y-3"
    >
      <div 
        v-for="message in chatHistory" 
        :key="message.id"
        :class="message.role === 'ai' ? 'text-left' : 'text-right'"
      >
        <div 
          :class="[
            'inline-block px-4 py-2 rounded-lg text-sm',
            message.role === 'ai' ? 'bg-white text-gray-700 border border-pink-200' : 'bg-pink-600 text-white'
          ]"
        >
          {{ message.text }}
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
        :disabled="isLoading"
      >
        {{ isLoading ? 'Sending...' : 'Send' }}
      </button>
    </form>
  </section>
</template>

<script setup>
import { ref, nextTick, onMounted } from 'vue';

// State
const userInput = ref('');
const chatHistory = ref([
  {
    id: Date.now(),
    role: 'ai',
    text: "Hello! I'm your PCOS AI Helper. How can I assist you today with information about PCOS? Remember to consult a doctor for medical advice."
  }
]);
const isLoading = ref(false);

// API chat history format
const apiChatHistory = ref([
  {
    role: "system",
    parts: [
      {
        text: "You are a helpful, empathetic, and knowledgeable AI assistant for a PCOS (Polycystic Ovary Syndrome) awareness website specifically targeted at Nigerian women. Your goal is to provide accurate information about PCOS, answer questions clearly, and gently encourage users to consult with healthcare professionals in Nigeria for diagnosis and treatment. Be mindful of potential cultural sensitivities and local context. Do not provide medical diagnoses or treatment plans. If asked for medical advice, politely decline and reiterate the importance of seeing a doctor. Keep responses concise and easy to understand. You can mention common symptoms, lifestyle adjustments, and the importance of medical consultation. Refer to 'Nigerian women' or 'women in Nigeria' when relevant and appropriate to personalize the interaction."
      }
    ]
  },
  {
    role: "model",
    parts: [
      {
        text: "Hello! I'm your PCOS AI Helper. How can I assist you today with information about PCOS? Remember to consult a doctor for medical advice."
      }
    ]
  }
]);

// Refs for DOM
const chatMessagesContainer = ref(null);

// Send Message
const sendMessage = async () => {
  const trimmedInput = userInput.value.trim();
  if (!trimmedInput) return;

  // Add user message to UI
  chatHistory.value.push({
    id: Date.now(),
    role: 'user',
    text: trimmedInput
  });

  // Add user message to API history
  apiChatHistory.value.push({
    role: "user",
    parts: [{ text: trimmedInput }]
  });

  userInput.value = '';
  isLoading.value = true;
  scrollToBottom();

  try {
    const apiKey = ""; // Add your API key here if required
    const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;

    const payload = {
      contents: apiChatHistory.value,
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
      console.error("API Error:", errorData);
      throw new Error(`API request failed with status ${response.status}: ${errorData.error?.message || 'Unknown error'}`);
    }

    const result = await response.json();
    let aiResponseText = "Sorry, I couldn't get a response. Please try again.";

    if (
      result.candidates &&
      result.candidates.length > 0 &&
      result.candidates[0].content &&
      result.candidates[0].content.parts &&
      result.candidates[0].content.parts.length > 0
    ) {
      aiResponseText = result.candidates[0].content.parts[0].text;
    } else {
      console.warn("Unexpected API response structure:", result);
    }

    // Add AI response to UI
    chatHistory.value.push({
      id: Date.now() + 1,
      role: 'ai',
      text: aiResponseText
    });

    // Add AI response to API history
    apiChatHistory.value.push({
      role: "model",
      parts: [{ text: aiResponseText }]
    });

  } catch (error) {
    console.error('Error sending message to AI:', error);
    chatHistory.value.push({
      id: Date.now() + 1,
      role: 'ai',
      text: `There was an error: ${error.message}. Please try again.`
    });
    apiChatHistory.value.push({
      role: "model",
      parts: [{ text: `System note: An error occurred in the previous turn: ${error.message}` }]
    });
  } finally {
    isLoading.value = false;
    scrollToBottom();
  }
};

// Auto-scroll to bottom
const scrollToBottom = () => {
  nextTick(() => {
    if (chatMessagesContainer.value) {
      chatMessagesContainer.value.scrollTop = chatMessagesContainer.value.scrollHeight;
    }
  });
};

// On mounted, scroll down to latest message
onMounted(() => {
  scrollToBottom();
});
</script>

<style scoped>

.font {
  font-family: 'Kiwi Maru', serif;
}
.chat-bubble {
            max-width: 70%;
            padding: 10px 15px;
            border-radius: 15px;
            margin-bottom: 10px;
            word-wrap: break-word;
        }
        .user-bubble {
            background-color: #ff8fab; /* Brighter pink for user */
            color: white;
            align-self: flex-end;
            border-bottom-right-radius: 5px;
        }
        .ai-bubble {
            background-color: #ffffff; /* White for AI */
            color: #5c3c47; /* Darker, warm text */
            align-self: flex-start;
            border: 1px solid #ffe4e9; /* Light pink border */
            border-bottom-left-radius: 5px;
        }
        /* Custom scrollbar for chat */
        .chat-messages::-webkit-scrollbar {
            width: 8px;
        }
        .chat-messages::-webkit-scrollbar-track {
            background: #ffeef2; /* Lighter pink track */
            border-radius: 10px;
        }
        .chat-messages::-webkit-scrollbar-thumb {
            background: #ffc0cb; /* Pink scrollbar thumb */
            border-radius: 10px;
        }
        .chat-messages::-webkit-scrollbar-thumb:hover {
            background: #ffb3c1; /* Darker pink thumb on hover */
        }
        /* Loading spinner */
        .loader {
            border: 4px solid #fde7ea; /* Light pink loader base */
            border-top: 4px solid #ff8fab; /* Brighter pink for spinner */
            border-radius: 50%;
            width: 24px;
            height: 24px;
            animation: spin 1s linear infinite;
            margin-right: 8px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
</style>