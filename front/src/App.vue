<template>
  <div id="app">
    Django frontend
    <hr>
  </div>
</template>

<script>

import django_front from '@/components/django_front'
export default {
  name: 'App',
  components: {
    django_front
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
