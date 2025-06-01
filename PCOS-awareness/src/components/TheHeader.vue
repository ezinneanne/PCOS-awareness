<template>
  <div>
    <!-- Navbar -->
    <nav class="navbar">
      <!-- Logo -->
      <div class="logo">PCOS Awareness</div>

      <!-- Middle Links -->
      <div class="nav-links">
        <a href="#hospitals">Hospitals</a>
        <a href="#nonprofits">Non-profit Organizations</a>
        <a href="#about">About PCOS</a>
      </div>

      <!-- Chat Button -->
      <div class="chat-btn">
        <button class="chat-button">Chat with AI Bot</button>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
      <!-- Text Side -->
      <div class="hero-text">
        <h1>Let’s Talk About PCOS</h1>
        <p>
          Speak with our AI assistant for early insights and support around
          Polycystic Ovary Syndrome. It’s fast, confidential, and supportive.
        </p>
        <button class="hero-btn">Start Chatting</button>
      </div>

      <!-- Image Side -->
      <div class="hero-image">
        <img
          src="https://via.placeholder.com/400x300?text=Nigerian+Women+Illustration"
          alt="PCOS Awareness"
        />
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'TheHeader',
};
</script>

<style scoped>
/* Navbar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  flex-wrap: wrap;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #ec4899;
}

.nav-links {
  display: flex;
  gap: 1.5rem;
  flex: 1;
  justify-content: center;
}

.nav-links a {
  color: #4b5563;
  font-weight: 500;
  text-decoration: none;
}

.nav-links a:hover {
  color: #ec4899;
}

.chat-btn .chat-button {
  background-color: #ec4899;
  color: white;
  border: none;
  padding: 0.5rem 1.2rem;
  border-radius: 9999px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.chat-btn .chat-button:hover {
  background-color: #db2777;
}

/* Hero Section */
.hero {
  display: flex;
  flex-direction: column-reverse;
  align-items: center;
  justify-content: center;
  background-color: #fce7f3; /* light pink */
  padding: 3rem 2rem;
}

.hero-text {
  text-align: center;
  max-width: 600px;
}

.hero-text h1 {
  font-size: 2rem;
  color: #1f2937;
  margin-bottom: 1rem;
}

.hero-text p {
  font-size: 1.125rem;
  color: #4b5563;
  margin-bottom: 1.5rem;
}

.hero-btn {
  background-color: #ec4899;
  color: white;
  border: none;
  padding: 0.75rem 2rem;
  border-radius: 9999px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.hero-btn:hover {
  background-color: #db2777;
}

.hero-image img {
  width: 100%;
  max-width: 400px;
  border-radius: 0.5rem;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

/* Responsive Design */
@media (min-width: 768px) {
  .hero {
    flex-direction: row;
    gap: 2rem;
    text-align: left;
  }

  .hero-text,
  .hero-image {
    flex: 1;
  }

  .hero-image {
    margin-bottom: 0;
  }
}
</style>
