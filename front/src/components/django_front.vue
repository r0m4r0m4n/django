<template>
  <div>
    <ul>

      <django v-for="i in array"
              v-bind:item="i"
      />
    </ul>
  </div>
</template>

<script>

import django from '@/components/1'

export default {
  props: ['array'],
  components: {
    django
  }
}
</script>
<style scoped>
  ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }
</style>