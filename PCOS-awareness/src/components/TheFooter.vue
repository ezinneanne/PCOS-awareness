<template>
  <footer class="bg-gray-800 text-white font pt-10 px-4">
    <section class="max-w-7xl mx-auto w-full">
      <div class="flex flex-col md:flex-row justify-between gap-10">
        
        <!-- Logo and About -->
        <div class="md:w-1/3">
          <div class="flex items-center gap-2 mb-4 text-2xl font-bold text-pink-600">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
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
            <span class="text-white">PCOS Awareness</span>
          </div>
          <p class="text-white">
            Creating awareness and saving lives through accessible, local resources.
          </p>
        </div>

        <!-- Info Links -->
        <div class="md:w-1/3">
          <h4 class="text-2xl font-bold mb-4 text-white">Info</h4>
          <ul class="space-y-2">
            <li><router-link to="/pcosbot" class="hover:text-gray-400">Chat with our bot</router-link></li>
            <li><router-link to="/about" class="hover:text-gray-400">About PCOS</router-link></li>
            <li><router-link to="/resources" class="hover:text-gray-400">PCOS Resources</router-link></li>
          </ul>
        </div>

        <!-- Newsletter -->
        <div class="md:w-1/3">
          <h4 class="text-2xl font-bold mb-4 text-white">Newsletter</h4>
          <p class="text-white mb-4">
            Subscribe to our newsletter for exclusive guides and updates on PCOS.
          </p>
          <form class="flex flex-col sm:flex-row gap-2">
            <input
              type="email"
              placeholder="Your email"
              required
              class="flex-1 px-4 py-2 rounded-md border border-gray-400 bg-gray-700 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400"
            />
            <button
              type="submit"
              class="bg-gray-800 hover:bg-gray-700 px-4 py-2 rounded-md text-white font-medium"
            >
              <a href="https://medium.com/@ezinneanne/subscribe">Subscribe</a>
            </button>
          </form>
          <div class="flex gap-4 mt-6">
            <a href="https://www.facebook.com/anne.hilary.779" class="hover:text-gray-400" aria-label="Facebook"><i class="fab fa-facebook fa-2x"></i></a>
            <a href="https://www.instagram.com/ezinneanneemilia/" class="hover:text-gray-400" aria-label="Instagram"><i class="fab fa-instagram fa-2x"></i></a>
            <a href="https://twitter.com/ezinne_anne" class="hover:text-gray-400" aria-label="Twitter"><i class="fab fa-twitter fa-2x"></i></a>
          </div>
        </div>
      </div>

      <!-- Divider and Bottom Text -->
      <hr class="border-gray-600 my-4" />

      <div class="text-sm text-gray-400 text-center">
        <p>&copy; {{ new Date().getFullYear() }} PCOS Awareness Nigeria. All rights reserved.</p>
        <p class="mt-2">
          Disclaimer: This website provides informational content and an AI assistant.
          It is not a substitute for professional medical advice, diagnosis, or treatment.
          Always consult a physician or qualified health provider in Nigeria for any medical concerns.
        </p>
      </div>
    </section>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.font {
  font-family: 'Kiwi Maru', serif;
}
</style>