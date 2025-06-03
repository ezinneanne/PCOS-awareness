<template>
  <section class="relative min-h-screen flex flex-col justify-between overflow-hidden container mx-auto px-4 py-12 font">
    <!-- Section Title -->
    <h1 class="text-4xl font-extrabold text-pink-600 mb-12 text-center p-4">
      About Polycystic Ovary Syndrome (PCOS)
    </h1>

    <!-- Content Wrapper -->
    <div class="flex flex-col md:flex-row items-center justify-between gap-10">
      
      <!-- Image First on Mobile -->
      <div class="md:w-1/2 p-4 flex justify-center">
        <img
          src="../assets/nigwomen.jpg"
          alt="Nigerian women in a hospital"
          class="w-full max-w-sm md:max-w-full h-auto rounded-lg shadow-lg object-cover"
        />
      </div>

      <!-- Text Content -->
      <div class="md:w-1/2 p-4 text-center md:text-left">
        <h2 class="text-2xl md:text-3xl font-bold mb-6 text-gray-800">A Brief Overview</h2>
        <p class="text-gray-700 leading-relaxed text-base md:text-lg mb-6">
          This platform is dedicated to raising awareness about Polycystic Ovary Syndrome (PCOS) among women in Nigeria. 
          PCOS is a common hormonal disorder that can affect women of reproductive age, and understanding it is the first step towards managing it effectively.
          <br /><br />
          We aim to provide clear information, support, and resources to help you navigate your health journey. 
          Explore our sections to learn more about PCOS, its symptoms, management, and connect with our AI assistant for quick answers.
        </p>
        <button class="bg-pink-600 hover:bg-pink-300 text-white px-6 py-3 rounded-full transition duration-300">
          Read More
        </button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.font {
  font-family: 'Kiwi Maru', serif;
}
</style>
