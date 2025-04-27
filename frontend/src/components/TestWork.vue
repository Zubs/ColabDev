<template>
  <div>
    <div class="d-flex" id="wrapper">
      <!-- Sidebar -->
      <div class="bg-light border-right" id="sidebar-wrapper">
        <div class="list-group list-group-flush">
          <div class="list-group-item bg-light">
            <a href="#" class="d-flex justify-content-between align-items-center" data-toggle="collapse" data-target="#dashboardDropdown" aria-expanded="false" aria-controls="dashboardDropdown">
              Dashboard
              <span class="caret"></span>
            </a>
            <div class="collapse" id="dashboardDropdown">
              <a href="#" class="list-group-item list-group-item-action bg-light">Sub-item 1</a>
              <a href="#" class="list-group-item list-group-item-action bg-light">Sub-item 2</a>
            </div>
          </div>
          <div class="list-group-item bg-light">
            <a href="#" class="d-flex justify-content-between align-items-center" data-toggle="collapse" data-target="#shortcutsDropdown" aria-expanded="false" aria-controls="shortcutsDropdown">
              Shortcuts
              <span class="caret"></span>
            </a>
            <div class="collapse" id="shortcutsDropdown">
              <a href="#" class="list-group-item list-group-item-action bg-light">Sub-item 1</a>
              <a href="#" class="list-group-item list-group-item-action bg-light">Sub-item 2</a>
            </div>
          </div>
          <!-- Add similar dropdowns for other items as needed -->
        </div>
      </div>
      <!-- /#sidebar-wrapper -->

      <!-- Page Content -->
      <div id="page-content-wrapper">
        <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
          <button class="btn btn-primary" id="menu-toggle">Toggle Menu</button>
        </nav>
        <div class="container-fluid">
          <h1 class="mt-4">Page Content</h1>
          <p>This is the main content area.</p>
        </div>
      </div>
      <!-- /#page-content-wrapper -->
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    document.getElementById('menu-toggle').addEventListener('click', function (e) {
      e.preventDefault()
      document.getElementById('wrapper').classList.toggle('toggled')
    })
  },
}
</script>

<style scoped>
#wrapper {
  display: flex;
  flex-direction: row;
}

#sidebar-wrapper {
  min-height: 100vh;
  width: 250px;
  margin-left: -250px;
  transition: margin 0.25s ease-out;
}

#wrapper.toggled #sidebar-wrapper {
  margin-left: 0;
}

#page-content-wrapper {
  flex: 1;
  width: 100%;
}
</style>
