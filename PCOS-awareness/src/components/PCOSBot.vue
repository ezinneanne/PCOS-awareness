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
import axios from 'axios';

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

// --- METHODS ---
const sendMessage = async () => {
  const trimmedInput = userInput.value.trim();
  if (!trimmedInput || isLoading.value) return;

  chatHistory.value.push({
    id: Date.now(),
    role: 'user',
    text: trimmedInput
  });

  userInput.value = '';
  isLoading.value = true;
  scrollToBottom();

  try {
    const response = await axios.post('/api/chat/query', { message: trimmedInput });

    const aiResponseText = response.data.response || "Sorry, I couldn't get a response. Please try again.";

    chatHistory.value.push({
      id: Date.now() + 1,
      role: 'ai',
      text: aiResponseText
    });

  } catch (error) {
    console.error('Error contacting backend:', error);
    chatHistory.value.push({
      id: Date.now() + 1,
      role: 'ai',
      text: `There was an error: ${error.message}. Please try again later.`
    });
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

//i have no acne or irregular period does that mean no pcos
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