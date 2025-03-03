<template>
  <AdminSideBar />
  <AdminDashboardNavBar />
  <DashboardBlocks />
</template>

<script setup lang="ts">
import DashboardBlocks from '../../components/DashboardBlocks.vue'
import AdminDashboardNavBar from '../../components/AdminDashboardNavBar.vue'
import AdminSideBar from '@/components/AdminSideBar.vue'
</script>

<style scoped>
h1 {
  color: #333;
}
</style>
