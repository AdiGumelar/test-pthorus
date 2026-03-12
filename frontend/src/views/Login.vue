<template>
  <div class="container d-flex justify-content-center align-items-center vh-100">
    <div class="card shadow" style="width: 400px">
      <div class="card-body">
        <h3 class="text-center mb-4">Login</h3>

        <form @submit.prevent="handleLogin">
          <div class="mb-3">
            <label class="form-label">Username</label>
            <input type="text" class="form-control" v-model="username" required />
          </div>

          <div class="mb-3">
            <label class="form-label">Password</label>
            <input type="password" class="form-control" v-model="password" required />
          </div>

          <button class="btn btn-primary w-100" type="submit">Login</button>
        </form>

        <p class="text-center mt-3">
          Belum punya akun?
          <router-link to="/register">Register</router-link>
        </p>

        <div v-if="error" class="alert alert-danger mt-3">
          {{ error }}
        </div>

        <div v-if="success" class="alert alert-success mt-3">
          {{ success }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  name: "Login",

  data() {
    return {
      username: "",
      password: "",
      error: "",
      success: "",
    };
  },

  methods: {
    async handleLogin() {
      this.error = "";
      this.success = "";

      if (!this.username || !this.password) {
        this.error = "Semua field harus diisi";
        return;
      }

      try {
        const res = await api.post("http://127.0.0.1:5000/users/login", {
          username: this.username,
          password: this.password,
        });

        localStorage.setItem("token", res.data.token);

        this.success = res.data.message;

        setTimeout(() => {
          this.$router.push("/dashboard");
        }, 1500);
      } catch (err) {
        if (err.response && err.response.data.message) {
          this.error = err.response.data.message;
        } else {
          this.error = "Terjadi kesalahan pada server";
        }
      }
    },
  },
};
</script>
