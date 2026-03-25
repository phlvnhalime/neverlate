<template>
  <div class="landing">
    <LandingNav />
    <LandingHero />
    <LandingFeatures />
    <LandingDownload />
    <LandingFooter />
  </div>
</template>

<script setup>
import LandingNav from '../components/landing/LandingNav.vue'
import LandingHero from '../components/landing/LandingHero.vue'
import LandingFeatures from '../components/landing/LandingFeatures.vue'
import LandingDownload from '../components/landing/LandingDownload.vue'
import LandingFooter from '../components/landing/LandingFooter.vue'
</script>

<style scoped>
.landing {
  min-height: 100vh;
}
</style>
