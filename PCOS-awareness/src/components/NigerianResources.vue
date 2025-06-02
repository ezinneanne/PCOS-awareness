<template>
  <section class="relative min-h-screen flex flex-col justify-between overflow-hidden container mx-auto px-4 py-8 font">
    <!-- Content Wrapper -->
    <div class="flex flex-col-reverse md:flex-row items-center justify-between h-full gap-6">

      <!-- Text Content -->
      <div class="md:w-1/2 p-4 text-center md:text-left">
        <h2 class="text-2xl font-bold mb-4 text-gray-800">PCOS Resources in Nigeria</h2>
        <p class="text-gray-700 leading-relaxed">
          Finding the right support and medical care is crucial when dealing with PCOS. 
          We have gathered some pointers for you to explore...
        </p>
        medic - <i class="fas fa-user-md"></i>
        communities - <i class="fas fa-users"></i>
        support - <i class="fas fa-hand-holding-heart"></i>
        lifestyle - <i class="fas fa-running"></i>

        <br/>
        <button class="bg-pink-600 hover:bg-pink-500 text-white px-4 py-2 rounded-full transition">
          Read More
        </button>
      </div>

      <!-- Icons Content -->
      <div class="md:w-1/2 p-4 flex justify-center">
        <img
          src="../assets/nigwomen.jpg"
          alt="Nigerian women in a hospital"
          class="w-full max-w-sm md:max-w-full h-auto rounded-lg shadow-lg object-cover"
        />
      </div>
    </div>
  </section>
</template>

<style scoped>
  .font {
    font-family: 'Kiwi Maru', serif;
  }
</style>