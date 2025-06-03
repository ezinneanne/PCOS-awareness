<template>
  <section class="w-full min-h-screen bg-pink-50 py-12 font">
    <!-- Content Wrapper -->
    <div class="max-w-7xl mx-auto px-4 flex flex-col-reverse md:flex-row items-center justify-between gap-8">
      
      <!-- Text Content -->
      <div class="md:w-1/2 text-center md:text-left">
        <h2 class="text-2xl font-bold mb-4 text-gray-800">PCOS Resources in Nigeria</h2>
        <p class="text-gray-700 leading-relaxed mb-6">
          Finding the right support and medical care is crucial when dealing with PCOS. 
          We have gathered some pointers for you to explore...
        </p>
        <button class="bg-pink-600 hover:bg-pink-500 text-white px-6 py-2 rounded-full transition">
          Read More
        </button>
      </div>

      <!-- Icons Grid -->
      <div class="md:w-1/2 grid grid-cols-1 sm:grid-cols-2 gap-6">
        <!-- Icon Card -->
        <div class="text-center bg-white p-4 rounded-lg shadow hover:shadow-md transition">
          <i class="fas fa-user-md fa-4x text-pink-600 text-4xl mb-2"></i>
          <h3 class="text-lg font-semibold text-gray-800 mb-1">Medical Professionals</h3>
          <p class="text-sm text-gray-600">Access PCOS-friendly hospitals and specialists across Nigeria.</p>
        </div>

        <div class="text-center bg-white p-4 rounded-lg shadow hover:shadow-md transition">
          <i class="fas fa-users fa-4x text-pink-600 text-4xl mb-2"></i>
          <h3 class="text-lg font-semibold text-gray-800 mb-1">PCOS Communities</h3>
          <p class="text-sm text-gray-600">Connect with other women who share your journey and insights.</p>
        </div>

        <div class="text-center bg-white p-4 rounded-lg shadow hover:shadow-md transition">
          <i class="fas fa-hand-holding-heart fa-4x text-pink-600 text-4xl mb-2"></i>
          <h3 class="text-lg font-semibold text-gray-800 mb-1">Support Groups</h3>
          <p class="text-sm text-gray-600">Join emotional support groups for guided discussions and care.</p>
        </div>

        <div class="text-center bg-white p-4 rounded-lg shadow hover:shadow-md transition">
          <i class="fas fa-running fa-4x text-pink-600 text-4xl mb-2"></i>
          <h3 class="text-lg font-semibold text-gray-800 mb-1">Lifestyle & Wellness</h3>
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