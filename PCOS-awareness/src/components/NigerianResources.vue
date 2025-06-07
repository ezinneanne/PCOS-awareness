<template>
  <section class="w-full min-h-screen bg-pink-50 py-16 font">
    <div class="container-standard flex flex-col md:flex-row items-center justify-between gap-10">
      
      <!-- Text Content (comes first on small screens) -->
      <div class="md:w-1/2 text-center md:text-left">
        <h2 class="text-3xl font-bold mb-6 text-gray-800">PCOS Resources in Nigeria</h2>
        <p class="text-gray-700 leading-relaxed mb-6 text-base md:text-lg">
          Finding the right support and medical care is crucial when dealing with PCOS. 
          We have gathered some pointers for you to explore and take the next steps confidently in your health journey.
        </p>
        <button class="bg-pink-600 hover:bg-pink-300 text-white px-6 py-3 rounded-full transition duration-300">
          Read More
        </button>
      </div>

      <!-- Icons Grid -->
      <div class="md:w-1/2 grid grid-cols-1 sm:grid-cols-2 gap-6">
        <!-- Icon Card 1 -->
        <div class="text-center bg-white p-6 rounded-lg shadow hover:shadow-lg transition">
          <i class="fas fa-user-md text-pink-600 text-4xl mb-4"></i>
          <h3 class="text-lg font-semibold text-gray-800 mb-2">Medical Professionals</h3>
          <p class="text-sm text-gray-600">Access PCOS-friendly hospitals and specialists across Nigeria.</p>
        </div>

        <!-- Icon Card 2 -->
        <div class="text-center bg-white p-6 rounded-lg shadow hover:shadow-lg transition">
          <i class="fas fa-users text-pink-600 text-4xl mb-4"></i>
          <h3 class="text-lg font-semibold text-gray-800 mb-2">PCOS Communities</h3>
          <p class="text-sm text-gray-600">Connect with other women who share your journey and insights.</p>
        </div>

        <!-- Icon Card 3 -->
        <div class="text-center bg-white p-6 rounded-lg shadow hover:shadow-lg transition">
          <i class="fas fa-hand-holding-heart text-pink-600 text-4xl mb-4"></i>
          <h3 class="text-lg font-semibold text-gray-800 mb-2">Support Groups</h3>
          <p class="text-sm text-gray-600">Join emotional support groups for guided discussions and care.</p>
        </div>

        <!-- Icon Card 4 -->
        <div class="text-center bg-white p-6 rounded-lg shadow hover:shadow-lg transition">
          <i class="fas fa-running text-pink-600 text-4xl mb-4"></i>
          <h3 class="text-lg font-semibold text-gray-800 mb-2">Lifestyle & Wellness</h3>
          <p class="text-sm text-gray-600">Explore health tips and routines tailored for PCOS management.</p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.font {
  font-family: 'Kiwi Maru', serif;
}
</style>
