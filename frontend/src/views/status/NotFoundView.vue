<template>
  <main class="status-page">
    <div class="status-card">
      <p class="status-code">404</p>
      <h1>页面不存在</h1>
      <p>你访问的地址没有找到，可能已经移动，或者链接本身就不太对。</p>
      <RouterLink class="status-link" to="/login">去登录页</RouterLink>
    </div>
  </main>
</template>

<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>
