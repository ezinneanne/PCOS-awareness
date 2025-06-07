<template>
  <section class="font py-10 px-4 bg-pink-50 min-h-screen">
    <div class="max-w-4xl mx-auto bg-white shadow-lg rounded-lg p-8 space-y-8">
      <!-- Title -->
      <h2 class="text-3xl md:text-4xl font-bold text-pink-700 text-center">Welcome!</h2>

      <!-- Image First on Mobile -->
      <div class="flex justify-center">
        <img
          src="../assets/nigwomen.jpg"
          alt="Nigerian women in a hospital"
          class="w-full max-w-md rounded-lg shadow-md object-cover"
        />
      </div>

      <!-- Introduction -->
      <div class="space-y-4 text-gray-700 leading-relaxed text-lg">
        <p>
          This platform is dedicated to raising awareness about Polycystic Ovary Syndrome (PCOS) among women in Nigeria.
          PCOS is a common hormonal disorder that can affect women of reproductive age, and understanding it is the first
          step towards managing it effectively.
        </p>
        <p>
          We aim to provide clear information, support, and resources to help you navigate your health journey.
          Explore our sections to learn more about PCOS, its symptoms, management, and connect with our AI assistant for
          quick answers.
        </p>
      </div>

      <!-- Did You Know -->
      <div class="p-6 bg-pink-50 border border-pink-200 rounded-lg space-y-2">
        <h3 class="font-semibold text-pink-600 text-xl">Did you know?</h3>
        <p class="text-gray-700 leading-relaxed text-lg">
          PCOS affects millions of women worldwide, and its prevalence in Nigeria is significant.
          Early diagnosis and management are key to preventing long-term health complications.
        </p>
      </div>

      <!-- Understanding PCOS -->
      <h2 class="text-3xl md:text-4xl font-bold text-pink-700 text-center">Understanding PCOS</h2>

      <!-- What is PCOS -->
      <div class="space-y-2">
        <h3 class="text-2xl font-semibold text-pink-600">What is PCOS?</h3>
        <p class="text-gray-700 leading-relaxed text-lg">
          Polycystic Ovary Syndrome (PCOS) is a hormonal disorder common among women of reproductive age.
          Women with PCOS may have infrequent or prolonged menstrual periods or excess male hormone (androgen) levels.
          The ovaries may develop numerous small collections of fluid (follicles) and fail to regularly release eggs.
        </p>
      </div>

      <!-- Common Symptoms -->
      <div class="space-y-2">
        <h3 class="text-2xl font-semibold text-pink-600">Common Symptoms</h3>
        <ul class="list-disc list-inside text-gray-700 text-lg space-y-1 leading-relaxed">
          <li>Irregular menstrual cycles (e.g., infrequent, irregular or prolonged)</li>
          <li>
            Excess androgen: Elevated levels of male hormones may result in physical signs, such as excess facial and body
            hair (hirsutism), and occasionally severe acne and male-pattern baldness.
          </li>
          <li>
            Polycystic ovaries: Your ovaries might be enlarged and contain follicles that surround the eggs. As a result,
            the ovaries might fail to function regularly.
          </li>
          <li>Weight gain or difficulty losing weight</li>
          <li>Fatigue</li>
          <li>Mood changes</li>
        </ul>
      </div>

      <!-- Diagnosis Importance -->
      <div class="space-y-2">
        <h3 class="text-2xl font-semibold text-pink-600">Why is Diagnosis Important?</h3>
        <p class="text-gray-700 leading-relaxed text-lg">
          Early diagnosis and treatment of PCOS can help reduce the risk of long-term complications,
          such as type 2 diabetes, heart disease, and endometrial cancer.
          If you suspect you have PCOS, it's crucial to consult a healthcare professional in Nigeria for proper evaluation
          and guidance.
        </p>
      </div>

      <!-- Important Note -->
      <div class="p-6 bg-rose-50 border border-rose-200 rounded-lg space-y-2">
        <h3 class="font-semibold text-rose-700 text-xl">Important Note:</h3>
        <p class="text-gray-700 leading-relaxed text-lg">
          This website provides general information.
          Always consult with a doctor or gynecologist for medical advice and diagnosis specific to your situation.
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.font {
  font-family: 'Kiwi Maru', serif;
}
</style>
