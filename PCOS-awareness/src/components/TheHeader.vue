<template>
  <div class="font">

    <!-- Hero Section -->
    <section class="bg-pink-50 py-16">
      <div class="container-standard flex flex-col md:flex-row items-center gap-12">
        
        <!-- Text Side -->
        <div class="md:w-1/2 text-center md:text-left">
          <h1 class="text-4xl font-bold text-gray-800 mb-4">Let’s Talk About PCOS</h1>
          <p class="text-lg text-gray-600 mb-6">
            Speak with our AI assistant for early insights and support around Polycystic Ovary Syndrome. It’s fast, confidential, and supportive.
          </p>
          <router-link to="/pcosbot">
            <button class="bg-pink-600 hover:bg-pink-300 text-white px-6 py-3 rounded-full transition">
              Start Chatting
            </button>
          </router-link>
        </div>

        <!-- Image Side -->
        <div class="md:w-1/2">
          <img src="../assets/images.jpeg" alt="Female Reproductive System" class="rounded-lg shadow-md w-full max-w-md mx-auto md:mx-0" />
        </div>

      </div>
    </section>
  </div>
</template>

<script setup>

</script>

<style scoped>
.font {
  font-family: 'Kiwi Maru', serif;
}

.container-standard {
  max-width: 80rem;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1rem;
  padding-right: 1rem;
}

@media (min-width: 768px) {
  .container-standard {
    padding-left: 2rem;
    padding-right: 2rem;
  }
}

</style>
