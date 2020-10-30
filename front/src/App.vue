<template>
  <div id="app">
    Django frontend
    <hr>
    <django_front
        v-bind:array="django_list"
    />
  </div>
</template>

<script>

import django_front from '@/components/django_front'

export default {
  name: 'App',
  data() {
    return {
      django_list: [
        {id: 1, title: 'first title', completed: false},
        {id: 2, title: 'second title', completed: false},
        {id: 3, title: 'third title', completed: false}
      ]
    }
  },
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
  color: #244966;
  margin-top: 60px;
}
</style>
