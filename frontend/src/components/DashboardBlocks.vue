<template>
  <div class="container">
    <div class="dashboard">
      <router-link :to="{ name: 'admin-events' }" class="dashboard-box">Events</router-link>
      <router-link :to="{ name: 'admin-registrations' }" class="dashboard-box">Registrations</router-link>
      <router-link :to="{ name: 'admin-staff' }" class="dashboard-box">Staff</router-link>
      <router-link :to="{ name: 'admin-faqs' }" class="dashboard-box">FAQ</router-link>
    </div>
  </div>
</template>

<style scoped>
.container {
  padding-top: 9px;
  margin-right: 100px;
}

.dashboard {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  padding: 20px;
  text-align: center;
}

.dashboard-box {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #3498db;
  color: white;
  text-decoration: none;
  padding: 50px;
  border-radius: 10px;
  font-size: 1.5rem;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.dashboard-box:hover {
  background-color: #2980b9;
}

/* stacking them vertically on mobile here */
@media (max-width: 768px) {
  .dashboard {
    grid-template-columns: 1fr;
  }

  .container {
    margin-right: 0;
    padding: 10px;
  }
}
</style>
