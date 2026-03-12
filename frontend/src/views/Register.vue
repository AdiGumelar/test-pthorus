<template>
  <div class="container d-flex justify-content-center align-items-center vh-100">
    <div class="card shadow" style="width: 400px">
      <div class="card-body">
        <h3 class="text-center mb-4">Register</h3>

        <form @submit.prevent="handleRegister">
          <div class="mb-3">
            <label class="form-label">Nama</label>
            <input type="text" class="form-control" v-model="nama" />
          </div>

          <div class="mb-3">
            <label class="form-label">Username</label>
            <input type="text" class="form-control" v-model="username" />
          </div>

          <div class="mb-3">
            <label class="form-label">Email</label>
            <input type="email" class="form-control" v-model="email" />
          </div>

          <div class="mb-3">
            <label class="form-label">Password</label>
            <input type="password" class="form-control" v-model="password" />
          </div>

          <button class="btn btn-primary w-100" type="submit">Register</button>
        </form>

        <p class="text-center mt-3">
          Sudah punya akun?
          <router-link to="/">Login</router-link>
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
  name: "Register",

  data() {
    return {
      nama: "",
      username: "",
      email: "",
      password: "",
      error: "",
      success: "",
    };
  },

  methods: {
    async handleRegister() {
      this.error = "";
      this.success = "";

      try {
        const res = await api.post("/users/register", {
          nama: this.nama,
          username: this.username,
          email: this.email,
          password: this.password,
        });

        this.success = res.data.message;

        setTimeout(() => {
          this.$router.push("/");
        }, 1500);
      } catch (err) {
        if (err.response && err.response.data.message) {
          this.error = err.response.data.message;
        } else {
          this.error = "Registrasi gagal";
        }
      }
    },
  },
};
</script>
