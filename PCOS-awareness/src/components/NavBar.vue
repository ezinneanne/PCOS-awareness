<template>
    <!-- Navbar -->
    <nav class="bg-white shadow-md px-4 py-3 font">
      <div class="flex justify-between items-center">
        <!-- Logo -->
        <div class="flex items-center text-xl font-bold text-pink-600">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32" aria-hidden="true">
            <circle cx="32" cy="32" r="6" fill="#e91e63"/>
            <path d="M32 10c3 0 5 7 5 10s-2 4-5 4-5-1-5-4 2-10 5-10z" fill="#f8bbd0"/>
            <path d="M32 54c-3 0-5-7-5-10s2-4 5-4 5 1 5 4-2 10-5 10z" fill="#f8bbd0"/>
            <path d="M10 32c0-3 7-5 10-5s4 2 4 5-1 5-4 5-10-2-10-5z" fill="#f8bbd0"/>
            <path d="M54 32c0 3-7 5-10 5s-4-2-4-5 1-5 4-5 10 2 10 5z" fill="#f8bbd0"/>
            <path d="M17 17c2-2 9 2 11 4s1 4-1 6-4 2-6 0-6-9-4-11z" fill="#f8bbd0"/>
            <path d="M47 47c-2 2-9-2-11-4s-1-4 1-6 4-2 6 0 6 9 4 11z" fill="#f8bbd0"/>
            <path d="M47 17c2 2-2 9-4 11s-4 1-6-1-2-4 0-6 9-6 11-4z" fill="#f8bbd0"/>
            <path d="M17 47c-2-2 2-9 4-11s4-1 6 1 2 4 0 6-9 6-11 4z" fill="#f8bbd0"/>
          </svg>
          <span class="ml-2">PCOS Awareness</span>
        </div>

        <!-- Desktop Links -->
        <div class="hidden md:flex space-x-6 text-gray-700 font-bold">
          <router-link to="/" class="hover:text-pink-600">Home</router-link>
          <router-link to="/about" class="hover:text-pink-600">About PCOS</router-link>
          <router-link to="/resources" class="hover:text-pink-600">PCOS Resources</router-link>
        </div>

        <!-- Chat Button -->
        <div class="hidden md:block">
          <router-link to="/pcosbot">
            <button class="bg-pink-600 hover:bg-pink-300 text-white px-4 py-2 rounded-full transition">
              Chat with AI Bot
            </button>
          </router-link>
        </div>

        <!-- Mobile Menu Button -->
        <button @click="toggleMenu" class="md:hidden focus:outline-none">
          <svg v-if="!isOpen" class="w-6 h-6 text-pink-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <svg v-else class="w-6 h-6 text-pink-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Mobile Menu -->
      <transition name="fade">
        <div v-if="isOpen" class="md:hidden mt-4 space-y-4 text-center font-bold">
          <router-link to="/" class="block text-gray-700 hover:text-pink-600">Home</router-link>
          <router-link to="/about" class="block text-gray-700 hover:text-pink-600">About PCOS</router-link>
          <router-link to="/resources" class="block text-gray-700 hover:text-pink-600">PCOS Resources</router-link>
          <router-link to="/pcosbot">
            <button class="bg-pink-600 hover:bg-pink-300 text-white px-4 py-2 rounded-full transition w-48">
              Chat with AI Bot
            </button>
          </router-link>
        </div>
      </transition>
    </nav>
</template>

<script setup>
  import { ref } from 'vue'

  const isOpen = ref(false)
  const toggleMenu = () => {
    isOpen.value = !isOpen.value
  }
</script>

<style scoped>
.font {
  font-family: 'Kiwi Maru', serif;
}

.fade-enter-active, .fade-leave-active {
  transition: all 0.3s ease;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

</style>