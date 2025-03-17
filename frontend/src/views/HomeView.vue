<template>
  <NavBar />
  <Hero />
  <section class="ftco-section services-section bg-light">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <section class="call-to-action-bar">
            <div class="call-to-action-bar__headings">
              <h2 class="call-to-action-bar__title">Open Day Guide</h2>
            </div>
            <div class="call-to-action-bar__cta">
              <a href="https://www.wlv.ac.uk/news-and-events/open-day/open-day-guide/?utm_medium=cpc&amp;utm_source=google&amp;utm_campaign=ug2025_ucasextra" target="_self" class="btn call-to-action-bar__cta-process" title="Click Here">Click Here</a>
              <span class="call-to-action-bar__cta-link"><p><span>This is your go-to resource for everything you need on your visit</span></p></span>
            </div>
          </section>
        </div>
      </div>
    </div>
  </section>

  <Events />

  <section class="ftco-section bg-light">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div class="header">
            Prepare for undergraduate open day...
          </div>
          <div class="content">
            Our undergraduate open day is ideal for every prospective student. Whether you just want to get an idea of what the University is like, or want to find out more about a specific subject or course, it's the perfect chance to discover what it's like to study with us.
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="video-section">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div class="video-container">
            <iframe
              width="560"
              height="315"
              src="https://www.youtube.com/embed/CuOINQvswsA"
              title="YouTube video player"
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen>
            </iframe>
          </div>
        </div>
      </div>
    </div>
  </section>

  <Gallery />
  <Footer />
</template>

<script setup>
import NavBar from "@/components/NavBar.vue";
import Hero from "@/components/Hero.vue";
import Events from "@/components/Events.vue";
import Gallery from "@/components/Gallery.vue";
import Footer from "@/components/Footer.vue";
</script>

<style scoped>
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 15px;
}

.row {
  display: flex;
  flex-wrap: wrap;
  margin: 0 -15px;
}

.col-12 {
  width: 100%;
  padding: 0 15px;
}

.ftco-section {
  padding: 60px 0;
}

.video-section {
  padding: 60px 0;
  background-color: #f8f9fa;
}

.header {
  font-size: 42px;
  text-align: left;
  margin-bottom: 20px;
  color: black;
  font-weight: bold;
  line-height: 1.2;
}

.content {
  font-size: 20px;
  margin-bottom: 30px;
  font-weight: 500;
  color: #0b2e13;
  line-height: 1.6;
}

.video-container {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  padding: 20px 0;
}

.video-container iframe {
  max-width: 100%;
  border-radius: 8px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.call-to-action-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f5f5f5;
  padding: 30px;
  border-radius: 8px;
  width: 100%;
  margin: 0 auto;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.call-to-action-bar__headings {
  flex: 1;
}

.call-to-action-bar__title {
  font-size: 32px;
  margin: 0;
  color: #333;
  font-weight: 700;
}

.call-to-action-bar__cta {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 15px;
}

.call-to-action-bar__cta-process {
  display: inline-block;
  padding: 15px 30px;
  font-size: 18px;
  font-weight: bold;
  text-decoration: none;
  background-color: #e91e63;
  color: white;
  border-radius: 6px;
  transition: all 0.3s ease;
  text-align: center;
  min-width: 200px;
}

.call-to-action-bar__cta-process:hover {
  background-color: #c2185b;
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.call-to-action-bar__cta-link {
  font-size: 16px;
  color: #666;
  text-align: right;
  max-width: 300px;
}

@media (max-width: 768px) {
  .call-to-action-bar {
    flex-direction: column;
    text-align: center;
    padding: 20px;
  }

  .call-to-action-bar__cta {
    margin-top: 20px;
    align-items: center;
  }

  .call-to-action-bar__cta-link {
    text-align: center;
  }

  .header {
    font-size: 32px;
  }

  .content {
    font-size: 18px;
    margin-left: 0;
  }
}
</style>
