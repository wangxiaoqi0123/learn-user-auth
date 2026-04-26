<template>
  <main class="status-page">
    <div class="status-card">
      <p class="status-code">401</p>
      <h1>没有访问权限</h1>
      <p>当前账号无法打开这个页面，请重新登录或联系管理员开通权限。</p>
      <RouterLink class="status-link" to="/login">返回登录</RouterLink>
    </div>
  </main>
</template>

<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>
