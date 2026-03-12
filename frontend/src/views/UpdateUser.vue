<template>
  <div class="container d-flex justify-content-center align-items-center vh-100">
    <div class="card shadow" style="width: 450px">
      <div class="card-body">
        <h3 class="text-center mb-4">Update User</h3>

        <!-- SUCCESS -->
        <div v-if="success" class="alert alert-success">
          {{ success }}
        </div>

        <!-- ERROR -->
        <div v-if="error" class="alert alert-danger">
          {{ error }}
        </div>

        <form @submit.prevent="updateUser">
          <div class="mb-3">
            <label class="form-label">Username</label>
            <input type="text" class="form-control" v-model="user.username" required />
          </div>

          <div class="mb-3">
            <label class="form-label">Email</label>
            <input type="email" class="form-control" v-model="user.email" required />
          </div>

          <div class="mb-3">
            <label class="form-label">Nama</label>
            <input type="text" class="form-control" v-model="user.nama" required />
          </div>

          <div class="d-flex justify-content-between">
            <button type="button" class="btn btn-secondary" @click="goBack">Kembali</button>

            <button type="submit" class="btn btn-primary">Update</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  name: "UpdateUser",

  data() {
    return {
      user: {
        username: "",
        email: "",
        nama: "",
      },
      success: "",
      error: "",
    };
  },

  methods: {
    async fetchUser() {
      try {
        const id = this.$route.params.id;

        const res = await api.get(`http://127.0.0.1:5000/users/${id}`);

        this.user = res.data;
      } catch (err) {
        console.error(err);
      }
    },

    async updateUser() {
      this.success = "";
      this.error = "";

      if (!this.user.username || !this.user.email || !this.user.nama) {
        this.error = "Semua field wajib diisi";
        return;
      }

      const id = this.$route.params.id;

      const token = localStorage.getItem("token");

      try {
        const res = await api.put(
          `/users/${id}`,
          {
            username: this.user.username,
            email: this.user.email,
            nama: this.user.nama,
          },
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          },
        );

        this.success = res.data.message;

        setTimeout(() => {
          this.$router.push("/dashboard");
        }, 1000);
      } catch (err) {
        if (err.response && err.response.data.message) {
          this.error = err.response.data.message;
        } else {
          this.error = "Gagal memperbarui user";
        }
      }
    },

    goBack() {
      this.$router.push("/dashboard");
    },
  },

  mounted() {
    this.fetchUser();
  },
};
</script>
