<template>
  <div class="layout-container">
    <Header />
    <div class="layout-content">
      <main class="main-content">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
</script>

<style scoped>
.layout-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  min-width: 1280px;
}

.layout-content {
  display: flex;
  flex: 1;
}
.main-content {
  flex: 1;
  background-color: #f5f5f5;
}
</style>
