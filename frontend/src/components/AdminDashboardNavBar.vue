<template>
  <div class="Container">
    <div class="buttonGroup">
      <div class="logo">
        <img
          src="https://www.wlv.ac.uk/media/2019-template-assets/graphics/logo.svg"
          alt="University Of Wolverhampton Logo"
        />
      </div>
      <a href="/settings" class="box">Settings</a>
      <router-link :to="{ name: 'admin' }" class="box">Home</router-link>
      <a href="/profile" class="box">Profile</a>
    </div>
  </div>
</template>

<style scoped>
.Container {
  display: flex;
  justify-content: flex-end;
  padding: 20px;
  margin: 50px;
}

.buttonGroup {
  display: flex;
  gap: 20px;
}

.box {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: grey;
  color: black;
  padding: 20px 30px;
  border-radius: 8px;
  font-size: 1.5rem;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.box:hover {
  background-color: #2980b9;
}

.logo {
  margin-right: 270px;
}
</style>
