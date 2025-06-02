<template>
  <div>
    <!-- Navbar -->
    <nav class="bg-white shadow-md px-4 py-3 flex justify-between items-center">
      <!-- Logo -->
      <div class="text-xl font-bold text-pink-600">PCOS Awareness</div>

      <!-- Middle Links -->
      <div class="hidden md:flex space-x-6 text-gray-700">
        <a href="#hospitals" class="hover:text-pink-600 font-medium">Hospitals</a>
        <a href="#nonprofits" class="hover:text-pink-600 font-medium">Non-profit Organizations</a>
        <a href="#about" class="hover:text-pink-600 font-medium">About PCOS</a>
      </div>

      <!-- Chat Button -->
      <div>
        <button class="bg-pink-500 hover:bg-pink-600 text-white px-4 py-2 rounded-full transition">
          Chat with AI Bot
        </button>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="bg-pink-50 py-12 px-4 md:px-12 flex flex-col-reverse md:flex-row items-center">
      <!-- Text Side -->
      <div class="md:w-1/2 text-center md:text-left">
        <h1 class="text-3xl md:text-4xl font-bold text-gray-800 mb-4">Let’s Talk About PCOS</h1>
        <p class="text-lg text-gray-600 mb-6">
          Speak with our AI assistant for early insights and support around Polycystic Ovary Syndrome. It’s fast, confidential, and supportive.
        </p>
        <button class="bg-pink-500 hover:bg-pink-600 text-white px-6 py-3 rounded-full transition">
          Start Chatting
        </button>
      </div>

      <!-- Image Side -->
      <div class="md:w-1/2 mb-8 md:mb-0">
        <img src="https://via.placeholder.com/400x300?text=Nigerian+Women+Illustration" alt="PCOS Awareness" class="rounded-lg shadow-md w-full" />
      </div>
    </section>
  </div>
</template>

<script setup>
// No script needed unless adding interactivity
</script>

<style scoped>
/* Optional additional styles */
</style>
