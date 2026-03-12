<template>
  <div class="container mt-5">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h3>Dashboard Users</h3>

      <button class="btn btn-danger" @click="logout">Logout</button>
    </div>

    <!-- SEARCH -->
    <div class="mb-3">
      <input type="text" class="form-control" placeholder="Cari nama atau username..." v-model="search" @input="fetchUsers" />
    </div>

    <div v-if="error" class="alert alert-danger mt-3">
      {{ error }}
    </div>

    <div v-if="success" class="alert alert-success mt-3">
      {{ success }}
    </div>

    <!-- TABLE -->
    <table class="table table-bordered table-striped">
      <thead class="table-dark">
        <tr>
          <th>ID</th>
          <th>Username</th>
          <th>Email</th>
          <th>Nama</th>
          <th>Aksi</th>
        </tr>
      </thead>

      <tbody v-if="users.length > 0">
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.nama }}</td>

          <td>
            <button class="btn btn-warning btn-sm me-2" @click="goToUpdate(user.id)">Update</button>

            <button class="btn btn-danger btn-sm" @click="deleteUser(user.id)">Delete</button>
          </td>
        </tr>
      </tbody>

      <tbody v-else>
        <tr>
          <td colspan="5" class="text-center text-muted">Data user kosong</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  name: "Dashboard",

  data() {
    return {
      users: [],
      search: "",
      error: "",
      success: "",
    };
  },

  methods: {
    async fetchUsers() {
      const token = localStorage.getItem("token");
      try {
        const res = await api.get("/users", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
          params: {
            search: this.search,
          },
        });

        this.users = res.data;
      } catch (err) {
        console.log(err.response.data);
      }
    },

    goToUpdate(id) {
      this.$router.push(`/update/${id}`);
    },

    async deleteUser(id) {
      const confirmDelete = confirm("Apakah Anda yakin ingin menghapus user ini?");

      if (!confirmDelete) return;

      try {
        const res = await api.delete(`/users/${id}`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        this.success = res.data.message;
        this.fetchUsers();
      } catch (err) {
        this.error = err.response.data.message;
      }
    },

    logout() {
      const confirmLogout = confirm("Apakah Anda yakin ingin keluar?");
      if (!confirmLogout) return;

      localStorage.removeItem("token");
      this.$router.push("/");
    },
  },

  mounted() {
    const token = localStorage.getItem("token");

    if (!token) {
      this.$router.push("/");
      return;
    }

    this.fetchUsers();
  },
};
</script>
