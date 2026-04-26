<script setup lang="ts">
import { reactive, ref } from "vue";

const form = reactive({
  account: "",
  password: "",
  remember: true,
});

const isSubmitting = ref(false);

const handleSubmit = async () => {
  if (isSubmitting.value) {
    return;
  }

  isSubmitting.value = true;

  await new Promise((resolve) => window.setTimeout(resolve, 900));

  isSubmitting.value = false;
};
</script>

<template>
  <main class="login-page">
    <section class="login-hero">
      <div class="login-hero__badge">AUTH PLATFORM</div>
      <h1>欢迎回来</h1>
      <p class="login-hero__summary">
        统一管理登录、授权和用户访问，让后台系统更清晰，也更容易维护。
      </p>

      <div class="login-hero__panel">
        <div>
          <span>安全校验</span>
          <strong>JWT / Session</strong>
        </div>
        <div>
          <span>多端接入</span>
          <strong>Web / Admin</strong>
        </div>
        <div>
          <span>权限策略</span>
          <strong>Role / Scope</strong>
        </div>
      </div>
    </section>

    <section class="login-card-wrap">
      <div class="login-card">
        <div class="login-card__header">
          <p class="login-card__eyebrow">SIGN IN</p>
          <h2>账号登录</h2>
          <p class="login-card__text">输入账号和密码进入系统控制台。</p>
        </div>

        <form class="login-form" @submit.prevent="handleSubmit">
          <label class="login-field">
            <span>账号</span>
            <input
              v-model.trim="form.account"
              type="text"
              autocomplete="username"
              placeholder="请输入用户名或邮箱"
            />
          </label>

          <label class="login-field">
            <span>密码</span>
            <input
              v-model="form.password"
              type="password"
              autocomplete="current-password"
              placeholder="请输入密码"
            />
          </label>

          <div class="login-form__row">
            <label class="login-checkbox">
              <input v-model="form.remember" type="checkbox" />
              <span>记住我</span>
            </label>
            <a href="/" @click.prevent>忘记密码</a>
          </div>

          <button class="login-button" type="submit" :disabled="isSubmitting">
            {{ isSubmitting ? "登录中..." : "登录" }}
          </button>
        </form>
      </div>
    </section>
  </main>
</template>
