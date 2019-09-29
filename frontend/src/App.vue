<template>
  <div id="app">
    <nav class="navbar navbar-dark bg-dark">
     <span class="navbar-brand mb-0 h2">Resume Eval</span>
     <a href="https://aveek-saha.github.io/" class="navbar-brand mb-0 h1 text-right">
       <i class="fab fa-github fa-inverse"></i>
     </a>
   </nav>
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
/* #nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
} */
</style>
